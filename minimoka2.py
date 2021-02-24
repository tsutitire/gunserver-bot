# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 23:41:51 2020

@author: tsutitire
"""
#imports
import discord
from discord.ext import commands
from voice_generator import creat_WAV
from discord.ext import tasks
#cogcog
from files.cog_game import gamecog
from files.cog_game2 import gamecog2
from files.cog_datas import datacog
from files.cog_twitt import twitcog
import files.func_cog_react
from files.func_cog_react import reactcog
import pya3rt
import asyncio

#EMOJIhosi
MOKA = 0
voice = None
player = None
TICKET = 0
CHANNEL = 0
USERS = [442263946402201612]
COINS = [1]
CATEGORY = 673806292393132052
translatem = 0

#react-file
file_inside = []
#bots
client = commands.Bot(command_prefix='$')
client.add_cog(gamecog(client))
client.add_cog(gamecog2(client))
client.add_cog(datacog(client))
client.add_cog(twitcog(client))
client.add_cog(reactcog(client))
voice_client = None


@client.event
async def on_ready():
    global file_inside
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------------')
    activity = discord.Game(name="HELP:$helps つちちれと戯れたり情報を提供したりしてますよ♪")
    await client.change_presence(activity=activity)
    #asyncio.ensure_future(greeting_gm())


    
    
@client.command()
async def join(ctx):
    print('#voicechannelを取得')
    ctxvoice = ctx.author.voice
    if (not ctxvoice) or (not ctxvoice.channel):
        return()
    channel = ctxvoice.channel
    print('#voicechannelに接続')
    await channel.connect()
    #print(channel.is_connected())





@client.command()
async def bye(ctx):
    print('#切断')
    await ctx.voice_client.disconnect()

'''
@tasks.loop(seconds=3)
async def loop():
    print("none")
    f = open("files/userdata-t.txt","r", 'utf-8')
    file_inside = f.read().split()
    count = 3
    for i in range(file_inside):
        count = count + 1
        if count == 4:
            chan = file_inside[i + 1]
            mes = file_inside[i + 2]
            await chan.send(mes)
            count = 1

async def greeting_gm():
    while True:
        f = open("files/userdata-t.txt","r", encoding="utf-8")
        file_inside = f.read().split()
        count = 3
        for i in range(len(file_inside)):
            count = count + 1
            if count == 4:
                channel = file_inside[i + 1]
                mes = file_inside[i + 2]
                channel = client.get_channel(int(channel))
                await channel.send(mes)
                count = 1
        await asyncio.sleep(3600)
'''
        
    
    
        
        

    



def send_message(message):
    apikey = "DZZQe7pMtSBMln1Ikb7aDb1AI8poHDHE"
    client = pya3rt.TalkClient(apikey)
    reply_message = client.talk(message)
    return reply_message['results'][0]['reply']

@client.event
async def on_message(message):
    msgclient = message.guild.voice_client
    if message.author.bot:
        return
    if message.content.startswith('$'):
        #the data which moved from old ver
        if message.content.startswith('$addrolesforeveryone'):
            for m in message.guild.members:
                role1 = 743746225311842355
                role2 = 743745448702902374
                role3 = 743744375846207510
                role4 = 743751779468181515
                myguild = 715613003306893378
                role11 = message.guild.get_role(role1)
                role22 = message.guild.get_role(role2)
                role33 = message.guild.get_role(role3)
                role44 = message.guild.get_role(role4)
                await m.add_roles(role11)
                await m.add_roles(role22)
                await m.add_roles(role33)
                await m.add_roles(role44)
        pass


    if message.content.startswith("k$"):
        await message.channel.send(send_message(message.content[2:]))
    else:
        if message.guild.voice_client:
            if message.content.startswith('$'):
                pass
            if message.content.startswith("::"):
                pass
            else:
                print(message.content)
                ids = message.author.id
                creat_WAV(message.content,ids)
                source = discord.FFmpegPCMAudio("files/output.wav")
                message.guild.voice_client.play(source)
        else:
            pass
    await client.process_commands(message)


client.run("")