import discord
import requests
import pandas as pd
from config import API_TOKEN
from config import TOKEN

pd.options.display.max_colwidth = 25
headers = {'X-Api-Key': API_TOKEN}

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = discord.Client(intents=intents)

url = 'https://newsapi.org/v2/everything'
params = {
    'q': '南海トラフ AND 災害',
    'sortBy': 'publishedAt',
    'pageSize': 100
}

response = requests.get(url, headers=headers, params=params)

@client.event
async def on_ready():
    print("Bot is ready!")

@client.event
async def on_message(message):
    if message.author == client.user and not response.ok:
        return
    
    data = response.json()
    df = pd.DataFrame(data['articles'])

    await message.channel.send(df[[ 'publishedAt', 'title', 'url']])

client.run(TOKEN)

