from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model="gpt-5-nano",
    temperature=0.6,
    max_tokens=1000
)

messages = []

print("Welcome to chatbot application, press 0 to exit")

while True:
    prompt = input("You: ")

    if prompt.strip() == "0":
        print("Bot: Goodbye!")
        break

    messages.append(prompt)

    response = model.invoke(messages)

    messages.append(response)

    print("Bot:", response.content)