import os

import streamlit as st
import streamlit_ace as sta

from utils.style import FAVICON_IMG, default_markdown


def editor_view():
    st.set_page_config(
        page_title='Authorization',
        page_icon=FAVICON_IMG,
        initial_sidebar_state='collapsed'
    )
    default_markdown()

    file_list = os.listdir('.')

    # case-1
    selected_file = st.selectbox("Select a file", file_list)

    if selected_file:
        with open(selected_file) as f:
            file_contents = f.read()
        # st.text_area("File Contents", file_contents)
        sta.st_ace(
            value=file_contents,

        )

    if st.button("Save File"):
        if selected_file:
            with open(selected_file, "w") as f:
                f.write(st.session_state.file_contents)
            st.success("File saved!")
        else:
            st.warning("Please select a file first.")
    #case-2
    # contents = os.listdir('.')
    # for content in contents:
    #     path = os.path.join('.', content)
    #     if os.path.isfile(path):
    #         if st.button(content):
    #             with open(content, 'w') as f:
    #                 text = st.text_input('Enter your text:')
    #                 f.write(text)
    #                 st.success('Saved!')
    #     elif os.path.isdir(path):
    #         try:
    #             with st.expander(content, expanded=False):
    #                 files = os.listdir(path)
    #                 for file in files:
    #                     st.write(file)
    #         except NotADirectoryError:
    #             pass


if __name__ == '__main__':
    editor_view()
