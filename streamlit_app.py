import streamlit as st
import random
from streamlit_extras import st_expander, st_animated_header, st_image_comparison
from spam_generator import generate_spam_messages

def main():
    st.set_page_config(page_title="Spam Attacker", layout="wide")

    # Application Header
    st_animated_header("Spam Attacker", animation="pulse", color="blue")

    st.sidebar.title("Spam Attacker Options")
    st.sidebar.subheader("Configuration")

    # Input fields
    phone_number = st.sidebar.text_input("Phone Number (10 digits)", "")
    num_messages = st.sidebar.number_input("Number of Messages", min_value=1, max_value=100, value=10)
    delay_between_messages = st.sidebar.number_input("Delay Between Messages (seconds)", min_value=0, value=1)
    
    if st.sidebar.button("Generate Spam Messages"):
        if len(phone_number) != 10 or not phone_number.isdigit():
            st.error("Please enter a valid 10-digit phone number.")
        else:
            with st.spinner("Generating spam messages..."):
                spam_messages = generate_spam_messages(num_messages)
                st.success("Spam messages generated successfully.")
                
                st.expander("Generated Messages", expanded=True).write("\n".join(spam_messages))
                st.image_comparison("Message Preview", [spam_messages[0]], ["Sample Message"], use_column_width=True)

    st.sidebar.subheader("Settings")
    st.sidebar.selectbox("Theme", ["Light", "Dark"])

if __name__ == "__main__":
    main()
