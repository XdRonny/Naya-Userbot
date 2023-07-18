# Ayra - UserBot
# Copyright (C) 2021-2022 senpai80
#
# This file is a part of < https://github.com/senpai80/Ayra/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/senpai80/Ayra/blob/main/LICENSE/>.
"""
✘ **Help For DMs**

๏ **Order:** `dm` <give message/reply message> <username/id> <reply/type>`
◉ **Information:** Send private messages to users.

๏ **Order:** `send` <reply to message`
◉ **Information:** Forward the message to the user.
"""

from . import ayra_cmd


@ayra_cmd(pattern="[dD][mM]( (.*)|$)", fullsudo=True)
async def dm(e):
    if len(e.text.split()) <= 1:
        return await e.eor(
            "`Provide username or Chat id where to send.`", time=5
        )
    chat = e.text.split()[1]
    try:
        chat_id = await e.client.parse_id(chat)
    except Exception as ex:
        return await e.eor(f"`{ex}`", time=5)
    if len(e.text.split()) > 2:
        msg = e.text.split(maxsplit=2)[2]
    elif e.reply_to:
        msg = await e.get_reply_message()
    else:
        return await e.eor("`Send a message or reply to a message.`", time=5)
    try:
        _ = await e.client.send_message(chat_id, msg)
        n_, time = "**Message Sent Successfully**", None
        if not _.is_private:
            n_ = f"[{n_}]({_.message_link})"
        await e.eor(n_, time=time)
    except Exception:
        await e.eor("Please type `help dm` for assistance.", time=5)


@ayra_cmd(pattern="send( (.*)|$)", fullsudo=False)
async def _(e):
    message = e.pattern_match.group(1).strip()
    if not e.reply_to_msg_id:
        return await e.eor("`Please reply to message...`", time=5)
    if not message:
        return await e.eor("`There are no messages to send...`", time=5)
    msg = await e.get_reply_message()
    fwd = await msg.forward_to(msg.sender_id)
    await fwd.reply(message)
    await e.eor("**Successfully Sent.**", time=5)
