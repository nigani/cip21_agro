import streamlit as st
import pandas as pd
import numpy as np
import time

map_api_key = 'pk.eyJ1IjoiZHN0LW9mZiIsImEiOiJja3Z3NzA1c2UxaWNnMnBtOTI5cDU1YzNqIn0.JtMa21105qINFxVeIwqnqw'

st.title("Авторизация")

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

with st.form(key='login_form'):
    if 'logged_in' not in st.session_state:
        email = st.text_input("Для демонстрации - имя `demo`, пароль `demo`")
        password = st.text_input("Пароль", type="password")
        submit_button = st.form_submit_button(label="Авторизация")

        if submit_button:
            if email.lower() == 'demo' and password == 'demo':
                st.success("Вы успешно авторизованы.")
                st.session_state.logged_in = True
                with st.spinner("Переход в приложение"):
                    time.sleep(1)
                    st.experimental_rerun()
            else:
                st.success("Проверьте имя и пароль. Используйте demo/demo")

st.title("Пример")

st.write("Основное приложения")
pdk = 0

if False:
    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        initial_view_state=pdk.ViewState(
            latitude=37.76,
            longitude=-122.4,
            zoom=11,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                'HexagonLayer',
                data=df,
                get_position='[lon, lat]',
                radius=200,
                elevation_scale=4,
                elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
            ),
            pdk.Layer(
                'ScatterplotLayer',
                data=df,
                get_position='[lon, lat]',
                get_color='[200, 30, 0, 160]',
                get_radius=200,
            ),
        ],
    ))
