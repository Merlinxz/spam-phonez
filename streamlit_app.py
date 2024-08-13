import streamlit as st
import time
from spam_generator import generate_spam_messages
import random

def format_phone_number(phone_number):
    cleaned_number = ''.join(filter(str.isdigit, phone_number))
    if len(cleaned_number) == 10:
        return f"{cleaned_number[:3]}-{cleaned_number[3:6]}-{cleaned_number[6:]}"
    return phone_number

def animated_text(text, delay=0.05):
    placeholder = st.empty()
    for i in range(len(text) + 1):
        placeholder.markdown(f"**{text[:i]}**")
        time.sleep(delay)

def main():
    st.set_page_config(page_title="Spam Attacker Pro", layout="wide")
    
    # Animated title
    animated_text("🚀 Spam Attacker Pro")
    st.subheader("Generate and Send Spam Messages with Style")
    
    # Sidebar Configuration
    st.sidebar.title("Spam Attacker Options")
    st.sidebar.subheader("Configuration")
    
    # Input fields with improved styling
    raw_phone_number = st.sidebar.text_input("📱 Phone Number (10 digits)", "")
    phone_number = format_phone_number(raw_phone_number)
    num_messages = st.sidebar.slider("📊 Number of Messages", min_value=1, max_value=100, value=10)
    delay_between_messages = st.sidebar.slider("⏱️ Delay Between Messages (seconds)", min_value=1, max_value=10, value=2)
    
    # Session state to persist messages
    if 'spam_messages' not in st.session_state:
        st.session_state.spam_messages = []
    
    # Button to generate spam messages
    if st.sidebar.button("🎲 Generate Spam Messages"):
        if len(raw_phone_number) != 10 or not raw_phone_number.isdigit():
            st.error("❌ Please enter a valid 10-digit phone number.")
        else:
            with st.spinner("🔄 Generating spam messages..."):
                st.session_state.spam_messages = generate_spam_messages(num_messages)
                
                # Animated success message
                success_placeholder = st.empty()
                for i in range(5):
                    success_placeholder.success(f"{'🎉 ' * i}Spam messages generated successfully!{'🎉 ' * i}")
                    time.sleep(0.3)
                
                # Displaying generated messages with animation
                with st.expander("📝 Generated Messages"):
                    for message in st.session_state.spam_messages:
                        st.write(message)
                        time.sleep(0.1)
                
                st.text_area("📜 Message Preview", value="\n".join(st.session_state.spam_messages), height=300)
    
    # Button to send spam messages
    if st.sidebar.button('📤 Send Spam Messages'):
        if not st.session_state.spam_messages:
            st.error('❌ No spam messages generated. Please generate messages first.')
        elif len(raw_phone_number) != 10 or not raw_phone_number.isdigit():
            st.error('❌ Please enter a valid phone number.')
        else:
            message_placeholder = st.empty()
            progress_placeholder = st.progress(0)
            
            with st.spinner('📡 Sending spam messages...'):
                for i, message in enumerate(st.session_state.spam_messages, start=1):
                    message_placeholder.markdown(f"**Spam message {i}/{num_messages} to Number {phone_number}:**\n\n{message}")
                    
                    # Animated sending indicator
                    for _ in range(3):
                        st.sidebar.markdown(f"Sending{'.' * (_ + 1)}")
                        time.sleep(delay_between_messages / 3)
                    
                    if i < num_messages:
                        message_placeholder.empty()
                    
                    progress_placeholder.progress(i / num_messages)
                
                # Animated success message
                success_placeholder = st.empty()
                for i in range(5):
                    success_placeholder.success(f"{'🚀 ' * i}Spam messages sent successfully!{'🚀 ' * i}")
                    time.sleep(0.3)

if __name__ == "__main__":
    main()