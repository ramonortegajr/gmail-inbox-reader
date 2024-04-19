#********************************************************************************************#
#Author: Ram Ortega																			 #
#Description: This script uses the Gmail API to mark all unread emails in the inbox as read. #
#********************************************************************************************#
import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# Define the scopes for accessing Gmail
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def authenticate():
    """
    Authenticates the user and returns the Gmail service object.
    """
    creds = None
   
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json')
   
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
      
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

   
    service = build('gmail', 'v1', credentials=creds)
    return service

def mark_as_read(service):
    """
    Marks all unread emails in the inbox as read.
    """
    try:
      
        has_more_unread = True
        
        while has_more_unread:
           
            unread_msgs = service.users().messages().list(userId='me', q='is:unread').execute()
            if 'messages' in unread_msgs:
                msg_ids = [msg['id'] for msg in unread_msgs['messages']]
              
                for msg_id in msg_ids:
                    service.users().messages().modify(userId='me', id=msg_id, body={'removeLabelIds': ['UNREAD']}).execute()
                print(f"{len(unread_msgs['messages'])} unread emails have been marked as read.")
            else:
                print("No more unread emails found in the inbox.")
                has_more_unread = False
    
    except Exception as e:
        print("An error occurred:", e)

def main():
    service = authenticate()
    mark_as_read(service)

if __name__ == '__main__':
    main()
