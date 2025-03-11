# 🎉 WhatsApp Birthday Reminder Bot  
A Python-based WhatsApp bot that automatically sends birthday wishes to contacts on their special day using the Twilio API.  

---

## **📌 Features**  
✅ Automatically sends birthday wishes to contacts via WhatsApp  
✅ Reads birthday data from a CSV file  
✅ Runs daily at a scheduled time using APScheduler  
✅ Uses Twilio API for sending WhatsApp messages  
✅ Lightweight and easy to deploy on any server  

---

## **🛠️ Tech Stack**  
- **Python** (for scripting and automation)  
- **Twilio API** (for sending WhatsApp messages)  
- **Pandas** (for handling birthday data)  
- **APScheduler** (for scheduling automatic execution)  
- **CSV** (for storing birthday data)  

---

## **📂 Project Structure**  
```
📁 WhatsApp-Birthday-Bot  
│── 📜 birthdays.csv           # Stores names, phone numbers, and birthdates  
│── 📜 birthday_bot.py         # Main script to check and send wishes  
│── 📜 README.md               # Project documentation  
```

---

## **📥 Installation**  
### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/prangowda/WhatsApp-Birthday-Bot.git
cd WhatsApp-Birthday-Bot
```

### **2️⃣ Install Dependencies**  
```bash
pip install twilio pandas apscheduler
```

### **3️⃣ Set Up Twilio API**  
1. Create an account on [Twilio](https://www.twilio.com/).  
2. Get your **Account SID** and **Auth Token** from the Twilio Console.  
3. Get your **Twilio WhatsApp Number**.  

---

## **📋 Configure Birthday Data**  
Modify `birthdays.csv` with your contacts' details:  

```
Name,Phone,Birthday
John Doe,+1234567890,02-12
Jane Smith,+1987654321,03-14
```
> **Format:** `MM-DD` for birthdays.

---

## **🚀 Run the Bot**  
```bash
python birthday_bot.py
```
> The bot will check for birthdays daily and send WhatsApp messages.

---

## **🛠️ How It Works**  
1. The script reads **birthdays.csv** to find contacts with birthdays today.  
2. It then sends a personalized birthday wish to them via WhatsApp.  
3. The script runs **daily at 9 AM** using APScheduler.  

---

## **🛠️ Deployment (Optional)**  
To keep the bot running continuously on a server:  
- **Linux (Background Process):**  
  ```bash
  nohup python birthday_bot.py &
  ```
- **Using systemd:**  
  ```bash
  sudo nano /etc/systemd/system/birthday_bot.service
  ```
  Add the following:
  ```
  [Unit]
  Description=WhatsApp Birthday Bot
  After=network.target

  [Service]
  ExecStart=/usr/bin/python3 /path/to/birthday_bot.py
  WorkingDirectory=/path/to/
  Restart=always
  User=username

  [Install]
  WantedBy=multi-user.target
  ```
  Then, enable and start the service:
  ```bash
  sudo systemctl enable birthday_bot
  sudo systemctl start birthday_bot
  ```

---

## **📌 Future Enhancements**  
🚀 Integrate Google Sheets API instead of CSV  
🚀 Add support for multiple messaging templates  
🚀 Host on AWS Lambda for a serverless approach  
