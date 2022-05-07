import streamlit as st

# Custom imports
from common.multipage import MultiPage
from pages import home, tool  # import your pages here




# Create an instance of the app
app = MultiPage()





# First command must be setting configs
# Initial Settings ------------------------
st.set_page_config(layout="wide")

# Title of the main page
# st.title("Carney Phase Plane Visualizer")
#st.markdown("<h1 style='text-align: center; color: red;'>Carney Phase Plane Visualizer</h1>", unsafe_allow_html=True)

if 'current_page' not in st.session_state:
    st.session_state.current_page = 'Home'

# Add all your applications (pages) here
app.add_page("Home", home.app)
app.add_page("Blur Tool", tool.app)


# The main app
app.run()