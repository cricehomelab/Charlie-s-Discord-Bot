# Charlie-s-Discord-Bot
This is a discord bot I'm working on

I've built this bot and am running it in an Ubuntu 20.04 environment
I've included a sample TOKEN.env file that does not have my server details but could be edited with the necessary information to work in another discord server with its own account. 

Current functionality
have created several commands that will cause the bot to respond to input in the server
  - !addquote - adds a quote to a sqlite database
  - !hello - responds with "Hello!"
  - !inspireme - queries the sqlite database for a quote and inputs it into the channel. 
  - !time - displays the current date and time. 

Specs:
This application runs on the python 3.9 interepreter. 
This was originally written on a Ubuntu 20.04 machine. 

Things to do if you are setting up this bot for yourself:
1. Create a discord bot account, and add it to your discord server. https://discordpy.readthedocs.io/en/stable/discord.html
2. Configure the token.env file to have the DISCORD_TOKEN and DISCORD_GUILD variables to have the correct tokens for your discord bot account. 
3. Configure the banned list words in the blacklisted_words.py file by adding the words you do not want to be present in your self.list_of_slurs
4. Run the bot.py application. This application needs to be running if you want the bot to respond to your commands. 


