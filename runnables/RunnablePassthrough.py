from dotenv import load_dotenv

load_dotenv()

from langchain_core.runnables import (
    RunnableParallel,
    RunnablePassthrough,
    RunnableLambda
)

# Function to convert input to uppercase
def make_uppercase(text):
    return text.upper()

# Create parallel runnable
chain = RunnableParallel(
    original=RunnablePassthrough(),
    uppercase=RunnableLambda(make_uppercase)
)

# Invoke
result = chain.invoke("hello world")

print(result)