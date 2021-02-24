# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 23:41:51 2020

@author: tsutitire
"""
from discord.ext import commands
import random
import time

osama_step = 0
osama_memb = []
osama_numb= []

def uranai():
    if True == True:
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

class gamecog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener(name='on_message')
    async def good_reaction(self, message):
        if message.author.bot:
            return
        if 'いいね' in message.content:
            await message.add_reaction('\U0001f44d')
    @commands.command()
    async def dice(self,ctx):
        maxim = ctx.message.content[6:]
        maxim = int(maxim)
        dice = random.randrange(maxim)
        dice += 1
        await ctx.message.channel.send(dice)
    @commands.command()
    async def slot(self,ctx):
        if ctx.message.content.startswith('$slot'):
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
            await ctx.message.channel.send("==========")
            await ctx.message.channel.send("|" + str(slot1) + "|" + str(slot2) + "|" + str(slot3) + "|")
            await ctx.message.channel.send("|" + str(slot4) + "|" + str(slot5) + "|" + str(slot6) + "|")
            await ctx.message.channel.send("|" + str(slot7) + "|" + str(slot8) + "|" + str(slot9) + "|")
            await ctx.message.channel.send("==========")
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
                await ctx.message.channel.send("全部外れました")
            if slot_hit != 0:
                await ctx.message.channel.send(str(slot_hit) + "列当たりました！")
                
    @commands.command()
    async def janken(self,ctx):
        janken = random.randrange(3)
        jankenw = ctx.message.content
        jankenw = jankenw[8:]
        if jankenw == "r":
            if janken == 1:
                await ctx.message.channel.send("グーとグーで、あいこですね")
            elif janken == 2:
                await ctx.message.channel.send("グーとパーで、ボクの勝ちです！(｀・ω・´)")
            else:
                await ctx.message.channel.send("グーとチョキで、キミの勝ちです！(´・ω・`)")
        elif jankenw == "p":
            if janken == 1:
                await ctx.message.channel.send("パーとグーで、キミの勝ちです！(´・ω・`)")
            elif janken == 2:
                await ctx.message.channel.send("パーとパーで、あいこですね")
            else:
                await ctx.message.channel.send("パーとチョキで、ボクの勝ちです！(｀・ω・´)")
        elif jankenw == "s":
            if janken == 1:
                await ctx.message.channel.send("チョキとグーで、ボクの勝ちです！(｀・ω・´)")
            elif janken == 2:
                await ctx.message.channel.send("チョキとパーで、キミの勝ちです！(´・ω・`)")
            else:
                await ctx.message.channel.send("チョキとチョキで、あいこですね")
        else:
            await ctx.message.channel.send("r/p/sで指定してくださいよぉ...(-_-;)")
            
    @commands.command()
    async def omikuzi(ctx):
        await ctx.message.channel.send(uranai())
        
    @commands.command()
    async def osama(self,ctx):
        global osama_step,osama_memb,osama_numb
        arg = ctx.message.content[7:]
        if arg == "begin":
            if osama_step == 0:    
                await ctx.message.channel.send("王様ゲームが始まります！参加：$osama join 開始：$osama start")
                osama_step = 1
        if arg == "join":
            if osama_step == 1:
                if ctx.message.author not in osama_memb:
                    osama_memb.append(ctx.message.author)
                    osama_step = 2
        if arg == "start":
            if osama_step == 2:
                await ctx.message.channel.send("それはまず、それぞれに番号を抽選します！")
               
                for i in range(len(osama_memb)):
                   osama_numbs = [[i*1 for i in range(len(osama_memb))]]
                   osama = random.randrange(len(osama_memb) - i)
                   osama_numb.append(osama)
                   osama_numbs.pop(osama)
                  
                time.sleep(3)
                await ctx.message.channel.send("では次に、王様を発表します！")
                osama = random.randrange(len(osama_memb))
                await ctx.message.channel.send("王様は、　" + osama_memb[osama].name + "でした\n王様の命令を入力してください！\n入力したら、$osama end と入れてください！")
                osama_step = 3
        if arg == "end":
            if osama_step == 3:
                await ctx.message.channel.send("では、其々の番号を発表します！")
                messages = ""
                for i in range(len(osama_memb)):
                    messages = messages + str(osama_memb[i]) + "　：　" + str(osama_numb[i] + 1) + "\n"
                await ctx.message.channel.send(messages)    
                osama_step = 0
                osama_memb = []
                osama_numb = []