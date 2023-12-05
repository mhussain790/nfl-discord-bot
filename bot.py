import os
import random
import discord
import datetime

from PIL import Image
from discord.ext import commands
from dotenv import load_dotenv
from quote import get_a_quote
from scores import get_scores, get_avatar, get_single_game_score
from meme import get_meme_url

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

@bot.command(name='meme', help='Responds with a random meme')
async def send_meme(ctx):
    if ctx.message.author == bot.user:
        return
    
    # Get image
    meme_image = await get_meme_url()

    # Create a new embed for img
    embed = discord.Embed(colour=discord.Colour.dark_orange())

    # Set the img
    embed.set_image(url=meme_image)
    # embed2.set_thumbnail(url=other_image)

    # await ctx.send(embeds=[embed1, embed2])
    await ctx.send(embed=embed)

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

def reformat_datetime(input):
    # 2023-12-10T18:00:00Z
    d1 = datetime.datetime.strptime(input,"%Y-%m-%dT%H:%M:%SZ")
    d2 = d1.strftime("%A, %B %d, %Y at %H:%M:%S")

    return d2

def combine_images(img1, img2):
    open_img_1 = Image.open(img1)
    open_img_2 = Image.open(img2)

    combined_img = Image.new('RGB', (open_img_1.width + open_img_2.width, open_img_1.height))
    combined_img.paste(open_img_1, (0, 0))
    combined_img.paste(open_img_2, (open_img_1.width, 0))

    return combined_img

@bot.command(name='detroit', help='Responds with Detroit Lions info')
async def send_scores(ctx):
    if ctx.message.author == bot.user:
        return
    
    # Get image
    det_image = await get_avatar('detroit')

    # Get game info
    game_info = await get_single_game_score('detroit lions')

    # Store dict values
    away_team = game_info.get("away_team")
    home_team = game_info.get("home_team")
    is_scores = game_info.get("scores")
    home_score = game_info.get("home_score")
    away_score = game_info.get("away_score")
    commence_time = game_info.get("commence_time")

    # Check if Detroit is Away/Home
    if 'detroit' in away_team:
        title_data = home_team + ' (HOME) VS ' + away_team + ' (AWAY)'
        # other_image = await get_avatar(home_team)
    else:
        title_data = home_team + ' (HOME) VS ' + away_team + ' (AWAY)'
        # other_image = await get_avatar(away_team)

    # Check if scores is empty
    if is_scores is None:
        commence_time = game_info.get("commence_time")
        formatted_datetime = reformat_datetime(commence_time)
        output_scores = "No scores yet! Game starts at " + formatted_datetime
    else:
        output_scores = home_team + " " + str(home_score) + " - " + str(away_score) + " " + away_team

    # Create separate embeds for each img
    embed = discord.Embed(title=title_data, description=output_scores, colour=discord.Colour.dark_orange())
    # embed2 = discord.Embed()

    # Set the images
    embed.set_thumbnail(url=det_image)
    # embed2.set_thumbnail(url=other_image)

    # await ctx.send(embeds=[embed1, embed2])
    await ctx.send(embed=embed)

@bot.command(name='sanfrancisco', help='Responds with San Francisco 49ers info')
async def send_scores(ctx):
    if ctx.message.author == bot.user:
        return
    
    # Get image
    team_image = await get_avatar('san francisco')

    # Get game info
    game_info = await get_single_game_score('san francisco 49ers')

    # Store dict values
    away_team = game_info.get("away_team")
    home_team = game_info.get("home_team")
    is_scores = game_info.get("scores")
    home_score = game_info.get("home_score")
    away_score = game_info.get("away_score")
    commence_time = game_info.get("commence_time")

    # Check if team is Away/Home
    if 'san francisco' in away_team:
        title_data = home_team + ' (HOME) VS ' + away_team + ' (AWAY)'
        # other_image = await get_avatar(home_team)
    else:
        title_data = home_team + ' (HOME) VS ' + away_team + ' (AWAY)'
        # other_image = await get_avatar(away_team)

    # Check if scores is empty
    if is_scores is None:
        commence_time = game_info.get("commence_time")
        formatted_datetime = reformat_datetime(commence_time)
        output_scores = "No scores yet! Game starts at " + formatted_datetime
    else:
        output_scores = home_team + " " + str(home_score) + " - " + str(away_score) + " " + away_team

    # Create separate embeds for each img
    embed = discord.Embed(title=title_data, description=output_scores, colour=discord.Colour.dark_orange())
    # embed2 = discord.Embed()

    # Set the images
    embed.set_thumbnail(url=team_image)
    # embed2.set_thumbnail(url=other_image)

    # await ctx.send(embeds=[embed1, embed2])
    await ctx.send(embed=embed)

