# bot.py
import os
import discord

from dotenv import load_dotenv
# file path for token.ENV file.
TOKEN_PATH = os.path.abspath(os.getcwd()) + "/token.ENV"
# setting environment variable.
load_dotenv(dotenv_path=TOKEN_PATH)

# required for discord API
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "$hello" or message.content == "$Hello":
        response = f'Hello!'
        await message.channel.send(response)
    


client.run(TOKEN)


