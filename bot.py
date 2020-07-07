import discord
from discord.ext import tasks, commands

token = "NzI5NTcxMjk2OTU4MjE4MjUw.XwK6gA.5LqIhriwyHI5thu1UH0oGQU6y5Y"

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        self.water_printer.start()
    
    @tasks.loop(seconds=10.0)
    async def water_printer(self):
        message_channel = self.get_channel(729573884722151486)
        print('sending message to channel ' + '729573884722151486: ' + message_channel.name + '\n')
        await message_channel.send('drink water pls domo arigatou - Sahil \'Darky\' Guleria')



client = MyClient()
client.run(token)
