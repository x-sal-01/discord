import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == cleint.user:
        return

    if message.content.startswitch('$hello'):
        await message.channel.send('Hello!')

client.run(ODA0Nzc2NDQ4NDc5OTg1NjY0.YBRQeQ.WtK3HfgWS3Q7tmSDo36NhGNcAN8)
