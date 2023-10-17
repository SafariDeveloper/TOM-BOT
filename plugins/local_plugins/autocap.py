import logging, asyncio, pyrogram, os
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
from os import environ
from pyrogram import filters, Client
from info import CAPTION_POSITION # BOT_TOKEN, API_ID, API_HASH, CAPTION_TEXT, CAPTION_POSITION
logging.getLogger("pyrogram").setLevel(logging.WARNING)
usercaption_position = CAPTION_POSITION
caption_position = usercaption_position.lower()
CAPTION_TEXT = os.environ.get("CAPTION_TEXT", "`{file_name}`")
CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "bottom")
     
@Client.on_message(filters.command("cstart") & filters.incoming)
async def start(bot, message):
        await message.reply("<I>I Am Auto Caption Bot Just Add me as a Admin in your channel with edit permission and See Magic</I>\n\n• **support** : @Hollywood_0980\n• **Source** : https://github.com/0AIB/TG-Caption-Bot")

@Client.on_message(filters.channel & (filters.document | filters.video | filters.audio ) & ~filters.edited, group=-1)
async def editing(bot, message):
      try:
         media = message.document or message.video or message.audio
         caption_text = CAPTION_TEXT
      except:
         caption_text = ""
         pass 
      if (message.document or message.video or message.audio): 
          if message.caption:                        
             file_caption = f"**{message.caption}**"                
          else:
             fname = media.file_name
             filename = fname.replace("_", ".")
             file_caption = f"`{filename}`"  
              
      try:
          if caption_position == "top":
             await bot.edit_message_caption(
                 chat_id = message.chat.id, 
                 message_id = message.message_id,
                 caption = caption_text + "\n" + file_caption,
                 parse_mode = "markdown"
             )
          elif caption_position == "bottom":
             await bot.edit_message_caption(
                 chat_id = message.chat.id, 
                 message_id = message.message_id,
                 caption = file_caption + "\n\n" + caption_text,
                 parse_mode = "markdown"
             )
          elif caption_position == "nil":
             await bot.edit_message_caption(
                 chat_id = message.chat.id,
                 message_id = message.message_id,
                 caption = caption_text, 
                 parse_mode = "markdown"
             ) 
      except:
          pass
