import os

from dotenv import load_dotenv

import discord
from discord.ext import commands

load_dotenv()

intents = discord.Intents.all()
intents.presences = False

# Define the actual subclassed bot inheriting from commands.Bot or commands.AutoShardedBot
class BadBot(commands.Bot):  # use commands.AutoShardedBot if you want to shard the bot
    def __init__(self, *args, **kwargs):
        # initialising the super class
        super().__init__(
            command_prefix=self._get_bot_prefix,  # The get prefix function
            owner_id=711444754080071714,  # fill this with your ID
            # owner_ids=[your_moms_id, your_dads_id] # use this if there are multiple owners,
            intents=intents,  # customise it accordingly, I prefer not to use presence intents, they have no use for me
            allowed_mentions=discord.AllowedMentions(
                everyone=False, roles=False, users=True, replied_user=False
            ),  # customise it accordingly again :)
            description="This is a bad bot, by Donut#4427 who doesn't even know how to code",  # the bot's description
            case_insensitive=True,  # case insensitivity
            strip_after_prefix=True,  # Whether to strip whitespace characters after encountering the command prefix
            *args,  # obvious
            **kwargs,  # obvious
        )
        self.secrets = {
            x: y
            for x, y in os.environ.items()
            if x in ["TOKEN"]  # add more to these keys accordingly
        }  # Our secrets keys kept as a dictionary
        self.bot_cogs = [
            f"cogs.{cog[:-3]}"
            for cog in os.listdir("cogs")
            if cog.endswith(".py")
            and not cog.startswith(
                "_"
            )  # files not starting with _ and ending with .py will be considered
        ]  # if you use cogs ¯\_(ツ)_/¯

    def run(self):
        try:
            for cog in self.bot_cogs:  # loading all the cogs
                try:
                    self.load_extension(cog)
                    print(f"Loaded {cog[5:]}")
                except:
                    raise
        except:
            raise
        super().run(self.secrets["TOKEN"])  # Running the bot :)

    async def _get_bot_prefix(self, bot, message):
        prefixes = ["!", "?"]  # do db stuff here, imma keep it static
        base = [f"<@!{bot.user.id}> ", f"<@{bot.user.id}> "]  # mention prefixes
        return [*prefixes, *base]

    async def on_ready(self):  # on_ready event
        print(f"Logged in as {self.user}.")

    async def process_commands(
        self, message
    ):  # https://discordpy.readthedocs.io/en/master/ext/commands/api.html#discord.ext.commands.Bot.process_commands
        if not message.guild or message.author.bot:
            return

        await super().process_commands(message)
