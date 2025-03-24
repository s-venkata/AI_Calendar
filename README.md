AI Calendar Assistant Bot 🤖

An intelligent Telegram bot that parses natural language messages to automatically create events in your Google Calendar using OpenAI's API.

Features
- Add events like `"Meeting with a friend tomorrow at 3 PM"`  
- Telegram bot interface  
- Google Calendar integration  

Installation

```bash
git clone https://github.com/your-username/ai-calendar-bot.git
cd ai-calendar-bot
pip install -r requirements.txt
```
Setup

1. **Set up environment variables** using a `.env` file:

```
TELEGRAM_BOT_KEY=your_telegram_bot_token
OPENAI_API_KEY=your_openai_api_key
```

2. **Enable Google Calendar API:**
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a project, enable the Calendar API
   - Create OAuth 2.0 credentials
   - Download `credentials.json` and place it in your project folder

3. **First time running?** You'll be prompted to log into your Google account to authorize access.

---

### Run the Bot

```bash
python bot.py
```

---

### ✅ Example Commands

```
/start
Lunch with a friend  next Friday at 2 PM
Hey!
Team sync every Monday at 10 AM
```
