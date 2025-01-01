import streamlit as st

from datetime import datetime, UTC
from apptrackr.db import DB
from apptrackr.llm import LLMClient
from apptrackr.config import Configuration
from apptrackr.types import JobApplication, Resume, SystemPrompt, JobDescription

if st.session_state['authentication_status'] == None:
    st.switch_page("main.py")
else:
    userhash = Configuration.getUserHash(st.session_state['username'])
    resumes = DB.retrieveRecords(Resume, userhash)
    sysprompts = DB.retrieveRecords(SystemPrompt, userhash)
    jds = DB.retrieveRecords(JobDescription, userhash)
    cv_index = 0
    sysprompt_index = 0

    st.title('Generate cover')

    st.selectbox("CV", [r.title for r in resumes], key="w_cv")
    st.selectbox("Prompt", [r.title for r in sysprompts], key="w_sysprompt")
    st.selectbox("Job Description", [f"{r.role_title} [{r.role_organization}]" for r in jds], key="w_jd")

    st.text_area("Cover letter", key="w_cover")
    st.checkbox("Save to DB", key="w_cb")

    def generate():
        save_to_db_flag = st.session_state.w_cb
        cv_title = st.session_state.w_cv
        sysprompt_title = st.session_state.w_sysprompt
        role_title_org = st.session_state.w_jd

        cv = [r.content for r in resumes if r.title == cv_title][0]
        sysprompt = [r.content for r in sysprompts if r.title == sysprompt_title][0]    
        jd = [r for r in jds if f"{r.role_title} [{r.role_organization}]" == role_title_org][0]
        jd_content = jd.content

        output = LLMClient.write(cv, jd_content, sysprompt)

        if save_to_db_flag:
            ja = JobApplication({
                "owner_id" : userhash,
                "job_description" : jd_content,
                "job_description_title" : jd.role_title,
                "role_title" : jd.role_title,
                "role_organization" : jd.role_organization,
                "resume_contents" : cv,
                "system_prompt" : sysprompt,
                "cover_letter" : output["cover_letter"],
                "application_status" : "open",
                "date_of_application" : datetime.now(UTC),
                "date_of_status_update" : datetime.now(UTC),
                "date_of_creation" : datetime.now(UTC)
            })
            DB.createRecord(ja)
        st.session_state.w_cover = output["cover_letter"]

    st.button("Generate", on_click=lambda : generate())
