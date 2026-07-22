🤖 PattiBot

A lightweight, automated Discord bot built with discord.py that listens for messages in designated channels and responds with random Patti GIFs—complete with slash command controls and a web health check server for 24/7 cloud hosting.
✨ Features

    Channel-Specific Triggers: Listens to targeted Discord channels and drops a quote + a random Patti GIF.

    Randomized Responses: Uses Python's random module to select a different GIF from your library on each trigger.

    Slash Commands (/):

        /pattikill [password] – Fake kill-code command with password validation.

        /restartpatti – Simulated reboot command.

    Built-in Web Server: Integrated aiohttp web server to handle HTTP pings (keeps the bot alive 24/7 on free hosting platforms like Render).

🛠️ Project Structure
Plaintext

.
├── main.py              # Main bot logic, slash commands, and web server
├── requirements.txt     # Python dependencies
├── PRIVACY_POLICY.md    # Privacy Policy template (optional)
├── TERMS_OF_SERVICE.md # Terms of Service template (optional)
└── README.md            # Project documentation

📋 Prerequisites

    Python 3.10+ installed on your machine.

    A Discord Developer Account with a created Bot Application.

    A free Render account (or any hosting provider) for continuous operation.

🚀 Setup & Local Installation
1. Clone the Repository
Bash

git clone https://github.com/your-username/pattibot.git
cd pattibot

2. Install Dependencies

Make sure you have your dependencies listed in requirements.txt:
Plaintext

discord.py
aiohttp

Install them using pip:
Bash

pip install -r requirements.txt

3. Environment Variables

Set up your Discord Bot token as an environment variable:

    Linux/macOS:
    Bash

export DISCORD_TOKEN="your-discord-bot-token-here"

Windows (Command Prompt):
DOS

set DISCORD_TOKEN=your-discord-bot-token-here

Windows (PowerShell):
PowerShell

    $env:DISCORD_TOKEN="your-discord-bot-token-here"

4. Configure Bot IDs

In main.py, replace the placeholder IDs with your actual Discord IDs:
Python

GUILD_ID = 123456789012345678  # Your Discord Server ID
TARGET_CHANNEL_IDS = [
    123456789012345678,        # Channel 1 ID
    987654321098765432         # Channel 2 ID
]

5. Run the Bot Locally
Bash

python main.py

🌐 Deploying to Render

    Push your code to a GitHub repository.

    Go to Render and create a new Web Service.

    Connect your GitHub repository.

    Set the following build options:

        Environment: Python 3

        Build Command: pip install -r requirements.txt

        Start Command: python main.py

    Under Environment Variables, add:

        Key: DISCORD_TOKEN

        Value: (Your actual Discord bot token)

    Deploy the Web Service!

    Keep-Alive Tip: To prevent Render's free tier from sleeping after 15 minutes, set up a free HTTP ping on UptimeRobot or Cron-Job.org pointing to your Render Web Service URL (e.g., [https://your-bot-name.onrender.com](https://your-bot-name.onrender.com)).

🤖 Discord Bot Permissions

When generating your invite link in the Discord Developer Portal (OAuth2 → URL Generator):

    Select Scopes:

        bot

        applications.commands

    Select Bot Permissions:

        Send Messages

        Embed Links

        Read Message History / View Channels

📄 License & Legal

This project is open-source. For bot verification on Discord, see PRIVACY_POLICY.md and TERMS_OF_SERVICE.md for hosted policy templates.
