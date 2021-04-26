# Импорт библиотек
import requests
import time
import datetime
import emoji

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
    
    precipitation = data['weather'][0]['main']
    prec = None

    if precipitation == 'Clouds':
        prec = emoji.emojize(':cloud:')
    elif precipitation == 'Fog':
        prec = emoji.emojize(':foggy:')
    elif precipitation == 'Clear':
        prec = emoji.emojize(':sun_with_face:')
    elif precipitation == 'Rain':
        prec = emoji.emojize(':umbrella:')
    elif precipitation == 'Snow':
        prec = emoji.emojize(':snowflake:')

    # Запись преобразованных данных в словарь
    d_data = {}
    d_data['City'] = city
    d_data['Time'] = time_res
    d_data['Temp'] = data['main']['temp']
    d_data['Prec'] = prec

    # Возвращает словарь с данными
    return d_data
