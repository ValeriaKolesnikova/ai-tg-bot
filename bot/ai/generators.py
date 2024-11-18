import os
from dotenv import load_dotenv
import asyncio
from openai import AsyncOpenAI

load_dotenv()

client = AsyncOpenAI(api_key=os.getenv('OPENAI_API_KEY'))


async def generate_text(request, model):
    completion = await client.chat.completions.create(
        messages=[{'role': 'user', 'content': request}],
        model=model
    )
    print(completion.choices[0].message.content) 


asyncio.run(generate_text('Hello world Java', 'gpt-3.5-turbo'))