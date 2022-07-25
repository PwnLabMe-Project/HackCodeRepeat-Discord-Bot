from discord.ext import commands
import discord
import config
import os

intents = discord.Intents(members= True, guilds=True, reactions=True,messages = True,presences=True ) 
Bot = commands.Bot(command_prefix = "$", intents = intents)
TOKEN = config.TOKEN

@Bot.event
async def on_ready():
    print("I'm ready")
    await Bot.change_presence(activity=discord.Game(name="ctf.pwnlab.me'de"))

@Bot.event
async def on_member_join(member):
    channel =discord.utils.get(member.guild.text_channels, name="🔄》hareketler")
    await channel.send(f"{member.mention} bize katıldı. Hoş geldi!")

@Bot.event
async def on_command_error(ctx, error):
    await ctx.send(error)

@Bot.command()
@commands.has_role("Yönetici")
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)

@Bot.command()
@commands.has_role("Yönetici")
async def send(ctx, message):
    await ctx.channel.purge(limit=1)
    await ctx.send(message)

@Bot.command()
@commands.has_role("Yönetici")
async def load(ctx, extension):
    Bot.load_extension(f"cogs.{extension}")

@Bot.command()
@commands.has_role("Yönetici")
async def unload(ctx, extension):
    Bot.unload_extension(f"cogs.{extension}")

@Bot.command()
@commands.has_role("Yönetici")
async def reload(ctx, extension):
    Bot.unload_extension(f"cogs.{extension}")
    Bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"{extension} has reloaded")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        Bot.load_extension(f"cogs.{filename[:-3]}")

Bot.run(TOKEN)
