import pandas as pd
from datetime import datetime
from twilio.rest import Client
from apscheduler.schedulers.blocking import BlockingScheduler

# Twilio API Credentials
ACCOUNT_SID = "your_twilio_sid"
AUTH_TOKEN = "your_twilio_auth_token"
TWILIO_NUMBER = "your_twilio_whatsapp_number"  # Example: 'whatsapp:+14155238886'

# Load birthday data (CSV file format: Name,Phone,Birthday)
df = pd.read_csv("birthdays.csv")

# Initialize Twilio client
client = Client(ACCOUNT_SID, AUTH_TOKEN)

def send_birthday_wish(name, phone):
    message = f"🎉 Happy Birthday {name}! 🎂🎈 Wishing you a fantastic year ahead! 🎊"
    client.messages.create(
        from_=TWILIO_NUMBER,
        body=message,
        to=f"whatsapp:{phone}"
    )
    print(f"Birthday wish sent to {name} at {phone}")

def check_and_send_wishes():
    today = datetime.now().strftime("%m-%d")  # Get today's date (MM-DD format)
    for _, row in df.iterrows():
        if row["Birthday"] == today:
            send_birthday_wish(row["Name"], row["Phone"])

# Schedule to run daily at 9 AM
scheduler = BlockingScheduler()
scheduler.add_job(check_and_send_wishes, "cron", hour=9, minute=0)
scheduler.start()
