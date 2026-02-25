import asyncio
import os

from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters


START_MESSAGE = (
    "✅ You have successfully found the *first flag*.\n\n"
    "Keep going — you’re closer than you think. Push towards the end!"
)

AUDIO_CLUE_CAPTION = "Here’s your *second clue*."

# Telegram file_id for the audio clue (captured via capture_audio_file_id).
SECOND_CLUE_AUDIO_FILE_ID = "BQACAgUAAxkBAANGaZ3k-OSxTjhqSLs_eEtyoDBOsZUAAqoaAAIOhvFUgvRicE6a5DQ6BA"

COMPLIMENT_MESSAGE = "🎉 Great job — keep going, you’re almost there!"

FINAL_CLUE_IMAGE_URL = "https://i.postimg.cc/L4WY27HP/flag.png"

FINAL_CLUE_MESSAGE = "Here’s your last clue: ID: @dinosaur.5942756"



WRONG_MESSAGE = "❌ Wrong message, try again."


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.message:
        return

    await update.message.reply_text(START_MESSAGE, parse_mode=ParseMode.MARKDOWN)

    # Send the second clue as an audio message using the stored file_id.
    await update.message.reply_audio(
        audio=SECOND_CLUE_AUDIO_FILE_ID,
        caption=AUDIO_CLUE_CAPTION,
        parse_mode=ParseMode.MARKDOWN,
    )


async def on_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.message or update.message.text is None:
        return

    text = update.message.text.strip().lower()
    if text == "nebuchadnezzar":
        # Compliment message
        await update.message.reply_text(COMPLIMENT_MESSAGE, parse_mode=ParseMode.MARKDOWN)

        # Image only (no caption)
        await update.message.reply_photo(photo=FINAL_CLUE_IMAGE_URL)

        # Final clue message (ID mentioned only once here)
        await update.message.reply_text(FINAL_CLUE_MESSAGE, parse_mode=ParseMode.MARKDOWN)
    else:
        await update.message.reply_text(WRONG_MESSAGE)


async def on_other(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Stickers, photos, voice notes, etc.
    if update.message:
        await update.message.reply_text(WRONG_MESSAGE)


def main() -> None:
    # WARNING: Hard-coding the token is not safe for production.
    # Do this only for quick local testing and NEVER commit this file to any public repo.
    token = "8745699534:AAHXbxeoLODJ6mB-iHtqaPZKjHZg0_IMUBM"

    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, on_text))
    app.add_handler(MessageHandler(~filters.TEXT & ~filters.COMMAND, on_other))

    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
