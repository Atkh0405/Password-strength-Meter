import streamlit as st
import re

# Page Title
st.markdown("<h1 style='text-align: center; color: #4B8BBE;'>🔐 Password Strength Checker</h1>", unsafe_allow_html=True)

password = st.text_input("Enter your password to evaluate:")

feedback = []
score = 0

if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔸 Password must be **at least 8 characters** long.")

    # Uppercase and Lowercase Check
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("🔸 Include **both uppercase and lowercase** letters.")

    # Digit Check
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("🔸 Include **at least one number** (0-9).")

    # Special Character Check
    if re.search(r'[$@&*]', password):
        score += 1
    else:
        feedback.append("🔸 Include **at least one special character** ($ @ & *).")

    # Display Result
    st.markdown("### 🔍 Password Analysis")

    if score == 4:
        st.success("✅ Your password is **strong**.")
    elif score == 3:
        st.warning("🟡 Your password is **moderate**. Consider strengthening it.")
    elif score == 2:
        st.warning("🟠 Your password is **weak**. Improvements needed.")
    elif score == 1:
        st.error("🔴 Your password is **very weak**. Please improve it.")
    else:
        st.error("❌ Your password does not meet any of the requirements.")

    # Show Suggestions
    if feedback:
        st.markdown("### 💡 Suggestions to Improve Your Password")
        for suggest in feedback:
            st.markdown(f"- {suggest}")
else:
    st.info("💬 Please enter a password to check its strength.")