from langchain.tools import tool
from dotenv import load_dotenv
from rich import print
from langchain_openai import ChatOpenAI

load_dotenv()


# Create a tool
@tool
def find_text_length(text: str) -> int:
    """Find the length of the given text"""
    return len(text)


# Tool binding
llm = ChatOpenAI(model="gpt-5-nano")

llm_binded_with_tool = llm.bind_tools([find_text_length])


# Tool calling
result = llm_binded_with_tool.invoke(
    "Use the find_text_length tool and get the number of characters in the given text: Hello Bhoomika how do u do!"
)


# Tool execution
if result.tool_calls:

    tool_call = result.tool_calls[0]

    final_result = find_text_length.invoke(
        tool_call["args"]
    )

    # Send the tool response back to the LLM
    final_length = llm.invoke(
    f"The tool calculated that the text has {final_result} characters. "
    f"Give the final answer to the user."
)


    print(final_length.content)