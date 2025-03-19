# Discord Meme Bot

This project is a Discord bot built with Python that responds to the `$meme` command by fetching and sending a random meme from Reddit using the Meme API.

## Features

- Responds to the `$meme` command with a random meme image.
- Uses the `discord.py` library to interact with the Discord API.
- Fetches memes from the Meme API.

## Prerequisites

- Python 3.10 or later
- A Discord account
- A Discord server where you have permission to add bots

## Installation

1. **Clone the repository**:
   git clone <your-github-repo-url>
   cd discord-meme-bot

2. Set up a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the required packages:
pip install discord.py requests python-dotenv

4. Create a .env file in the project directory and add your Discord bot token:
DISCORD_TOKEN=your-discord-bot-token

5. Usage
Run the bot: python bot.py

6. Interact with the bot:
In your Discord server, type $meme in a channel where the bot is present.
The bot will respond with a random meme image.

Bot Setup
1. Create a Discord Application:
Go to the Discord Developer Portal and create a new application.
Add a bot to your application and copy the token.

2. Invite the Bot to Your Server:
Generate an OAuth2 URL with the bot scope and necessary permissions.
Use the URL to invite the bot to your server.

3. Enable Privileged Intents:
In the Discord Developer Portal, enable the "Message Content Intent" for your bot.

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Discord.py for providing the library to interact with Discord.
Meme API for providing random memes from Reddit.