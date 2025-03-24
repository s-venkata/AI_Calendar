import os


from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

from cal_login import get_calendar
from parse import parse


#load keys from .env files
load_dotenv()

#keys
telegram_bot_token = os.getenv("TELEGRAM_BOT_KEY")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hey, I am your AI calendar Assitant. \n How can i help you ?")
    