from pyrogram import Client
import asyncio
from Music.config import SUDO_USERS, PMPERMIT, OWNER_ID, SUPPORT_GROUP
from pyrogram import filters
from pyrogram.types import Message
from Music.MusicUtilities.tgcallsrun.callsmusic import client as USER

PMSET =True
pchats = []

@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
    if PMPERMIT == "ENABLE":
        if PMSET:
            chat_id = message.chat.id
            if chat_id in pchats:
                return
            await USER.send_message(
                message.chat.id,
            f"Hi,Saya adalah **Layanan Asistant [Vieena Robot]{t.me/vieenarobot}.**\n\n ❗️ **Rules:**\n   - Jangan Spam Pesan disini\n   - Jangan Spam Lagu Biar Ga Error\n   - Cara Menggunakan Bot Hanya Memasukan bot ke dalam grup dan jadikan admin \n\n 👉 **KIRIM LINK INVITE ATAU USERNAME GRUP, JIKA ASSISTANT TIDAK DAPAT BERGABUNG DENGAN GRUP ANDA.**\n\n **Group Support :** @vieenasuport - **Owner** @zxcskyy\n\n",
            )
            return

    

@Client.on_message(filters.command(["/pmpermit"]))
async def bye(client: Client, message: Message):
    if message.from_user.id in SUDO_USERS:
        global PMSET
        text = message.text.split(" ", 1)
        queryy = text[1]
        if queryy == "on":
            PMSET = True
            await message.reply_text("Pmpermit turned on")
            return
        if queryy == "off":
            PMSET = None
            await message.reply_text("Pmpermit turned off")
            return

@USER.on_message(filters.text & filters.private & filters.me)        
async def autopmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("Approoved to PM due to outgoing messages")
        return
    message.continue_propagation()    
    
@USER.on_message(filters.command("yes", [".", ""]) & filters.me & filters.private)
async def pmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("Approoved to PM")
        return
    message.continue_propagation()    
    

@USER.on_message(filters.command("no", [".", ""]) & filters.me & filters.private)
async def rmpmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if chat_id in pchats:
        pchats.remove(chat_id)
        await message.reply_text("Dispprooved to PM")
        return
    message.continue_propagation()    
