# Импорт библиотек
import requests
import time
import datetime

# API-ключ для сайта openweathermap.org
API_KEY = 'f80c68c910ec32bfb6928c1f483bb0ad'

# Функия получения информации о погоде в заданном городе,
def get_weather(city: str) -> dict:
    # Запрос о погоде в заданном городе
    res = requests.get('http://api.openweathermap.org/data/2.5/weather',
                      params={'q':city, 'units':'metric', 'lang':'ru', 'APPID':API_KEY})
    
    # Преобразование ответа сайта в .json формат
    data = res.json()
    
    # Преобразование времени в удобный формат 
    time_d = str(time.ctime(data['dt']))[4:]
    time_res = str(datetime.datetime.strptime(time_d, '%b %d %H:%M:%S %Y'))
    
    # Запись преобразованных данных в словарь
    d_data = {}
    d_data['City'] = city
    d_data['Time'] = time_res
    d_data['Temp'] = data['main']['temp']

    # Возвращает словарь с данными
    return d_data


def get_weather_for_the_month(sity:str) -> dict:
    res = requests.get('https://pro.openweathermap.org/data/2.5/forecast/climate',
                      params={'q':city, 'units':'metric', 'lang':'ru', 'APPID':API_KEY})
    
    data = res.json()
    print(data)

get_weather_for_the_month('Moscow,RU')
