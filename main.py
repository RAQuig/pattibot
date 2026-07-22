import discord

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

TARGET_CHANNEL_ID = 1448879000863899719  

PATTI_GIFS = [
    "https://tenor.com/view/hrithik-roshan-fighter-teaser-bollywood-teaser-vande-mataram-sujalam-sufalam-gif-4951463871021573191"
]

@client.event
async def on_ready():
    print(f'Bot active as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.id == TARGET_CHANNEL_ID:
        await message.channel.send("Yeah but have you seen Patti?")
        for gif in PATTI_GIFS:
            await message.channel.send(gif)

#Fetch token from server
TOKEN = os.getenv("DISCORD_TOKEN")
client.run(TOKEN)
