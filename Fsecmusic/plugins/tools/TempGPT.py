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
            question = message.text.split(' ', 1)[1]
            url = f'https://chatgpt.apinepdev.workers.dev/?question={question}'
            try:
                response = requests.get(url)
                response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
                
                try:
                    response_json = response.json()
                    if "answer" in response_json:
                        answer = response_json["answer"]
                        end_time = time.time()
                        telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ms"
                        await message.reply_text(
                            f"{answer}",
                            parse_mode=ParseMode.MARKDOWN
                        )
                    else:
                        await message.reply_text("No 'answer' key found in the response.")
                except (KeyError, ValueError) as e:
                    await message.reply_text(f"Error processing the response: {e}")
            except requests.exceptions.RequestException as e:
                await message.reply_text(f"HTTP request error: {e}")
                print(f"HTTP request error: {e}")
    except Exception as e:
        await message.reply_text(f"**Error: {e}**")
        print(f"General error: {e}")
                        
