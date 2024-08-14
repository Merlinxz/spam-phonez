import streamlit as st
import time
import random
import pandas as pd
import plotly.express as px
from spam_generator import generate_spam_messages

def format_phone_number(phone_number):
    cleaned_number = ''.join(filter(str.isdigit, phone_number))
    if len(cleaned_number) == 10:
        return f"{cleaned_number[:3]}-{cleaned_number[3:6]}-{cleaned_number[6:]}"
    return ""  # Return an empty string if the phone number is not exactly 10 digits

def animated_text(text, delay=0.05):
    placeholder = st.empty()
    for i in range(len(text) + 1):
        placeholder.markdown(f"<h1 style='text-align: center; color: #FF4B4B;'>{text[:i]}</h1>", unsafe_allow_html=True)
        time.sleep(delay)

def generate_report(target_numbers, num_messages):
    data = {
        "Phone Number": target_numbers,
        "Messages Sent": [num_messages] * len(target_numbers),
        "Delivery Rate": [random.uniform(0.8, 1.0) for _ in target_numbers],
        "Response Rate": [random.uniform(0.0, 0.2) for _ in target_numbers]
    }
    df = pd.DataFrame(data)
    return df

def plot_delivery_rates(df):
    fig = px.bar(df, x="Phone Number", y="Delivery Rate", title="Message Delivery Rates")
    return fig

def plot_response_rates(df):
    fig = px.scatter(df, x="Messages Sent", y="Response Rate", hover_data=["Phone Number"], title="Response Rates vs Messages Sent")
    return fig

