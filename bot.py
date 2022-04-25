# bot.py
import os
import discord
from database import Database
from dotenv import load_dotenv
from datetime import datetime
from bot_functions import BotFunctions

# file path for token.ENV file.
TOKEN_PATH = os.path.abspath(os.getcwd()) + "/token.ENV"
# setting environment variable.
load_dotenv(dotenv_path=TOKEN_PATH)

# required for discord API
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# object initialization
client = discord.Client()
actions = BotFunctions()

# Database object and variables
DATABASE_PATH = f"{os.getcwd()}/discord.db"
database = Database()

# creating database
connection = database.create_connection(DATABASE_PATH)


for table in database.sql_create_tables:
    # print(table)
    db_conn = database.create_connection(DATABASE_PATH)
    database.create_table(db_conn, table)


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

    if message.content == "!hello" or message.content == "!Hello":
        response = f'Hello!'
        await message.channel.send(response)
    elif message.content == "!time" or message.content == "!Time":
        date_time = datetime.now()
        response = f'Here is the date and time: {date_time}'
        await message.channel.send(response)
    elif message.content.startswith("!addquote"):
        quote = message.content
        trimmed_quote = actions.get_quote(quote)
        conn = database.create_connection(DATABASE_PATH)
        database.add_quote(conn, trimmed_quote)
        response = f"added quote {trimmed_quote[0]} {trimmed_quote[1]}"
        await message.channel.send(response)
    elif message.content == "!inspireme":
        conn = database.create_connection(DATABASE_PATH)
        quotes = database.get_quote(conn)
        inspiration = actions.inspire_me(quotes)
        response = f"{inspiration[1]} {inspiration[2]}"
        await message.channel.send(response)
    elif message.content.startswith("!roll"):
        ignore = len("!roll ")
        dice = message.content[ignore:]
        dice_to_roll = actions.roll(dice)
        response = f"{message.author} rolls {dice_to_roll[0]} dice with {dice_to_roll[1]} sides! \n" \
                   f"for a total of {dice_to_roll[2]}! \n" \
                   f"your rolls were {dice_to_roll[3]}"
        await message.channel.send(response)








client.run(TOKEN)


