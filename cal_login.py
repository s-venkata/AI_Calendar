import os

#Google API imports
from google.oauth2.credentials import Credentials 
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build 
from google.auth.transport.requests import Request

#user_creds=Credentials.from_authorized_user_file("token.json",SCOPES)
SCOPES = ['https://www.googleapis.com/auth/calendar']

#user login 
#token exist use it 
#no token exist , it redirects to login page 
def get_calendar():
    user_creds = None

    if not user_creds or not user_creds.valid:
        if user_creds and user_creds.expired and user_creds.refresh_token:
            user_creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            user_creds = flow.run_local_server(port=0)

        # Save the new token only if creds is valid
        if user_creds:
            with open("token.json", "w") as token_file:
                token_file.write(user_creds.to_json())

    service = build("calendar", "v3", credentials=user_creds)
    return service
