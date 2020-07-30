import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix='#')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('hello'):
        await message.channel.send(f"Hi {message.author.name} 😍")
    await client.process_commands(message)

@client.command()
async def test(ctx):
    await ctx.send("You just revoked the command test")
    

client.run(os.environ['TOKEN'])
