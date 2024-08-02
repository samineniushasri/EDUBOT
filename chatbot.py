import streamlit as st
import google.generativeai as genai


# Configure the Gemini API
GOOGLE_API_KEY = 'AIzaSyBV7laxv2BbsNtLq4_r7finhiaUF3YtRNs'
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')


# Set Streamlit page configuration
st.set_page_config(
   page_title="Educational Chatbot",
   page_icon="✨",
   layout="wide"
)


# Check for messages in session and create a title if not exists
if "messages" not in st.session_state.keys():
   st.session_state.messages = [
       {"role": "assistant", "content": "Hello, this is Chatbot and how I can help you today?"}
   ]
   st.title(":rainbow[Hello, How may I help you today?]")

# Display all messages
for message in st.session_state.messages:
   with st.chat_message(message["role"]):
       st.write(message["content"])
# Receive user input
user_input = st.chat_input()

# Store user input in session
if user_input is not None:
   st.session_state.messages.append({"role": "user", "content": user_input})
   with st.chat_message("user"):
       st.write(user_input)
# Generate AI response and display
if st.session_state.messages[-1]["role"] != "assistant":
   with st.chat_message("assistant"):
       with st.spinner("Loading..."):
           ai_response = model.generate_content(user_input)
           st.write(ai_response.text)
   new_ai_message = {"role": "assistant", "content": ai_response.text}
   st.session_state.messages.append(new_ai_message)