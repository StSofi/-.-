import discord, os, random, requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.event
async def on_ready():
    print(f'Бот {bot.user} запущен!')

@bot.command()
async def hi(ctx):
    await ctx.send('Привет, я бот который может вкидывать тебе мемы')

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command('duck')
async def duck(ctx):
    image_url1 = get_duck_image_url()
    await ctx.send(image_url1)

@bot.command()
async def bb(ctx):
    await ctx.send('Ну пока')


bot.run('ВАШ ТОКЕН')

