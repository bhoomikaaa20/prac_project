from dotenv import load_dotenv
load_dotenv()

from langchain_core.runnables import RunnableLambda
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

def clean_text(text):
    return text.strip().lower()

prompt = ChatPromptTemplate.from_template(
    "Explain this topic simply: {topic}"
)

model = ChatOpenAI(model="gpt-5-nano")

chain = (
    RunnableLambda(lambda x: {"topic": clean_text(x)})
    | prompt
    | model
)

result = chain.invoke("   RAG   ")

print(result.content)