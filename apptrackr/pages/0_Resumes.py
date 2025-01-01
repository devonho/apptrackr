import streamlit as st
import pandas as pd

from datetime import datetime, UTC
from apptrackr.db import DB
from apptrackr.types import Resume
from apptrackr.config import Configuration

if st.session_state['authentication_status'] == None:
    st.switch_page("main.py")
else:
    userhash = Configuration.getUserHash(st.session_state['username'])

    @st.dialog("Update")
    def update():
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
    st.button("Update", on_click=update)

    st.text_area("Title", key="w_cv_title_add")
    st.text_area("Contents", key="w_cv_content_add")

    def handle_add():
        new_cv = Resume({
            "owner_id" : userhash,
            "date_of_creation" : datetime.now(UTC),
            "date_of_update" : datetime.now(UTC),
            "content" : st.session_state.w_cv_title_add,
            "title" : st.session_state.w_cv_content_add
        })

    st.button("Add", on_click=handle_add)

