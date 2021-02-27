# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 23:41:51 2020

@author: tsutitire
"""
from discord.ext import commands
import random
import discord
import asyncio
import os
import subprocess
import ffmpeg
import random
import urllib3
import urllib.error
import urllib.request
import requests
import urllib.parse
import json
import datetime
import time
#import requests as rqs
import bs4
from bs4 import BeautifulSoup
import codecs
class datacog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def helps(self,ctx):
        embed = discord.Embed(title="The help of Minimoka",description="ボク、ミニもかについてのいろいろが書いてあるよ！" )
        embed.set_image(url="https://b.imgef.com/POuypFI.png")
        embed.add_field(name="$janken",value="じゃんけんができます！ $jankeng(グー)/p(パー)/s(チョキ)で指定可能ですよ～")
        embed.add_field(name="$omikuzi",value="キミを占ってあげよう")
        embed.add_field(name="$bj/$bjget/$bjstand",value="ブラックジャックができます！ $bjで開始、 カードを引くなら$bjget,引かないなら$bjstandです!")
        embed.add_field(name="$slot",value="スロットができます　リアルマネーをとかす心配はないですよ♪")
        embed.add_field(name="$UUID ユーザー名",value="誰かのマイクラでのUUIDを取得できます") 
        embed.add_field(name="$skin UUID",value="誰かのマイクラでのスキンを取得できます")
        embed.add_field(name="$sknf UUID",value="誰かのマイクラでのスキンを取得できます")
        embed.add_field(name="$avat ユーザー名",value="誰かのマイクラでの頭を取得できます")
        embed.add_field(name="$skn2 ユーザー名",value="誰かのマイクラでのスキンの展開図を取得できます")
        embed.add_field(name='$trsl 変換元言語,変換先言語,"変換する文章"',value="Google翻訳をしてくれます　言語の例：ru(ロシア)en(英語)ja(日本語)")
        embed.add_field(name='$radar',value="誰かと艦隊ゲームで遊べます！")
        embed.add_field(name='$bitc',value="ビットコインのレートが見れます♪")
        embed.add_field(name='$join',value="VCにログインします。チャット内容を読み上げてくれます。")
        embed.add_field(name="$bye",value="VCからログアウトします")
        embed.add_field(name="$voiceadd 1～5",value="みにもかの読み上げる声をカスタムします（自分だけです）")
        embed.add_field(name="k$ を最初に入れる", value="みにもかと会話ができます、例えば:k$おはよう")
        embed.add_field(name="$twitter", value="$twitter help => help")
        await ctx.message.channel.send(embed=embed)
    
    
        
    @commands.command()
    async def bitc(self,ctx):
        http = urllib3.PoolManager()
        link = 'https://api.coindesk.com/v1/bpi/currentprice/JPY.json'
        r = http.request('GET',link)
        rr = str(r.data)
        print(rr)
        rind1 = rr.find('"rate"')
        rind2 = rr.find('","',rind1)
        rind3 = rr.find('"rate"',rind2)
        rind4 = rr.find('","',rind3)
        print(str(rind1) + "a" + str(rind2) + "b" + str(rind3) + "c" + str(rind4))
        rdat1 = rr[(rind1 + 8):(rind2 - 1)]
        rdat2 = rr[(rind3 + 8):(rind4 - 1)]
        await ctx.message.channel.send("USD: " + rdat1 + " $ and JPY: " + rdat2 + "￥")
        
    @commands.command()
    async def skin(self,ctx):
        http = urllib3.PoolManager()
        UUID = ctx.message.content[6:]
        print (UUID)
        UUID = 'https://crafatar.com/renders/body/' + UUID + "?overlay"
        print (UUID)
        r = http.request('GET',UUID)
        embed = discord.Embed(title=str(ctx.message.content[6:]) + 's SKIN',description="スキンだよ！" )
        embed.set_image(url=UUID)
        await ctx.message.channel.send(embed=embed)    
        
    @commands.command()
    async def sknf(self,ctx):
        http = urllib3.PoolManager()
        UUID = ctx.message.content[6:]
        print (UUID)
        UUID = 'https://crafatar.com/renders/body/' + UUID 
        print (UUID)
        r = http.request('GET',UUID)
        embed = discord.Embed(title=str(ctx.message.content[6:]) + 's SKIN',description="スキンだよ！" )
        embed.set_image(url=UUID)
        await ctx.message.channel.send(embed=embed)
        
    @commands.command()
    async def skn2(self,ctx):
        http = urllib3.PoolManager()
        UUID = ctx.message.content[6:]
        print (UUID)
        UUID = 'https://minotar.net/skin/' + UUID
        print (UUID)
        r = http.request('GET',UUID)
        embed = discord.Embed(title=str(ctx.message.content[6:]) + 's Skins',description="展開図だよ！" )
        embed.set_image(url=UUID)
        await ctx.message.channel.send(embed=embed)   
    @commands.command()
    async def avat(self,ctx):
        http = urllib3.PoolManager()
        UUID = ctx.message.content[6:]
        print (UUID)
        UUID = 'https://minotar.net/avatar/' + UUID
        print (UUID)
        r = http.request('GET',UUID)
        embed = discord.Embed(title=str(ctx.message.content[6:]) + 's Avatar',description="顔面だよ！" )
        embed.set_image(url=UUID)
        await ctx.message.channel.send(embed=embed)
        http = urllib3.PoolManager()
        UUID = ctx.message.content[6:]
        print (UUID)
        UUID = 'https://minotar.net/skin/' + UUID
        print (UUID)
        r = http.request('GET',UUID)
        embed = discord.Embed(title=str(ctx.message.content[6:]) + 's Skins',description="展開図だよ！" )
        embed.set_image(url=UUID)
        await ctx.message.channel.send(embed=embed)
        
    
    @commands.command()
    async def uuid(self,ctx):
        http = urllib3.PoolManager()
        MCID = ctx.message.content[6:]
        MCID = 'https://api.mojang.com/users/profiles/minecraft/' + MCID
        print (MCID)
        r = http.request('GET',MCID)
        print (r.data)
        findr = str(r.data)
        indA = findr.find(',')
        findr = findr[(indA + 7):-3]
        await ctx.message.channel.send(findr)
        findr = findr[0:8] + '-' + findr[8:12] + '-' + findr[12:16] + '-' + findr[16:20] + '-' + findr[20:]
        await ctx.message.channel.send(findr)
        
    @commands.command()
    async def mojang(self,ctx):
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
        await ctx.message.channel.send(embed=embed)
    
    
    
    #@commands.command()
    #async def mcbans(ctx):
        #mcid = ctx.message.content[8:]
        #res = rqs.get('https://www.mcbans.com/player/' + str(mcid))
        #res.raise_for_status()
        #soup = bs4.BeautifulSoup(res.text, "html.parser")
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
        #print(soup)
        #soup = str(soup)
        #count = 0
        #count2 = 0
        #embed = discord.Embed(title="MCBANS",description=str(mcid) + "'s mcbans data")
        #count2 = 0
        #while count != 4: 
            #count = count + 1
            #count2 = count2 + 1
            #print(count)
            #print(count2)
            #if count == 1:
                #sind1 = soup.find("section-content")
                #print(sind1)
                #sind2 = soup.find("<",sind1)
                #print(sind2)
                #sind3 = sind1 + 15
            #if count != 1:
                #sind1 = soup.find("section-content",sind3)
                #sind1 = soup.find(">",(sind1 + 17))
                #sind2 = soup.find("<",sind1)
                #print(sind1)
                #print(sind2)
                #sind3 = sind1 + 15
            #if count == 1:
                #embed.add_field(name=str(mcid) + "'s Reputation", value=soup[(sind1 + 17):(sind2)])
            #if count == 2:
                #embed.add_field(name=str(mcid) + "'s Issued Bans", value=soup[(sind1 + 17):(sind2)])     
            #if count == 3:
                #embed.add_field(name=str(mcid) + "'s UUID", value=soup[(sind1 + 40):(sind2)])
            #if count == 4:
                #embed.add_field(name=str(mcid) + "'s Bans", value=soup[(sind1 + 17):(sind2)])
        #await ctx.message.channel.send(embed=embed)
        
    @commands.command()
    async def voiceadd(self,ctx,arg):
        input_file = 'files/userdata-v.txt'
        with open(input_file,'r',encoding='utf-8') as file:
            lists = file.read()
        lista = lists.split()
        pid = ctx.message.author.id
        pid = str(pid)
        if pid in lista:
            al = lista.index(pid)
            dummy = lista.pop(al)
            dummy = lista.pop(al)
            dummy = dummy
            try:
                arg1 = int(arg)
            except:
                await ctx.message.channel.send("形式が正しくないです...")
            arg1 = str(arg1)
            lista.insert(al, pid)
            lista.insert(al + 1, arg1)
        else:
            lista.append(pid)
            arg1 = str(arg)
            lista.append(arg1)
        strings = ""
        for i in range(len(lista)):
            strings = strings + " " + lista[i]
        print(strings)
        strings = strings[1:]
        with open(input_file,'w',encoding='utf-8') as file:
            file.write(strings)
        
    @commands.command()
    async def teikiadd(self,ctx,arg):
        global file_inside
        input_file = 'files/userdata-t.txt'
        with open(input_file,'r',encoding='utf-8') as file:
            lists = file.read().replace(":"," ")
        lista = lists.split()
        pid = ctx.message.author.id
        pid = str(pid)
        #channel = discord.utils.get(ctx.guild.channels, name=ctx.message.channel)
        cid = ctx.message.channel.id
        cid = str(cid)
        
        #Userid:channelid:message userid...
        
        if pid in lista:
            al = lista.index(pid)
            dummy = lista.pop(al)
            dummy = lista.pop(al)
            dummy = lista.pop(al)
            dummy = dummy
            
            arg1 = str(arg)
            lista.insert(al, pid)
            lista.insert(al + 1, cid)
            lista.insert(al + 2, arg1)
            
        else:
            lista.append(pid)
            lista.append(cid)
            arg1 = str(arg)
            lista.append(arg1)
        strings = ""
        for i in range(len(lista)):        
            strings = strings + " " + lista[i]
            
        print(strings)
        strings = strings[1:]
        with open(input_file,'w',encoding='utf-8') as file:
            file.write(strings)
            
            
    @commands.command()
    async def trsl(self,ctx):
        mescn = ctx.message.content
        mesind1 = mescn.find(",")
        mesind2 = mescn.find(",",(mesind1))
        mesind3 = mescn.find(",",(mesind2 + 1))
        arg1 = mescn[6:mesind1]
        arg2 = mescn[(mesind2 + 1):(mesind3)]
        arg3 = mescn[(mesind3 + 1):]
        '''
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
        '''
        url = 'https://script.google.com/macros/s/AKfycby2Ly9d0yXAqYlW50zo1D51CQmTHEdnKnHd3gzNdlME4sPrC_U/exec?text=' + urllib.parse.quote(arg3) + "&source=" + arg1 + "&target=" + arg2
        req = requests.get('https://script.google.com/macros/s/AKfycby2Ly9d0yXAqYlW50zo1D51CQmTHEdnKnHd3gzNdlME4sPrC_U/exec?text=' + urllib.parse.quote(arg3) + "&source=" + arg1 + "&target=" + arg2)
        
        #await ctx.message.channel.send(datas)
        #print(codecs.decode("b'" + datas + "'",'utf-8')) 
        #datase = codecs.decode(datas,"utf-8")
        #await ctx.message.channel.send(datase)
        rtext = req.text
        rtext = rtext[22:-4]
        await ctx.message.channel.send(rtext)
