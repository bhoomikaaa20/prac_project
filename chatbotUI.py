import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage


# Model
model = ChatOpenAI(
    model="gpt-5-nano",
    temperature=0.6,
    max_tokens=1000
)


# Messages
messages = [
    SystemMessage(content="You are a funny Ai Agent!")
]


# UI
st.title("🤖 Funny AI Chatbot")
st.write("Chat with your AI agent")


# User input
prompt = st.chat_input("Type your message...")


if prompt:

    # Exit functionality from your original code
    if prompt.strip() == "0":
        st.write("Bot: Goodbye!")
    else:

        # Add human message
        messages.append(HumanMessage(content=prompt))

        # Get response
        response = model.invoke(messages)

        # Add AI response
        messages.append(AIMessage(content=response.content))

        # Display response
        st.write("Bot:", response.content)
