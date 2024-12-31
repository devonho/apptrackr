import streamlit as st
import pandas as pd

from apptrackr.db import DB
from apptrackr.llm import LLMClient

save_button = None
cv_text_area = None

def handle_save():
    print(cv_text_area.value)


def show_generate_cover_page():
    global cv_text_area
    st.title('Update CV')    
    docs = [doc.get("content") for doc in DB.retrieveResumes()]
    cv_text_area = st.text_area("CV", docs[0])  

    st.button("Save", on_click=handle_save)

if __name__ == "__main__":
    show_generate_cover_page()