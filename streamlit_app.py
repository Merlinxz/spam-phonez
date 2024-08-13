import streamlit as st
import time
import random
from spam_generator import generate_spam_messages

# Set page config at the very beginning
st.set_page_config(page_title="Spam Attacker Pro", layout="wide", page_icon="🚀")

# Custom CSS for better styling
st.markdown("""
<style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        border: none;
        padding: 10px 20px;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #45a049;
        transform: scale(1.05);
    }
    .success-message {
        padding: 10px;
        border-radius: 5px;
        animation: pulse 1s infinite;
    }
    @keyframes pulse {
        0% { box-shadow: 0 0 0 0px rgba(76, 175, 80, 0.7); }
        100% { box-shadow: 0 0 0 10px rgba(76, 175, 80, 0); }
    }
</style>
""", unsafe_allow_html=True)

def format_phone_number(phone_number):
    cleaned_number = ''.join(filter(str.isdigit, phone_number))
    if len(cleaned_number) == 10:
        return f"{cleaned_number[:3]}-{cleaned_number[3:6]}-{cleaned_number[6:]}"
    return phone_number

def animated_text(text, delay=0.05):
    placeholder = st.empty()
    for i in range(len(text) + 1):
        placeholder.markdown(f"<h1 style='text-align: center; color: #4CAF50;'>{text[:i]}</h1>", unsafe_allow_html=True)
        time.sleep(delay)

def loading_animation():
    progress_text = "Operation in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(0.5)
    my_bar.empty()

def main():
    # Animated title
    animated_text("🚀 Spam Attacker Pro")
    
    st.markdown("<h3 style='text-align: center; color: #666;'>Generate and Send Spam Messages with Style</h3>", unsafe_allow_html=True)
    
    # Create two columns for layout
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("<h2 style='color: #4CAF50;'>Configuration</h2>", unsafe_allow_html=True)
        raw_phone_number = st.text_input("📱 Phone Number (10 digits)", "")
        phone_number = format_phone_number(raw_phone_number)
        num_messages = st.number_input("📊 Number of Messages", min_value=1, max_value=99999, value=10)
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
                loading_animation()
                with st.spinner("🔄 Generating spam messages..."):
                    generated_messages = generate_spam_messages(int(num_messages))
                    
                    # Animated success message
                    success_placeholder = st.empty()
                    for i in range(5):
                        success_placeholder.markdown(f"<div class='success-message' style='background-color: rgba(76, 175, 80, 0.1);'>{'🎉 ' * i}Spam messages generated successfully!{'🎉 ' * i}</div>", unsafe_allow_html=True)
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
                
                loading_animation()
                with st.spinner('📡 Sending spam messages...'):
                    for i in range(int(num_messages)):
                        message = generate_spam_messages(1)[0]  # Generate a single message
                        message_placeholder.markdown(f"<div style='background-color: #f0f0f0; padding: 10px; border-radius: 5px;'><strong>Spam message {i+1}/{num_messages} to Number {phone_number}:</strong><br><br>{message}</div>", unsafe_allow_html=True)
                        
                        # Animated sending indicator
                        for j in range(3):
                            sending_placeholder.markdown(f"<div style='text-align: center; font-size: 24px;'>Sending{'.' * (j + 1)}</div>", unsafe_allow_html=True)
                            time.sleep(delay_between_messages / 3)
                        
                        if i < int(num_messages) - 1:
                            message_placeholder.empty()
                            sending_placeholder.empty()
                        
                        progress_placeholder.progress((i + 1) / int(num_messages))
                    
                    # Animated success message
                    success_placeholder = st.empty()
                    for i in range(5):
                        success_placeholder.markdown(f"<div class='success-message' style='background-color: rgba(76, 175, 80, 0.1);'>{'🚀 ' * i}Spam messages sent successfully!{'🚀 ' * i}</div>", unsafe_allow_html=True)
                        time.sleep(0.3)

    # Add a fun fact section
    st.markdown("---")
    st.markdown("<h3 style='text-align: center; color: #4CAF50;'>📚 Fun Fact about Spam</h3>", unsafe_allow_html=True)
    fun_facts = [
        "The term 'spam' for junk messages comes from a Monty Python sketch about spam meat!",
        "The first spam email was sent in 1978 to 400 ARPANET users.",
        "About 85% of all emails sent worldwide are considered spam.",
        "The most common language for spam emails is English, followed by Chinese.",
        "Some countries have laws that make sending unsolicited bulk emails illegal."
    ]
    st.markdown(f"<div style='text-align: center; font-style: italic;'>{random.choice(fun_facts)}</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()