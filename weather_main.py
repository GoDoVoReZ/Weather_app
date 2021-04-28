# БРАУЗЕРНАЯ ВЕРСИЯ

# Импорт библиотек
import streamlit as st 
from api_script import get_weather
import time

# Вывод строки с названием
st.title('Weather in your city')

# Установка поля ввода
text = st.text_input('Enter city here')

# Установка кнопки поиска
btn = st.button('Find')

# Отображение боковой панели с чекбоксами
# Чекбокс проверяющий нужно ли строить график погоды
plot_check = st.sidebar.checkbox('Show the plot?')

# Чекбокс проверяющий нужно ли указывать время при выводе
time_check = st.sidebar.checkbox('Show the time?')


# Блок главных условий

# Если поле ввода не пустое и кнопка поиска нажата
if text is not None and btn:
    try:
        # Вызов функции get_weather()
        data = get_weather(text)
        # Если чекбокс времени активен добавить в строку вывода время
        if time_check:
            # Создание строки вывода
            mess = 'Weather in {} ({}): {} C, {}'.format(data['City'], data['Time'], data['Temp'], data['Prec'])
            st.markdown(f'# {mess}')
        # Если чекбокс времени НЕ активен не добавлять время в строку вывода
        else:
            mess = 'Weather in {}: {} C, {}'.format(data['City'], data['Temp'], data['Prec'])
            st.markdown(f'# {mess}')
        if plot_check:
            pass
    # Если функция get_weather() отработала не правильно 
    # Вывести строку с информацией об ошибке
    except:
        st.write('Something went wrong.Try again')