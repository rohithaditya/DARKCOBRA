# plugin made by @hellboi_atul
# gaandu bina credits ka plugin liya toh tu maderchod...tera khandaan maderchod😂😂
# Thanks to @Lucy_robot

from telethon import events
import asyncio
#from userbot.utils import admin_cmd
from userbot.events import register 
from userbot import bot, CMD_HELP
from telethon.errors.rpcerrorlist import YouBlockedUserError
import os
try:
 import subprocess
except:
 os.system("pip install instantmusic")



os.system("rm -rf *.mp3")


def bruh(name):

    os.system("instantmusic -q -s "+name)

@register(outgoing=True, pattern="^.s(?: |$)(.*)")
async def getmusic(s):
    if s.fwd_from:
        return
    song = s.pattern_match.group(1)
    chat = "@Lucy_robot"
    link = f"/song {song}"
    await getmusic.edit("```Getting Your Music```")
    async with bot.conversation(chat) as conv:
          await asyncio.sleep(2)
          await s.edit("`Downloading...Please wait`")
          try:
              msg = await conv.send_message(link)
              response = await conv.get_response()
              respond = await conv.get_response()
              """ - don't spam notif - """
              await bot.send_read_acknowledge(conv.chat_id)
          except YouBlockedUserError:
              await s.edit("```Please unblock @Lucy_robot and try again```")
              return
          await s.edit("`Sending Your Music...weit!😎`")
          await asyncio.sleep(3)
          await bot.send_file(s.chat_id, respond)
    await s.client.delete_messages(conv.chat_id,
                                       [msg.id, response.id, respond.id])
    await s.delete()
