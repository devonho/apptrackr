import streamlit as st
import pandas as pd

from apptrackr.db import DB
from apptrackr.types import JobApplication
from apptrackr.config import Configuration

if st.session_state['authentication_status'] == None:
    st.switch_page("main.py")
else:
    userhash = Configuration.getUserHash(st.session_state['username'])

    st.title('Applications')
    recs = [rec.toDict() for rec in DB.retrieveRecords(JobApplication, userhash)]
    if len(recs) > 0:
        df = pd.DataFrame(recs)[[
                "role_title",
                "role_organization",            
                "application_status",
                "date_of_application"
        ]]
        st.write(df)

