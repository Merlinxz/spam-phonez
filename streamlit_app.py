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
        placeholder.markdown(f"<h1 style='text-align: center; color: #FF4B4B;'>{text[:i]}</h1>", unsafe_allow_html=True)
        time.sleep(delay)

def pulsing_text(text, iterations=5):
    placeholder = st.empty()
    for _ in range(iterations):
        for size in range(20, 30, 2):
            placeholder.markdown(f"<h1 style='text-align: center; font-size: {size}px;'>{text}</h1>", unsafe_allow_html=True)
            time.sleep(0.1)
        for size in range(30, 20, -2):
            placeholder.markdown(f"<h1 style='text-align: center; font-size: {size}px;'>{text}</h1>", unsafe_allow_html=True)
            time.sleep(0.1)

def main():
    st.set_page_config(page_title="Spam Attacker Pro", layout="wide", page_icon="🚀")
    
    # Custom CSS
    st.markdown("""
    <style>
    .stButton>button {
        color: #ffffff;
        background-color: #FF4B4B;
        border-radius: 20px;
    }
    .stProgress > div > div > div {
        background-color: #FF4B4B;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Animated title
    animated_text("🚀 Spam Attacker Pro")
    
    # Create two columns for layout
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("<h3 style='text-align: center; color: #FF4B4B;'>Configuration</h3>", unsafe_allow_html=True)
        raw_phone_number = st.text_input("📱 Phone Number (10 digits)", "")
        phone_number = format_phone_number(raw_phone_number)
        num_messages = st.number_input("📊 Number of Messages", min_value=1, max_value=99999, value=10)
        delay_between_messages = st.slider("⏱️ Delay Between Messages", min_value=1, max_value=15, value=2, format="%d seconds")
        
        # Create two columns for buttons
        button_col1, button_col2 = st.columns(2)
        with button_col1:
            generate_button = st.button("🎲 Generate", use_container_width=True)
        with button_col2:
            send_button = st.button('📤 Send', use_container_width=True)
        
        # Add a fun fact section
        st.markdown("---")
        st.markdown("<h4 style='text-align: center; color: #FF4B4B;'>Fun Fact</h4>", unsafe_allow_html=True)
        fun_facts = [
            "The term 'spam' for junk messages comes from a Monty Python sketch!",
            "The first spam email was sent in 1978 to 600 people.",
            "Over 50% of all emails sent are considered spam.",
            "The most common language for spam emails is English.",
            "Some countries have laws specifically against spamming!"
        ]
        st.info(random.choice(fun_facts))
    
    with col2:
        # Generate spam messages
        if generate_button:
            if len(raw_phone_number) != 10 or not raw_phone_number.isdigit():
                st.error("❌ Please enter a valid 10-digit phone number.")
            else:
                with st.spinner("🔄 Generating spam messages..."):
                    generated_messages = generate_spam_messages(num_messages)
                    
                    # Animated success message
                    pulsing_text("🎉 Spam messages generated successfully! 🎉")
                    
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
                    for i in range(int(num_messages)):
                        message = generate_spam_messages(1)[0]  # Generate a single message
                        message_placeholder.markdown(f"**Spam message {i+1}/{num_messages} to Number {phone_number}:**\n\n{message}")
                        
                        # Animated sending indicator
                        for j in range(3):
                            sending_placeholder.markdown(f"<h3 style='text-align: center; color: #FF4B4B;'>Sending{'.' * (j + 1)}</h3>", unsafe_allow_html=True)
                            time.sleep(delay_between_messages / 3)
                        
                        if i < num_messages - 1:
                            message_placeholder.empty()
                            sending_placeholder.empty()
                        
                        progress_placeholder.progress((i + 1) / num_messages)
                    
                    # Animated success message
                    pulsing_text("🚀 Spam messages sent successfully! 🚀")

if __name__ == "__main__":
    main()