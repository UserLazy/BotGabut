from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.events import register
from userbot import bot, CMD_HELP, ALIVE_NAME


# Ihsan ganteng mks sm sm
# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname()
# ============================================


@register(outgoing=True, pattern="^.bypass ?(.*)")
async def insta(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("`Please reply to kusonime/wibudesu url`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await event.edit("`Sorry, i am need kusonime/wibudesu url`")
        return
    chat = "@SaraProjectBot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("`Processing....`")
        return
    await event.edit("`Processing.....`")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1705735308)
            )
            await event.client.send_message(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.edit("`Please unblock` @SaraProjectBot `and try again`")
            return
        if response.text.startswith("Forward"):
            await event.edit(
                "Uhmm not respon."
            )
        else:
            await event.delete()
            await event.client.send_file(
                event.chat_id,
                response.message.media,
                caption=f"**Bypass By {DEFAULTUSER}**",
            )
            await event.client.send_read_acknowledge(conv.chat_id)
            await bot(functions.messages.DeleteHistoryRequest(peer=chat, max_id=0))
            await event.delete()



CMD_HELP.update({"lk21": "Modules: lk21\n\n**command:** `.bypass`"
                 "\nUsage: bypass kusonime/wibudesu url `.bypass`"})
