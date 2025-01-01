import streamlit as st

from apptrackr.db import DB
from apptrackr.llm import LLMClient
from apptrackr.config import Configuration

if st.session_state['authentication_status'] == None:
    st.switch_page("main.py")
else:
    cv = Configuration.getResume()
    sysprompt = Configuration.getSystemPrompt()

    st.title('Generate cover')

    st.text_area("CV", value=cv.content, key="w_cv")
    st.text_area("Prompt", value=sysprompt.content, key="w_sysprompt")
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
