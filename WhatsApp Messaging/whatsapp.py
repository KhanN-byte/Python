import requests
import time

# Your Twilio Account SID and Auth Token
account_sid = 'AC4ac5b09b4664cc6376f21e0c77a7bcea'
auth_token = 'e36d539c7cf59057e8edb8a6e7015b31'

# Twilio phone number
from_number = 'whatsapp:+14155238886'
to_number = 'whatsapp:+xxx-xxx-xxxx' # your recipient's phone number

# Function to send a WhatsApp message
def send_whatsapp_message(body):
    url = f'https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages.json'
    payload = {
        'From': from_number,
        'To': to_number,
        'Body': body,
    }
    response = requests.post(url, data=payload, auth=(account_sid, auth_token))
    return response.json()

# Function to fetch incoming WhatsApp messages
def fetch_incoming_messages():
    url = f'https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages.json'
    response = requests.get(url, auth=(account_sid, auth_token))
    messages = response.json().get('messages', [])
    return messages

# Function to store incoming WhatsApp messages
def store_messages():
    callFetchMsgs = fetch_incoming_messages()
    getMsg = []  # Initialize an empty list to store messages
    for msg in callFetchMsgs:
        if msg.get("from") == 'whatsapp:+1xxx-xxx-xxxx':
            getMsg.append(msg.get('body'))
    return getMsg

# Example usage to send a message
msg_ = input("Enter the message to send: ")
send_whatsapp_message(msg_)

# Continuous loop to fetch and display incoming messages
while True:
    time.sleep(5)  # Adjust the delay time as needed
    msgs_ = store_messages()
    if msgs_:
        print("Recipient's Reply:")
        print(msgs_)
        break  # Break out of the loop once a reply is received
