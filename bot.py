import random
from random import choice, shuffle

import time

import discord

import os

TOKEN = inserttokenhere

client = discord.Client()
random_messages = ['example 1', 'example 2', 'example 3'] # put your random messages here

@client.event
async def on_ready():
    channel = client.get_channel(#insert ur channel id here)
    message = (random.choice(random_messages)) # alternative: random_messages[random.randrange(0, len(random_messages))]
    await channel.send(message) 
    while True: # very lazy solution to loop it forever 
        time.sleep(100)
        message = (random.choice(random_messages))
        await channel.send(message)
client.run(TOKEN)
