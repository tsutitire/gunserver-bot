# -*- coding: utf-8 -*-
"""
Created on Tue May 26 16:29:19 2020

@author: tsutitire
"""
import random
import discord
import urllib3
import urllib.error
import urllib.request
import urllib.parse
import json
import time
import requests as rqs
import bs4
from bs4 import BeautifulSoup
import codecs
from discord.ext import commands
client = discord.Client()
greetchannel = 682930148093460558
ROLE_WELCOME = 676570304285376515
CHANNEL_WELCOME = 683107957923512349
SP_ID = 682917849999998986
discord_voice_channel_id = '653565863911227423'
EMOJI_WELCOME = '✅'
BJ_uje = 0
BJ_total = 0
BJ_wait = 0

RD_alr = 0
RD_sos = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
RD_uss = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
RD_usstat = 0
RD_sostat = 0
RD_sop = 0
RD_usp = 0
RD_turn = 0
RD_som = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
RD_usm = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]

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
bot = commands.Bot(command_prefix='$')

client = commands.Bot(command_prefix = '$')   
@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()

# discord.py lib 
TOKEN = 'Oh, there is no token here. sorry.'
#token
client = discord.Client()
@client.event
async def on_ready():
    print('loggined!')
    channel = client.get_channel(greetchannel)
    await channel.send('Hi,everyone!')
    print("やぁ！ミニもかが来たよ！")
    activity = discord.Game(name="HELP:$help つちちれと戯れたり情報を提供したりしてますよ♪")
    await client.change_presence(status=discord.Status.idle, activity=activity)


    


    

async def on_disconnect():
    print('logouted!')
    channel = client.get_channel(greetchannel)
    await channel.send('Goodbye,everyone! пока!')
    print("パカー!")

