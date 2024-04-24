from pathlib import Path

import streamlit as st

st.set_page_config(page_title="🧾🤖Invoice extractor Bot")

if "openai_api_key" not in st.session_state:
    st.session_state["openai_api_key"] = None

intro_message = Path("MAIN.md").read_text()
st.markdown(intro_message, unsafe_allow_html=True)


with st.sidebar:
    openai_key = st.text_input(label="OpenAI key", type="password")
    if openai_key and st.session_state.openai_api_key is None:
        st.session_state["openai_api_key"] = openai_key
    elif st.session_state.openai_api_key is None:
        st.warning("Please enter your OpenAI API key!!!")
