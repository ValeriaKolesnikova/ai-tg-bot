import os
from dotenv import load_dotenv
import httpx
from openai import AsyncOpenAI

load_dotenv()

client = AsyncOpenAI(
    api_key=os.getenv('OPENAI_API_KEY'),
    http_client=httpx.AsyncClient(proxies=os.getenv('PROXY'),
                                  transport=httpx.HTTPTransport(local_address=os.getenv('LOCAL_ADRESS'))
    )
)


async def generate_text(request, model):
    completion = await client.chat.completions.create(
        messages=[{'role': 'user', 'content': request}],
        model=model
    )
    return {
        'response': completion.choices[0].message.content,
        'tokens': completion.usage.total_tokens
    }



async def generate_image(request, model):
    response = await client.images.generate(
        model="dall-e-3",
        prompt=request,
        size="1024x1024",
        quality="standard",
        n=1
    )

    return {
        'response': response.data[0].url,
        'tokens': 1
    }