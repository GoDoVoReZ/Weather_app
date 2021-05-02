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

city_info_check = st.sidebar.checkbox('Show the city info')


# Блок главных условий

# Если поле ввода не пустое и кнопка поиска нажата
if text is not None and btn:
    try:
        # Вызов функции get_weather()
        data = get_weather(text)
        mess = 'Temp in {}: {} °C'.format(data['City'], data['Temp'])
        time = ''
        info = ''
        if plot_check:
            # Заебашить сюда график погоды за 7, 14, 30 дней
            pass
        if time_check:
            time = data['Time']

        if city_info_check:
            info = city_wiki_info(data['City'])

        st.markdown(f'# {mess} #')
        st.markdown(f'## {time} ##')
        st.markdown(f'**{info}**')
        
        
    # Если функция get_weather() отработала не правильно 
    # Вывести строку с информацией об ошибке
    except:
        st.markdown('## **Something went wrong.Try again** ##')