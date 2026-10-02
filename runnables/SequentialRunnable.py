from dotenv import load_dotenv

load_dotenv()


from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Model
model = ChatOpenAI(model="gpt-5-nano")

# Prompt
prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple words."
)

# Output parser
parser = StrOutputParser()

# Sequence
chain = prompt | model | parser

# Run
result = chain.invoke({"topic": "RAG"})

print(result)