import requests
from config import API_TOKEN
import pandas as pd

pd.options.display.max_colwidth = 25

headers = {'X-Api-Key': API_TOKEN}

url = 'https://newsapi.org/v2/everything'
params = {
    'q': 'プロセカ AND 初音ミク',
    'sortBy': 'publishedAt',
    'pageSize': 100
}

response = requests.get(url, headers=headers, params=params)

if response.ok:
    data = response.json()
    df = pd.DataFrame(data['articles'])
    print('totalResults:', data['totalResults'])

print(df[[ 'publishedAt', 'title', 'url']])