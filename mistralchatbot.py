# import necessary modules
import langchain
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
import streamlit as st

# define a prompt template for the chatbot
prompt = ChatPromptTemplate.from_messages(
    
    [
        ("system", "You are a helpful assistant. Please respond to the questions"),
        ("user", "Question:{question}")
    ]
)

# Set up the streamlit framework
st.title('Chatbot powered by mistral') #set the title of the streamlit app
input_text = st.text_input("Hi, I am mistral. You can ask any questions.") #create a text input field in a streamlit app

#Initialize the llama model
llm = Ollama(model = "mistral")

#create a chain that combines the prompt and Ollama model
chain = prompt|llm

if input_text:
    st.write(chain.invoke({"question":input_text}))