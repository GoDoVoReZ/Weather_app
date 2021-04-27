import streamlit as st 
from api_script import get_weather
import time

st.title('Weather in your city')
text = st.text_input('Enter city here')
btn = st.button('Find')

plot_check = st.sidebar.checkbox('Show the plot?')
time_check = st.sidebar.checkbox('Show the time?')

if text is not None and btn:
    try:
        data = get_weather(text)
        if time_check:
            mess = 'Weather in {} ({}): {} C, {}'.format(data['City'], data['Time'], data['Temp'], data['Prec'])
            st.markdown(f'# {mess}')
        else:
            mess = 'Weather in {}: {} C, {}'.format(data['City'], data['Temp'], data['Prec'])
            st.markdown(f'# {mess}')
        if plot_check:
            pass
    except:
        st.write('Something went wrong.Try again')