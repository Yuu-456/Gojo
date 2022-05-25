import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Gojo.events import register
from Gojo import telethn as tbot


PHOTO = "https://telegra.ph/file/37fbf569f9b0bf5fdd809.jpg"


@register(pattern=("/kaisen"))
async def awake(event):
    TEXT = f"**Welcome to 𓊈𒆜 ꧁༺WɛɛɮAʀƈǟɖɛ༻꧂ 𒆜𓊉(https://t.me/WeebArcadeNetwork)** \n\n"
    TEXT += "**◈꧁༺WɛɛɮAʀƈǟɖɛ༻꧂is an anime based Community with a motive to spread Knowledge and Awareness for all OF it's Members . Join the Group if it draws your attention.◈"
    BUTTON = [
        [
            
            Button.url("【Owner Sama】", "https://t.me/zenin_hodaka"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=TEXT, buttons=BUTTON)

__help__ = """
 ──| ꧁༺WɛɛɮAʀƈǟɖɛ༻꧂ |──                         
 
❂ /arcade: Get information about the Arcade Netowrk ! using it in groups may create promotion so we don't support using it in groups."""
   
__mod_name__ = "꧁༺WɛɛɮAʀƈǟɖɛ༻꧂"
