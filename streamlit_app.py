import streamlit as st
import time
from spam_generator import generate_spam_messages

def streamlit():
    st.markdown(
        "![Streamlit App](https://img.shields.io/badge/Streamlit-Example-green)"
    )

def main():
    st.set_page_config(page_title="Spam Attacker", layout="wide")

    # Application Header
    st.title("Spam Attacker")
    st.subheader("Generate and Send Spam Messages")

    # Add Streamlit Badge
    streamlit()

    # Sidebar Configuration
    st.sidebar.title("Spam Attacker Options")
    st.sidebar.subheader("Configuration")

    # Input fields
    phone_number = st.sidebar.text_input("Phone Number (10 digits)", "")
    num_messages = st.sidebar.number_input("Number of Messages", min_value=1, max_value=100, value=1)
    delay_between_messages = st.sidebar.slider("Delay Between Messages (seconds)", min_value=1, max_value=5, value=1)

    # Session state to persist messages
    if 'spam_messages' not in st.session_state:
        st.session_state.spam_messages = []

    # Button to generate spam messages
    if st.sidebar.button("Generate Spam Messages"):
        if len(phone_number) != 10 or not phone_number.isdigit():
            st.error("Please enter a valid 10-digit phone number.")
        else:
            with st.spinner("Generating spam messages..."):
                st.session_state.spam_messages = generate_spam_messages(num_messages)
                st.success("Spam messages generated successfully.")
                
                # Displaying generated messages
                with st.expander("Generated Messages"):
                    for message in st.session_state.spam_messages:
                        st.write(message)
                
                st.text_area("Message Preview", value="\n".join(st.session_state.spam_messages), height=300)

    # Button to send spam messages
    if st.sidebar.button('Send Spam Messages'):
        if not st.session_state.spam_messages:
            st.error('No spam messages generated. Please generate messages first.')
        elif len(phone_number) != 10 or not phone_number.isdigit():
            st.error('Please enter a valid phone number.')
        else:
            # Placeholder for spam messages
            message_placeholder = st.empty()
            progress_placeholder = st.progress(0)  # Placeholder for progress bar

            with st.spinner('Sending spam messages...'):
                for i, message in enumerate(st.session_state.spam_messages, start=1):
                    # Update the placeholder with the current spam count and message
                    message_placeholder.write(f'Spam message {i}/{num_messages} to Number {phone_number}:\n\n{message}')
                    time.sleep(delay_between_messages)  # Delay based on user input
                    if i < num_messages:  # Clear only if more messages are to be sent
                        message_placeholder.empty()
                    
                    # Update progress bar
                    progress_placeholder.progress(i / num_messages)

                st.success('Spam messages sent successfully!')

if __name__ == "__main__":
    main()
