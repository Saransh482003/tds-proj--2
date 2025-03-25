import requests
import json

def get_embeddings(input_array, api_key):
    url = "https://aiproxy.sanand.workers.dev/openai/v1/embeddings"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "input": input_array,
        "model": "text-embedding-3-small",
        "encoding_format": "float"
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()

    