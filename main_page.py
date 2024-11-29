import streamlit as st

st.set_page_config(page_title="Main Page", page_icon="🏠", layout="centered")

# Check login state
if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
    st.warning("You need to log in to access this page!")
    st.stop()

# Main page content
st.title("Welcome to the main page!")
st.write("This is the main page of the application.")
if st.button("logout"):
    st.session_state['logged_in'] = False
    st.experimental_rerun()