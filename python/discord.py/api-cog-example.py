# kind of "basic" cog with api get reqs using aiohttp
from discord.ext import commands
import discord
import aiohttp
import io


class MyApiCog(commands.Cog):
  
  
  def __init__(self, bot):
    self.bot = bot
    self.base_url = "https://some-random-api.ml/"  # we'll be using sra
    
    self._available_animals = ("dog", "cat", "panda", "red_panda", "fox", "birb", "bird", "koala", "whale", "racoon", "kangaroo")
    self.session = aiohttp.ClientSession()
    
    
  def cog_unload(self):
    if not self.session.closed:
      self.bot.loop.create_task(self.session.close())  # closes session when cog gets unloaded
  
  async def _canvas_to_file(self, *, endpoint, member: discord.Member, img_type="png"):  # converts canvas endpoint to discord.File
    async with self.session.get(self.base_url + f"canvas/{endpoint}?avatar={member.avatar_url_as(format='png', size=1024)}") as f:
      data = io.BytesIO(await f.read())
    return discord.File(data, f"sra-image.{img_type}")
    
  @commands.command(name="triggered")
  async def _triggered(self, ctx, user: discord.Member = None):
    if user is None:
      user = ctx.author
                                
    _trigger_gif = await self._canvas_to_file(endpoint="triggered", member=user, img_type="gif")
    
    await ctx.send(file=_trigger_gif)
    # why didn't i just embed this instead? 
                                
    # 1. You can't embed a discord.File object
    # 2. You can only use url for embedding images
    # 2.1. If the user changes pfp after the cmd has been executed with embed and url, the 
    #      img url won't embed anymore bc no one can access old pfp links aka the img link is now useless

    
  @commands.command(name="wasted")
  async def _wasted(self, ctx, user: discord.Member = None):
    if user is None:
      user = ctx.author
                                
    _wasted_img = await self._canvas_to_file(endpoint="wasted", member=user)
    
    await ctx.send(file=_wasted_img)

  # you can continue making image manipulation cmds with the same format on every canvas endpoint in sra
                                
                                
  async def _get_animal_fact(self, animal_name):
    if animal_name not in self._available_animals:
      raise RuntimeError("Given animal name '{}' is not available.".format(animal_name))
      
    async with self.session.get(self.base_url + f"facts/{animal_name}") as _fact:
      fact_json = await _fact.json()
    return fact_json["fact"]
  
  async def _get_animal_img(self, animal_name):
    if animal_name not in self._available_animals:
      raise RuntimeError("Given animal name '{}' is not available.".format(animal_name))
      
    async with self.session.get(self.base_url + f"img/{animal_name}") as _img:
      img_json = await _img.json()
    return img_json["link"]

    
  @commands.command(name="dog_fact")
  async def _dog_fact(self, ctx):
    _animal_fact = await self._get_animal_fact("dog")
    _animal_img = await self._get_animal_img("dog")
    
    em = discord.Embed(title="Dog Fact", description=_animal_fact, color=0xab7343)
    em.set_thumbnail(url=_animal_img)
    
    await ctx.send(embed=em)
    
  @commands.command(name="birb_fact")
  async def _birb_fact(self, ctx):
    _animal_fact = await self._get_animal_fact("bird")
    _animal_img = await self._get_animal_img("birb")
    
    em = discord.Embed(title="Birb Fact", description=_animal_fact, color=0x019fd3)
    em.set_thumbnail(url=_animal_img)
    
    await ctx.send(embed=em)
    
  # you can continue adding fact commands of each animal on self._available_animals
  
  # references used:
  #   https://discordpy.readthedocs.io/en/latest/faq.html#how-do-i-upload-an-image
  #   https://github.com/iDutchy/sr_api/blob/master/sr_api/client.py
  #   https://docs.aiohttp.org/en/stable/client_reference.html
  #   https://some-random-api.ml/
    
def setup(bot):
  bot.add_cog(MyApiCog(bot))