@client.event
async def discord.on_bulk_message_delete(message):
    
    
@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content.startswith('$translate'):
        global translatem
        translatem = message.content
    if message.content.startswith('$musc'):
        ID = message.content[6:]
        voice = await client.join_voice_channel(message.author.voice_channel)
        player = await voice.create_ytdl_player(ID)
        player.start()
        return
    if message.content.startswith('$dice'):
        maxim = message.content[6:]
        maxim = int(maxim)
        dice = random.randrange(maxim)
        dice += 1
        await message.channel.send(dice)
    if message.content.startswith('$cjoin'):
        channel = message.author.voice.channel
        await channel.connect()
    if message.content.startswith('$cleave'):
        channel = message.author.voice.channel
        await client.disconnect()
    global RD_alr
    global RD_sos
    global RD_som
    global RD_usm
    global RD_sop
    global RD_uss
    global RD_usp
    global RD_usstat
    global RD_sostat
    global RD_turn
    global RD_usc
    global RD_soc
    if message.content.startswith('$radar'):
        if RD_alr != 0:
            await message.channel.send("既に始まってますよ？")
        if RD_alr == 0:
            await message.channel.send("始まりますよ～! $rjoin してくださいね～")
            await message.channel.send("$rsetp 1-1 みたいな感じで、戦艦(横4マス),巡洋艦(縦3マス)駆逐艦(横2マス)潜水艦(縦2マス) の指定を行ってください この順番で登録されます(それぞれ下端、左端を指定してください)")
            await message.channel.send("マップ説明：　上が自陣、下が相手陣マップです。　自陣：青マス＝海 緑マス=船 黄色マス=相手の攻撃があったマス 爆発=相手に爆撃された船マス 相手陣:青マス＝未攻撃マス 黄色マス=攻撃済みのマス 爆発=攻撃して、命中したマス(前後左右のどこかに敵艦の残りが隠れてます)")
            await message.channel.send("マップマス 左上から、0-0 0-1 0-2…って感じです 9×9になっています。")
            await message.channel.send("DMでやらないと相手にばれちゃいますよ！")
            RD_sop = message.author.id
            RD_alr = 1
    if message.content.startswith("$rjoin"):
        if RD_alr == 0:
            await message.channel.send("まだはじまってません。 $radarしよう！")
        if RD_alr == 1:
            RD_usp = message.author.id
            RD_alr = 2
            await message.channel.send('<@' + str(RD_sop) + '>' + 'VS' + '<@' + str(RD_usp) + '>')
    if message.content.startswith("$rreset"):
        RD_alr = 0
        RD_sos = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
        RD_uss = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
        RD_usstat = 0
        RD_sostat = 0
        RD_sop = 0
        RD_usp = 0
        RD_turn = 0
        RD_usc = 0
        RD_soc = 0
        RD_som = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
        RD_usm = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
    if message.content.startswith("$rsetp"):
        if RD_alr == 0:
            await message.channel.send("まだはじまってません。 $radarしよう！")
        if RD_alr == 2:
            if message.author.id == RD_sop:
                if RD_sostat == 0:
                    shipa = message.content[7:8]
                    shipb = message.content[9:10]
                    shipa = int(shipa)
                    shipb = int(shipb)
                    soer = await client.fetch_user(RD_sop)
                    if RD_sos[shipa][shipb] == 0 and RD_sos[shipa][shipb + 1] == 0 and RD_sos[shipa][shipb + 2] == 0 and RD_sos[shipa][shipb + 3] == 0:
                        RD_sos[shipa][shipb] = 1
                        RD_sos[shipa][shipb + 1] = 1
                        RD_sos[shipa][shipb + 2] = 1
                        RD_sos[shipa][shipb + 3] = 1
                        RD_sostat = 1
                    else:
                        await soer.send("範囲外/範囲がかぶっている状態ですよ！")
                    mess = str(RD_sos[0]) + "\n" + str(RD_sos[1]) + "\n" + str(RD_sos[2]) + "\n" + str(RD_sos[3]) + "\n" + str(RD_sos[4]) + "\n" + str(RD_sos[5]) + "\n" + str(RD_sos[6]) + "\n" + str(RD_sos[7]) + "\n" + str(RD_sos[8]) + "\n"
                    mess = mess.replace('0', ':blue_square:')
                    mess = mess.replace('1', ':green_square:')
                    await soer.send(mess)
                    return
                if RD_sostat == 1:
                    shipa = message.content[7:8]
                    shipb = message.content[9:10]
                    shipa = int(shipa)
                    shipb = int(shipb)
                    soer = await client.fetch_user(RD_sop)
                    if RD_sos[shipa][shipb] == 0 and RD_sos[shipa + 1][shipb] == 0 and RD_sos[shipa + 2][shipb] == 0:
                        RD_sos[shipa][shipb] = 1
                        RD_sos[shipa + 1][shipb] = 1
                        RD_sos[shipa + 2][shipb] = 1
                        RD_sostat = 2
                    else:
                        await soer.send("範囲外/範囲がかぶっている状態ですよ！")
                    mess = str(RD_sos[0]) + "\n" + str(RD_sos[1]) + "\n" + str(RD_sos[2]) + "\n" + str(RD_sos[3]) + "\n" + str(RD_sos[4]) + "\n" + str(RD_sos[5]) + "\n" + str(RD_sos[6]) + "\n" + str(RD_sos[7]) + "\n" + str(RD_sos[8]) + "\n"
                    mess = mess.replace('0', ':blue_square:')
                    mess = mess.replace('1', ':green_square:')
                    await soer.send(mess)
                    return
                if RD_sostat == 2:
                    shipa = message.content[7:8]
                    shipb = message.content[9:10]
                    shipa = int(shipa)
                    shipb = int(shipb)
                    soer = await client.fetch_user(RD_sop)
                    if RD_sos[shipa][shipb] == 0 and RD_sos[shipa][shipb + 1] == 0:
                        RD_sos[shipa][shipb] = 1
                        RD_sos[shipa][shipb + 1] = 1
                        RD_sostat = 3
                    else:
                        await soer.send("範囲外/範囲がかぶっている状態ですよ！")
                    mess = str(RD_sos[0]) + "\n" + str(RD_sos[1]) + "\n" + str(RD_sos[2]) + "\n" + str(RD_sos[3]) + "\n" + str(RD_sos[4]) + "\n" + str(RD_sos[5]) + "\n" + str(RD_sos[6]) + "\n" + str(RD_sos[7]) + "\n" + str(RD_sos[8]) + "\n"
                    mess = mess.replace('0', ':blue_square:')
                    mess = mess.replace('1', ':green_square:')
                    await soer.send(mess)
                    return
                if RD_sostat == 3:
                    shipa = message.content[7:8]
                    shipb = message.content[9:10]
                    shipa = int(shipa)
                    shipb = int(shipb)
                    soer = await client.fetch_user(RD_sop)
                    user = await client.fetch_user(RD_usp)
                    if RD_sos[shipa][shipb] == 0 and RD_sos[shipa  + 1][shipb] == 0:
                        RD_sos[shipa][shipb] = 1
                        RD_sos[shipa + 1][shipb] = 1
                        RD_sostat = 4
                    else:
                        await soer.send("範囲外/範囲がかぶっている状態ですよ！")
                    mess = str(RD_sos[0]) + "\n" + str(RD_sos[1]) + "\n" + str(RD_sos[2]) + "\n" + str(RD_sos[3]) + "\n" + str(RD_sos[4]) + "\n" + str(RD_sos[5]) + "\n" + str(RD_sos[6]) + "\n" + str(RD_sos[7]) + "\n" + str(RD_sos[8]) + "\n"
                    mess = mess.replace('0', ':blue_square:')
                    mess = mess.replace('1', ':green_square:')
                    await soer.send(mess)
                    if RD_sostat != 4:
                        await user.send("設定完了しました。相手の設定完了をお待ちください")
                        return
                    await user.send("始まります！ 先行はあなたです！攻撃するマスを$rbomb 0-0 みたいな感じで指定してください！")
                    await soer.send("始まります！　後攻はあなたです！相手の操作を待って、自分の順番が来たら攻撃するマスを$rbomb 0-0 みたいな感じで指定してください！")
                    RD_som = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
                    RD_usm = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]

            if message.author.id == RD_usp:
                if RD_usstat == 0:
                    shipa = message.content[7:8]
                    shipb = message.content[9:10]
                    shipa = int(shipa)
                    shipb = int(shipb)
                    user = await client.fetch_user(RD_usp)
                    if RD_uss[shipa][shipb] == 0 and RD_uss[shipa][shipb + 1] == 0 and RD_uss[shipa][shipb + 2] == 0 and RD_uss[shipa][shipb + 3] == 0:
                        RD_uss[shipa][shipb] = 1
                        RD_uss[shipa][shipb + 1] = 1
                        RD_uss[shipa][shipb + 2] = 1
                        RD_uss[shipa][shipb + 3] = 1
                        RD_usstat = 1
                    else:
                        await user.send("範囲外/範囲がかぶっている状態ですよ！")
                    mess = str(RD_uss[0]) + "\n" + str(RD_uss[1]) + "\n" + str(RD_uss[2]) + "\n" + str(RD_uss[3]) + "\n" + str(RD_uss[4]) + "\n" + str(RD_uss[5]) + "\n" + str(RD_uss[6]) + "\n" + str(RD_uss[7]) + "\n" + str(RD_uss[8]) + "\n"
                    mess = mess.replace('0', ':blue_square:')
                    mess = mess.replace('1', ':green_square:')
                    await user.send(mess)
                    return
                if RD_usstat == 1:
                    shipa = message.content[7:8]
                    shipb = message.content[9:10]
                    shipa = int(shipa)
                    shipb = int(shipb)
                    user = await client.fetch_user(RD_usp)
                    if RD_uss[shipa][shipb] == 0 and RD_uss[shipa + 1][shipb] == 0 and RD_uss[shipa + 2][shipb] == 0:
                        RD_uss[shipa][shipb] = 1
                        RD_uss[shipa + 1][shipb] = 1
                        RD_uss[shipa + 2][shipb] = 1
                        RD_usstat = 2
                    else:
                        await user.send("範囲外/範囲がかぶっている状態ですよ！")
                    mess = str(RD_uss[0]) + "\n" + str(RD_uss[1]) + "\n" + str(RD_uss[2]) + "\n" + str(RD_uss[3]) + "\n" + str(RD_uss[4]) + "\n" + str(RD_uss[5]) + "\n" + str(RD_uss[6]) + "\n" + str(RD_uss[7]) + "\n" + str(RD_uss[8]) + "\n"
                    mess = mess.replace('0', ':blue_square:')
                    mess = mess.replace('1', ':green_square:')
                    await user.send(mess)
                    return
                if RD_usstat == 2:
                    shipa = message.content[7:8]
                    shipb = message.content[9:10]
                    shipa = int(shipa)
                    shipb = int(shipb)
                    user = await client.fetch_user(RD_usp)
                    if RD_uss[shipa][shipb] == 0 and RD_uss[shipa][shipb + 1] == 0:
                        RD_uss[shipa][shipb] = 1
                        RD_uss[shipa][shipb + 1] = 1
                        RD_usstat = 3
                    else:
                        await user.send("範囲外/範囲がかぶっている状態ですよ！")
                    mess = str(RD_uss[0]) + "\n" + str(RD_uss[1]) + "\n" + str(RD_uss[2]) + "\n" + str(RD_uss[3]) + "\n" + str(RD_uss[4]) + "\n" + str(RD_uss[5]) + "\n" + str(RD_uss[6]) + "\n" + str(RD_uss[7]) + "\n" + str(RD_uss[8]) + "\n"
                    mess = mess.replace('0', ':blue_square:')
                    mess = mess.replace('1', ':green_square:')
                    await user.send(mess)
                    return
                if RD_usstat == 3:
                    shipa = message.content[7:8]
                    shipb = message.content[9:10]
                    shipa = int(shipa)
                    shipb = int(shipb)
                    soer = await client.fetch_user(RD_sop)
                    user = await client.fetch_user(RD_usp)
                    if RD_uss[shipa][shipb] == 0 and RD_uss[shipa  + 1][shipb] == 0:
                        RD_uss[shipa][shipb] = 1
                        RD_uss[shipa + 1][shipb] = 1
                        RD_usstat = 4
                    else:
                        await user.send("範囲外/範囲がかぶっている状態ですよ！")
                    mess = str(RD_uss[0]) + "\n" + str(RD_uss[1]) + "\n" + str(RD_uss[2]) + "\n" + str(RD_uss[3]) + "\n" + str(RD_uss[4]) + "\n" + str(RD_uss[5]) + "\n" + str(RD_uss[6]) + "\n" + str(RD_uss[7]) + "\n" + str(RD_uss[8]) + "\n"
                    mess = mess.replace('0', ':blue_square:')
                    mess = mess.replace('1', ':green_square:')
                    await user.send(mess)
                    if RD_sostat != 4:
                        await user.send("設定完了しました。相手の設定完了をお待ちください")
                        return
                    await user.send("始まります！ 先行はあなたです！攻撃するマスを$rbomb 0-0 みたいな感じで指定してください！")
                    await soer.send("始まります！　後攻はあなたです！相手の操作を待って、自分の順番が来たら攻撃するマスを$rbomb 0-0 みたいな感じで指定してください！")
                    RD_usstat = 5
                    RD_turn = 1
                    RD_sostat = 5
                    RD_som = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
                    RD_usm = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
    if message.content.startswith("$rbomb"):
        soer = await client.fetch_user(RD_sop)
        user = await client.fetch_user(RD_usp)
        if RD_turn == 1 and message.author.id == RD_usp and RD_sostat == 5:     
            bomba = int(message.content[7:8])
            bombb = int(message.content[9:10])
            if int(bomba) >= 0 and int(bomba) <= 8 and int(bombb) >= 0 and int(bombb) <= 8:
                if RD_sos[bomba][bombb] == 1:   
                    RD_som[bomba][bombb] = 2
                    RD_sos[bomba][bombb] = 2
                    RD_usc = RD_usc + 1
                if RD_sos[bomba][bombb] == 0:
                    RD_som[bomba][bombb] = 1
                    RD_sos[bomba][bombb] = 3
                if RD_sos[bomba][bombb] == 2:
                    RD_som[bomba][bombb] = 2
                    RD_sos[bomba][bombb] = 2
                if RD_sos[bomba][bombb] == 3:
                    RD_sos[bomba][bombb] = 3
                    RD_som[bomba][bombb] = 1
                mess = str(RD_uss[0]) + "\n" + str(RD_uss[1]) + "\n" + str(RD_uss[2]) + "\n" + str(RD_uss[3]) + "\n" + str(RD_uss[4]) + "\n" + str(RD_uss[5]) + "\n" + str(RD_uss[6]) + "\n" + str(RD_uss[7]) + "\n" + str(RD_uss[8]) + "\n"
                mess2 = str(RD_som[0]) + "\n" + str(RD_som[1]) + "\n" + str(RD_som[2]) + "\n" + str(RD_som[3]) + "\n" + str(RD_som[4]) + "\n" + str(RD_som[5]) + "\n" + str(RD_som[6]) + "\n" + str(RD_som[7]) + "\n" + str(RD_som[8]) + "\n"
                mess = mess.replace('0', ':blue_square:')
                mess = mess.replace('1', ':green_square:')
                mess = mess.replace('2', ':boom:')
                mess = mess.replace('3', ':yellow_square:')
                mess2 = mess2.replace('0', ':blue_square:')
                mess2 = mess2.replace('2', ':boom:')
                mess2 = mess2.replace('1', ':yellow_square:')
                mess3 = str(RD_sos[0]) + "\n" + str(RD_sos[1]) + "\n" + str(RD_sos[2]) + "\n" + str(RD_sos[3]) + "\n" + str(RD_sos[4]) + "\n" + str(RD_sos[5]) + "\n" + str(RD_sos[6]) + "\n" + str(RD_sos[7]) + "\n" + str(RD_sos[8]) + "\n"
                mess4 = str(RD_usm[0]) + "\n" + str(RD_usm[1]) + "\n" + str(RD_usm[2]) + "\n" + str(RD_usm[3]) + "\n" + str(RD_usm[4]) + "\n" + str(RD_usm[5]) + "\n" + str(RD_usm[6]) + "\n" + str(RD_usm[7]) + "\n" + str(RD_usm[8]) + "\n"
                mess3 = mess3.replace('0', ':blue_square:')
                mess3 = mess3.replace('1', ':green_square:')
                mess3 = mess3.replace('2', ':boom:')
                mess3 = mess3.replace('3', ':yellow_square:')
                mess4 = mess4.replace('0', ':blue_square:')
                mess4 = mess4.replace('2', ':boom:')
                mess4 = mess4.replace('1', ':yellow_square:')
                await user.send(mess)
                await user.send(mess2)
                await soer.send(mess3)
                await soer.send(mess4)
                await  user.send("相手のターンです...")
                await soer.send("あなたのターンです...")
                RD_turn = 2
                mess = str(mess)
                if RD_usc == 11:
                    await user.send('<@' + str(RD_usp) + '>' + "さんの勝ちだよ！おめでとう！")
                    RD_alr = 0
                    RD_sos = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
                    RD_uss = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
                    RD_usstat = 0
                    RD_sostat = 0
                    RD_sop = 0
                    RD_turn = 0
                    RD_usc = 0
                    RD_soc = 0
                    RD_usp = 0
                    RD_som = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
                    RD_usm = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
        print(RD_turn)
        if RD_turn == 2 and message.author.id == RD_sop and RD_sostat == 5:
            bomba = int(message.content[7:8])
            bombb = int(message.content[9:10])
            if int(bomba) >= 0 and int(bomba) <= 8 and int(bombb) >= 0 and int(bombb) <= 8:
                if RD_uss[bomba][bombb] == 1:   
                    RD_usm[bomba][bombb] = 2
                    RD_uss[bomba][bombb] = 2
                    RD_soc = RD_soc + 1
                if RD_uss[bomba][bombb] == 0:
                    RD_usm[bomba][bombb] = 1
                    RD_uss[bomba][bombb] = 3
                if RD_uss[bomba][bombb] == 2:
                    RD_usm[bomba][bombb] = 2
                    RD_uss[bomba][bombb] = 2
                if RD_uss[bomba][bombb] == 3:
                    RD_uss[bomba][bombb] = 3
                    RD_usm[bomba][bombb] = 1
                mess = str(RD_uss[0]) + "\n" + str(RD_uss[1]) + "\n" + str(RD_uss[2]) + "\n" + str(RD_uss[3]) + "\n" + str(RD_uss[4]) + "\n" + str(RD_uss[5]) + "\n" + str(RD_uss[6]) + "\n" + str(RD_uss[7]) + "\n" + str(RD_uss[8]) + "\n"
                mess2 = str(RD_som[0]) + "\n" + str(RD_som[1]) + "\n" + str(RD_som[2]) + "\n" + str(RD_som[3]) + "\n" + str(RD_som[4]) + "\n" + str(RD_som[5]) + "\n" + str(RD_som[6]) + "\n" + str(RD_som[7]) + "\n" + str(RD_som[8]) + "\n"
                mess = mess.replace('0', ':blue_square:')
                mess = mess.replace('1', ':green_square:')
                mess = mess.replace('2', ':boom:')
                mess = mess.replace('3', ':yellow_square:')
                mess2 = mess2.replace('0', ':blue_square:')
                mess2 = mess2.replace('2', ':boom:')
                mess2 = mess2.replace('1', ':yellow_square:')
                mess3 = str(RD_sos[0]) + "\n" + str(RD_sos[1]) + "\n" + str(RD_sos[2]) + "\n" + str(RD_sos[3]) + "\n" + str(RD_sos[4]) + "\n" + str(RD_sos[5]) + "\n" + str(RD_sos[6]) + "\n" + str(RD_sos[7]) + "\n" + str(RD_sos[8]) + "\n"
                mess4 = str(RD_usm[0]) + "\n" + str(RD_usm[1]) + "\n" + str(RD_usm[2]) + "\n" + str(RD_usm[3]) + "\n" + str(RD_usm[4]) + "\n" + str(RD_usm[5]) + "\n" + str(RD_usm[6]) + "\n" + str(RD_usm[7]) + "\n" + str(RD_usm[8]) + "\n"
                mess3 = mess3.replace('0', ':blue_square:')
                mess3 = mess3.replace('1', ':green_square:')
                mess3 = mess3.replace('2', ':boom:')
                mess3 = mess3.replace('3', ':yellow_square:')
                mess4 = mess4.replace('0', ':blue_square:')
                mess4 = mess4.replace('2', ':boom:')
                mess4 = mess4.replace('1', ':yellow_square:')
                await user.send(mess)
                await user.send(mess2)
                await soer.send(mess3)
                await soer.send(mess4)
                await user.send("あなたのターンです...")
                await soer.send("相手のターンです...")
                RD_turn = 1
                mess3 = str(mess3)
                if RD_soc == 11:
                    await user.send('<@' + str(RD_sop) + '>' + "さんの勝ちだよ！おめでとう！")
                    RD_alr = 0
                    RD_sos = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
                    RD_uss = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
                    RD_usstat = 0
                    RD_sostat = 0
                    RD_sop = 0
                    RD_usp = 0
                    RD_turn = 0
                    RD_usc = 0
                    RD_soc = 0
                    RD_som = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
                    RD_usm = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
                
                    
                    
                    
    
    if message.content.startswith('$PIdt'):
        http = urllib3.PoolManager()
        MCID = message.content[6:]
        MCID2 = 'https://playerislands.com/api/getplayer/' + MCID
        print(MCID2)
        r = http.request('GET',MCID2)
        rr = str(r.data)
        print(rr)
        rr = rr[2:]
        print(rr) 
        indA = rr.find(',')
        print(rr[10:(indA)])
        if (rr[10:(indA)] == 'true'):
            await message.channel.send("データがあったみたいですよ！貼り付けますね")
            indA = rr.find(',')
            indB = rr.find(',',(indA + 1))
            indC = rr.find(',',(indB + 1))
            indD = rr.find(',',(indC + 1))
            indE = rr.find(',',(indD + 1))
            indF = rr.find(',',(indE + 1))
            indG = rr.find(',',(indF + 1))
            indH = rr.find(',',(indG + 1))
            datA = rr[(indA + 9):(indB -1)]
            datB = rr[(indB + 9):(indC - 1)]
            datC = rr[(indC + 9):(indD - 1)]
            datD = rr[(indD + 15):(indE - 1)]
            datE = rr[(indE + 12):(indF - 1)]
            datF = rr[(indF + 15):(indG - 1)]
            datF = datF.encode('cp932')
            datG = rr[(indG + 15):-3]
            datG = datG.encode('cp932')
            embed = discord.Embed(title=str(message.content[6:]) + 's PI datas',description="PIのデータらしき者ども" )
            embed.add_field(name="name",value=datA)
            embed.add_field(name="UUID",value=datB)
            embed.add_field(name="rank",value=datC)
            embed.add_field(name="fst. login",value=datD)
            embed.add_field(name="playtime",value=datE)
            embed.add_field(name="lst. server",value=datF)
            embed.add_field(name="sev. name",value=datG)
            await message.channel.send(embed=embed)
            
            
            
        if (rr[10:(indA)] == 'false'):
            await message.channel.send("ごめんなさい、データが見つかりませんでした...")
    if message.content.startswith('$ninnsyo'):
        path = 'players.txt'
        f = open(path,"r")
        datas = f.read()
        f.close()
        f = open(path,"a")
        if datas.find(str(message.author.id)) != -1:
            f.close
            f = open(path,"w")
            datai1 = datas.find(str(message.author.id))
            print(datai1)
            datai2 = datas.find(".",(datai1 + 1))
            print(datai2)
            data = datas[:datai1 - 1] + datas[datai2:]
            print(data)
            data = data[:-1]
            writes = message.author.id
            writes = "." + str(writes) + ":" + message.content[9:]
            writes = data + writes
            f.write(writes)    
            f.close
            await message.channel.send("登録上書き完了♪")
            return
        if datas.find(str(message.author.id)) == -1:
            writes = message.author.id
            writes = "." + str(writes) + ":" + message.content[9:]
            f.write(writes)
            await message.channel.send("登録完了♪")
        f.close()
        
        
    
    
    
    
    if message.content.startswith('$PIsv'):
        http = urllib3.PoolManager()
        MCID = message.content[6:]
        MCID2 = 'https://playerislands.com/api/getserver/' + MCID
        print(MCID2)
        r = http.request('GET',MCID2)
        rr = str(r.data)
        print(rr)
        rr = rr[2:]
        print(rr)
        indA = rr.find(',')
        print(rr[10:(indA)])
        if (rr[10:(indA)] == 'true'):
            await message.channel.send("データがあったみたいですよ！貼り付けますね")
            indA = rr.find(',')
            indB = rr.find(',',(indA + 1))
            
            
            indC = rr.find(',',(indB + 1))
            indD = rr.find(',',(indC + 1))
            indE = rr.find(',',(indD + 1))
            indF = rr.find(',',(indE + 1))
            indG = rr.find(',',(indF + 1))
            indH = rr.find(',',(indG + 1))
            indI = rr.find(',',(indH + 1))
            indJ = rr.find(',',(indI + 1))
            indK = rr.find(',',(indJ + 1))
            indL = rr.find(',',(indK + 1))
            indM = rr.find(',',(indL + 1))
            indN = rr.find(',',(indM + 1))
            indO = rr.find(',',(indN + 1))
            await message.channel.send('データ収集、目印作成完了...')
            datA = rr[(indA + 9):(indB -1)]
            datB = rr[(indB + 10):(indC - 1)]  
            datC = rr[(indC + 9):(indD - 1)]
            datD = rr[(indD + 11):(indE - 1)]
            datE = rr[(indE + 9):(indF - 1)]
            datF = str('0')
            datF = rr[(indF + 11):(indG)]
            datG = rr[(indG + 14):(indH)]
            datH = rr[(indH + 12):(indI)]
            datI = rr[(indI + 9):(indJ)]
            datJ = rr[(indJ + 11):(indK)]
            datK = rr[(indK + 17):(indL)]
            datL = rr[(indL + 14):(indM)]
            datM = rr[(indM + 13):(indN)]
            datN = rr[(indN + 13):(indO)]
            datO = rr[(indO + 7):-2]
            await message.channel.send('データ登録完了...')
            embed = discord.Embed(title=str(message.content[6:]) + ' PI server datas',description="PIのデータらしき者ども 1/1" )
            embed.add_field(name="name",value=datA)
            embed.add_field(name="own.",value=datB)
            embed.add_field(name="motd",value=datC)
            embed.add_field(name="stat",value=datD)
            embed.add_field(name="icon",value=datE)
            await message.channel.send(embed=embed)
            embed2 = discord.Embed(title=str(message.content[6:]) + ' PI server datas',description="PIのデータらしき者ども 2/2" )
            datF = str(datF)
            print(datF)
            embed2.add_field(name="player cnt.",value=datF)
            embed2.add_field(name="max players",value=datG)
            embed2.add_field(name="lang.",value=datH)
            embed2.add_field(name="votes",value=datI)
            embed2.add_field(name="premium",value=datJ)
            embed2.add_field(name="ULTRA PREMIUM",value=datK)
            embed2.add_field(name="third party",value=datL)
            embed2.add_field(name="lst. start",value=datM)
            embed2.add_field(name="whitelist",value=datN)
            embed2.add_field(name="tick p sec.",value=datO)
            await message.channel.send(embed=embed2)
            
        if (rr[10:(indA)] == 'false'):
            await message.channel.send("ごめんなさい、データが見つかりませんでした...")
            
    if message.content.startswith('$UUID'):
        http = urllib3.PoolManager()
        MCID = message.content[6:]
        MCID = 'https://api.mojang.com/users/profiles/minecraft/' + MCID
        print (MCID)
        r = http.request('GET',MCID)
        print (r.data)
        findr = str(r.data)
        indA = findr.find(',')
        findr = findr[(indA + 7):-3]
        await message.channel.send(findr)
        findr = findr[0:8] + '-' + findr[8:12] + '-' + findr[12:16] + '-' + findr[16:20] + '-' + findr[20:]
        await message.channel.send(findr)
    if message.content.startswith('$skin'):
        http = urllib3.PoolManager()
        UUID = message.content[6:]
        print (UUID)
        UUID = 'https://crafatar.com/renders/body/' + UUID 
        print (UUID)
        r = http.request('GET',UUID)
        embed = discord.Embed(title=str(message.content[6:]) + 's SKIN',description="スキンだよ！" )
        embed.set_image(url=UUID)
        await message.channel.send(embed=embed)
    if message.content.startswith('$sknf'):
        http = urllib3.PoolManager()
        UUID = message.content[6:]
        print (UUID)
        UUID = 'https://crafatar.com/renders/body/' + UUID  + '?overlay=true'
        print (UUID)
        r = http.request('GET',UUID)
        embed = discord.Embed(title=str(message.content[6:]) + 's SKIN',description="スキンだよ！" )
        embed.set_image(url=UUID)
        await message.channel.send(embed=embed)
    if message.content.startswith('$avat'):
        http = urllib3.PoolManager()
        UUID = message.content[6:]
        print (UUID)
        UUID = 'https://minotar.net/avatar/' + UUID
        print (UUID)
        r = http.request('GET',UUID)
        embed = discord.Embed(title=str(message.content[6:]) + 's Avatar',description="顔面だよ！" )
        embed.set_image(url=UUID)
        await message.channel.send(embed=embed)
    if message.content.startswith('$skn2'):
        http = urllib3.PoolManager()
        UUID = message.content[6:]
        print (UUID)
        UUID = 'https://minotar.net/skin/' + UUID
        print (UUID)
        r = http.request('GET',UUID)
        embed = discord.Embed(title=str(message.content[6:]) + 's Skins',description="展開図だよ！" )
        embed.set_image(url=UUID)
        await message.channel.send(embed=embed)
    if message.content.startswith('$mojang'):
        http = urllib3.PoolManager()
        r = http.request('GET','https://status.mojang.com/check')
        print(r.status)
        mojangdata = str(r.data)
        indA = mojangdata.find(',')
        mjdt1 = mojangdata[4:(indA - 1)]
        print(mjdt1)
        indB = mojangdata.find(',', (indA + 1))
        mjdt2 = mojangdata[(indA + 2):(indB - 1)]
        print(mjdt2)
        indC = mojangdata.find(',', (indB + 1))
        mjdt3 = mojangdata[(indB + 2):(indC - 1)]
        print(mjdt3)
        indD = mojangdata.find(',', (indC + 1))
        mjdt4 = mojangdata[(indC + 2):(indD - 1)]
        print(mjdt4)
        indE = mojangdata.find(',', (indD + 1))
        mjdt5 = mojangdata[(indD + 2):(indE - 1)]
        print(mjdt5)
        indF = mojangdata.find(',', (indE + 1))
        mjdt6 = mojangdata[(indE + 2):(indF - 1)]
        print(mjdt6)
        indG = mojangdata.find(',', (indF + 1))
        mjdt7 = mojangdata[(indF + 2):(indG - 1)]
        print(mjdt7)
        indH = mojangdata.find(',', (indG + 1))
        mjdt8 = mojangdata[(indG + 2):(indH - 2)]
        print(mjdt8)
        
        indA = mjdt1.find(':')
        mjdta1 = mjdt1[1:(indA - 1)]
        mjdtb1 = mjdt1[(indA + 2):-1]
        indA = mjdt2.find(':')
        mjdta2 = mjdt2[1:(indA - 1)]
        mjdtb2 = mjdt2[(indA + 2):-1]
        indA = mjdt3.find(':')
        mjdta3 = mjdt3[1:(indA - 1)]
        mjdtb3 = mjdt3[(indA + 2):-1]
        indA = mjdt4.find(':')
        mjdta4 = mjdt4[1:(indA - 1)]
        mjdtb4 = mjdt4[(indA + 2):-1]
        indA = mjdt5.find(':')
        mjdta5 = mjdt5[1:(indA - 1)]
        mjdtb5 = mjdt5[(indA + 2):-1]
        indA = mjdt6.find(':')
        mjdta6 = mjdt6[1:(indA - 1)]
        mjdtb6 = mjdt6[(indA + 2):-1]
        indA = mjdt7.find(':')
        mjdta7 = mjdt7[1:(indA - 1)]
        mjdtb7 = mjdt7[(indA + 2):-1]
        indA = mjdt8.find(':')
        mjdta8 = mjdt8[1:(indA - 1)]
        mjdtb8 = mjdt8[(indA + 2):-1]
        
        embed = discord.Embed(title="MojangAPI",description="もやんえーぴーあいとやら" )
        embed.add_field(name=mjdta1,value=mjdtb1)
        embed.add_field(name=mjdta2,value=mjdtb2)
        embed.add_field(name=mjdta3,value=mjdtb3)
        embed.add_field(name=mjdta4,value=mjdtb4)
        embed.add_field(name=mjdta5,value=mjdtb5)
        embed.add_field(name=mjdta6,value=mjdtb6)
        embed.add_field(name=mjdta7,value=mjdtb7)
        embed.add_field(name=mjdta8,value=mjdtb8)
        await message.channel.send(embed=embed)
        
    if message.content.startswith('$tasdfasdfsdfaicket'):
        category_id = message.channel.category_id
        await message.channel.send(str({message.author.mention}) + 'さん、チケットはうまくできてるかな...？んまぁ、たぶんできたよ！')
        category = message.guild.get_channel(category_id)
        channel = client.get_channel(673797808582688768)
        guild = client.get_guild(673797808582688768)
        overwrites = {guild.default_role: discord.PermissionOverWrite(send_messages=False,read_messages=False),
                      guild.me: discord.PermissionOverWrite(send_messages=True,read_messages=True)
        }
        new_channel = await category.create_text_channel(name='Ticket',overwrites=overwrites)
        member = channel.guild.get_member(442263946402201612)
        await channel.set_permissions(member,read_messages=True,send_messages=True)
        member = channel.guild.get_member(475584322108129282)
        await channel.set_permissions(member,read_messages=True,send_messages=True)
        member = channel.guild.get_member(391545714918031360)
        await channel.set_permissions(member,read_messages=True,send_messages=True)
        member = channel.guild.get_member(475810805863022638)
        await channel.set_permissions(member,read_messages=True,send_messages=True)
        embed = discord.Embed(title="The ticket of Minimoka",description="ん、ticket?大丈夫？すぐに運営の皆さんが対応してくれるから安心しててね！" )
        await message.new_channel.send(embed=embed)
        
    #help        
    if message.content.startswith('$help'):
        embed = discord.Embed(title="The help of Minimoka",description="ボク、ミニもかについてのいろいろが書いてあるよ！" )
        embed.set_image(url="https://b.imgef.com/POuypFI.png")
        embed.add_field(name="$touroku",value="Ok.と返しますよ！")
        embed.add_field(name="$janken",value="じゃんけんができます！ $jankeng(グー)/p(パー)/s(チョキ)で指定可能ですよ～")
        embed.add_field(name="$hima",value="ひまもかさんを賛美します☆")
        embed.add_field(name="$uranai",value="キミを占ってあげよう")
        embed.add_field(name="$oumu",value="$oumu の後に入力した文字を返答しますよ 変なことは言わせないでね？")
        embed.add_field(name="$pan",value="PAN☆")
        embed.add_field(name="$bj/$bjget/$bjstand",value="ブラックジャックができます！ $bjで開始、 カードを引くなら$bjget,引かないなら$bjstandです!")
        embed.add_field(name="$slot",value="スロットができます　リアルマネーをとかす心配はないですよ♪")
        embed.add_field(name="$UUID ユーザー名",value="誰かのマイクラでのUUIDを取得できます")
        embed.add_field(name="$skin UUID",value="誰かのマイクラでのスキンを取得できます")
        embed.add_field(name="$sknf UUID",value="誰かのマイクラでのスキンを取得できます")
        embed.add_field(name="$avat ユーザー名",value="誰かのマイクラでの頭を取得できます")
        embed.add_field(name="$skn2 ユーザー名",value="誰かのマイクラでのスキンの展開図を取得できます")
        embed.add_field(name="$PIdt ユーザー名",value="PlayerIslamds内のユーザーデータを取得できます♪")
        embed.add_field(name="$PIsv サーバー名",value="PlayerIslands内のサーバーデータを取得できます ※ごめんなさい、土が無能なせいでボクの機能がうまく行かず、UNICORD形式の部分アリ")
        embed.add_field(name='$trsl 変換元言語,変換先言語,"変換する文章"',value="Google翻訳をしてくれます　言語の例：ru(ロシア)en(英語)ja(日本語) 土が無能なせいで機能がないため、文字コード変換が必須です")
        embed.add_field(name='$radar',value="誰かと艦隊ゲームで遊べます！")
        embed.add_field(name="文字コード変換用サイトです", value="https://uguisu.skr.jp\netgame/conv/")
        await message.channel.send(embed=embed)
    
    if message.content.startswith('$mcbans'):
        mcid = message.content[8:]
        res = rqs.get('https://www.mcbans.com/player/' + str(mcid))
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        #http = urllib3.PoolManager()
        #r = http.request('GET','https://www.mcbans.com/player/' + str(mcid))
        #ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) '\
             #'AppleWebKit/537.36 (KHTML, like Gecko) '\
             #'Chrome/55.0.2883.95 Safari/537.36 '
             
        #req = urllib.request.Request('https://www.mcbans.com/player/' + str(mcid), headers={'User-Agent': ua})
        #html = urllib.request.urlopen(req)
            #Link = a.gt.urlopen(req)
        #soup = BeautifulSoup(html, "html.parser")
        #soup = str(r.data)
        print(soup)
        soup = str(soup)
        count = 0
        count2 = 0
        embed = discord.Embed(title="MCBANS",description=str(mcid) + "'s mcbans data")
        count2 = 0
        while count != 4: 
            count = count + 1
            count2 = count2 + 1
            print(count)
            print(count2)
            if count == 1:
                sind1 = soup.find("section-content")
                print(sind1)
                sind2 = soup.find("<",sind1)
                print(sind2)
                sind3 = sind1 + 15
            if count != 1:
                sind1 = soup.find("section-content",sind3)
                #sind1 = soup.find(">",(sind1 + 17))
                sind2 = soup.find("<",sind1)
                print(sind1)
                print(sind2)
                sind3 = sind1 + 15
            if count == 1:
                embed.add_field(name=str(mcid) + "'s Reputation", value=soup[(sind1 + 17):(sind2)])
            if count == 2:
                embed.add_field(name=str(mcid) + "'s Issued Bans", value=soup[(sind1 + 17):(sind2)])     
            if count == 3:
                embed.add_field(name=str(mcid) + "'s UUID", value=soup[(sind1 + 40):(sind2)])
            if count == 4:
                embed.add_field(name=str(mcid) + "'s Bans", value=soup[(sind1 + 17):(sind2)])
        await message.channel.send(embed=embed)
    if message.content.startswith('$kongyo'):
        voice = await client.channel.connect(client.get_channel("653565863911227423"))
        player = voice.play(discord.FFmpegPCMAudio("コンギョ.mp3"))
        player.start()
    if message.content.startswith('$janken'):
        janken = random.randrange(3)
        jankenw = message.content
        jankenw = jankenw[8:]
        if jankenw == "r":
            if janken == 1:
                await message.channel.send("グーとグーで、あいこですね")
            elif janken == 2:
                await message.channel.send("グーとパーで、ボクの勝ちです！(｀・ω・´)")
            else:
                await message.channel.send("グーとチョキで、キミの勝ちです！(´・ω・`)")
        elif jankenw == "p":
            if janken == 1:
                await message.channel.send("パーとグーで、キミの勝ちです！(´・ω・`)")
            elif janken == 2:
                await message.channel.send("パーとパーで、あいこですね")
            else:
                await message.channel.send("パーとチョキで、ボクの勝ちです！(｀・ω・´)")
        elif jankenw == "s":
            if janken == 1:
                await message.channel.send("チョキとグーで、ボクの勝ちです！(｀・ω・´)")
            elif janken == 2:
                await message.channel.send("チョキとパーで、キミの勝ちです！(´・ω・`)")
            else:
                await message.channel.send("チョキとチョキで、あいこですね")
        else:
            await message.channel.send("r/p/sで指定してくださいよぉ...(-_-;)")
    if message.content.startswith('$hima'):
        await message.channel.send('Oh! do you know him?, yes, he is god!')
    if message.content.startswith('$uranai'):
        uranaid = await uranai()
        await message.channel.send(uranaid)
    if message.content.startswith('$oumu'):
        messageoumu = "オウム返しです"
        messageoumu = message.content
        print (messageoumu)
        await message.channel.send(messageoumu[5:])
    if message.content.startswith('$pan'):
        messagepan = "PAN☆"
        messagepan = message.content
        messagepan = messagepan[5:]
        await message.channel.send("@" + messagepan + " さんがPANされました！")
    if message.content.startswith('おはよう'):
        await message.channel.send("おはようございます！")
    if message.content.startswith('$moka'):
        global MOKA
        MOKA = MOKA + 1
        await message.channel.send('WOW! everyone said moka in this server ' + MOKA + 'Times!')
    if message.content.startswith('$bj'):
        global BJ_wait
        global BJ_uje
        global BJ_total
        if BJ_uje == 0:
            BJ_uje = 1
            BJ_total = 0
            BJ_random = 0
            BJ_card1 = 0
            BJ_card2 = 0
            await message.channel.send("あなたのカードは")
            cards = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
            BJ_random = random.randrange(52)
            BJ_card1 = cards[BJ_random]
            BJ_random = random.randrange(52)
            BJ_card2 = cards[BJ_random]
            await message.channel.send(str(BJ_card1) + "&" + str(BJ_card2))
            if BJ_card1 == 1:
                if BJ_card2 == 10:
                    await message.channel.send("すごい..ボクの負けです!")
                    BJ_uje = 0
                    return
            if BJ_card1 == 10:
                if BJ_card2 == 1:
                    await message.channel.send("すごい..ボクの負けです!")
                    BJ_uje = 0
                    return
            BJ_total = BJ_card1 + BJ_card2
    if message.content.startswith('$bjget'):
        if BJ_uje == 1:
            cards = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
            BJ_random = random.randrange(52)
            BJ_card1 = cards[BJ_random]
            await message.channel.send(str(BJ_card1) + "でした！")
            if BJ_card1 == 1:
                BJ_wait = 1
                while BJ_wait == 1:
                    dummy = dummy + 1
                dummy = 0
            BJ_total = BJ_card1 + BJ_total
            if BJ_total > 21:
                await message.channel.send("ボクの番ですね! カードは...")
                cards = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
                BJ_random = random.randrange(52)
                BJ_card1 = cards[BJ_random]
                BJ_random = random.randrange(52)
                BJ_card2 = cards[BJ_random]
                BJ_total2 = BJ_card1 + BJ_card2
                await message.channel.send(str(BJ_card1) + "と" + str(BJ_card2) + "ですか...")
                if BJ_card1 == 1:
                    if BJ_card2 == 10:
                        await message.channel.send("ってこれは！やった！!ボクの勝ちです！！")
                        BJ_uje = 0
                        return
                if BJ_card1 == 10:
                    if BJ_card2 == 1:
                        await message.channel.send("ってこれは！やった！!ボクの勝ちです！！")
                        BJ_uje = 0
                        return
                while BJ_total2 < 17:
                    BJ_random = random.randrange(52)
                    BJ_card1 = cards[BJ_random]
                    BJ_total2 = BJ_card1 + BJ_total2
                    await message.channel.send("引きます!. . ." + str(BJ_card1) + "ですか、なるほど")                    
                    if BJ_total2 > 21:
                        await message.channel.send("オーバーしちゃいました...引き分けです！")
                        BJ_uje = 0
                        return
                await message.channel.send(str(BJ_total2) + "! ボクの勝ちですね！")
                BJ_uje = 0
                return
    if message.content.startswith('$bjstand'):
        if BJ_uje == 1:
            await message.channel.send(str(BJ_total) + "ですね。")
            await message.channel.send("ボクの番ですね! カードは...")
            cards = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
            BJ_random = random.randrange(52)
            BJ_card1 = cards[BJ_random]
            Bj_random = random.randrange(52)
            BJ_card2 = cards[BJ_random]
            BJ_total2 = BJ_card1 + BJ_card2
            await message.channel.send(str(BJ_card1) + "と" + str(BJ_card2) + "ですか...")
            if BJ_card1 == 1:
                if BJ_card2 == 10:
                    await message.channel.send("ってこれは！やった！!ボクの勝ちです！！")
                    BJ_uje = 0
                    return
            if BJ_card1 == 10:
                if BJ_card2 == 1:
                    await message.channel.send("ってこれは！やった！!ボクの勝ちです！！")
                    BJ_uje = 0
                    return
            while BJ_total2 < 17:
                BJ_random = random.randrange(52)
                BJ_card1 = cards[BJ_random]
                BJ_total2 = BJ_card1 + BJ_total2
                await message.channel.send("引きます!. . ." + str(BJ_card1) + "ですか、なるほど")                    
                if BJ_total2 > 21:
                    await message.channel.send("オーバーしちゃいました...ボクの負けです！")
                    BJ_uje = 0
                    return
            while BJ_total2 < BJ_total:
                BJ_random = random.randrange(52)
                BJ_card1 = cards[BJ_random]
                BJ_total2 = BJ_card1 + BJ_total2
                await message.channel.send("引きます!. . ." + str(BJ_card1) + "ですか、なるほど")                    
                if BJ_total2 > 21:
                    await message.channel.send("オーバーしちゃいました...ボクの負けです！")
                    BJ_uje = 0
                    return
                if BJ_total2 == 21:
                    if BJ_total == BJ_total2:   
                        await message.channel.send("21!!...引き分けですね！")
                        BJ_uje = 0
                        return
                    if BJ_total != BJ_total2:   
                        await message.channel.send("21!!...ボクの勝ちですね！")
                        BJ_uje = 0
                        return
                if BJ_total2 == 21:
                    await message.channel.send("21!!...引き分けですね！")
                    BJ_uje = 0
                    return
            if BJ_total2 > BJ_total:
                await message.channel.send("ボクの勝ちですね！")
                BJ_uje = 0
                return
            if BJ_total2 == BJ_total:
                await message.channel.send("...引き分けですね！")
                BJ_uje = 0
                return
    if message.content.startswith("$sleep"):
        bot_vc = message.author.voice.channel
        for member in bot_vc.members:
            channel = client.get_channel(718967261989437550)
            await member.move_to(channel)
    if message.content.startswith("$trsl"):
        mescn = message.content
        mesind1 = mescn.find(",")
        mesind2 = mescn.find(",",(mesind1))
        mesind3 = mescn.find(",",(mesind2 + 1))
        arg1 = mescn[6:mesind1]
        arg2 = mescn[(mesind2 + 1):(mesind3)]
        arg3 = mescn[(mesind3 + 1):]
        print(arg1 + "a")
        print(arg2 + "b")
        print(arg3 + "c")
        http = urllib3.PoolManager()
        print('https://script.google.com/macros/s/AKfycby2Ly9d0yXAqYlW50zo1D51CQmTHEdnKnHd3gzNdlME4sPrC_U/exec?text=' + urllib.parse.quote(arg3) + "&source=" + arg1 + "&target=" + arg2)
        r = http.request('GET','https://script.google.com/macros/s/AKfycby2Ly9d0yXAqYlW50zo1D51CQmTHEdnKnHd3gzNdlME4sPrC_U/exec?text=' + urllib.parse.quote(arg3) + "&source=" + arg1 + "&target=" + arg2)
        rd = r.data
        rdd = codecs.decode(r.data,'utf-8')
        print(rdd)
        rd = str(rd)
        find = rd.find("xt")
        datas = rd[(find + 5):-3]
        #datas = datas[3:-3]
        
        
        await message.channel.send(datas)
        print(codecs.decode("b'" + datas + "'",'utf-8')) 
        datase = codecs.decode(datas,"utf-8")
        await message.channel.send(datase)
    if message.content.startswith('$slot'):
        slot1 = 0
        slot2 = 0
        slot3 = 0
        slot4 = 0
        slot5 = 0
        slot6 = 0
        slot7 = 0
        slot8 = 0
        slot9 = 0
        slot_hit = 0
        slot_random = random.randrange(5)
        if slot_random == 0:
            slot1 = ":heart:"
        elif slot_random == 1:
            slot1 = ":yen:"
        elif slot_random == 2:
            slot1 = ":mahjong:"
        elif slot_random == 3:
            slot1 = ":flag_kp:"
        else:
            slot2 = ":video_game:"
        slot_random = random.randrange(5)
        if slot_random == 0:
            slot2 = ":heart:"
        elif slot_random == 1:
            slot2 = ":yen:"
        elif slot_random == 2:
            slot2 = ":mahjong:"
        elif slot_random == 3:
            slot2 = ":flag_kp:"
        else:
            slot3 = ":video_game:"
        slot_random = random.randrange(5)
        if slot_random == 0:
            slot3 = ":heart:"
        elif slot_random == 1:
            slot3 = ":yen:"
        elif slot_random == 2:
            slot3 = ":mahjong:"
        elif slot_random == 3:
            slot3 = ":flag_kp:"
        else:
            slot3 = ":video_game:"
        slot_random = random.randrange(5)
        if slot_random == 0:
            slot4 = ":heart:"
        elif slot_random == 1:
            slot4 = ":yen:"
        elif slot_random == 2:
            slot4 = ":mahjong:"
        elif slot_random == 3:
            slot4 = ":flag_kp:"
        else:
            slot4 = ":video_game:"
        slot_random = random.randrange(5)
        if slot_random == 0:
            slot5 = ":heart:"
        elif slot_random == 1:
            slot5 = ":yen:"
        elif slot_random == 2:
            slot5 = ":mahjong:"
        elif slot_random == 3:
            slot5 = ":flag_kp:"
        else:
            slot5 = ":video_game:"
        slot_random = random.randrange(5)
        if slot_random == 0:
            slot6 = ":heart:"
        elif slot_random == 1:
            slot6 = ":yen:"
        elif slot_random == 2:
            slot6 = ":mahjong:"
        elif slot_random == 3:
            slot6 = ":flag_kp:"
        else:
            slot6 = ":video_game:"
        slot_random = random.randrange(5)
        if slot_random == 0:
            slot7 = ":heart:"
        elif slot_random == 1:
            slot7 = ":yen:"
        elif slot_random == 2:
            slot7 = ":mahjong:"
        elif slot_random == 3:
            slot7 = ":flag_kp:"
        else:
            slot7 = ":video_game:"
        slot_random = random.randrange(5)
        if slot_random == 0:
            slot8 = ":heart:"
        elif slot_random == 1:
            slot8 = ":yen:"
        elif slot_random == 2:
            slot8 = ":mahjong:"
        elif slot_random == 3:
            slot8 = ":flag_kp:"
        else:
            slot8 = ":video_game:"
        slot_random = random.randrange(5)
        if slot_random == 0:
            slot9 = ":heart:"
        elif slot_random == 1:
            slot9 = ":yen:"
        elif slot_random == 2:
            slot9 = ":mahjong:"
        elif slot_random == 3:
            slot9 = ":flag_kp:"
        else:
            slot9 = ":video_game:"
        await message.channel.send("==========")
        await message.channel.send("|" + str(slot1) + "|" + str(slot2) + "|" + str(slot3) + "|")
        await message.channel.send("|" + str(slot4) + "|" + str(slot5) + "|" + str(slot6) + "|")
        await message.channel.send("|" + str(slot7) + "|" + str(slot8) + "|" + str(slot9) + "|")
        await message.channel.send("==========")
        if slot1 == slot2 and slot2 == slot3:
            slot_hit = slot_hit + 1
        if slot4 == slot5 and slot5 == slot6:
            slot_hit = slot_hit + 1
        if slot7 == slot8 and slot8 == slot9:
            slot_hit = slot_hit + 1
        if slot1 == slot4 and slot4 == slot7:
            slot_hit = slot_hit + 1
        if slot2 == slot5 and slot5 == slot8:
            slot_hit = slot_hit + 1
        if slot3 == slot6 and slot6 == slot9:
            slot_hit = slot_hit + 1
        if slot1 == slot5 and slot5 == slot9:
            slot_hit = slot_hit + 1
        if slot3 == slot5 and slot5 == slot7:
            slot_hit = slot_hit + 1
        if slot_hit == 0:
            await message.channel.send("全部外れました")
        if slot_hit != 0:
            await message.channel.send(str(slot_hit) + "列当たりました！")

        
