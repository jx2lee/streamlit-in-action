import streamlit as st

from core.slack import request_auth_slack
from utils.style import FAVICON_IMG, default_markdown


def auth_view():
    st.set_page_config(
        page_title='Authorization',
        page_icon=FAVICON_IMG,
        initial_sidebar_state='collapsed'
    )
    default_markdown()

    st.title('Authorization')

    selected_services = st.multiselect(
        label='Service(s): ',
        options=['BigQuery', 'Lightdash', 'DataHub']
    )
    if selected_services:
        st.write('You selected', len(selected_services), 'service(s)')

    username = st.text_input(label='Enter your name.')
    if username:
        st.success(f'username: {username}')

    email = st.text_input(label='Enter your email.')
    if email:
        st.success(f'email: {email}')

    if selected_services and username and email:
        st.button(
            label='submit',
            use_container_width=True,
            on_click=request_auth_slack(
                services=selected_services,
                username=username,
                email=email
            )
        )


if __name__ == '__main__':
    auth_view()
