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

    def handle_save():
        print(cv_text_area.value)


    st.title('Update CV')    
    docs = [doc.content for doc in DB.retrieveRecords(Resume, userhash)]
    cv_text_area = st.text_area("CV", docs[0])  

    st.button("Save", on_click=handle_save)
