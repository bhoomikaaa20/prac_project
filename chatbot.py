# System + User Prompts
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage,SystemMessage,HumanMessage
model = ChatOpenAI(
    model="gpt-5-nano",
    temperature=0.6,
    max_tokens=1000
)

messages = [
    SystemMessage(content="You are a funny Ai Agent!")
]

print("Welcome to chatbot application, press 0 to exit")

while True:
    prompt = input("You: ")

    if prompt.strip() == "0":
        print("Bot: Goodbye!")
        break

    messages.append(HumanMessage(content=prompt))

    response = model.invoke(messages)

    messages.append(AIMessage(content=response.content))

    print("Bot:", response.content)


print(messages)