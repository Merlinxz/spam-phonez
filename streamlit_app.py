import streamlit as st
import time
import random
from spam_generator import generate_spam_messages

def format_phone_number(phone_number):
    cleaned_number = ''.join(filter(str.isdigit, phone_number))
    if len(cleaned_number) == 10:
        return f"{cleaned_number[:3]}-{cleaned_number[3:6]}-{cleaned_number[6:]}"
    return phone_number

def animated_text(text, delay=0.05):
    placeholder = st.empty()
    for i in range(len(text) + 1):
        placeholder.markdown(f"<h1 style='text-align: center; color: #FF4B4B;'>{text[:i]}</h1>", unsafe_allow_html=True)
        time.sleep(delay)

def generate_fake_phone_number():
    return f"{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"

def main():
    st.set_page_config(page_title="Spam Attacker Pro 2.0", layout="wide")
    
    # Animated title
    animated_text("🚀 Spam Attacker Pro 2.0")
    
    # Create two columns for layout
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("📊 Message Settings")
        target_type = st.radio("👤 Target Type", ["Single Number", "Multiple Numbers"])
        
        if target_type == "Single Number":
            raw_phone_number = st.text_input("📱 Phone Number (10 digits)", "")
            phone_number = format_phone_number(raw_phone_number)
        else:
            num_targets = st.number_input("🎯 Number of Targets", min_value=1, max_value=100, value=5)
            target_numbers = [generate_fake_phone_number() for _ in range(num_targets)]
            st.write("Generated Target Numbers:", ", ".join(target_numbers))
        
        num_messages = st.number_input("📨 Number of Messages", min_value=1, max_value=99999, value=10)
        delay_between_messages = st.number_input("⏱️ Delay Between Messages (seconds)", min_value=0.1, max_value=15.0, value=2.0, step=0.1)
        
        st.subheader("🎛️ Advanced Options")
        message_type = st.selectbox("💬 Message Type", ["Random", "Sequential", "Custom"])
        if message_type == "Custom":
            custom_message = st.text_area("✍️ Enter your custom message template")
        
        use_proxies = st.checkbox("🔒 Use Proxy Servers")
        if use_proxies:
            proxy_list = st.text_area("Enter proxy servers (one per line)")
        
        # Create two columns for buttons
        button_col1, button_col2 = st.columns(2)
        with button_col1:
            generate_button = st.button("🎲 Generate", use_container_width=True)
        with button_col2:
            send_button = st.button('📤 Send', use_container_width=True)
    
    with col2:
        # Generate spam messages
        if generate_button:
            if target_type == "Single Number" and (len(raw_phone_number) != 10 or not raw_phone_number.isdigit()):
                st.error("❌ Please enter a valid 10-digit phone number.")
            else:
                with st.spinner("🔄 Generating spam messages..."):
                    if message_type == "Custom":
                        generated_messages = [custom_message] * num_messages
                    else:
                        generated_messages = generate_spam_messages(num_messages, message_type)
                    
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
            if target_type == "Single Number" and (len(raw_phone_number) != 10 or not raw_phone_number.isdigit()):
                st.error('❌ Please enter a valid phone number.')
            else:
                message_placeholder = st.empty()
                progress_placeholder = st.progress(0)
                sending_placeholder = st.empty()
                
                with st.spinner('📡 Sending spam messages...'):
                    total_messages = num_messages * (1 if target_type == "Single Number" else num_targets)
                    for i in range(total_messages):
                        message = generate_spam_messages(1, message_type)[0]
                        if target_type == "Single Number":
                            target = phone_number
                        else:
                            target = random.choice(target_numbers)
                        
                        message_placeholder.markdown(f"**Spam message {i+1}/{total_messages} to Number {target}:**\n\n{message}")
                        
                        # Animated sending indicator
                        for j in range(3):
                            sending_placeholder.markdown(f"Sending{'.' * (j + 1)}")
                            time.sleep(delay_between_messages / 3)
                        
                        if i < total_messages - 1:
                            message_placeholder.empty()
                            sending_placeholder.empty()
                        
                        progress_placeholder.progress((i + 1) / total_messages)
                    
                    # Animated success message
                    success_placeholder = st.empty()
                    for i in range(5):
                        success_placeholder.success(f"{'🚀 ' * i}Spam messages sent successfully!{'🚀 ' * i}")
                        time.sleep(0.3)
    
    # Footer
    st.markdown("---")
    st.markdown("📊 Spam Attacker Pro 2.0 - For educational purposes only")

if __name__ == "__main__":
    main()