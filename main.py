import discord 
import os

os.environ['TOKEN'] = 'bot-token'

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in! Go on {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$fala'):
        await message.channel.send('Meteu essa??????!!!!!')

client.run(os.environ.get('TOKEN'))
