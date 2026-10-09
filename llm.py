
import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

MODEL_NAME = "Qwen/Qwen2.5-7B-Instruct"

client = InferenceClient(
    model=MODEL_NAME,
    token=os.getenv("HF_TOKEN")
)


def generate_response(prompt, temperature=0.2, max_tokens=1200):

    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=temperature,
        max_tokens=max_tokens
    )

    return response.choices[0].message.content



