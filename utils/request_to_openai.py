from openai import OpenAI, RateLimitError
from config_data.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def request_to_openai(message, character_info):
    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=[
                {"role": "system", "content": character_info},
                {"role": "user", "content": f"{message}"}
            ],
            temperature=0.1
        )
        return completion.choices[0].message.content
    except RateLimitError:
        return False
