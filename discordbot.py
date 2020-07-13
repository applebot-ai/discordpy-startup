from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix="/")
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def peke(ctx):
    await ctx.send('ponpon')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def scb(ctx):
    await ctx.send('https://tt2-compendium.com/en/builds/sc')    

@bot.command()
async def hsb(ctx):
    await ctx.send('https://tt2-compendium.com/en/builds/hs')   

@bot.command()
async def csb(ctx):
    await ctx.send('https://tt2-compendium.com/en/builds/cs')   

@bot.command()
async def petb(ctx):
    await ctx.send('https://tt2-compendium.com/en/builds/pet')       

@bot.command()
async def raid(ctx):
    await ctx.send('https://docs.google.com/spreadsheets/d/166QB9bVQE37K8KdnITG_cu-_cvi8iE78EFIWemdJ6X0/edit#gid=736827398')     

@bot.command()
async def decks(ctx):
    await ctx.send('https://docs.google.com/spreadsheets/d/18vZdCWrcXAQKEraoSDWVFnT_jwk84iXEs6uAAPQ9OM0/edit')     
   

bot.run(token)





