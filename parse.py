import openai
import json
import os

openai_api_key = os.getenv("OPENAI_API_KEY")

def parse(message):
    prompt = f""" Extract calendar event information from this message: "{message}" 
    
    Return result in this  JSON format:
    {{
      "title": "Event Title",
      "start_time": "YYYY-MM-DDTHH:MM:SS",
      "end_time": "YYYY-MM-DDTHH:MM:SS"
    }}

    If date/time is missing, ask the user,
    if not provided, assume it's 1 hour from now.
    
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages = [
            {
                "role": "user",
                "content":prompt
            }
     ]
    )
    reply = response.choices[0].message.content

    return json.loads(reply)



