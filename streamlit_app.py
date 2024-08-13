import streamlit as st
import time
from spam_generator import generate_spam_messages

def format_phone_number(phone_number):
    # Remove any non-digit characters
    cleaned_number = ''.join(filter(str.isdigit, phone_number))
    # Format as xxx-xxx-xxxx
    if len(cleaned_number) == 10:
        return f"{cleaned_number[:3]}-{cleaned_number[3:6]}-{cleaned_number[6:]}"
    return phone_number

def main():
    st.set_page_config(page_title="Spam Attacker", layout="wide")

    # Application Header
    st.title("Spam Attacker")
    st.subheader("Generate and Send Spam Messages")

    # Sidebar Configuration
    st.sidebar.title("Spam Attacker Options")
    st.sidebar.subheader("Configuration")

    # Input fields
    raw_phone_number = st.sidebar.text_input("Phone Number (10 digits)", "")
    phone_number = format_phone_number(raw_phone_number)
    num_messages = st.sidebar.deley_input("Number of Messages", min_value=1, max_value=100, value=1)

    # Input for delay between messages
    delay_input = st.sidebar.delay_input("Delay Between Messages (seconds)", "1")
    try:
        delay_between_messages = int(delay_input)
        if delay_between_messages < 1:
            st.error("Delay must be at least 1 second.")
            delay_between_messages = 1
    except ValueError:
        st.error("Please enter a valid integer for the delay.")
        delay_between_messages = 1

    # Session state to persist messages
    if 'spam_messages' not in st.session_state:
        st.session_state.spam_messages = []

    # Button to generate spam messages
    if st.sidebar.button("Generate Spam Messages"):
        if len(raw_phone_number) != 10 or not raw_phone_number.isdigit():
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
        elif len(raw_phone_number) != 10 or not raw_phone_number.isdigit():
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
