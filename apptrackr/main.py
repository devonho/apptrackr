import os
import streamlit as st
import streamlit_authenticator as stauth

from apptrackr.db import DB
from apptrackr.types import Username

usernames = {un.username : {"first_name": un.first_name, "last_name": un.last_name, "email": un.email } for un in DB.retrieveRecords(Username) }  

authenticator = stauth.Authenticate(
    {"usernames": usernames},
    "apptrackr",
    "key",
    30
)

oauth2_config = {
    "google" : {
        "client_id": os.environ["OAUTH2_CLIENT_ID"],
        "client_secret": os.environ["OAUTH2_CLIENT_SECRET"],
        "redirect_uri": os.environ["OAUTH2_REDIRECT_URL"]
    } 
}

if st.session_state['authentication_status'] == None:
    try:
        authenticator.experimental_guest_login('Login with Google',
                                            provider='google',
                                            oauth2=oauth2_config)
    except Exception as e:
        st.error(e)
else:
    st.title('Apptrackr')
    st.write(f"Welcome *{st.session_state["name"]}* ({st.session_state["username"]})")
    authenticator.logout()
    st.markdown("""
             
             ## Features
             
            * Generate cover letters
            * Curate different versions of CVs
            * Track and update application status
            * Scan designated email (coming)
                
            ## Usage
            1. Create resume
            2. Add JD
            3. Chat with JD and resume
            4. Create cover letter
            5. Check on application status 

            ## Github
            Check out our [repo](https://github.com/devonho/apptrackr.git)
            """)
