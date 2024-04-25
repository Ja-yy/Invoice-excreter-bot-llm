import shutil
import tempfile
from typing import List

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts.chat import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
from pydantic.v1 import BaseModel
from streamlit.runtime.uploaded_file_manager import UploadedFile
import streamlit as st


class Invoice(BaseModel):

    class Items(BaseModel):
        description: str
        quantity: int
        unit_price: float
        amount: float

    invoiceID: str
    date: str
    items: List[Items]
    tax_rate: str
    total_amount: float


class ExtracterAgent:

    output_parser: PydanticOutputParser = PydanticOutputParser(
        pydantic_object=Invoice)

    def parse_pdf_input(self, uploaded_files: UploadedFile):
        parded_pdf = []
        for file in uploaded_files:
            with tempfile.NamedTemporaryFile(delete=False) as tmp:
                shutil.copyfileobj(file, tmp)
            pdf_loader = PyPDFLoader(tmp.name)
            pdf_reader = pdf_loader.load()
            parded_pdf.append(pdf_reader)
        return parded_pdf

    def create_prompt(self):
        sys_template = """You are expert at data extraction.
You tasked to extracted data from given tax invoice.
"""
        prompt = ChatPromptTemplate.from_messages(
            [("system", sys_template), ("human", "{pdf_input}")]
        ).partial(format_instruction=self.output_parser.get_format_instructions())
        return prompt

    def create_chain(self):
        llm = ChatOpenAI(model="gpt-3.5-turbo",
                         api_key=st.session_state.get("openai_api_key"))
        prompt = self.create_prompt()
        chain = (
            {"pdf_input": RunnablePassthrough()}
            | prompt
            | llm.with_structured_output(schema=Invoice)
        )
        return chain

    def run_agent(self, pdf):
        loaded_file = self.parse_pdf_input(pdf)
        chain = self.create_chain()
        llm_res = chain.batch(loaded_file)
        return llm_res
