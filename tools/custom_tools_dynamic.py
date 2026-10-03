from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain.messages import HumanMessage,AIMessage,SystemMessage
from langchain.tools import tool
from rich import print

@tool
def find_text_length(text: str) -> int:
    """Find the length of the given text"""
    return len(text)

llm=ChatOpenAI(model='gpt-5-nano')

messages=[]
tools={
    "find_text_length":find_text_length
}

prompt=input("You:")
human_message=HumanMessage(prompt)

query=messages.append(human_message)


#Tool binding
llm_with_tool=llm.bind_tools([find_text_length])

result=llm_with_tool.invoke(messages)
messages.append(result)




#Tool calling

if result.tool_calls:
    tool_name=result.tool_calls[0]["name"]
    tool_message=tools[tool_name].invoke(result.tool_calls[0])
    messages.append(tool_message)


result=llm_with_tool.invoke(messages)
print(result.content)



