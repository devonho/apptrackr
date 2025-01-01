import streamlit as st
import pandas as pd

from datetime import datetime, UTC

from apptrackr.db import DB
from apptrackr.types import Username
from apptrackr.config import Configuration

if st.session_state['authentication_status'] == None:
    st.switch_page("main.py")
else:
    userhash = Configuration.getUserHash(st.session_state['username'])    
    userrole = [r.role for r in DB.retrieveRecords(Username) if r.username == st.session_state.username][0]
    
    if userrole == "manager":
        def handle_save():
            jd = Username({
                "owner_id" : userhash,
                "date_of_creation" : datetime.now(UTC),
                "date_of_update" : datetime.now(UTC),
                "username" : st.session_state.w_username,
                "email" : st.session_state.w_email,
                "first_name" : st.session_state.w_first_name,
                "last_name" : st.session_state.w_last_name,
                "role" : st.session_state.w_role
            })
            DB.createRecord(jd)
            st.success("Successful.")

        st.title('Add user')    
        st.text_area("Username", key="w_username")  
        st.text_area("Email", key="w_email")  
        st.text_area("First name", key="w_first_name")  
        st.text_area("Last name", key="w_last_name")  
        st.selectbox("Role", ["manager","user"], key="w_role")

        st.button("Save", on_click=handle_save)
    else:
        st.write("Only managers can add users.")
