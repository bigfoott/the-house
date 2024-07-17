import os
import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    try:
        await bot.tree.sync()
    except Exception as e:
        print(e)
    print(f'Bot is ready. Logged in as {bot.user}')


@bot.tree.command(name="add_league_of_legends_account", description="Add a League of Legends account")
@app_commands.describe(username="The League of Legends username to add")
async def add_league_of_legends_account(interaction: discord.Interaction, username: str):
    await interaction.response.send_message(f'Account name "{username}" has been set.')


if __name__ == '__main__':
    bot.run(TOKEN)
