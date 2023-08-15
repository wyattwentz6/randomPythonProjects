import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()

intents = discord.Intents.default()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello, {ctx.author.mention}!')

@bot.command()
async def about(ctx):
    await ctx.send("I'm a simple Discord bot created using discord.py!")

@bot.command()
async def dice(ctx, sides: int = 6):
    import random
    if sides <= 0:
        await ctx.send("Number of sides must be a positive integer.")
    else:
        roll = random.randint(1, sides)
        await ctx.send(f"You rolled a {roll}!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if 'hello' in message.content.lower():
        await message.channel.send(f"Hello, {message.author.mention}!")

    await bot.process_commands(message)

if __name__ == '__main__':
    bot_token = os.getenv('BOT_TOKEN')
    if bot_token is None:
        raise ValueError("BOT_TOKEN enviroment variable is not set.")
    bot.run(bot_token)
