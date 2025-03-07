import streamlit as st
import re
import random
import string

def check_password_strength(password):
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("📏 Password should be at least 8 characters long.")
    
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("🔡 Include at least one uppercase letter.")
    
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("🔠 Include at least one lowercase letter.")
    
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("🔢 Include at least one digit (0-9).")
    
    if any(char in "!@#$%^&*" for char in password):
        score += 1
    else:
        feedback.append("❗ Include at least one special character (!@#$%^&*).")
    
    return score, feedback

def generate_strong_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(12))

# Load saved passwords from session state
if 'saved_passwords' not in st.session_state:
    st.session_state.saved_passwords = []

# Streamlit UI
st.set_page_config(page_title="🔐 Password Strength Meter", page_icon="🔑", layout="wide")

st.markdown(
    """
    <style>
        body {
            background-color: #0f0f0f;
            color: white;
            font-family: Arial, sans-serif;
        }
        .main-container {
            text-align: center;
        }
        .stTextInput > div > div > input {
            border-radius: 10px;
            padding: 12px;
            font-size: 18px;
            border: 2px solid #ff9800;
            background-color: #222;
            color: white;
        }
        .password-strength {
            font-size: 22px;
            font-weight: bold;
            padding: 12px;
            border-radius: 10px;
            margin-top: 15px;
            display: inline-block;
        }
        .strong {
            background-color: #4caf50;
            color: white;
        }
        .moderate {
            background-color: #ff9800;
            color: white;
        }
        .weak {
            background-color: #f44336;
            color: white;
        }
        .stButton > button {
            background: linear-gradient(to right, #ff9800, #ff5722);
            color: white;
            border-radius: 10px;
            font-size: 16px;
            padding: 12px;
        }
        .generated-password {
            font-size: 18px;
            color: #ff9800;
            font-weight: bold;
            margin-top: 10px;
        }
        .saved-passwords-box {
            background-color: #222;
            border-radius: 10px;
            padding: 15px;
            margin-top: 20px;
            color: #ff9800;
            font-size: 16px;
            font-weight: bold;
        }
        .saved-password-button {
            background: linear-gradient(to right, #4caf50, #2e7d32);
            color: white;
            border-radius: 10px;
            font-size: 14px;
            padding: 8px;
            margin-top: 5px;
            width: 100%;
            text-align: center;
            font-weight: bold;
            cursor: pointer;
        }
        .delete-button {
            background: linear-gradient(to right, #f44336, #d32f2f);
            color: white;
            border-radius: 10px;
            font-size: 14px;
            padding: 8px;
            margin-top: 10px;
            width: 100%;
            text-align: center;
            font-weight: bold;
            cursor: pointer;
        }
        .footer {
            text-align: center;
            margin-top: 20px;
            font-size: 16px;
            color: #bbb;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🔐 Password Strength Meter")
st.write("Enter your password to check its strength.")

password = st.text_input("Enter Password", type="password")

if password:
    score, feedback = check_password_strength(password)
    
    if score == 5:
        st.markdown("<div class='password-strength strong'>✅ Strong Password!</div>", unsafe_allow_html=True)
    elif score >= 3:
        st.markdown("<div class='password-strength moderate'>⚠️ Moderate Password! Consider improving it.</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='password-strength weak'>❌ Weak Password! Improve security.</div>", unsafe_allow_html=True)
    
    st.write(f"🔢 Password Length: {len(password)} characters")
    
    for tip in feedback:
        st.write(f"- {tip}")
    
    # Save password in session state
    st.session_state.saved_passwords.append(password)

if st.button("🔄 Generate Strong Password"):
    strong_password = generate_strong_password()
    st.markdown(f"<div class='generated-password'>Generated Password: {strong_password}</div>", unsafe_allow_html=True)

if st.session_state.saved_passwords:
    st.subheader("🔐 Saved Passwords")
    st.markdown("<div class='saved-passwords-box'>", unsafe_allow_html=True)
    for saved_pass in st.session_state.saved_passwords:
        st.markdown(f"<button class='saved-password-button'>{saved_pass}</button>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Delete button
    if st.button("🗑️ Delete All Saved Passwords"):
        st.session_state.saved_passwords = []

st.markdown("<div class='footer'>Developed by <b>Farhad Gul</b></div>", unsafe_allow_html=True)
 