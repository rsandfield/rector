import discord
from discord.ext import commands
from discord.utils import get

import utilities.utilities as utilities

class ClassCog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.group(name="class", pass_context=True)
  async def class_(self, ctx):
    pass

  @class_.command(name="join")
  async def class_add(self, ctx, code):
    await utiliites.change_role(ctx, ctx.author, code, True)

  @class_.command(name="leave")
  async def class_remove(self, ctx, code):
      await utilities.change_role(ctx, ctx.author, code, False)

  @class_.command(name="list")
  async def class_list(self, ctx):
      pass
      
  @class_.command(name="create")
  @commands.has_guild_permissions(manage_channels=True)
  async def class_create(self, ctx, letters, code, name='', description=''):
    guild = ctx.guild
    category = code[0] + "00 Level"
    classCode = letters.upper() + code
    if(not get(guild.categories, name=category)):
      await ctx.send("Creating {}".format(category))
      await guild.create_category(category)
    await ctx.send("Creating channel and role for {}".format(classCode))
    if(len(name) > 0):
      await utilities.create_channel(ctx, classCode + " " + name, category, description)
    else:
      await utilities.create_channel(ctx, classCode, description, category)
    await utilities.create_role(ctx, classCode, discord.Colour(0x0000FF))

def setup(bot):
  bot.add_cog(ClassCog(bot))