@bot.command(name='kansascity', help='Responds with Kansas City Chiefs info')
async def send_scores(ctx):
    if ctx.message.author == bot.user:
        return
    
    city = 'kansas city'
    # Get image
    team_image = await get_avatar(city)

    # Get game info
    game_info = await get_single_game_score('kansas city chiefs')

    # Store dict values
    away_team = game_info.get("away_team")
    home_team = game_info.get("home_team")
    is_scores = game_info.get("scores")
    home_score = game_info.get("home_score")
    away_score = game_info.get("away_score")
    commence_time = game_info.get("commence_time")

    # Check if team is Away/Home
    if city in away_team:
        title_data = home_team + ' (HOME) VS ' + away_team + ' (AWAY)'
        # other_image = await get_avatar(home_team)
    else:
        title_data = home_team + ' (HOME) VS ' + away_team + ' (AWAY)'
        # other_image = await get_avatar(away_team)

    # Check if scores is empty
    if is_scores is None:
        commence_time = game_info.get("commence_time")
        formatted_datetime = reformat_datetime(commence_time)
        output_scores = "No scores yet! Game starts at " + formatted_datetime
    else:
        output_scores = home_team + " " + str(home_score) + " - " + str(away_score) + " " + away_team

    # Create separate embeds for each img
    embed = discord.Embed(title=title_data, description=output_scores, colour=discord.Colour.dark_orange())
    # embed2 = discord.Embed()

    # Set the images
    embed.set_thumbnail(url=team_image)
    # embed2.set_thumbnail(url=other_image)

    # await ctx.send(embeds=[embed1, embed2])
    await ctx.send(embed=embed)

@bot.command(name='cincinnati', help='Responds with Cincinnati Bengals info')
async def send_scores(ctx):
    if ctx.message.author == bot.user:
        return
    
    city = 'cincinnati'
    # Get image
    team_image = await get_avatar(city)

    # Get game info
    game_info = await get_single_game_score('cincinnati bengals')

    # Store dict values
    away_team = game_info.get("away_team")
    home_team = game_info.get("home_team")
    is_scores = game_info.get("scores")
    home_score = game_info.get("home_score")
    away_score = game_info.get("away_score")
    commence_time = game_info.get("commence_time")

    # Check if team is Away/Home
    if city in away_team:
        title_data = home_team + ' (HOME) VS ' + away_team + ' (AWAY)'
        # other_image = await get_avatar(home_team)
    else:
        title_data = home_team + ' (HOME) VS ' + away_team + ' (AWAY)'
        # other_image = await get_avatar(away_team)

    # Check if scores is empty
    if is_scores is None:
        commence_time = game_info.get("commence_time")
        formatted_datetime = reformat_datetime(commence_time)
        output_scores = "No scores yet! Game starts at " + formatted_datetime
    else:
        output_scores = home_team + ": " + str(home_score) + "\n" + away_team + ": " + str(away_score) 

    # Create separate embeds for each img
    embed = discord.Embed(title=title_data, description=output_scores, colour=discord.Colour.dark_orange())
    # embed2 = discord.Embed()

    # Set the images
    embed.set_thumbnail(url=team_image)
    # embed2.set_thumbnail(url=other_image)

    # await ctx.send(embeds=[embed1, embed2])
    await ctx.send(embed=embed)

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