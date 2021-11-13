import os
import random

import pandas as pd
import numpy as np

import streamlit as st

import time

st.set_page_config(
    page_title="ЦП 2021: Бизнес-планер",
    layout='wide',
    initial_sidebar_state='auto',
)

cultures = {
    'картофель': {
        'id': 0,
        'Температура_min': 16,
        'Температура_max': 25,
        'Влажность_min': 0.4,
        'Влажность_max': 0.6,
        'Осадки_min': 300,
        'Почва': ['Суглинистые', 'Песчаные суглинки'],
        'pH_min': 4.5,
        'pH_max': 7.5,
    },
    'капуста': {
        'id': 1,
        'Температура_min': 20,
        'Температура_max': 25,
        'Влажность_min': 0.7,
        'Влажность_max': 0.8,
        'Осадки_min': 250,
        'Осадки_max': 300,
        'Почва': ['Суглинистые'],
        'pH_min': 5.6,
        'pH_max': 7.0,
    },
    'морковь': {
        'id': 2,
        'Температура_min': 18,
        'Температура_max': 25,
        'Влажность_min': 0.7,
        'Влажность_max': 0.8,
        'Осадки_min': 334.1,
        'Почва': ['Песчаные', 'Супесчаные', 'Легкосуглинистые'],
        'pH_min': 4.5,
        'pH_max': 7.5,
    },
    'свекла': {
        'id': 3,
        'Температура_min': 15,
        'Температура_max': 29,
        'Влажность_min': 0.7,
        'Влажность_max': 0.8,
        'Осадки_min': 334.1,
        'Почва': ['Песчаные', 'Супесчаные', 'Легкосуглинистые'],
        'pH_min': 5.0,
        'pH_max': 8.0,
    },
    'огурец': {
        'id': 4,
        'Температура_min': 22,
        'Температура_max': 25,
        'Влажность_min': 0.8,
        'Влажность_max': 0.8,
        'Осадки_min': 200,
        'Осадки_max': 250,
        'Почва': ['Супесчаные', 'Легкосуглинистые', 'Среднесуглинистые'],
        'pH_min': 6.5,
        'pH_max': 7.4,
    },
    'дыня': {
        'id': 5,
        'Температура_min': 25,
        'Температура_max': 30,
        'Влажность_min': 0.6,
        'Влажность_max': 0.7,
        'Осадки_min': 300,
        'Осадки_max': 400,
        'Почва': ['Легкосуглинистые'],
        'pH_min': 6.5,
        'pH_max': 7.0,
    },
    'арбуз': {
        'id': 6,
        'Температура_min': 25,
        'Температура_max': 30,
        'Влажность_min': 0.6,
        'Влажность_max': 0.7,
        'Осадки_min': 300,
        'Осадки_max': 400,
        'Почва': ['Легкосуглинистые'],
        'pH_min': 6.5,
        'pH_max': 7.0,
    },
    'рис': {
        'id': 7,
        'Температура_min': 25,
        'Температура_max': 28,
        'Влажность_min': 0.8,
        'Влажность_max': 0.9,
        'Осадки_min': 250,
        'Осадки_max': 300,
        'Почва': ['Суглинистые', 'Глинистые'],
        'pH_min': 5.5,
        'pH_max': 6.5,
    },
}


def next_step():
    pages = st.session_state.pages
    next_page_id = pages[st.session_state.page]['id']+1
    if next_page_id > 10:
        next_page_id = 0
    st.session_state.page = list(pages.keys())[next_page_id]
    st.experimental_rerun()


