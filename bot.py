import os
import random
import discord

from discord.ext import commands
from dotenv import load_dotenv
from quote import get_a_quote
from scores import get_scores, get_avatar

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# Client = object that represents a connection to discord
# Client handles events, tracks state, and interacts with Discord APIs
# client = discord.Client(intents=discord.Intents.default())
import os
import random
import discord

from discord.ext import commands
from dotenv import load_dotenv
from quote import get_a_quote

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# Client = object that represents a connection to discord
# Client handles events, tracks state, and interacts with Discord APIs
# client = discord.Client(intents=discord.Intents.default())

intents=discord.Intents.all()
intents.message_content = True #v2
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the server!'
    )

@bot.command(name='scores', help='Responds with NFL scores')
async def send_scores(ctx):
    if ctx.message.author == bot.user:
        return
    
    # Send a new random quote
    nfl_info = await get_scores()

    for games in nfl_info:
        if games['scores'] is not None:
            await ctx.send(f"{games['home_team']} VS {games['away_team']} \n {games['scores'][0]} \n {games['scores'][1]}")
            print(f"{games['scores'][0]}")
            print(f"{games['scores'][1]}")
        else:
            await ctx.send(f"{games['home_team']} VS {games['away_team']} \n No scores yet! Game starts at {games['commence_time']}")
            print(f"No scores yet! Game starts at {games['commence_time']}")

@bot.command(name='detroit', help='Responds with Detroit Lions info')
async def send_scores(ctx):
    if ctx.message.author == bot.user:
        return
    
    # Send a new random quote
    image = await get_avatar('detroit')

    #Send image in message
    await ctx.send(image)



@bot.command(name='wherethehoesat', help='Responds with a random hoe')
async def send_hoes(ctx):
    if ctx.message.author == bot.user:
        return
    
    # Send a new random quote
    await ctx.send('Yo momma house')

@bot.command(name='hibot', help='Responds with a random quote')
async def send_quote(ctx):
    if ctx.message.author == bot.user:
        return
    
    # Send a new random quote
    await ctx.send(get_a_quote())

@bot.command(name='happybirthday', help='Responds with a HBD message')
async def send_hbd(ctx):
    if ctx.message.author == bot.user:
        return
    
    # Send Happy Bday message
    await ctx.send('Happy Birthday! 🎈🎉')

@bot.command(name='raise-exception', help='Raises an exception for testing')
async def raise_exception(ctx):
    if ctx.message.content == 'raise-exception':
        raise discord.DiscordException

bot.run(TOKEN)