async def greet():
    channel = client.get_channel(greetchannel)
    await channel.send('Hi,everyone!')





async def uranai():
    uranai = 0
    uranai = random.randrange(10)
    if uranai == 0:
        return '大凶です^^'
    if uranai == 1:
        return '凶くらいです^^'
    if uranai == 2:
        return '中凶です^^'
    if uranai == 3:
        return '小凶です^^'
    if uranai == 4:
        return 'なんともないでしょう^^'
    if uranai == 5:
        return '小吉です^^'
    if uranai == 6:
        return '末吉です^^'
    if uranai == 7:
        return '中吉です^^'
    if uranai == 8:
        return '吉です^^'
    if uranai == 9:
        return '大吉です^^'
    if uranai == 10:
        return '見事枠にない1つに当たりましたね！大凶です！'
#役職君
async def rolegive1(payload):
        if payload.emoji.name != EMOJI_WELCOME:
            return
        channel = client.get_channel(payload.channel_id)
        if channel.id != CHANNEL_WELCOME:
            return
        member = channel.guild.get_member(payload.user_id)
        role = channel.guild.get_role(ROLE_WELCOME)
        await member.add_roles(role)
        return member
@client.event
async def on_raw_reaction_add(payload):
    member = await rolegive1(payload)
#実行らしい
class MyBot(commands.Bot):
    @commands.command()
    async def test(self, ctx):
        await ctx.send('pong!')
if __name__ == '__main__':
    bot = MyBot(command_prefix='!')
client.run(TOKEN)
         
                  
        

