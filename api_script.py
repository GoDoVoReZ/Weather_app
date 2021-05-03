# Импорт библиотек
import requests
import time
import datetime
import emoji
import wikipedia
import seaborn as sns

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
    
    # Получение информации об осадках
    precipitation = data['weather'][0]['main']
    prec = None

    # Выбор эмодзи в зависимости от осадков
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


# Функция построения графика погоды за 5 дней
def week_weather(city: str)->dict:
    try:
        # API-запрос
        res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                           params={'q':city, 'units': 'metric', 'lang': 'ru', 'APPID': API_KEY})
        # Перевод ответа в json-формат                   
        data = res.json()
        time = []
        temp = []
        # Вытаскиваем нужные данные из json-файла
        # Нужные данные это время и температура
        for i in data['list']:
            time.append(i['dt_txt'][:10])
            temp.append('{0:+3.0f}'.format(i['main']['temp_max']))

        # Построение графика по температуре и времени
        sns.lineplot(x=time, y=temp)

    # Если запрос немного ♂SUCK SOME DICK♂ выводим ошибку и ничего не делаем
    # Чтобы ничего не отъебнуло
    except Exception as e:
        print("Exception (forecast):", e)
        pass

# функция поиска информации о городе
# Использует Википедию, и возвращает строку с заметкой о данном городе
def city_wiki_info(city:str):
    return wikipedia.summary(city)