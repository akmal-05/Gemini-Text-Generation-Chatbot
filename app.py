import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
 

env_path ="myChatBot\env.env"
load_dotenv(env_path)
api_key= os.getenv('GEMINI_API_KEY')
print("API_KEY:",api_key)

genai.configure(api_key=api_key)

def get_text_response(prompt):
    """Generate a text response using the Gemini API."""
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"

st.title("Gemini Text Generation Chatbot")
# st.write("Ask me anything, and I'll generate a response!")
with st.chat_message("assistant"):
    st.write("Hello human! How can I help you?")


user_input = st.text_input("You: ")

if st.button("Ask"):
    if user_input:
        response = get_text_response(user_input)
        st.write(f"QABot: {response}")
    else:
        st.write("Please enter a question.")

     








