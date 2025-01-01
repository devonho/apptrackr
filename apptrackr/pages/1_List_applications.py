import streamlit as st
import pandas as pd

from apptrackr.db import DB
from apptrackr.types import JobApplication

if st.session_state['authentication_status'] == None:
    st.switch_page("main.py")
else:
    recs = [rec.toDict() for rec in DB.retrieveRecords(JobApplication)]
    df = pd.DataFrame(recs)[[
            "role_title",
            "role_organization",            
            "application_status",
            "date_of_application"
    ]]

    st.title('Applications')
    st.write(df)