def main_page():
    st.title("Описание сервиса «Бизнес-планер»")
    st.write("## ЦИФРОВОЙ ПРОРЫВ 2021 // Команда DST-OFF")
    st.image("http://mari-el.gov.ru/PublishingImages/gerb_title.gif")
    st.write(
        """
        ## Разработка системы контроля энергетических ресурсов крестьянско-фермерских хозяйств в проактивном режиме
        ### Порядок работы с сервисом:
        
        В меню слева приведен список разделов сервиса в виде последовательного переченя шагов:
         
        1. Выберите сельскохозяйственную культуру
        2. Мыберите месторасположение земельного участка (район)
        3. Выберите вариант возделывания сельхозкультуры (открытый грунт или теплица)
        4. Получите рекомендацию сервиса о возможности возделывания выбранной культуры. \
        Рекомендация будет содержать обоснования и альтернативные варианты.  
        5. Изучите расчет энергозатрат. При необходимости вы можете скорректировать стоимость энергоресурсов.
        6. Сервис подготовит комплексный свод затрат на подготовку к посеву, выращивание и сбор урожая.
        7. Вы сможете ознакомится с ожидаемой выручкой и суммой прибыли, а также сроком окупаемости проекта.
        8. Сервис проведет расчет прибыли и срока окупаемости проекта
        9. В этом разделе исходные данные для расчетов могут быть скорректированы и дополнены 
        10. Воспользуйтесь программами государственной поддержки в Республике Марий Эл \
        """
    )

    st.button("Перейти к выбору сельхозкультуры", on_click=next_step)

    st.write(
        """
        ---
        Сервис разработан в рамках конкурса [Цифровой прорыв 2021. Агротех]\
        (https://leadersofdigital.ru/event/63012/case/1079464)
        """
    )
    st.caption(
        "по заказу [Министерства сельского хозяйства и продовольствия Республики Марий Эл]\
        (http://mari-el.gov.ru/Pages/main.aspx)"
    )


def select_culture():
    st.title("Выбор сельхозкультуры")
    if "culture" not in st.session_state:
        st.session_state.cultures = cultures
        st.session_state.culture = list(cultures.keys())[0]
    culture = st.selectbox('', st.session_state.cultures, st.session_state.cultures[st.session_state.culture]['id'])
    st.session_state.culture = culture

    with st.expander("Описание сельскохозяйственных культур"):
        st.dataframe(pd.DataFrame(st.session_state.cultures).astype(str).T)

    st.button("Перейти к выбору месторасположения", on_click=next_step)


def select_place():
    st.title("Выбор месторасположения")

    if "place" not in st.session_state:
        st.session_state.places = ['Йошкар-Ола', 'Юринский район', 'Сернурский район', 'Волжский район']
        st.session_state.place = 0
    place = st.selectbox('', st.session_state.places, st.session_state.place)
    st.session_state.culture = place

    with st.expander("Замли сельскохозяйственного назначения Республики Марий Эл"):
        st.image("http://mari-el.gov.ru/minstroy/DocLib30/120412_05.jpg")

    st.button("Перейти к выбору варианта возделывания", on_click=next_step)


pages = {
    'Описание сервиса': {'id': 0, 'func': main_page},
    'Выбор сельхозкультуры': {'id': 1, 'func': select_culture},
    'Выбор месторасположения': {'id': 2, 'func': select_place},
    'Выбор варианта возделывания': {'id': 3, 'func': select_culture},
    'Рекомендация': {'id': 4, 'func': select_culture},
    'Расчет энергозатрат на год': {'id': 5, 'func': select_culture},
    'Комплексный расчет затрат': {'id': 6, 'func': select_culture},
    'Планирование прибыли': {'id': 7, 'func': select_culture},
    'Оценка рисков': {'id': 8, 'func': select_culture},
    'Изменение данных': {'id': 9, 'func': select_culture},
    'Меры господдержки в Марий Эл': {'id': 10, 'func': select_culture},
}

st.sidebar.title(f"Бизнес-планер")
if "page" not in st.session_state:
    st.session_state.pages = pages
    st.session_state.page = list(pages.keys())[0]
page = st.sidebar.radio("", pages, pages[st.session_state.page]['id'])
st.session_state.page = page

# Draw main page
pages[page]['func']()
