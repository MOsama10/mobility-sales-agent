import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('open_router_api')

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

data = {
    "model": "mistralai/mistral-7b-instruct",  # غيره لموديل متاح إذا لزم الأمر
    "messages": [{"role": "user", "content": "Hello, how are you?"}]
}

response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)

print("Status Code:", response.status_code)
print("Response:", response.json())
