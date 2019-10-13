import discord

client = discord.Client()
TOKEN = "<Token>"

@client.event
async def on_ready():

    ch_name = "チャンネル名"

    for channel in client.get_all_channels():
        if channel.name == ch_name:
            await channel.send("起動しました")

client.run(TOKEN)