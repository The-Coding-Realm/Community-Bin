from discord.ext import commands


# Just a testing cog
class Handlers(commands.Cog):
    def __init__(self, trashest_bot_ever):
        self.trashest_bot_ever = trashest_bot_ever


def setup(trashest_bot_ever):
    trashest_bot_ever.add_cog(Handlers(trashest_bot_ever))
