from dotenv import load_dotenv
load_dotenv()

from langchain_tavily import TavilySearch
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser


prompt = ChatPromptTemplate.from_template(
    """You are a helpful AI assistant.
    Give the news in clear bullet points.

    {news}
    """
)

llm = ChatOpenAI(model="gpt-5-nano")

chain = prompt | llm | StrOutputParser()

tool = TavilySearch(max_results=5)

search_results = tool.invoke(
    "Search news about Captain Smit Machchhar on saving passengers"
)

result = chain.invoke({
    "news": search_results
})

print(result)