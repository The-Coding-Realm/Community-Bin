# Code made by Myst | 죽음#9105

# This Modules are Really Important for these commands so Make sure you have Installed them!
import discord
from discord.ext import commands

import io, os, sys # Some Small Tools!

import platform # For Showing the OS
import datetime # For Time
import psutil # For Cool And Awesome Stats

class Info(commands.Cog):
    def __init__(self, Bot):
        self.Bot = Bot

# For People who wants to make a cool Botinfo Command with some useful Stats 

    @commands.command()
    async def botinfo(self, ctx):

        # Basic Information of the Bot
        botName = "" # <- Place Your Bot Name Here
        botID = "" # <- Place your Bot ID here!


        # System and Stats 
        pythonVersion = platform.python_version() # Shows the Version of Python
        dpyVersion = discord.__version__ # Shows the Version of Discord.py
        serverCount = len(self.Bot.guilds) # Shows the Server Count! 
        memberCount = len(set(self.Bot.get_all_members())) # Shows the Member Count
        self.Bot.version = '0.1' # Optional | You can set your Bot Version Here :)
        botCommands = len(self.Bot.commands) # Gets the number of commands that you have made in Bot!
        latency = f"{round(self.Bot.latency*1000)} ms." # Gets the Bot's Latency
        cpu = str(psutil.cpu_percent()) # Shows the CPU's Stats
        
        # Boot Function
        boot_time = str(psutil.boot_time() / 100000000) # Boot Function which is rounded
        boot_time_round = boot_time[:4] # The Final Boot Variable

        # Owner Variables
        RealOwner = self.Bot.get_user() # <- Place Your User ID Inside the () brackets
        CoOwner = self.Bot.get_user() # < -Optional | If you got another CO - Owner then place his User ID inside the brackets

        embed = discord.Embed(description = f"```\nBot's Name: {botName}  [{botID}]\nBot's Latency: {latency}\nWeb Socket Latency: {round(self.Bot.latency * 1000, 2)}ms```", color = 0x9d88e6, timestamp = ctx.message.created_at)
        
        embed.add_field(name = f"General" , value = "```\nBoot Time: {}\nUsers: {}\nServers: {}```".format(boot_time_round, memberCount, serverCount))
        embed.add_field(name = f"Other Info" , value = "```\nDiscord.py: {}\nPython: {}\nArezCore v{}```".format(pythonVersion, dpyVersion, self.Bot.version))
        embed.add_field(name = f"System" , value = "```\nOS: {}\nCPU: {}%\nCommands: {}\n```".format(platform.system(), cpu, botCommands))

        embed.add_field(name = f"Creator [2]" , value = f"```Owners: {RealOwner.name}#{RealOwner.discriminator} [{RealOwner.id}]\n      - {CoOwner.name}#{CoOwner.discriminator} [{CoOwner.id}]```\nMentions: {RealOwner.mention}, {CoOwner.mention}")
        embed.add_field(name = f"Some Important Links!" , value = f"[Invite](https://discord.com/oauth2/authorize?client_id={botID}&scope=bot&permissions=470150352)", inline = False)

        embed.set_thumbnail(url = self.Bot.user.avatar_url)
        embed.set_author(name = self.Bot.user.name + ("'s Information") , icon_url = self.Bot.user.avatar_url)

        await ctx.send(embed = embed)

    
    
    # Userinfo Command | I have renovated it and it Looks nice tbh :)
    
    # Some Important Things
    # For Emojis, Create a Folder Outside the Cogs named "Others" and inside create a new file named "emote.py"
    # Now Inside create a Variable and paste the emoji id, For Example:

    # Status Emojis
    # online = "<:Online:818737517603717130>"
    
    # And For the Emojis, It Depends on you that Do you want to Add Emojis to Not! For Beauty I have Added Emoji so it Depends on you :D
    
    # For More Clear View, Copy the link and paste it in your broswer and then yeh you can see it!
    #https://cdn.discordapp.com/attachments/809279767403954206/823452151765794826/emoji.png


    @commands.command(aliases=["whois"])
    @commands.guild_only()
    async def userinfo(self, ctx, member: discord.Member = None):
        """
        Get all the information about a user
        """
        member = ctx.author if not member else member
        roles = [role for role in member.roles]

        status_activity = ""

        for status_activity in member.status:
           
            if "online" in member.status:
                status_activity = f"Online {emote.online}"   

            if "offline" in member.status:
                status_activity = f"Offline {emote.offline}" 

            if "idle" in member.status:
                status_activity = f"Idle {emote.idle}" 

            if "dnd" in member.status:
                status_activity = f"DND {emote.dnd}"    

            else:
                pass



        embed = discord.Embed(colour=0x9d88e6, timestamp=ctx.message.created_at)
        
        embed.add_field(name = "📘 __General Information__" , value = f"**Username :** {member}\n" 
                                                                   f"**Nickname :** {member.nick}\n" f"**User ID :** {member.id}\n"                                                                    
                                                                   f"**Is Bot? :** {member.bot}\n" f"**Created At :** {member.created_at.strftime('%a, %#d %B %Y, %I:%M %p')}\n")

        embed.add_field(name = "📜 __Server Information!__" , value = f"**Joined At :** {member.joined_at.strftime('%a, %#d %B %Y, %I:%M %p')}\n" 
                                                                      f"**Boosting? : [Working on it]** ",
                                                                      inline = False)

        embed.add_field(name = f"🎑 __Roles Information__" , value=f"**Highest Role :** {member.top_role.mention}\n" 
                                                                                 f"**Role(s) [{len(member.roles)}]** " + ", ".join([role.mention for role in roles]))
        
        embed.add_field(name = f"🎫 __Activities__" , value = f"**Status :** {status_activity}\n"
                                                                       f"**Activity : ** {member.activity}",
                                                                       inline = False)        

    # An Cool Looking "Avatar" Command with "Download Avatar" Option
    # This is a Really Good Looking thing so.. Enjoy? :D

    @commands.command()
    @commands.guild_only()
    async def avatar(self, ctx, *,  member : discord.Member=None):
        """
        Sends the Avatar of an User
        """
        if member is None:
            member = ctx.author
        
        userAvatarUrl = member.avatar_url
        embed=discord.Embed(title=f"{member.name}'s' avatar" , description = f"Click Here to [Download Avatar]({member.avatar_url})" , color = 0x9d88e6)
        embed.set_image(url=userAvatarUrl)
        
        embed.set_footer(text = f"Requested by {ctx.author.name}")
        embed.set_author(name = f"{ctx.author}" , icon_url=userAvatarUrl)
        
        await ctx.send(embed=embed)

    # An Cool Looking "Servericon" Command with "Download Server Icon" Option
    # Hence Another Command lol!

    @commands.command(pass_context=True)
    @commands.guild_only()
    async def servericon(self, ctx, msg: str = None):
        """
        Shows the Server Guild Icon!
        """
        embed = discord.Embed(titile="", description = f"**{ctx.guild.name}'s** Server Icon. [Click Here to Download]({ctx.guild.icon_url})", color = 0x9d88e6)
        
        embed.set_author(name = f"{ctx.author}" , icon_url= ctx.author.avatar_url)
        embed.set_image(url = ctx.guild.icon_url)
        await ctx.send(embed=embed)


def setup(Bot):
    Bot.add_cog(Info(Bot))

# At last I don't what to say but I want you to learn Python! I won't help you anything regarding this codes
# Because, what are you achieving without learning Coding or Python? If I get useless DM and you say something really stupid
# Then I am Sorry, I can't help you. Learn Something by your own! I have given some tips and basic idea!
# I suggest not to Copy - Paste because it's really useless for you and your time :)
# Hope you Understand :D! Peace!!!
