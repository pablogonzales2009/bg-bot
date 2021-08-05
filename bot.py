import random

import time

import discord

import os

TOKEN = open("TOKEN.txt","r").readline() # token.txt just includes the bot token

client = discord.Client()
random_messages = ['example 1', 'example 2', 'example 3'] # put your random messages here

@client.event
async def on_ready():
    CHANNEL_ID = open("channel.txt","r").readline() # channel id
    channel = client.get_channel(int(CHANNEL_ID))
    message = random_messages[random.randrange(0, len(random_messages))] # using the random library, get a message
    await channel.send(message) 
    while True: # very lazy solution to loop it forever
        time.sleep(100)
        message = random_messages[random.randrange(0, len(random_messages))] # using the random library, get a message
        await channel.send(message)
client.run(TOKEN)
