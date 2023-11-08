import requests
import json
import pprint
url = "https://api.tvmaze.com/search/shows"
params = {"q":"girls"}

response = requests.get(url, params)

if response.status_code == 200:
    data = json.loads(response.text)
    print(data)
    pprint.pprint(data)
else:
    print(f"Error: {response.status_code}")