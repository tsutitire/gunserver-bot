# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 23:41:51 2020

@author: tsutitire
"""
from discord.ext import commands
import random

#variables
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
RD_soc = 0
RD_usc = 0
RD_turn = 0
RD_som = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
RD_usm = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]



class gamecog2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener(name='on_message')
    async def good_reaction(self, message):
        if message.author.bot:
            return
        if 'いいね' in message.content:
            await message.add_reaction('\U0001f44d')
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
                    dummy = 0
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
                        soer = await message.guild.fetch_user(RD_sop)
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
                        soer = await message.guild.fetch_user(RD_sop)
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
                        soer = await message.guild.fetch_user(RD_sop)
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
                        soer = await message.guild.fetch_user(RD_sop)
                        user = await message.guild.fetch_user(RD_usp)
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
                        user = await message.guild.fetch_user(RD_usp)
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
                        user = await message.guild.fetch_user(RD_usp)
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
                        user = await message.guild.fetch_user(RD_usp)
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
                        soer = await message.guild.fetch_user(RD_sop)
                        user = await message.guild.fetch_user(RD_usp)
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
            soer = await message.guild.fetch_user(RD_sop)
            user = await message.guild.fetch_user(RD_usp)
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
            
    