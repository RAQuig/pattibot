import os
import random
from asyncio import create_task
from aiohttp import web
import discord

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

TARGET_CHANNEL_ID = [
    1448879000863899719,
    1529561211522519191
]
    
PATTI_GIFS = [
    "https://tenor.com/view/hrithik-roshan-fighter-teaser-bollywood-teaser-vande-mataram-sujalam-sufalam-gif-4951463871021573191",
    "https://tenor.com/view/hrithik-roshan-fighter-teaser-bollywood-teaser-deepika-padukone-vande-mataram-gif-6989259302099312995",
    "https://tenor.com/view/hrithik-roshan-fighter-teaser-bollywood-teaser-vande-mataram-sujalam-sufalam-gif-10333642642613646704",
    "https://tenor.com/view/hrithik-roshan-fighter-teaser-bollywood-teaser-deepika-padukone-vande-mataram-gif-3952919288663474187",
    "https://tenor.com/view/bhaag-running-hrithik-roshan-fighter-teaser-bollywood-teaser-gif-14448913600170022205",
    "https://tenor.com/view/hrithik-roshan-fighter-teaser-bollywood-teaser-%E0%A4%8B%E0%A4%A4%E0%A4%BF%E0%A4%95-%E0%A4%B0%E0%A5%8B%E0%A4%B6%E0%A4%A8-hrithik-roshan-movie-gif-11389820009296918697",
    "https://tenor.com/view/hrithik-fire-shamsher-fire-fighter-fire-patty-fire-hrithik-fighter-gif-14649325419096231176"
    
    
    
    
]

@client.event
async def on_ready():
    print(f'Bot active as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.id in TARGET_CHANNEL_ID:
        await message.channel.send("Yeah but have you seen Patti?")
        for gif in PATTI_GIFS:
            chosen_gif = random.choice(PATTI_GIFS)
            await message.channel.send(chosen_gif)

# --- Web Server to make bot stay awake at all times ---
async def handle_ping(request):
    return web.Response(text="Bot is alive!")

async def start_web_server():
    app = web.Application()
    app.router.add_get("/", handle_ping)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.getenv("PORT", 8000))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

@client.event
async def setup_hook():
    #start web server alongside the bot
    client.loop.create_task(start_web_server())

#Fetch token from server
TOKEN = os.getenv("DISCORD_TOKEN")
client.run(TOKEN)
