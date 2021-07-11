# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

import asyncio

from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import CMD_HELP, bot
from userbot.events import register


@register(outgoing=True, pattern=r"^\.gen(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    query = event.pattern_match.group(1)
    if not query:
        return await event.edit("**Silahkan masukan bin yang mau di generate!**")
    await event.edit(f"```Generated CC {query}..```")
    async with bot.conversation("@Carol5_bot") as conv:
        try:
            send = await conv.send_message(f"!gen {query}")
            await asyncio.sleep(8)
            get = await conv.get_response()
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await event.reply("Unblock @Carol5_bot or chat them")
        if get.text.startswith("Wait for result..."):
            return await event.edit(f"Failed generate {query}!")
        await event.edit(get.message)
        await event.client.delete_messages(conv.chat_id, [send.id, get.id])


@register(outgoing=True, pattern=r"^\.chk(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    query = event.pattern_match.group(1)
    if not query:
        return await event.edit("**Silahkan masukan cc yang mau di check!**")
    await event.edit("```Checking CC Number..```")
    async with bot.conversation("@Carol5_bot") as conv:
        try:
            send = await conv.send_message(f"!ss {query}")
            await asyncio.sleep(20)
            get = await conv.get_response()
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await event.reply("Unblock @Carol5_bot or chat them")
        if get.text.startswith("Wait for result..."):
            return await event.edit(f"Failed Check {query}!")
        await event.edit(get.message)
        await event.client.delete_messages(conv.chat_id, [send.id, get.id])


@register(outgoing=True, pattern=r"^\.bin(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    query = event.pattern_match.group(1)
    if not query:
        return await event.edit("**Silahkan masukan BIN yang mau di check!**")
    await event.edit(f"```Checking BIN {query}```")
    async with bot.conversation("@Carol5_bot") as conv:
        try:
            send = await conv.send_message(f"!bin {query}")
            await asyncio.sleep(10)
            get = await conv.get_response()
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await event.reply("Unblock @Carol5_bot or chat them")
        if get.text.startswith("Wait for result..."):
            return await event.edit(f"Bin {query} Invalid!")
        await event.edit(get.message)
        await event.client.delete_messages(conv.chat_id, [send.id, get.id])


@register(outgoing=True, pattern=r"^\.skey(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    query = event.pattern_match.group(1)
    if not query:
        return await event.edit("**Silahkan masukan SK-KEY yang mau di check!**")
    await event.edit(f"```Checking SK KEY {query}```")
    async with bot.conversation("@Carol5_bot") as conv:
        try:
            send = await conv.send_message(f"!bin {query}")
            await asyncio.sleep(10)
            get = await conv.get_response()
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await event.reply("Unblock @Carol5_bot or chat them")
        if get.text.startswith("Wait for result..."):
            return await event.edit("SK KEY Invalid!")
        await event.edit(get.message)
        await event.client.delete_messages(conv.chat_id, [send.id, get.id])


@register(outgoing=True, pattern=r"^\.alc(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    query = event.pattern_match.group(1)
    if not query:
        return await event.edit(
            "**Silahkan masukan cc yang mau di cek Alive apa Dead**"
        )
    await event.edit("```Checking CC Number..```")
    async with bot.conversation("@Carol5_bot") as conv:
        try:
            send = await conv.send_message(f"!ch {query}")
            await asyncio.sleep(20)
            get = await conv.get_response()
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await event.reply("Unblock @Carol5_bot or chat them")
        if get.text.startswith("Wait for result..."):
            return await event.edit(f"Failed Check {query}!")
        await event.edit(get.message)
        await event.client.delete_messages(conv.chat_id, [send.id, get.id])


CMD_HELP.update(
    {
        "anu": ">`.gen` **<bin>**"
        "\nUsage: to generate cc with bin.."
        "\n\n> `.chk` **<cc>**"
        "\nUsage: to check respond cc."
        "\n\n> `.bin` **<bin number>**"
        "\nUsage: to check your bin information."
        "\n\n> `.skey` **<SK-Key Number>**"
        "\nUsage: to check your bin information."
        "\n\n> `.alc` **<CC|D|Y|Number>**"
        "\nUsage: to check Your bin is dead or Alive."
    }
)
