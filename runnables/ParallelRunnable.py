from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model = ChatOpenAI(model="gpt-5-nano")

# Prompt 1
explanation_prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple words."
)

# Prompt 2
points_prompt = ChatPromptTemplate.from_template(
    "Give 5 important points about {topic}."
)

parser = StrOutputParser()

# Two chains
explanation_chain = explanation_prompt | model | parser
points_chain = points_prompt | model | parser

# Run both in parallel
parallel_chain = RunnableParallel(
    explanation=explanation_chain,
    key_points=points_chain
)

result = parallel_chain.invoke({
    "topic": "RAG"
})

print(result)