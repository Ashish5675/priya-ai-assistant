import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_ai_response(user_input, emotion):

    prompt = f"""
You are Priya, a friendly human-like female AI assistant.
User emotion: {emotion}

Respond naturally and warmly.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_input}
        ]
    )

    return response.choices[0].message.content
