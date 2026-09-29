import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from helpers import setup_page, render_footer

setup_page("Home")
st.title("🇮🇳 India Governance & Economic Dashboard")
st.markdown("Welcome to the India Governance & Economic Dashboard. Please select a view from the sidebar.")
st.info("👈 Select **Union Government**, **Lok Sabha**, or **State Government** to begin.")
render_footer()
