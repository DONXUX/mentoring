from bs4 import BeautifulSoup
from telegram.ext import Updater, MessageHandler, Filters
from emoji import emojize
from urllib.request import urlopen
import ssl
import re

TOKEN = "1299833693:AAGBzW6Qcnb7X3y09VKXC5jwZdVFPUSEdJc" # 텔레그램 봇(남친) 토큰

updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher
updater.start_polling() # 텔레그램 봇(남친) 수신대기

### 대화 핸들러
def handler(bot, update):
    text = update.message.text
    chat_id = update.message.chat_id

    if '모해' in text:
        bot.send_message(chat_id=chat_id, text='뭐하긴 너 생각하지ㅎㅎ')
    elif '아잉' in text:
        bot.send_message(chat_id=chat_id, text=emojize('아이잉:heart_eyes:', use_aliases=True))
    elif '날씨 알려줘' in text:
        bot.send_message(chat_id=chat_id, text=f'{getWeather()}')
    else:
        bot.send_message(chat_id=chat_id, text='뭐라구?')

echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)

### 현재 날씨 정보 클래스
class Weather:
    # 생성자
    def __init__(self, temperature, weather, feeling, rainfall, wind, humidity):
        self.temperature = temperature
        self.weather = weather
        self.feeling = feeling
        self.rainfall = rainfall
        self.wind = wind
        self.humidity = humidity        

    # 출력
    def __str__(self):
        return  f"""오늘 날씨는 이래 ㅎㅎ
현재 온도 : {self.temperature}
현재 날씨 : {self.weather}
체감 온도 : {self.feeling}
강수 확률 : {self.rainfall}
바람 : {self.wind}
습도 : {self.humidity}"""

### 네이버로부터 날씨 정보를 불러옵니다.
def getWeather():
    # 네이버 날씨 HTML 불러오기
    context = ssl._create_unverified_context()
    html = urlopen('https://n.weather.naver.com/today/03170119', context=context)
    soup = BeautifulSoup(html.read(), 'html.parser')

    # 현재 날씨 파트 파싱
    todayWeather = soup.select('.today_weather')[0]

    # 세부 정보 파싱
    temperature = f"{re.sub('[|가-힣]+','',todayWeather.select('.current')[0].get_text())}" # 현재 온도
    weather = f"{todayWeather.select('.weather')[0].get_text()}" # 현재 날씨
    feeling = f"{todayWeather.select('.desc_feeling')[0].get_text()}" # 체감 온도
    rainfall = f"{todayWeather.select('.desc_rainfall')[0].get_text()}" # 강수 확률
    wind = f"{todayWeather.select('.desc_wind')[0].get_text()}" # 바람
    humidity = f"{todayWeather.select('.desc_humidity')[0].get_text()}" # 습도

    # 현재 날씨 정보 객체를 생성하고 반환
    return Weather(temperature, weather, feeling, rainfall, wind, humidity) 
