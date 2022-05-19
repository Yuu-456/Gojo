import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from horisan.events import register
from horisan import telethn as tbot


PHOTO = "https://telegra.ph/file/37fbf569f9b0bf5fdd809.jpg"


@register(pattern=("/kaisen"))
async def awake(event):
    TEXT = f"**Welcome to [ Aηιмє Kαιѕєη ☆ᴀᴄɢ☆](https://t.me/Anime_Kaisen_ACG)** \n\n"
    TEXT += "**◈ Aηιмє Kαιѕєη is an anime based Community with a motive to spread Knowledge nd Awareness for all OF it's Members . Join the Group if it draws your attention. ◈"
    BUTTON = [
        [
            
            Button.url("【Owner Sama】", "https://t.me/zenin_hodaka"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=TEXT, buttons=BUTTON)

__help__ = """
 ──| Aηιмє Kαιѕєη ☆ᴀᴄɢ☆ |──                         
 
❂ /kaisen: Get information about the Owner's Group ! using it in groups may create promotion so we don't support using it in groups."""
   
__mod_name__ = "Aηιмє Kαιѕєη"
