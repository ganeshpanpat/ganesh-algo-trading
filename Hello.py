import streamlit as st
from streamlit.logger import get_logger
import yfinance as yf
LOGGER = get_logger(__name__)
st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )
st.write("# Welcome to Streamlit! 👋")
def run():
    pass
    
    


if __name__ == "__main__":
    run()
