import streamlit as st
import pandas as pd

from apptrackr.db import DB
from apptrackr.types import Resume
from apptrackr.config import Configuration

if st.session_state['authentication_status'] == None:
    st.switch_page("main.py")
else:
    userhash = Configuration.getUserHash(st.session_state['username'])
    save_button = None
    cv_text_area = None

    def handle_select():
        cv = [cv for cv in cvs if cv.title == st.session_state.w_cv_title][0]
        st.session_state.w_cv_content = cv.content
        
    def handle_save():
        cv = [cv for cv in cvs if cv.title == st.session_state.w_cv_title][0]
        cv.content = st.session_state.w_cv_content
        DB.updateRecord(cv.document_id, cv)
        st.success("Successful.")

    st.title('Update CV')    

    cvs = [cv for cv in DB.retrieveRecords(Resume, userhash)]
    st.selectbox("CV", [cv.title for cv in cvs], index=None, key="w_cv_title", on_change=handle_select)
    st.text_area("Contents", key="w_cv_content")

    st.button("Save", on_click=handle_save)
