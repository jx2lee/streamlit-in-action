import streamlit as st
from streamlit_extras.switch_page_button import switch_page

from utils.style import (
    HIDE_STREAMLIT_STYLE,
    FAVICON_IMG,
    PUBLIC_DIR,
    HIDE_SIDEBAR_STYLE
)


def home():
    st.set_page_config(
        page_title='Coinone Data App',
        page_icon=FAVICON_IMG,
        initial_sidebar_state='collapsed'
    )

    st.title('Welcome, Coinone Data App.')
    st.image(image=PUBLIC_DIR + "logo-symbol-light.png", width=300)

    st.write("""
    The crypto industry continues to progress and its development has never stopped. Contributors
    of each blockchain keep developing each segment of the industry and the whole crypto ecosystem.
    This tool is designed to allow viewers to journey into the world of crypto ecosystems of some
    of the major blockchains, and compare their performance.
    This tool is designed and structured in multiple **Pages** that are accessible using the sidebar.
    Each of these Pages addresses a different segment of the crypto industry. Within each segment
    (Macro, Transfers, Swaps, NFTs, etc.) you are able to filter your desired blockchains to
    narrow/expand the comparison. By selecting a single blockchain, you can observe a deep dive
    into that particular network.
    All values for amounts, prices, and volumes are in **U.S. dollars** and the time frequency of the
    analysis was limited to the last **30 days**.
    """)

    st.button("login", type="primary", use_container_width=True)

    st.write("""
    If you want to apply for permission to bigquery, lightdash, and datahub
    provided by Data Cell, please click the button below.
    """)

    st.subheader("Authorization")
    if st.button("Link", type="secondary", ):
        switch_page(page_name='authorization')

    st.markdown(HIDE_STREAMLIT_STYLE, unsafe_allow_html=True)
    st.markdown(HIDE_SIDEBAR_STYLE, unsafe_allow_html=True)


if __name__ == '__main__':
    home()
