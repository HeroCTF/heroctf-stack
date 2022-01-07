import asyncio
import discord
from discord.channel import TextChannel
from discord.ext.commands import Bot
from time import strftime

Client = Bot(">")

CHANNELS = {"welcome": 616347322271531021, "twitter": 810791819318919198}

CATEGORIES = {
    "information": 616346582488580120,
    "general": 613165484548030494,
    "challenge": 637656141249118212,
    "writeups": 810797492550762516,
}


def print_log(msg):
    print(f"[{strftime('%d/%m/%Y - %H:%M:%S')}] {msg}")


@Client.event
async def on_ready():
    print_log("Bot is ready !")


@Client.command(name="clear_all", help="Reset all the non-admin channels.")
async def clear_non_admin_channels(ctx):
    print_log("Clear all ...")
    for channel in Client.get_all_channels():
        if (
            isinstance(channel, TextChannel)
            and channel.category_id in CATEGORIES.values()
            and channel.id not in CHANNELS.values()
        ):
            print_log(f"Clear all : Cloning {channel.name} ...")
            await channel.clone(name=channel.name)
            print_log(f"Clear all : Deleting {channel.name} ...")
            await channel.delete()
    print_log("Clear all, done !")


if __name__ == "__main__":
    print_log("Bot is starting ...")
    ENV_VARIABLE = {}
    with open(".env", "r") as env_file:
        for line in env_file:
            name, value = line.strip().split("=")
            ENV_VARIABLE[name] = value

    Client.run(ENV_VARIABLE["TOKEN"])
