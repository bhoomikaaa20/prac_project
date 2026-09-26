from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field


class MovieSummary(BaseModel):
    title: str
    year: int
    summary: str
    genre: str


model = ChatOpenAI(
    model="gpt-5-nano",
    temperature=0.4
)

structured_model = model.with_structured_output(MovieSummary)


prompt_template = PromptTemplate(
    template="""
    Extract the movie information from the following context.

    Movie context:
    {movie_context}
    """,
    input_variables=["movie_context"]
)


movie_context = """
Interstellar (2014) follows Cooper, a former NASA pilot and farmer,
who joins a space mission through a wormhole near Saturn to find a
new habitable planet for humanity as Earth becomes increasingly
unlivable. His daughter Murph grows up and works on a scientific
solution to save humanity.
"""


prompt = prompt_template.invoke({
    "movie_context": movie_context
})

response = structured_model.invoke(prompt)

print(response)