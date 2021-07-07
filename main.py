import discord
from discord.ext import commands
from discord.utils import get
import os

bot = commands.Bot(command_prefix=os.getenv("prefix"))

initial_extensions = [
  'cogs.class'
]

@bot.event
async def on_ready():
  print("Logged in as {0.user}".format(bot))

@bot.command()
async def helpMe(ctx):
    await ctx.send("Thank you for asking for help. These commands are available:")
    await ctx.send("$class add [code] <- Gives you a role showing you are in the given class")
    await ctx.send("$class remove [code] <- Gives you a role showing you are in the given class")
    await ctx.send("$class list <- Lists all classes which have been added to the server")
    await ctx.send("$class create <- Admin-only command to create a new class on the server")

@bot.command()
async def rector(ctx):
    await ctx.send("Yes, hello. I am the bot called Rector.")

if __name__ == '__main__':
  for extension in initial_extensions:
    bot.load_extension(extension)

bot.run(os.getenv("token")) 