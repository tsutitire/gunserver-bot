# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 17:54:58 2021

@author: tsuti
"""
import discord
from discord.ext import commands
#files/userdata-r
#@client.event
#async def on_reaction_add(reaction,member):
    #mes = reaction.message()
    
#@client.event
#async def on_reaction_remove(reaction,member):     
    #mes = reaction.message()

class reactcog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rolepanel(self,ctx,arg1,arg2):
        print("none")