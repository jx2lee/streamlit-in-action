import streamlit as st

from utils.style import HIDE_STREAMLIT_STYLE, HIDE_SIDEBAR_STYLE


def view():
    st.markdown(HIDE_STREAMLIT_STYLE, unsafe_allow_html=True)
    st.markdown(HIDE_SIDEBAR_STYLE, unsafe_allow_html=True)

    st.write("""
    kkkkkkkkkkk
    """)


view()
