from openai import OpenAI
import json
import os
from dotenv import load_dotenv

#load keys from .env files
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))



def parse(message):
    prompt = f""" 
                  You are an AI assistant who helps users by either:
                        1. Extracting calendar events from natural language and replying ONLY with JSON like this:
                        {{
                        "title": "Event Title",
                        "start_time": "YYYY-MM-DDTHH:MM:SS",
                        "end_time": "YYYY-MM-DDTHH:MM:SS"
                        }}
                        2. If the message is a greeting, small talk, or doesn't contain an event, respond like a human assistant (text reply). No JSON needed in that case.
                        Rules:
                        - If it's an event, return ONLY the JSON (no text).
                        - If it's not an event, respond conversationally (e.g., "Hello! How can I help you today?").
                        - If you're unsure, ask for clarification.

                        User message: "{message}"
    
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages = [
            {
                "role": "user",
                "content":prompt
            }
     ]
    )
    reply = response.choices[0].message.content
    

    try:
       return json.loads(reply)
    except json.JSONDecodeError as e:
       print(" JSON decode error:", e)
       return None




