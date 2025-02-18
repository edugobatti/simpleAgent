import streamlit as st
import requests


# URL da API que fornece as respostas do LLM
API_URL = "http://0.0.0.0:5000/llm/"

def chat_with_llm(prompt,llm_selectbox):
    response = requests.post(API_URL, json={"query": prompt, "llm_model":llm_selectbox})
    return response.json().get("content", "Erro na resposta da API")

st.set_page_config(
    page_title="SimpleAgent",
    page_icon="🤖",
    layout="wide"
)

st.title("Playground 🤖")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
with st.chat_message("assistant"):
    st.write("Olá posso ajudar apenas com localização de CEP e cálculos simples (soma, subtração, multiplicação, divisão)")

# Using object notation
llm_selectbox = st.sidebar.selectbox(
    "Qual LLM vai usar?",
    ("ollama", "openai",)
)


if prompt := st.chat_input("Escreva aqui"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = chat_with_llm(prompt,llm_selectbox)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})