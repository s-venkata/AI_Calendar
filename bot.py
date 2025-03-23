import os
import datetime
import json

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

from cal_login import get_calendar

#OpenAI
import openai

#load keys from .env files
load_dotenv()

#keys
telegram_bot_token = os.getenv("TELEGRAM_BOT_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")
