### Nama : Arnoldus Bryan Hendry
### NIM : 1301220409
import streamlit as st

from chat import init_cs_bot_session
 
st.title('AI Chatbot Mall Information Centre')

if 'chat_bot' not in st.session_state:
    st.session_state['chat_bot'] = init_cs_bot_session()

if 'messages' not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Halo! Apakah ada yang bisa saya bantu?"}]

user_input = st.chat_input()

if user_input:
    try:
        model_answer = st.session_state['chat_bot'].send_message(user_input).candidates[0].content.parts[0].text.strip()
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.session_state.messages.append({"role": "assistant", "content": model_answer})
    except Exception as e:
        st.error(f"Error processing chatbot request: {e}")


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])