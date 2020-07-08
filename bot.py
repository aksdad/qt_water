import discord
from discord.ext import tasks, commands

token = ""
emoji = '💦'


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
        user = self.get_user()
        print('sending message to channel ' +
              '729573884722151486: ' + message_channel.name + '\n')
        message = await message_channel.send('drink water pls domo arigatou - Sahil \'Darky\' Guleria')
        await message.add_reaction(emoji)
        print('sending message to user ' +
              '240873900307775498: ' + user.name + '\n')
        await user.send('drinkit')


client = MyClient()
client.run(token)
