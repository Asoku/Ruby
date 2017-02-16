import discord
from discord.ext import commands
import random

client = discord.Client()

#from utils import checks

description = '''A bot'''


bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name='async is the future'))
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    
@bot.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    await client.send_message(server, fmt.format(member, server))
    
@bot.command(pass_context=True)
async def name(ctx):
    """Gives you the link to apply."""
    await bot.say(" https://goo.gl/forms/y0rLWeuMvpjBzTf72")   

@bot.command(description='For when you wanna settle the score some other way')
async def choose(*choices : str):
    """Chooses between multiple choices."""
    await bot.say(random.choice(choices))
    
@bot.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))

@bot.command()
async def say(content):
"""Makes me say something :eyes:"""
await bot.say(content)

@bot.group(pass_context=True)
async def cool(ctx):
    """Tell someone that they're cool :)"""
    if ctx.invoked_subcommand is None:
        await bot.say('No, {0.subcommand_passed} is cool <3'.format(ctx))
      

@bot.command(hidden=True, pass_context=True)
#@checks.is_dev()
async def shutdown(ctx):
    """Shuts down the bot"""
    await bot.say("Goodbye.")
    log.warning("{} has shut down the bot!".format(ctx.message.author))
    await _shutdown_bot()

@bot.command(pass_context=True)
async def name(ctx):
    """Tells you my name"""
    await bot.say("My name is Ruby and I hate tomatoes")

@bot.command(pass_context=True)
async def developers(ctx):
    """Lists the developers."""
    await bot.say("[Adaptified, Open Space, Open Space]")


@bot.command(pass_context=True)
async def sex(ctx):
    """You dont wanna know..."""
    await bot.say(":point_right: :ok_hand: **u like sex boi**")

        

       
bot.run('MjgxNjk4MjQ0NjAwNTI4ODk3.C4bvcw.WSxJYN_EMTVIgibgnWgf0PHr4WQ')
