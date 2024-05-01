import json
import requests

completion_query = "nvidia"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

response = requests.get(f'http://google.com/complete/search?client=chrome&q={completion_query}')

for completion in json.loads(response.text)[1]:
    print(completion)