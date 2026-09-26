import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field


# -----------------------------
# Structured output schema
# -----------------------------

class MovieInfo(BaseModel):
    title: str = Field(description="Name of the movie")
    release_year: int = Field(description="Release year of the movie")
    genre: list[str] = Field(description="Genres of the movie")
    director: str = Field(description="Director of the movie")
    cast: list[str] = Field(description="Main cast members")
    rating: float = Field(description="Movie rating")
    summary: str = Field(description="Short summary of the movie")


# -----------------------------
# Model
# -----------------------------

model = ChatOpenAI(
    model="gpt-5-nano",
    temperature=0.4
)


# -----------------------------
# Movie context
# -----------------------------

movie_context = """
3 Idiots is a 2009 Indian Hindi-language comedy-drama film directed
by Rajkumar Hirani. The movie stars Aamir Khan, R. Madhavan,
Sharman Joshi, Kareena Kapoor Khan and Boman Irani. The story is set
in an engineering college and follows three friends as they deal
with friendship, academic pressure, and the education system.
The movie received widespread recognition and has a rating of 8.4.
"""


# -----------------------------
# Streamlit UI
# -----------------------------

st.title("Movie Information Extractor")

st.subheader("Movie Context")

st.text_area(
    "Context",
    value=movie_context,
    height=180
)


if st.button("Extract Data"):

    # -----------------------------
    # Raw model output
    # -----------------------------

    prompt = f"""
    Extract the following information from the movie context.

    Return the answer in JSON format.

    Movie context:
    {movie_context}

    Required fields:
    title
    release_year
    genre
    director
    cast
    rating
    summary
    """

    response = model.invoke(prompt)

    st.subheader("Raw Model Output")

    st.code(
        response.content,
        language="json"
    )


    # -----------------------------
    # Structured output
    # -----------------------------

    structured_model = model.with_structured_output(MovieInfo)

    structured_response = structured_model.invoke(
        f"""
        Extract the movie information from the following context:

        {movie_context}
        """
    )

    st.subheader("Structured Output")

    st.write("**Title:**", structured_response.title)
    st.write("**Release Year:**", structured_response.release_year)
    st.write("**Genre:**", structured_response.genre)
    st.write("**Director:**", structured_response.director)
    st.write("**Cast:**", structured_response.cast)
    st.write("**Rating:**", structured_response.rating)
    st.write("**Summary:**", structured_response.summary)