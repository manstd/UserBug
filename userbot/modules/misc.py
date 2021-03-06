# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
# You can find misc modules, which dont fit in anything xD
""" Userbot module for other small commands. """

from random import randint
from asyncio import sleep
from os import execl
import sys
import os
import io
import sys
import json
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, bot
from userbot.events import register


@register(outgoing=True, pattern="^.rannnnnnnnnnn")
async def randomise(items):
    """ For .random command, get a random item from the list of items. """
    itemo = (items.text[8:]).split()
    if len(itemo) < 2:
        await items.edit(
            "2 or more items are required! Check .h random for more info."
        )
        return
    index = randint(1, len(itemo) - 1)
    await items.edit("**Query: **\n" + items.text[8:] + "\n**Output: **\n" +
                     itemo[index] + "")


@register(outgoing=True, pattern="^.sleep( [0-9]+)?$")
async def sleepybot(time):
    """ For .sleep command, let the userbot snooze for a few second. """
    message = time.text
    if " " not in time.pattern_match.group(1):
        await time.reply("Syntax: .sleep [seconds]")
    else:
        counter = int(time.pattern_match.group(1))
        await time.edit("I am sulking and snoozing....")
        await sleep(2)
        if BOTLOG:
            await time.client.send_message(
                BOTLOG_CHATID,
                "You put the bot to sleep for " + str(counter) + " seconds",
            )
        await sleep(counter)
        await time.edit("OK, I'm awake now.")


@register(outgoing=True, pattern="^.shutdown$")
async def killdabot(event):
    """ For .shutdown command, shut the bot down."""
    await event.edit("See you soon...")
    if BOTLOG:
        await event.client.send_message(BOTLOG_CHATID, "#SHUTDOWN \n"
                                        "Bot shutdown")
    await bot.disconnect()


@register(outgoing=True, pattern="^.restart$")
async def killdabot(event):
    await event.edit("Restarting My Brain...brb")
    if BOTLOG:
        await event.client.send_message(BOTLOG_CHATID, "#RESTART \n"
                                        "Bot Restarted")
    await bot.disconnect()
    # Spin a new instance of bot
    execl(sys.executable, sys.executable, *sys.argv)
    # Shut the existing one down
    exit()


@register(outgoing=True, pattern="^.com$")
async def bot_community(community):
    """ For .community command, just returns OG Paperplane's group link. """
    await community.edit(
        "Join the [UserBug Community Indonesia](https://t.me/userbotindo).")


@register(outgoing=True, pattern="^.sup$")
async def bot_support(wannahelp):
    """ For .support command, just returns the group link. """
    await wannahelp.edit(
        "Join the [UserBug Community](https://t.me/userbotindo) | [𝐁𝐋𝟒𝐂𝐊_𝐈𝐃](https://t.me/BL4CK_ID)")


@register(outgoing=True, pattern="^.creator$")
async def creator(e):
    await e.edit("Creator by [TeKnoways](https://t.me/Three_Cube_TeKnoways) Edited by [𝐁𝐋𝟒𝐂𝐊_𝐈𝐃](https://t.me/BL4CK_ID)")


@register(outgoing=True, pattern="^.readme$")
async def reedme(e):
    await e.edit(
        "Here's something for you to read:\n"
        "\n[OpenUserBot's README.md file](https://github.com/mkaraniya/OpenUserBot/blob/sql-extended/README.md)"
        "\n[Setup Guide - Basic](https://telegra.ph/How-to-host-a-Telegram-Userbot-11-02)"
        "\n[Setup Guide - Google Drive](https://telegra.ph/How-To-Setup-GDrive-11-02)"
        "\n[Setup Guide - LastFM Module](https://telegra.ph/How-to-set-up-LastFM-module-for-Paperplane-userbot-11-02)"
        "\n[Video Tutorial - 576p](https://mega.nz/#!ErwCESbJ!1ZvYAKdTEfb6y1FnqqiLhHH9vZg4UB2QZNYL9fbQ9vs)"
        "\n[Video Tutorial - 1080p](https://mega.nz/#!x3JVhYwR!u7Uj0nvD8_CyyARrdKrFqlZEBFTnSVEiqts36HBMr-o)"
        "\n[Special - Note](https://telegra.ph/Special-Note-11-02)")

@register(outgoing=True, pattern="^.rp$")
async def repo_is_here(wannasee):
    """ For .repo command, just returns the repo URL. """
    await wannasee.edit(
        "I'm Currently Using [𝐁𝐋𝟒𝐂𝐊_𝐈𝐃](https://github.com/BL4CKID/UserBug) Github's Repository.")


@register(outgoing=True, pattern="^.rawwwwwwwwwwwwww$")
async def raw(event):
    the_real_message = None
    reply_to_id = None
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        the_real_message = previous_message.stringify()
        reply_to_id = event.reply_to_msg_id
    else:
        the_real_message = event.stringify()
        reply_to_id = event.message.id
    with io.BytesIO(str.encode(the_real_message)) as out_file:
        out_file.name = "raw_message_data.txt"
        await event.edit(
            "Check the userbot log for the decoded message data !!")
        await event.client.send_file(
            BOTLOG_CHATID,
            out_file,
            force_document=True,
            allow_cache=False,
            reply_to=reply_to_id,
            caption="Here's the decoded message data !!")

