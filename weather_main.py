# БРАУЗЕРНАЯ ВЕРСИЯ

# Импорт библиотек
import streamlit as st 
from api_script import *
import time

# Вывод строки с названием
st.title('Weather in your city')

# Установка поля ввода
text = st.text_input('Enter city here')

# Установка кнопки поиска
btn = st.button('Find')

# Отображение боковой панели с чекбоксами
# Чекбокс проверяющий нужно ли строить график погоды
plot_check = st.sidebar.checkbox('Show the plot')

# Чекбокс проверяющий нужно ли указывать время при выводе
time_check = st.sidebar.checkbox('Show the time')

# Чекбокс проверяющий нужно ли выводить строку с информацией о городе
city_info_check = st.sidebar.checkbox('Show the city info')


# Блок главных условий

# Если поле ввода не пустое и кнопка поиска нажата
if text is not None and btn:
    try:
        # Вызов функции get_weather()
        data = get_weather(text)
        # Переменные погоды,осадков
        # Времени
        # И информации о городе
        mess = 'Temp in {}: {} °C {}'.format(data['City'], data['Temp'], data['Prec'])
        time = ''
        info = ''
        # Если активен чекбокс plot_check покзать график погоды
        if plot_check:
            # Вызываем функцию для построения графика
            week_weather(data['City'])

        # Если активен чекбокс time_check показать время
        if time_check:
            time = data['Time']

        # Если фктивен чекбокс city_info_check показать информацию о городе
        if city_info_check:
            info = city_wiki_info(data['City'])

        # Основной вывод
        st.markdown(f'# {mess} #')
        st.markdown(f'## {time} ##')
        # Если активен чекбокс plot_check покзать график погоды
        if plot_check:
            # Вызываем функцию для построения графика
            week_weather(data['City'])
            # Отрисовываем график
            st.pyplot()
        st.markdown(f'**{info}**')
        
        
    # Если функция get_weather() отработала не правильно 
    # Вывести строку с информацией об ошибке
    except:
        st.markdown('## **Something went wrong.Try again** ##')