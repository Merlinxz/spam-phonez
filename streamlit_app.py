import streamlit as st
import time
from spam_generator import generate_spam_messages

def format_phone_number(phone_number):
    cleaned_number = ''.join(filter(str.isdigit, phone_number))
    if len(cleaned_number) == 10:
        return f"{cleaned_number[:3]}-{cleaned_number[3:6]}-{cleaned_number[6:]}"
    return phone_number

def animated_text(text, delay=0.05):
    placeholder = st.empty()
    for i in range(len(text) + 1):
        placeholder.markdown(f"<h1 style='text-align: center;'>{text[:i]}</h1>", unsafe_allow_html=True)
        time.sleep(delay)

def main():
    st.set_page_config(page_title="Spam Attacker Pro", layout="wide")
    
    # Animated title
    animated_text("🚀 Spam Attacker Pro")
    
    # Create two columns for layout
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Configuration")
        raw_phone_number = st.text_input("📱 Phone Number (10 digits)", "")
        phone_number = format_phone_number(raw_phone_number)
        num_messages = st.slider("📊 Number of Messages", min_value=1, max_value=999999, value=10)
        delay_between_messages = st.slider("⏱️ Delay Between Messages (seconds)", min_value=1, max_value=15, value=2)
        
        # Create two columns for buttons
        button_col1, button_col2 = st.columns(2)
        with button_col1:
            generate_button = st.button("🎲 Generate", use_container_width=True)
        with button_col2:
            send_button = st.button('📤 Send', use_container_width=True)
    
    with col2:
        # Generate spam messages
        if generate_button:
            if len(raw_phone_number) != 10 or not raw_phone_number.isdigit():
                st.error("❌ Please enter a valid 10-digit phone number.")
            else:
                with st.spinner("🔄 Generating spam messages..."):
                    generated_messages = generate_spam_messages(num_messages)
                    
                    # Animated success message
                    success_placeholder = st.empty()
                    for i in range(5):
                        success_placeholder.success(f"{'🎉 ' * i}Spam messages generated successfully!{'🎉 ' * i}")
                        time.sleep(0.3)
                    
                    # Displaying generated messages with animation
                    with st.expander("📝 Generated Messages", expanded=True):
                        for message in generated_messages:
                            st.write(message)
                            time.sleep(0.1)
                    
                    st.text_area("📜 Message Preview", value="\n".join(generated_messages), height=300)
        
        # Send spam messages
        if send_button:
            if len(raw_phone_number) != 10 or not raw_phone_number.isdigit():
                st.error('❌ Please enter a valid phone number.')
            else:
                message_placeholder = st.empty()
                progress_placeholder = st.progress(0)
                sending_placeholder = st.empty()
                
                with st.spinner('📡 Sending spam messages...'):
                    for i in range(num_messages):
                        message = generate_spam_messages(1)[0]  # Generate a single message
                        message_placeholder.markdown(f"**Spam message {i+1}/{num_messages} to Number {phone_number}:**\n\n{message}")
                        
                        # Animated sending indicator
                        for j in range(3):
                            sending_placeholder.markdown(f"Sending{'.' * (j + 1)}")
                            time.sleep(delay_between_messages / 3)
                        
                        if i < num_messages - 1:
                            message_placeholder.empty()
                            sending_placeholder.empty()
                        
                        progress_placeholder.progress((i + 1) / num_messages)
                    
                    # Animated success message
                    success_placeholder = st.empty()
                    for i in range(5):
                        success_placeholder.success(f"{'🚀 ' * i}Spam messages sent successfully!{'🚀 ' * i}")
                        time.sleep(0.3)

if __name__ == "__main__":
    main()