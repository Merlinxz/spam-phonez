import streamlit as st
import os
import time
import json
import random
import pandas as pd
import plotly.express as px
from spam_generator import generate_spam_messages

def format_phone_number(phone_number):
    cleaned_number = ''.join(filter(str.isdigit, phone_number))
    return f"{cleaned_number[:3]}-{cleaned_number[3:6]}-{cleaned_number[6:]}" if len(cleaned_number) == 10 else phone_number

def animated_text(text, delay=0.05):
    placeholder = st.empty()
    for i in range(len(text) + 1):
        placeholder.markdown(f"<h1 style='text-align: center; color: #FF4B4B;'>{text[:i]}</h1>", unsafe_allow_html=True)
        time.sleep(delay)

def generate_report(target_numbers, num_messages, message_type):
    data = {
        "Phone Number": target_numbers,
        "Messages Sent": [num_messages] * len(target_numbers),
        "Delivery Rate": [random.uniform(0.8, 1.0) for _ in target_numbers],
        "Response Rate": [random.uniform(0.0, 0.2) for _ in target_numbers]
    }
    return pd.DataFrame(data)

def plot_delivery_rates(df):
    return px.bar(df, x="Phone Number", y="Delivery Rate", title="Message Delivery Rates")

def plot_response_rates(df):
    return px.scatter(df, x="Messages Sent", y="Response Rate", hover_data=["Phone Number"], title="Response Rates vs Messages Sent")

def save_campaign(campaign_data, filename='campaign_data.json'):
    try:
        with open(filename, 'w') as file:
            json.dump(campaign_data, file, indent=4)
        st.success(f"Campaign saved successfully! File: {filename}")
    except Exception as e:
        st.error(f"An error occurred while saving the campaign: {e}")

def load_campaign(filename='campaign_data.json'):
    try:
        if not os.path.exists(filename):
            st.error("Campaign file not found.")
            return None
        
        with open(filename, 'r') as file:
            return json.load(file)
    except Exception as e:
        st.error(f"An error occurred while loading the campaign: {e}")
        return None

def main():
    st.set_page_config(page_title="Spam Attacker Pro 3.0", layout="wide")
    
    animated_text("🚀 Spam Attacker Pro 3.0")
    
    tabs = st.tabs(["📊 Campaign Setup", "📈 Analytics", "⚙️ Advanced Settings", "💾 Campaign Management"])
    
    with tabs[0]:
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.subheader("📱 Target Setup")
            target_type = st.radio("👤 Target Type", ["Single Number", "Multiple Numbers", "Import from CSV"])
            
            target_numbers = []
            if target_type == "Single Number":
                raw_phone_number = st.text_input("📱 Phone Number (10 digits)", "")
                target_numbers = [format_phone_number(raw_phone_number)] if raw_phone_number else []
            elif target_type == "Multiple Numbers":
                raw_numbers = st.text_area("", height=150)
                target_numbers = [format_phone_number(num.strip()) for num in raw_numbers.split('\n') if num.strip()]
            elif target_type == "Import from CSV":
                uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
                if uploaded_file is not None:
                    df = pd.read_csv(uploaded_file)
                    target_numbers = df['Phone Number'].tolist()
            
            st.write(f"Number of target numbers: {len(target_numbers)}")
        
        with col2:
            st.subheader("💬 Message Setup")
            num_messages = st.number_input("📨 Number of Messages per Target", min_value=1, max_value=99999, value=10)
            delay_between_messages = st.number_input("⏱️ Delay Between Messages (seconds)", min_value=0.1, max_value=15.0, value=2.0, step=0.1)
            message_type = st.selectbox("💬 Message Type", ["Random", "Sequential", "Custom"])
            custom_message = st.text_area("✍️ Enter your custom message template") if message_type == "Custom" else ""
    
    with tabs[1]:
        if 'report_data' not in st.session_state:
            st.session_state.report_data = None
        
        if st.button("📊 Generate Report"):
            if not target_numbers:
                st.error("❌ Please enter at least one valid phone number.")
            else:
                with st.spinner("Generating report..."):
                    st.session_state.report_data = generate_report(target_numbers, num_messages, message_type)
                    st.success("Report generated successfully!")
        
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
    
    with tabs[3]:
        st.subheader("💾 Campaign Management")
        if st.button("📂 Load Campaign"):
            campaign_data = load_campaign()
            if campaign_data:
                st.session_state.target_numbers = campaign_data['target_numbers']
                st.session_state.num_messages = campaign_data['num_messages']
                st.session_state.message_type = campaign_data['message_type']
                st.session_state.custom_message = campaign_data.get('custom_message', '')
                st.success("Campaign loaded successfully!")
            else:
                st.error("❌ No campaign data found.")
        
        if st.button("💾 Save Campaign"):
            if 'target_numbers' in st.session_state and st.session_state.target_numbers:
                campaign_data = {
                    'target_numbers': st.session_state.target_numbers,
                    'num_messages': st.session_state.num_messages,
                    'message_type': st.session_state.message_type,
                    'custom_message': st.session_state.get('custom_message', '')
                }
                save_campaign(campaign_data)
                st.success("Campaign saved successfully!")
            else:
                st.error("❌ No campaign data to save.")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🎲 Generate Messages", use_container_width=True):
            if not target_numbers:
                st.error("❌ Please enter at least one valid phone number.")
            else:
                with st.spinner("🔄 Generating spam messages..."):
                    messages = [custom_message] * num_messages if message_type == "Custom" else generate_spam_messages(num_messages, message_type)
                    st.success("✅ Messages generated successfully!")
                    with st.expander("📝 Generated Messages", expanded=True):
                        for message in messages:
                            st.write(message)
    
    with col2:
        if st.button("📤 Send Messages", use_container_width=True):
            if not target_numbers:
                st.error("❌ Please enter at least one valid phone number.")
            else:
                with st.spinner("📡 Simulating message sending..."):
                    messages = [custom_message] * num_messages if message_type == "Custom" else generate_spam_messages(num_messages, message_type)
                    
                    placeholder = st.empty()
                    progress_bar = st.progress(0)
                    countdown_placeholder = st.empty()
                    
                    total_messages = len(messages)
                    total_time = total_messages * delay_between_messages
                    sent_messages = []
                    
                    try:
                        for i, message in enumerate(messages):
                            time.sleep(delay_between_messages)
                            recipient = random.choice(target_numbers)
                            sent_message = f"📩 Sent to {recipient}: {message}"
                            sent_messages.append(sent_message)
                            placeholder.markdown(sent_message)
                            progress_bar.progress((i + 1) / total_messages)
                            countdown_placeholder.markdown(f"⏳ Time remaining: {total_time - (i + 1) * delay_between_messages:.1f} seconds")
                        
                        placeholder.empty()
                        countdown_placeholder.empty()
                        st.success("✅ Messages sent successfully!")
                    
                    except Exception as e:
                        st.error(f"❌ An error occurred: {e}")
                    
                    with st.expander("📜 Sent Messages", expanded=True):
                        for sent_message in sent_messages:
                            st.write(sent_message)

if __name__ == "__main__":
    main()