def main():
    st.set_page_config(page_title="Spam Attacker Pro 3.0", layout="wide")
    
    # Animated title
    animated_text("🚀 Spam Attacker Pro 3.0")
    
    # Main content area
    tabs = st.tabs(["📊 Campaign Setup", "📈 Analytics", "⚙️ Advanced Settings"])
    
    with tabs[0]:
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.subheader("📱 Target Setup")
            target_type = st.radio("👤 Target Type", ["Single Number", "Multiple Numbers", "Import from CSV"])
            
            if target_type == "Single Number":
                raw_phone_number = st.text_input("📱 Phone Number (10 digits)", "")
                target_numbers = [format_phone_number(raw_phone_number)] if format_phone_number(raw_phone_number) else []
            elif target_type == "Multiple Numbers":
                st.write("📱 Enter phone numbers (one per line):")
                raw_numbers = st.text_area("", height=150)
                target_numbers = [format_phone_number(num.strip()) for num in raw_numbers.split('\n') if format_phone_number(num.strip())]
            else:
                uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
                if uploaded_file is not None:
                    df = pd.read_csv(uploaded_file)
                    target_numbers = [format_phone_number(num) for num in df['Phone Number'].astype(str)]
                    # Show phone numbers in an expandable box
                    with st.expander("📋 Phone Numbers from CSV", expanded=True):
                        for number in target_numbers:
                            if number:  # Ensure the number is not an empty string
                                st.write(number)
                else:
                    target_numbers = []
            
            st.write(f"Number of target numbers: {len(target_numbers)}")
        
        with col2:
            st.subheader("💬 Message Setup")
            num_messages = st.number_input("📨 Number of Messages per Target", min_value=1, max_value=99999, value=10)
            delay_between_messages = st.number_input("⏱️ Delay Between Messages (seconds)", min_value=0.1, max_value=15.0, value=2.0, step=0.1)
            message_type = st.selectbox("💬 Message Type", ["Random", "Sequential", "Custom"])
            if message_type == "Custom":
                custom_message = st.text_area("✍️ Enter your custom message template")
    
    with tabs[1]:
        if 'report_data' not in st.session_state:
            st.session_state.report_data = None
        
        if st.button("📊 Generate Report"):
            if not target_numbers:
                st.error("❌ Please enter at least one valid phone number.")
            else:
                with st.spinner("Generating report..."):
                    st.session_state.report_data = generate_report(target_numbers, num_messages)
                    st.success("✅ Report generated successfully!")
        
        if st.session_state.report_data is not None:
            st.subheader("📊 Campaign Analytics")
            col1, col2 = st.columns(2)
            with col1:
                st.plotly_chart(plot_delivery_rates(st.session_state.report_data))
            with col2:
                st.plotly_chart(plot_response_rates(st.session_state.report_data))
            
            st.subheader("📑 Detailed Report")
            st.dataframe(st.session_state.report_data)
    
    with tabs[2]:
        st.subheader("🛠️ Advanced Settings")
        use_proxies = st.checkbox("🔒 Use Proxy Servers")
        if use_proxies:
            proxy_list = st.text_area("Enter proxy servers (one per line)")
        
        st.subheader("⏱️ Scheduling")
        use_schedule = st.checkbox("📅 Schedule Campaign")
        if use_schedule:
            schedule_date = st.date_input("Select start date")
            schedule_time = st.time_input("Select start time")
        
        st.subheader("📈 A/B Testing")
        use_ab_testing = st.checkbox("🔬 Enable A/B Testing")
        if use_ab_testing:
            message_a = st.text_area("Message A")
            message_b = st.text_area("Message B")
            split_ratio = st.slider("A/B Split Ratio", 0.0, 1.0, 0.5)
    
    # Action buttons
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🎲 Generate Messages", use_container_width=True):
            if not target_numbers:
                st.error("❌ Please enter at least one valid phone number.")
            else:
                with st.spinner("🔄 Generating spam messages..."):
                    if message_type == "Custom":
                        generated_messages = [custom_message] * num_messages
                    else:
                        generated_messages = generate_spam_messages(num_messages, message_type)
                    
                    st.success("✅ Messages generated successfully!")
                    
                    # Display generated messages
                    with st.expander("📝 Generated Messages", expanded=True):
                        for message in generated_messages:
                            st.write(message)
    
    with col2:
        if st.button("📤 Send Messages", use_container_width=True):
            if not target_numbers:
                st.error("❌ Please enter at least one valid phone number.")
            else:
                with st.spinner("📡 Simulating message sending..."):
                    if message_type == "Custom":
                        messages = [custom_message] * num_messages
                    else:
                        messages = generate_spam_messages(num_messages, message_type)
                    
                    placeholder = st.empty()
                    progress_bar = st.progress(0)
                    countdown_placeholder = st.empty()
                    
                    try:
                        total_messages = len(messages)
                        sent_messages = []
                        total_time = total_messages * delay_between_messages
                        
                        for i, message in enumerate(messages):
                            time.sleep(delay_between_messages)
                            # Simulate sending message
                            recipient = random.choice(target_numbers)
                            sent_message = f"📩 Sent to {recipient}: {message}"
                            sent_messages.append(sent_message)
                            # Update placeholder and progress bar
                            placeholder.markdown(f"<p style='text-align: center;'>{sent_message}</p>", unsafe_allow_html=True)
                            progress = (i + 1) / total_messages if total_messages > 0 else 1
                            progress_bar.progress(progress)
                            remaining_time = total_time - (i + 1) * delay_between_messages
                            countdown_placeholder.markdown(f"<p style='text-align: center;'>⏳ Time remaining: {remaining_time:.1f} seconds</p>", unsafe_allow_html=True)
                        
                        # Clear placeholder
                        placeholder.empty()
                        countdown_placeholder.empty()
                        
                        # Show success message
                        st.success("✅ Messages sent successfully!")
                    
                    except Exception as e:
                        st.error(f"❌ An error occurred: {e}")
                    
                    # Display sent messages in an expandable box
                    with st.expander("📬 Sent Messages", expanded=True):
                        for msg in sent_messages:
                            st.write(msg)
    
    # Footer
    st.markdown("---")
    st.markdown("<p style='text-align: center;'>📊 Spam Attacker Pro 3.0 - For educational purposes only</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
