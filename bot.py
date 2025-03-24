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

#to handle /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hey, I am your AI calendar Assitant. \n How can i help you ?")

#to handle chat messeges 
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    

    await update.message.reply_text(" Let me check that...")

    try:
        event_data = parse(user_input)
    
    except Exception as e:
        await update.message.reply_text("Something went wrong while understanding your message.")
        return

    if not event_data:
        await update.message.reply_text(" I couldn’t understand your event. Try again?")
        return

    try:
        service = get_calendar()
        event = {
            'summary': event_data['title'],
            'start': {
                'dateTime': event_data['start_time'],
                'timeZone': 'Europe/Berlin',
            },
            'end': {
                'dateTime': event_data['end_time'],
                'timeZone': 'Europe/Berlin',
            },
        }

        

        service.events().insert(calendarId='primary', body=event).execute()
        await update.message.reply_text(f" Event '{event_data['title']}' added to your calendar!")
    except Exception as e:
        await update.message.reply_text(" Failed to create event. Check the logs.")

   
    

def main ():
            app = ApplicationBuilder().token(telegram_bot_token).build()

            app.add_handler(CommandHandler("start",start))
            app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,handle_message))

            
            app.run_polling()

if __name__ == '__main__':
            main()


