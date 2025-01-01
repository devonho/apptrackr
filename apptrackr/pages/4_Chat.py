import streamlit as st
from apptrackr.db import DB
from apptrackr.types import Resume, JobDescription
from apptrackr.config import Configuration
from apptrackr.llm import LLMClient

if st.session_state['authentication_status'] == None:
    st.switch_page("main.py")
else:
    userhash = Configuration.getUserHash(st.session_state['username'])
    cvs = [ r for r in DB.retrieveRecords(Resume, userhash)]
    jds = [ r for r in DB.retrieveRecords(JobDescription, userhash)]
    cv = cvs[0].content
    jd = jds[0].content

    st.title("CV Bot")

    
    st.selectbox("CV", [r.title for r in cvs], key="w_cv_select")
    st.selectbox("JD", [r.role_title for r in jds], key="w_jd_select")

    #@st.dialog("Chat", width="large")
    #def dialog():
    #if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "user", "content": f"Resume:\n {cv} "}, {"role": "user", "content": f"Job Description\n {jd}"}]

    for message in st.session_state.messages[2:]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("How can I help you?"):
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        response = LLMClient.chat(st.session_state.messages)

        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

    #st.button("Chat", on_click=dialog)
