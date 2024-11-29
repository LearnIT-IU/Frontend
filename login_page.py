import json
import streamlit as st

# Set page configuration
st.set_page_config(page_title="Login Page", page_icon="🔒", layout="centered")

# Commonwealth-styled HTML and CSS
COMMONWEALTH_STYLE = """
<style>
    body {
        font-family: 'Arial', sans-serif;
        background: linear-gradient(to bottom right, #283048, #859398);
        color: #fff;
    }
    .login-container {
        width: 100%;
        max-width: 400px;
        margin: auto;
        padding: 20px;
        background: rgba(0, 0, 0, 0.7);
        border-radius: 10px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3);
    }
    .login-container h2 {
        text-align: center;
        color: #fff;
    }
    .login-container label {
        font-weight: bold;
        margin-top: 10px;
    }
    .login-container input {
        width: 100%;
        padding: 10px;
        margin: 5px 0 20px;
        border: none;
        border-radius: 5px;
    }
    .login-container button {
        width: 100%;
        padding: 10px;
        background: #1e90ff;
        color: #fff;
        font-weight: bold;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background 0.3s ease;
    }
    .login-container button:hover {
        background: #4682b4;
    }
</style>
"""

# Embed the style
st.markdown(COMMONWEALTH_STYLE, unsafe_allow_html=True)

# Load demo credentials from config.json
def load_credentials():
    with open('config.json') as f:
        return json.load(f)["users"]
    
# Authenticate user by email and password
def authenticate(email, password):
    user = load_credentials()
    for user in user:
        if user['email'] == email and user['password'] == password:
            return True
        return False

# Iniitialize session state for login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Redirect to main page if logged in
if st.session_state.logged_in:
    st.experimental_rerun()

# Login Form
st.markdown("<h2>Login</h2>", unsafe_allow_html=True)
email = st.text_input("Email", placeholder="Enter your email")
password = st.text_input("Password", type="password", placeholder="Enter your password")
login_button = st.button("Login")

# Handle login
if login_button:
    if authenticate(email, password):
        st.success
        st.write
        st.experimental_rerun()
    else:
        st.error("Invalid email or password")