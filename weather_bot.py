import requests
from telegram import Bot
weather_api_key = "30b0191d14ed6972c1328b7d3e176b6c"
telegram_token = "8076547583:AAHNwl53_J-iAej7SMP8R8KgbTM21dTR14M"
chat_id = "5559563400"

def get_weather(city="Taichung"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric&lang=zh_tw"
    res = requests.get(url)
    data = res.json()

    if data.get("main"):
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        return f"{city} 現在溫度 {temp}°C，天氣狀況：{description}"
    else:
        return "取得天氣資料失敗"

def send_to_telegram(message):
    bot = Bot(token=telegram_token)
    print("準備傳送到 Telegram...")
    bot.send_message(chat_id=chat_id, text=message)
    print("訊息已送出（已呼叫 Telegram API）！")

msg = get_weather("Taichung")
send_to_telegram(msg)
print(msg)

import schedule
import time

def job():
    msg = get_weather("Taichung")
    send_to_telegram(msg)

schedule.every().hour.at(":00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
