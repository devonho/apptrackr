import streamlit as st

from apptrackr.db import DB
from apptrackr.llm import LLMClient
from apptrackr.config import Configuration

def show_generate_cover_page():
    cv = Configuration.getResume()
    sysprompt = Configuration.getSystemPrompt()

    st.title('Generate cover')    

    st.text_area("CV", value=cv["content"], key="w_cv")
    st.text_area("Prompt", value=sysprompt["content"], key="w_sysprompt")
    st.text_area("Job Description", key="w_jd")
    st.text_area("Cover letter", key="w_cover")
    st.checkbox("Save to DB", key="w_cb")

    def generate():
        save_to_db_flag = st.session_state.w_cb
        cv = st.session_state.w_cv
        jd = st.session_state.w_jd
        sysprompt = st.session_state.w_sysprompt

        cover_letter = LLMClient.write(cv, jd, sysprompt, save_to_db_flag)

        st.session_state.w_cover = cover_letter["cover_letter"]

    st.button("Generate", on_click=lambda : generate())

if __name__ == "__main__":
    show_generate_cover_page()