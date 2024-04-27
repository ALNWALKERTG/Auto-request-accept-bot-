from os import environ
import os
import asyncio
from pyrogram import Client, filters, enums
from pyrogram.errors import PeerIdInvalid
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, User, ChatJoinRequest

API_ID = int(os.environ.get('API_ID', ''))
API_HASH = os.environ.get('API_HASH', '')
BOT_TOKEN = os.environ.get('BOT_TOKEN', '')

user=Client(
    "Auto Approved Bot",
    api_id = API_ID,
    api_hash = API_HASH,
    bot_token = BOT_TOKEN
)

@Client.on_message(filters.command("start"))
async def start(client, message: Message):
    mine = await client.get_me()
    button = [[ InlineKeyboardButton("🔸 ɢʀᴏᴜᴩ 1 🔸", url="https://t.me/+q9PpzTvYD882OTU1"),
                InlineKeyboardButton("🔸 ɢʀᴩᴜᴩ 2 🔸", url="https://t.me/+q9PpzTvYD882OTU1")
                ],[
                InlineKeyboardButton("🔸 ᴄʜᴀɴɴᴇʟ 1 🔸" , url="https://t.me/+1AtPM7FXm_pjNDA9") ,
                InlineKeyboardButton("🔸 ᴄʜᴀɴɴᴇʟ 2 🔸" , url="https://t.me/+v5I41M1IIH5iYzll")
                ] , [
                InlineKeyboardButton("🔸 ᴍᴏᴠɪᴇ ʀᴇqᴜᴇꜱᴛɪɴɢ ʙᴏᴛ 🔸", url="https://t.me/Movie_Requesting_Robot")
            ]]
    await client.send_message(chat_id=message.chat.id, text=f"__Hello {message.from_user.mention} Iam Auto Approver Join Request Bot Just [Add Me To Your Group or Channnl](http://t.me/{mine.username}?startgroup=botstart)__", reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview=True)

@Client.on_chat_join_request()
async def autoapprove(client, message: ChatJoinRequest):
  try:
    chat=message.chat
    user=message.from_user
    print(f"{user.first_name} Joined 🤝")
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    print(user.id)
    photo_path = "https://telegra.ph/file/4ee563b2e8a1efc87e582.jpg"
    caption = f"Hello {user.mention} ✨\n\nYour Request to Join {chat.title} has been Approved.\n\nSend /start to know more.\nJoin US 👇👇"
    buttons = [
        [InlineKeyboardButton("requesting group", url="https://t.me/+N-d6LxO8-VozOTc9")],
        [InlineKeyboardButton("latest movies", url="https://t.me/+ASrQmyP1AGIwOTU9")]
    ]
    user_m = user.id
    x=await client.send_photo(
        chat_id=user_m,
        photo=photo_path,
        caption=caption,
        reply_markup=InlineKeyboardMarkup(buttons)
    )
    await asyncio.sleep(300)
    await x.delete()
  except PeerIdInvalid:
      pass

print("Auto Approved Bot")
user.run()
