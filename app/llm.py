import os
from mistralai import Mistral
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-small-latest"

client = Mistral(api_key=api_key)

def call_mistral_model(prompt):
    messages = [
        {
            "role" : "user",
            "content" : prompt
        }
    ]
    response = client.chat.complete(
        model = model,
        messages = messages,
        temperature = 0.7
    )
    return response.choices[0].message.content