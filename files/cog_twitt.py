# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 23:41:51 2020

@author: tsutitire
"""
from discord.ext import commands
import discord
import random
import tweepy
class twitcog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def twitter(self,ctx,*args):
        if len(args) == 0:
            await ctx.message.channel.send("引数が少なすぎます. なにが指定できるかは $twitter help で!")
            pass
        if args[0] == "help":
            embed = discord.Embed(title="The help of Minimoka commands obout twitter",description="Twitterコマンドのいろいろが書いてあるよ！" )
            embed.add_field(name="$twitter search <アカウントID> <遡るツイート数>",value="その人のツイートを調べられます")
            embed.add_field(name="$twitter search-all <検索キーワード> <遡るツイート数>",value="ツイートを調べられます")
            await ctx.message.channel.send(embed=embed)
        if args[0] == "search":
            if len(args) == 3:
            
                embed = discord.Embed(title="Twitter info",description="minimoka-twitter-serch" )
                
                CONSUMER_KEY = ''
                
                CONSUMER_SECRET = ''
                
                ACCESS_KEY = ''
                
                ACCESS_SECRET = ''
                
                auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
                
                auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
                
                api = tweepy.API(auth)
                
                
                #api.update_status("テストメッセージを投稿してみてます、つちさんです。")
                
                Account = args[1] #取得したいユーザーのユーザーIDを代入
                try:
                    if int(args[2]) >= 30:
                        args[2] = 30
                except:
                    await ctx.message.channel.send("取得ツイート数は半角数字で入力してくださいな それか数がおかしいか多すぎるかも？")
                    pass
                
                try:
                    tweets = api.user_timeline(Account, count=int(args[2]), page=1)
                except:
                    await ctx.message.channel.send("名前とか、間違ってませんか？")
                    pass
                num = 1 #ツイート数を計算するための変数
                for tweet in tweets:
                    #print('twid : ', tweet.id)               # tweetのID
                    #print('user : ', tweet.user.screen_name)  # ユーザー名
                    #print('date : ', tweet.created_at)      # 呟いた日時
                    #print('favo : ', tweet.favorite_count)  # ツイートのいいね数
                    #print('retw : ', tweet.retweet_count)  # ツイートのリツイート数
                    #print('ツイート数 : ', num) # ツイート数
                    #print('='*80) # =を80個表示
                    print("twitter:serch:embed added...")
                    embed.add_field(name="contents： " + str(tweet.text),value="time： " + str(tweet.created_at) + " likes/retweet： " + str(tweet.favorite_count) + "/" + str(tweet.retweet_count))
                    num += 1 # ツイート数を計算
                await ctx.message.channel.send(embed=embed)
            else:
                await ctx.message.channel.send("引数が不正ですよ!")
                
        if args[0] == "search-all":
            if len(args) == 3:
            
                embed = discord.Embed(title="Twitter info",description="minimoka-twitter-serch" )
                
                CONSUMER_KEY = ''
                
                CONSUMER_SECRET = ''
                
                ACCESS_KEY = ''
                
                ACCESS_SECRET = ''
                
                auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
                
                auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
                
                api = tweepy.API(auth)
                
                
                try:
                    if int(args[2]) >= 30:
                        args[2] = 30
                except:
                    await ctx.message.channel.send("取得ツイート数は半角数字で入力してくださいな それか数がおかしいか多すぎるかも？")
                    pass
                
                try:
                    tweets = api.search(q=args[1], count=int(args[2]))
                except:
                    await ctx.message.channel.send("引数、間違ってませんか？")
                    pass
                num = 1 #ツイート数を計算するための変数
                for tweet in tweets:
                    #print('twid : ', tweet.id)               # tweetのID
                    #print('user : ', tweet.user.screen_name)  # ユーザー名
                    #print('date : ', tweet.created_at)      # 呟いた日時
                    #print('favo : ', tweet.favorite_count)  # ツイートのいいね数
                    #print('retw : ', tweet.retweet_count)  # ツイートのリツイート数
                    #print('ツイート数 : ', num) # ツイート数
                    #print('='*80) # =を80個表示
                    print("twitter:serch:embed added...")
                    embed.add_field(name="contents： " + str(tweet.text),value="time： " + str(tweet.created_at) + " likes/retweet： " + str(tweet.favorite_count) + "/" + str(tweet.retweet_count))
                    num += 1 # ツイート数を計算
                await ctx.message.channel.send(embed=embed)
            else:
                await ctx.message.channel.send("引数が不正ですよ!")
                