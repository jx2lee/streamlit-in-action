import os.path
import streamlit as st

from PIL import Image

HIDE_STREAMLIT_MARK = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

HIDE_SIDEBAR = """
<style>
    div[data-testid="collapsedControl"] {display: none;}
    div[data-testid="stSidebarNav"] {display: none;}
</style>
"""

FONT = """
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono&display=swap');
html, body, [class*="css"]  {
    font-family: 'JetBrains Mono', sans-serif;
}
</style>
"""

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUBLIC_DIR = ROOT_DIR + "/public/"
FAVICON_IMG = Image.open(PUBLIC_DIR + 'favicon.ico').resize((300, 300))


def default_markdown() -> None:
    """default page markdown settings"""
    st.markdown(HIDE_STREAMLIT_MARK, unsafe_allow_html=True)
    st.markdown(HIDE_SIDEBAR, unsafe_allow_html=True)
    st.markdown(FONT, unsafe_allow_html=True)
