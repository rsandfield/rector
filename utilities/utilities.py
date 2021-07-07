import discord
from discord.ext import commands
from discord.utils import get

async def change_role(ctx, user, role, add = True):
  role = get(guild.roles, role)
  if(role == None):
    await ctx.send("Sorry, {} is not available.".format(role))
  else:
    if(add):
      await bot.add_roles(user, role)
    else:
      await bot.remove_roles(user, role)

async def create_channel(ctx, name, category_name='', description=''):
  guild = ctx.guild
  channel = get(guild.channels, name=name)
  if(channel == None):
    channel = await guild.create_text_channel(name)
    if(len(description) > 0):
      await channel.edit(topic=description)
    category = get(guild.categories, name=category_name)
    if(category == None):
      await ctx.send("Category {} does not exist!".format(category_name))
    else:
      await channel.edit(category=category)
  else:
    ctx.send("Channel #{} already exists!".format(name))

async def create_role(ctx, role_name, color):
  guild = ctx.guild
  role = get(guild.roles, name=role_name)
  if(role == None):
    await guild.create_role(name=role_name, color=color)
  else:
    await ctx.send("{} already exists.".format(role_name))