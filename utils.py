import pandas as pd
import streamlit as st


def format_output(output_type: str, llm_res):
    if output_type == "JSON":
        dict_output = [res.dict() for res in llm_res]
        st.json(dict_output)
    else:
        for res in llm_res:
            st.write(f'Invoice-ID: {res.dict().get("invoiceID")}')
            df = pd.DataFrame(res.dict().get("items"))
            st.dataframe(df)
