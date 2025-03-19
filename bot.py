import discord
import requests
import json
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

def get_meme():
    response = requests.get('https://meme-api.com/gimme') # Make a GET request to the Meme API to fetch random memes
    json_data = json.loads(response.text) # Parse JSON response to extract meme URL
    return json_data['url']

class MyClient(discord.Client):
    async def on_ready(self):
        # This method is called after bot has successfully connected to Discord
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        # This method is called whenever a message is sent in a channel the bot can access
        if message.author == self.user:
            return # Ignore messages sent by the bot itself
        if message.content.startswith('$meme'):
            await message.channel.send(get_meme())

# Specifies the events the bot should listen to
intents = discord.Intents.default()
intents.message_content = True # Enable access to message content

client = MyClient(intents=intents)
client.run(token) # Discord Token running from .env file

