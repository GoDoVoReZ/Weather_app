# ДЕСКТОПНАЯ ВЕРСИЯ

# Импорт библиотек и модуля api_script
import PySimpleGUI as sg
import numpy as np 
from api_script import get_weather

# Тема главного окна
sg.theme('DarkAmber')

# Главная функция отображения, вызывает функцию get_weather из модуля api_script,
# отображает значение температуры в заданном городе
def update(city):
    try:
        # Вызываем функцию get_weather() 
        # Выводим строку с информацией о городе, времени, температуре и осадках
        weather = get_weather(city)
        text_elem = window['-text-']
        text_elem.update('Temp in {}: {} Celcius, {}'.format(weather['City'], weather['Temp'], weather['Prec']))
    except:
        # Если функция get_weather() не срабатывает выводим строку 
        # с иформацией об ошибке
        text_elem = window['-text-']
        text_elem.update("Some fucked'up")
# Слои окна:
    # sg.Text, sg.InputText - поле ввода необходимого города
    # sg.Button - кнопка окна вызывающая функию update()
    # sg.Text - поле вывода информации о температуре в заданном городе
layout = [[sg.Text('Enter city name here'), sg.InputText()],
         [sg.Button('Find', enable_events=True, key='-FUNCTION-', font='Helvetica 16')],
         [sg.Text('', size=(40,1), key='-text-', font='Helvetica 16')]]

# Вызов главного окна
window = sg.Window('Temperature in your sity', layout, size=(400,150))

# Основной цикл, в зависимости от нажатой кнопки вызывает функцию update() или закрывает окно
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == '-FUNCTION-':
        try:
            update(values[0])
        except Exception as e:
            print(e)
            pass    


# Закрытие главного окна
window.close()