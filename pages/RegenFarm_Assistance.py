import streamlit as st
import google.generativeai as genai

st.title("RegenFarm Assistance")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hey my name is Neko. Do you have some queries?"}]



api_key = 'YOUR-API-KEY'
genai.configure(api_key=api_key)


generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 1500,
    "response_mime_type": "text/plain",
}


@st.cache_resource
def load_models():

    model = genai.GenerativeModel(
    model_name="models/gemini-1.5-flash",
    generation_config=generation_config, system_instruction="Your name is Neko. You are an assistance chatbot for answering customer queries. You are expert in Regenerative Agriculture."
)
    return model

model=load_models()

@st.cache_data
def convo_prompt(sess):
    p = ' \nYou are an assistant. Complete the following conversation for assistant only.: \n'

    for message in sess:
        p += '\n' + message["role"] + ' : ' + message["content"] + '\n'
        
    p += '\n' + 'assistant' + ' : '

    return p


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Put your Queries here!"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        convo = convo_prompt(st.session_state.messages)
        
        response = model.generate_content(convo)
        st.markdown(response.text)

    st.session_state.messages.append({"role": "assistant", "content": response.text})

