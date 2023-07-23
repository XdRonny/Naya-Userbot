# Ayra - UserBot
# Copyright (C) 2021-2022 senpai80
#
# This file is a part of < https://github.com/senpai80/Ayra/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/senpai80/Ayra/blob/main/LICENSE/>.


from . import LOG_CHANNEL, Button, asst, ayra_cmd, eor, get_string

REPOMSG = """
◈ **ᴀʏʀᴀ ꭙ ᴜꜱᴇʀʙᴏᴛ​** ◈\n
◈ Repo - [Click Here](https://t.me/ItzStarRonny)
◈ Support - @BotsHub1
"""

RP_BUTTONS = [
    [
        Button.url(get_string("bot_3"), "https://t.me/ItzStarRonny"),
    ],
    [Button.url("Support Group", "t.me/BotsHub1")],
]

AYSTRING = """🥀 **Thanks for Deploying Ronny UserBot**

• Here, are the Some Basic stuff from, where you can Know, about its Usage."""


@ayra_cmd(pattern="repo")
async def useAyra(rs):
    button = Button.inline("Start >>", "initft_2")
    msg = await asst.send_message(
        rs.chat_id,
        AYSTRING,
        file="https://te.legra.ph/file/795da224f0d4d6ab717e3.jpg",
        buttons=button,
    )
    if not (rs.chat_id == LOG_CHANNEL and rs.client._bot):
        await eor(rs, f"**[Click Here]({msg.message_link})**")
