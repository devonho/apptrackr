import streamlit as st
import pandas as pd

from datetime import datetime, UTC

from apptrackr.db import DB
from apptrackr.types import JobDescription
from apptrackr.config import Configuration

if st.session_state['authentication_status'] == None:
    st.switch_page("main.py")
else:
    userhash = Configuration.getUserHash(st.session_state['username'])

    def handle_save():
        jd = JobDescription({
            "owner_id" : userhash,
            "date_of_creation" : datetime.now(UTC),
            "date_of_update" : datetime.now(UTC),
            "content" : st.session_state.w_content,
            "role_title" : st.session_state.w_role_title,
            "role_organization" : st.session_state.w_role_org
        })
        DB.createRecord(jd)
        st.success("Successful.")

    st.title('Add JD')    
    #docs = [doc.content for doc in DB.retrieveRecords(Resume, userhash)]
    st.text_area("Role Title", key="w_role_title")  
    st.text_area("Role Organization", key="w_role_org")  
    st.text_area("Job Description", key="w_content")  

    st.button("Add", on_click=handle_save)
