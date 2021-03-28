import discord
from discord.ext import commands


TOKEN = "YOUR BOT TOKEN"

class Owner(commands.Cog):
    def __init__(self, Bot):
        self.Bot = Bot

    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, name: str):
        """Load any extension"""
        try:
            self.bot.load_extension(f"cogs.{name}")

        except Exception as e:
            return await ctx.send(default.traceback_maker(e))
        await ctx.send(f"✅ | Loaded extension **{name}**")

    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, name: str):
        """Unload any extension"""
        try:
            self.bot.unload_extension(f"cogs.{name}")
        except Exception as e:
            return await ctx.send(default.traceback_maker(e))
        await ctx.send(f"✅ | Unloaded extension **{name}**")

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, name: str):
        """Reload any loaded extension."""
        try:
            self.bot.reload_extension(f"cogs.{name}")
        except Exception as e:
            return await ctx.send(default.traceback_maker(e))
        await ctx.send(f"✅ | Reloaded extension **{name}**")

    @commands.command()
    @commands.is_owner()
    async def shutdown(self, ctx):
        """Shutdown the bot"""
        await ctx.send(f"✅ | Shutting down the system ...")
        await self.bot.close(TOKEN)

    @commands.command()
    @commands.is_owner()
    async def restart(self, ctx):
        """Restart the bot"""
        await ctx.send(f"✅ | Restarting down the system ...")
        await self.bot.login()
        
def setup(Bot):
    Bot.add_cog(Owner(Bot))
