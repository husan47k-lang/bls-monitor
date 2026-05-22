import requests, os

TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

URLS = [
    "https://blsitalypakistan.com/page/schedule_an_appointment",
    "https://theitalyvisa.com/page/schedule_an_appointment"
]

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

def send_telegram(msg):
    requests.post(
        f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": msg}
    )

def check():
    for url in URLS:
        try:
            r = requests.get(url, headers=headers, timeout=15)
            html = r.text.lower()
            no_slot = ["no slots","no appointment","fully booked","not available"]
            has_slot = ["select date","choose slot","book now","select time","available"]
            if not any(w in html for w in no_slot) and any(w in html for w in has_slot):
                send_telegram(f"🚨 BLS ITALY SLOT OPEN!\nBook NOW: {url}")
                print("ALERT SENT!")
            else:
                print(f"No slot: {url}")
        except Exception as e:
            print(f"Error: {e}")

check()
