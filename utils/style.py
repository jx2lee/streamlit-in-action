import os.path

from PIL import Image

HIDE_STREAMLIT_STYLE = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

HIDE_SIDEBAR_STYLE = """
<style>
    div[data-testid="collapsedControl"] {display: none;}
    div[data-testid="stSidebarNav"] {display: none;}
</style>
"""

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUBLIC_DIR = ROOT_DIR + "/public/"
FAVICON_IMG = Image.open(PUBLIC_DIR + 'favicon.ico').resize((300, 300))
