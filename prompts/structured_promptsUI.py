import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field


# Structured output schema
class MovieSummary(BaseModel):
    title: str = Field(description="Name of the movie")
    year: int = Field(description="Release year of the movie")
    summary: str = Field(description="Short summary of the movie")
    genre: str = Field(description="Genre of the movie")


# Model
model = ChatOpenAI(
    model="gpt-5-nano",
    temperature=0.4
)

structured_model = model.with_structured_output(MovieSummary)


# Movie context
movie_context = """
Interstellar (2014) follows Cooper, a former NASA pilot and farmer,
who joins a space mission through a wormhole near Saturn to find a
new habitable planet for humanity as Earth becomes increasingly
unlivable. His daughter Murph grows up and works on a scientific
solution to save humanity.
"""


# Streamlit UI
st.title("Movie Information Extractor")

st.write("Movie Context:")

st.text_area(
    "Movie context",
    value=movie_context,
    height=180
)


if st.button("Generate Movie Information"):

    response = structured_model.invoke(
        f"""
        Extract the movie information from the following context:

        {movie_context}
        """
    )

    st.write("Movie Information")

    st.write("Title:", response.title)
    st.write("Year:", response.year)
    st.write("Summary:", response.summary)
    st.write("Genre:", response.genre)