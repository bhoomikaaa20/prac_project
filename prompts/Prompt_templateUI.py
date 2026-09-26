import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate


model = ChatOpenAI(
    model="gpt-5-nano",
    temperature=0.4,
)


prompt_template = PromptTemplate(
    template="""
    Give a short summary of the following movie:

    Movie context:
    {movie_context}

    Return the summary as normal text, not JSON.
    """,
    input_variables=["movie_context"]
)


movie_context = """
Interstellar (2014) follows Cooper, a former NASA pilot and farmer, who joins a space mission through a wormhole near Saturn to find a new habitable planet for humanity as Earth becomes increasingly unlivable; while he travels across distant planets with his crew, his daughter Murph grows up and works on a scientific solution to save humanity, forcing Cooper to confront the effects of time, sacrifice, and his desire to return to his family.
"""


st.title("Movie Summary Generator")

st.write("Movie Context:")

st.text_area(
    "Movie context",
    value=movie_context,
    height=180
)

if st.button("Generate Summary"):

    prompt = prompt_template.invoke({
        "movie_context": movie_context
    })

    response = model.invoke(prompt)

    st.write("Movie Summary:")
    st.write(response.content)