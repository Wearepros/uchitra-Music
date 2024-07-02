import random
import time
import requests
from Fsecmusic import app
from config import BOT_USERNAME

from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters

@app.on_message(filters.command(["chatgpt", "alcon"],  prefixes=[".", "/", "F", "f"]))
async def chat_gpt(bot, message):
    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            await message.reply_text(
                "**Hello Sir, Welcome to Falcon Help. How can I help you today?**"
            )
        else:
            a = message.text.split(' ', 1)[1]
            response = requests.get(f'https://chatgpt.apinepdev.workers.dev/?question={a}')

            try:
                response_json = response.json()
                if "answer" in response_json:
                    x = response_json["answer"]
                    end_time = time.time()
                    telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ms"
                    await message.reply_text(
                        f"{x}",
                        parse_mode=ParseMode.MARKDOWN
                    )
                else:
                    await message.reply_text("No 'answer' key found in the response.")
            except (KeyError, ValueError) as e:
                await message.reply_text(f"Error processing the response: {e}")
    except Exception as e:
        await message.reply_text(f"**Error: {e}**")
