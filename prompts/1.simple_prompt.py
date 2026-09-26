from dotenv import load_dotenv
load_dotenv()


import os
from langchain.chat_models import init_chat_model


model = init_chat_model(
    "auto",
    model_provider="openrouter",
    max_tokens=1000
)

response = model.invoke("Why do parrots talk?")


print(response.content)