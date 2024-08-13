import streamlit as st
import time
from spam_generator import generate_spam_messages

def main():
    st.title('Spam Attacker')

    # Input field for phone number
    phone_number = st.text_input('Enter phone number')

    # Validate phone number to ensure it's numeric and exactly 10 digits long
    if phone_number and (not phone_number.isdigit() or len(phone_number) != 10):
        st.error('Please enter a valid phone number containing exactly 10 digits.')
        return

    # Input field for spam count
    spam_count = st.number_input('Number of spam messages', min_value=1, max_value=999, value=1)

    # Input field for delay between messages
    delay = st.slider('Delay between messages (seconds)', min_value=1, max_value=50, value=1)

    if st.button('Attack'):
        if phone_number:
            # Placeholder for spam messages
            message_placeholder = st.empty()
            progress_placeholder = st.progress(0)  # Placeholder for progress bar

            with st.spinner('Sending spam messages...'):
                messages = generate_spam_messages(spam_count)
                for i, message in enumerate(messages, start=1):
                    # Update the placeholder with the current spam count and message
                    message_placeholder.write(f'Spam message {i}/{spam_count} to Number {phone_number}:\n\n{message}')
                    time.sleep(delay)  # Delay based on user input
                    if i < spam_count:  # Clear only if more messages are to be sent
                        message_placeholder.empty()
                    
                    # Update progress bar
                    progress_placeholder.progress(i / spam_count)

                st.success('Spam messages sent successfully!')
        else:
            st.error('Please enter a phone number.')

if __name__ == '__main__':
    main()
