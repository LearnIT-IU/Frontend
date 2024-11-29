import streamlit as st

st.set_page_config(page_title="Main Page", page_icon="🏠", layout="centered")

# Check login state
# if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
   # st.warning("You need to log in to access this page!")
   # st.stop()

# Main page content
st.title("Welcome to the main page!")
st.write("This is the main page of the application.")

uploaded_file = st.file_uploader("Choose a file", type=["csv"])

if uploaded_file is not None:
    st.write("File uploaded...")

if st.button("logout"):
    st.session_state['logged_in'] = False
    st.experimental_rerun()

# Create two columns for layout
col1, col2 = st.columns([1, 1], gap="medium")

# Left column: Answer by Student
with col1:
    st.markdown("Answer by Student")
    st.write("This is the answer by student")
    st.text_area("Student's Answer", placeholder="Displays the answer by student", height=200)

# Right column: Answer by AI
with col2:
    st.markdown("Answer by AI")
    st.write("This is the answer by AI")
    st.text_area("AI's Answer", placeholder="Displays the answer by AI", height=200)