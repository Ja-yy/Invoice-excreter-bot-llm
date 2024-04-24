import streamlit as st

from extracter_agent import ExtracterAgent
from utils import format_output

st.title("🤖Invoice extractor Bot")

if st.session_state.openai_api_key is None:
    st.warning("Please enter your OpenAI API key on main page!!!")
else:
    try:
        col1, col2 = st.columns([4, 1])
        llm_res = ""
        with col1:
            uploaded_files = st.file_uploader(
                "Upload invoices here, only PDF files allowed",
                type=["pdf"],
                accept_multiple_files=True,
            )
            extract_btn = st.button(label="Extract")
        with col2:
            output_type = st.radio(
                label="Select output type",
                options=["JSON", "CSV"],
                index=0,
                help="CSV formate may not include all excreted data!!!",
            )

        if uploaded_files and extract_btn:
            ex_agent = ExtracterAgent()
            with st.spinner("Extracting data.."):
                llm_res = ex_agent.run_agent(uploaded_files)
            st.success("Done!")
        elif extract_btn and (uploaded_files is None):
            st.warning("Please,Uploaded a file!!!")

        st.divider()
        if llm_res:
            with st.expander(label="Extracted Invoice"):
                format_output(output_type, llm_res)
    except Exception as e:
        st.warning("Something went wrong!!")
