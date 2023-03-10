import streamlit as st

from utils.style import FAVICON_IMG, default_markdown


def editor_view():
    st.set_page_config(
        page_title='Authorization',
        page_icon=FAVICON_IMG,
        initial_sidebar_state='collapsed'
    )
    default_markdown()

    st.header(body='Generate Metric')
    st.write("""
        <b>DBT Metric</b> 은 미리 생성해놓은 dbt model 을 이용하여 빠르게 metric 을 생성할 수 있습니다.
        이 앱은 사용자가 클릭으로 DBT Metric을 생성하여 사용자가 데이터를 쉽게 이해하는 것을 목표로 합니다.

        앱은 간단한 UI를 가지며 사용자가 Metric 생성을 위해 필요한 정보를 입력하고, 그에 따라 DBT를 사용해 Metric 을 생성합니다.
        간편하게 Metric을 생성하고, lightdash 로 시각화하여 데이터를 더욱 쉽게 이해할 수 있습니다.
        """, unsafe_allow_html=True)

    st.subheader(body='Select model')
    st.write('메트릭 생성을 위한 모델을 선택해주세요.')
    st.selectbox(
        label='메트릭 생성을 원하는 테이블 목록을 나타냅니다. description 을 확인할 수 있으니 살펴보시고 눌러주세요.',
        options=''
    )


if __name__ == '__main__':
    editor_view()
