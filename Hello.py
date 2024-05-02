import streamlit as st
from streamlit.logger import get_logger
import yfinance as yf
LOGGER = get_logger(__name__)
st.set_page_config(page_title="Algo App",layout="wide",initial_sidebar_state="expanded",)
st.markdown("""
  <style>
    .block-container {padding-top: 0.5rem;padding-bottom: 0rem;padding-left: 2rem;padding-right: 5rem;}
  </style>
  """, unsafe_allow_html=True)

st.write("# Welcome to My Algo!")
def run():
    pass

if __name__ == "__main__":
    run()
