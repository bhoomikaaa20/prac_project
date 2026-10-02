from dotenv import load_dotenv

load_dotenv()

from langchain_core.runnables import RunnableLambda
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

def uppercase(data):
    return {"name": data["name"].upper()}

prompt = ChatPromptTemplate.from_template(
    "Say hello to {name}"
)

model = ChatOpenAI(model="gpt-5-nano")

chain = (
    RunnableLambda(uppercase)
    | prompt
    | model
)

result = chain.invoke({"name": "bhoomika"})

print(result.content)