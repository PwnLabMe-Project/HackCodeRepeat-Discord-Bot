import discord
from discord.ext import commands

class Social_Media(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command(aliases=["pwnlab","Pwnlab","PwnLab","PwnLabme","PwnLab.me","pwnlab.me"])
    async def pwnlabme(self, ctx):
        await ctx.channel.purge(limit=1)
        await ctx.send("https://pwnlab.me")

    @commands.command()
    async def ctf(self, ctx):
        await ctx.channel.purge(limit=1)
        await ctx.send("https://ctf.pwnlab.me")

    @commands.command()
    async def twitter(self, ctx):
        await ctx.channel.purge(limit=1)
        await ctx.send("https://twitter.com/PwnlabMe")

    @commands.command()
    async def linkedin(self, ctx):
        await ctx.channel.purge(limit=1)
        await ctx.send("https://www.linkedin.com/company/pwnlab")

    @commands.command()
    async def telegram(self, ctx):
        await ctx.channel.purge(limit=1)
        await ctx.send("https://t.me/CyberSec_TR")

    @commands.command()
    async def discord(self, ctx):
        await ctx.channel.purge(limit=1)
        await ctx.send("https://discord.gg/pwnlabme")

    @commands.command()
    async def github(self, ctx):
        await ctx.channel.purge(limit=1)
        await ctx.send("https://github.com/PwnLabMe-Project")
    
    @commands.command(aliases=["insta","ins"])
    async def instagram(self, ctx):
        await ctx.channel.purge(limit=1)
        await ctx.send("https://www.instagram.com/pwnlab.me/")    
    
    @commands.command(aliases=["sosyal","medya"])
    async def social(self, ctx):
        await ctx.channel.purge(limit=1)
        await ctx.send("""
        twitter: https://twitter.com/PwnlabMe
        instagram: https://www.instagram.com/pwnlab.me/
        linkedin:  https://www.linkedin.com/company/pwnlab
        telegram: https://t.me/CyberSec_TR
        discord: https://discord.gg/pwnlabme
        github: https://github.com/PwnLabMe-Project
        """)  

def setup(bot):
    bot.add_cog(Social_Media(bot))