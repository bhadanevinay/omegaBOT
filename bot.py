import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from telegram.ext import Application, CommandHandler, CallbackContext

# Load environment variables
load_dotenv()

# Get Bot Token from .env file
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Default Mini App URL
MAIN_WEB_APP_URL = "https://omegaofts.blogspot.com/"

async def start(update: Update, context: CallbackContext):
    """Handle the /start command and generate a dynamic blog post link if provided"""

    # Get the start parameter (if any)
    args = context.args
    if args:
        # Convert Telegram-safe format (underscores) back to original format (slashes)
        post_slug = args[0].replace("_", "/")  # Convert back to the original format

        # Construct the blog post URL dynamically
        post_url = f"https://omegaofts.blogspot.com/{post_slug}.html"
    else:
        post_url = MAIN_WEB_APP_URL  # Default to Mini App homepage

    # Create the button to open the Mini App with the correct link
    keyboard = [[InlineKeyboardButton("🚀 Open Mini App", web_app=WebAppInfo(url=post_url))]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send the message with the button
    await update.message.reply_text(
        "🔗 Click below to open your requested post in the Mini App:",
        reply_markup=reply_markup
    )

def main():
    """Start the bot"""
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
