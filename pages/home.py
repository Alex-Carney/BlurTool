import streamlit as st


def app():
    # Only render the background image for home page
    if st.session_state.current_page == 'Home':
        st.markdown(
            f"""
             <style>
             .stApp {{
                 background: url("https://images.unsplash.com/photo-1465146344425-f00d5f5c8f07?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=876&q=80");
                 background-size: contain;
                 background-repeat: no-repeat;
                 -webkit-background-size: cover;
             }}
             </style>
             """,
            unsafe_allow_html=True
        )

        st.markdown("<h1 style='text-align: center; color: black; font-style: italic;'>Suprbluur</h1>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; color: grey; font-style: italic;'>Built by Alex Carney and Jane O'Reilly</h4>", unsafe_allow_html=True)
