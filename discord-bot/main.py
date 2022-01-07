import asyncio
import discord
from discord.channel import TextChannel
from discord.ext.commands import Bot, has_any_role, MissingAnyRole
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


async def print_send_log(msg, channel=None):
    print_log(msg)
    await channel.send(f"[{strftime('%d/%m/%Y - %H:%M:%S')}] {msg}")


@Client.event
async def on_ready():
    print_log("Bot is ready !")


@Client.command(name="clear_all", help="Reset all the non-admin channels.")
@has_any_role("Hero")
async def clear_all(ctx):
    await print_send_log(f"{ctx.author.name} run clear all ...", channel=ctx.channel)
    for channel in Client.get_all_channels():
        if (
            isinstance(channel, TextChannel)
            and channel.category_id in CATEGORIES.values()
            and channel.id not in CHANNELS.values()
        ):
            await print_send_log(
                f"Clear all : Cloning {channel.name} ...", channel=ctx.channel
            )
            await channel.clone(name=channel.name)
            await print_send_log(
                f"Clear all : Deleting {channel.name} ...", channel=ctx.channel
            )
            await channel.delete()
    await print_send_log("Clear all, done !", channel=ctx.channel)


@clear_all.error
async def clear_all_error(ctx, error):
    if isinstance(error, MissingAnyRole):
        await print_send_log(
            f"Sorry {ctx.author.name}, you do not have permissions to do that!",
            channel=ctx.channel,
        )


if __name__ == "__main__":
    print_log("Bot is starting ...")
    ENV_VARIABLE = {}
    with open(".env", "r") as env_file:
        for line in env_file:
            name, value = line.strip().split("=")
            ENV_VARIABLE[name] = value

    Client.run(ENV_VARIABLE["TOKEN"])
