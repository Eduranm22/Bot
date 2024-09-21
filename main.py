import discord
from discord.ext import commands
import random
from bot_logic import * 

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='$', intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.command() 
async def hello(ctx):
    await ctx.send("Hi!")

@client.command() 
async def bye(ctx):
    await ctx.send("\U0001f642")

@client.command()
async def pass_gen(ctx):
    password = gen_pass(10)
    await ctx.send(f"Tu contraseña generada es: {password}")

@client.command() 
async def coin(ctx):
    coin_result = flip_coin()
    await ctx.send(coin_result)

@client.command()
async def smile(ctx):
    emoji = gen_emodji()
    await ctx.send(emoji)

@client.command()
async def add(ctx, left: int, right: int):
    result = left + right  # Calculate the sum of the two numbers
    await ctx.send(f"La suma de {left} y {right} es: {result}")

@client.command()
async def commands(ctx):
    """Muestra todos los comandos disponibles del bot."""
    help_message = (
        "**Comandos disponibles:**\n"
        "`$hello`: Saluda al bot.\n"
        "`$bye`: Envía un emoji de sonrisa.\n"
        "`$pass`: Genera una contraseña aleatoria.\n"
        "`$coin`: Lanza una moneda al aire (cara o cruz).\n"
        "`$smile`: Genera un emoji al azar.\n"
        "`$add <num1> <num2>`: Suma dos números.\n"
    )
    await ctx.send(help_message)

client.run("SECRET TOKEN")
