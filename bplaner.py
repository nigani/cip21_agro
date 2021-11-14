﻿import plotly.graph_objects as go

import pandas as pd
import numpy as np

import streamlit as st

st.set_page_config(
    page_title="ЦП 2021: Бизнес-планер",
    layout='wide',
    initial_sidebar_state='auto',
)

st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden; }
    footer {visibility: hidden;}</style>
    """,
    unsafe_allow_html=True
)

cultures = {
    'Картофель': {
        'id': 0,
        't_min': 16,
        't_max': 25,
        'Влажность_min': 0.4,
        'Влажность_max': 0.6,
        'Осадки_min': 300,
        'Осадки_max': 300,
        'Почва': ['Суглинистые', 'Песчаные суглинки'],
        'pH_min': 4.5,
        'pH_max': 7.5,
    },
    'Капуста': {
        'id': 1,
        't_min': 20,
        't_max': 25,
        'Влажность_min': 0.7,
        'Влажность_max': 0.8,
        'Осадки_min': 250,
        'Осадки_max': 300,
        'Почва': ['Суглинистые'],
        'pH_min': 5.6,
        'pH_max': 7.0,
    },
    'Морковь': {
        'id': 2,
        't_min': 18,
        't_max': 25,
        'Влажность_min': 0.7,
        'Влажность_max': 0.8,
        'Осадки_min': 334,
        'Осадки_max': 400,
        'Почва': ['Песчаные', 'Супесчаные', 'Легкосуглинистые'],
        'pH_min': 4.5,
        'pH_max': 7.5,
    },
    'Свекла': {
        'id': 3,
        't_min': 15,
        't_max': 29,
        'Влажность_min': 0.7,
        'Влажность_max': 0.8,
        'Осадки_min': 334,
        'Осадки_max': 400,
        'Почва': ['Песчаные', 'Супесчаные', 'Легкосуглинистые'],
        'pH_min': 5.0,
        'pH_max': 8.0,
    },
    'Огурец': {
        'id': 4,
        't_min': 22,
        't_max': 25,
        'Влажность_min': 0.8,
        'Влажность_max': 0.8,
        'Осадки_min': 200,
        'Осадки_max': 250,
        'Почва': ['Супесчаные', 'Легкосуглинистые', 'Среднесуглинистые'],
        'pH_min': 6.5,
        'pH_max': 7.4,
    },
    'Дыня': {
        'id': 5,
        't_min': 25,
        't_max': 30,
        'Влажность_min': 0.6,
        'Влажность_max': 0.7,
        'Осадки_min': 300,
        'Осадки_max': 400,
        'Почва': ['Легкосуглинистые'],
        'pH_min': 6.5,
        'pH_max': 7.0,
    },
    'Арбуз': {
        'id': 6,
        't_min': 25,
        't_max': 30,
        'Влажность_min': 0.6,
        'Влажность_max': 0.7,
        'Осадки_min': 300,
        'Осадки_max': 400,
        'Почва': ['Легкосуглинистые'],
        'pH_min': 6.5,
        'pH_max': 7.0,
    },
    'Рис': {
        'id': 7,
        't_min': 25,
        't_max': 28,
        'Влажность_min': 0.8,
        'Влажность_max': 0.9,
        'Осадки_min': 250,
        'Осадки_max': 300,
        'Почва': ['Суглинистые', 'Глинистые'],
        'pH_min': 5.5,
        'pH_max': 6.5,
    },
}

places = {
    'Йошкар-Ола': {
        'id': 0,
        't_лето': 20.17,
        't_апр_сент': 15.30,
        'Влажность': 0.67,
        'Осадки': 370,
        'Почва': ['Дерново-подзолистые', 'Суглинистые'],
        'pH': 6.7,
    },
    'Юринский': {
        'id': 1,
        't_лето': 20.27,
        't_апр_сент': 15.34,
        'Влажность': 0.67,
        'Осадки': 370,
        'Почва': ['Дерново-слабоподзолистые', 'Дерново-среднеподзолистые', 'Песчаные'],
        'pH': 6.7,
    },
    'Сернурский': {
        'id': 2,
        't_лето': 20.23,
        't_апр_сент': 15.15,
        'Влажность': 0.67,
        'Осадки': 370,
        'Почва': ['Дерново-подзолистые', 'Суглинистые'],
        'pH': 6.7,
    },
    'Волжский': {
        'id': 3,
        't_лето': 20.50,
        't_апр_сент': 15.22,
        'Влажность': 0.67,
        'Осадки': 370,
        'Почва': ['Дерново-подзолистые', 'Песчаные'],
        'pH': 6.7,
    },
}


def next_step():
    save_pages = st.session_state.pages
    next_page_id = pages[st.session_state.page]['id'] + 1
    if next_page_id > 10:
        next_page_id = 0
    st.session_state.page = list(save_pages.keys())[next_page_id]
    st.experimental_rerun()


def main_page():
    st.title("БИЗНЕС-ПЛАНЕР")
    st.write(
        """
        ## • Выберите сельскохозяйственную культуру
        ## • Выберите расположение земельного участка
        ## • Выберите вариант возделывания
        ## • Получите рекомендации!
        ###
        
        """
    )

    st.button("ПРИСТУПИТЬ", on_click=next_step)

    with st.expander("Расширенные инструкции"):
        st.write(
            """
            Также Вы сможете:
            * Изучить расчет энергозатрат. При необходимости Вы можете скорректировать стоимость энергоресурсов
            * Проанализировать комплексный свод затрат на подготовку к посеву, выращивание и сбор урожая
            * Ознакомится с ожидаемой выручкой и суммой годовой прибыли
            * Увидеть расчет срока окупаемости капитальгных затрат
            * Сделать предложение по ценам на семена и услуги для крестьянско-фермерских хозяйств
            * Предложить земельный участок или теплицу под выращивание сельхозкультур 
            * Воспользоваться программами государственной поддержки Республики Марий Эл
            """
        )


def highlight_idx(x, idx):
    return np.where(x.index == idx, 'background-color: #e6ffe6;', None)


def select_culture():
    st.title("Выбор сельхозкультуры")
    if "culture" not in st.session_state:
        st.session_state.cultures = cultures
        st.session_state.culture = list(cultures.keys())[0]
    culture = st.selectbox('Выберите культуру',
                           st.session_state.cultures, st.session_state.cultures[st.session_state.culture]['id'])
    st.session_state.culture = culture

    with st.expander("Описание сельскохозяйственных культур", expanded=True):
        st.dataframe(pd.DataFrame(st.session_state.cultures).astype(str).T.style.apply(highlight_idx, idx=culture))

    st.button("Перейти к выбору месторасположения", on_click=next_step)


def select_place():
    st.title("Выбор месторасположения")
    st.write("## Культура: " + st.session_state.culture)

    if "place" not in st.session_state:
        st.session_state.places = places
        st.session_state.place = list(places.keys())[0]
    place = st.selectbox('Выберите расположение земельного участка',
                         st.session_state.places, st.session_state.places[st.session_state.place]['id'])
    st.session_state.place = place

    with st.expander("Описание расположения земельных участков", expanded=True):
        st.dataframe(pd.DataFrame(st.session_state.places).astype(str).T.style.apply(highlight_idx, idx=place))

    st.button("Перейти к выбору варианта возделывания", on_click=next_step)

    with st.expander("Земли сельскохозяйственного назначения Республики Марий Эл", expanded=True):
        st.image("Схема границ.jpg")


def select_gr_type():
    st.title("Выбор варианта возделывания")
    st.write("## Культура: " + st.session_state.culture + " / Место: " + st.session_state.place)

    if "gr_type" not in st.session_state:
        st.session_state.gr_types = ['Открытый грунт', 'Теплица']
        st.session_state.gr_type = st.session_state.gr_types[0]
    gr_type = st.selectbox('Выберите вариант возделывания',
                           st.session_state.gr_types, st.session_state.gr_types.index(st.session_state.gr_type))
    st.session_state.gr_type = gr_type

    with st.expander("Варианты возделывания", expanded=True):
        st.image("Варианты возделывания.jpg")

    st.button("Получить рекомендацию", on_click=next_step)


def select_recomend():
    st.title("Рекомендация")
    st.write("## " + st.session_state.culture + " / Место: " + st.session_state.place +
             " / Тип возделывания: " + st.session_state.gr_type)
    st.write("---")
    st.write("## Анализ данных")
    st.write()
    st.write(st.session_state.cultures[st.session_state.culture]['t_max'])
    st.write(st.session_state.cultures[st.session_state.culture]['Влажность_min'])
    st.write(st.session_state.cultures[st.session_state.culture]['Влажность_max'])
    st.write(st.session_state.cultures[st.session_state.culture]['Осадки_min'])
    st.write(st.session_state.cultures[st.session_state.culture]['Осадки_max'])
    st.write(st.session_state.cultures[st.session_state.culture]['Почва'])
    st.write(st.session_state.cultures[st.session_state.culture]['pH_min'])
    st.write(st.session_state.cultures[st.session_state.culture]['pH_max'])

    with st.container():
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            t_min = st.session_state.cultures[st.session_state.culture]['t_min']
            t_max = st.session_state.cultures[st.session_state.culture]['t_max']
            t_place = st.session_state.places[st.session_state.place]['t_лето']
            fig_c1 = go.Figure(go.Indicator(
                mode="gauge+number",
                value=t_place,
                domain={'x': [0, 1], 'y': [0, 1]},
                title={'text': "Температура"},
                gauge={'axis': {'range': [None, 50]},
                       'bar': {'thickness': 0},
                       'steps': [
                           {'range': [0, 50], 'color': "lightgray"},
                           {'range': [t_min , t_max], 'color': "green"}],
                       'threshold': {'line': {'color': "red", 'width': 6}, 'thickness': 0.75, 'value': t_place}}))

            fig_c1.update_layout(autosize=False, width=200, height=200, margin=dict(l=20, r=20, b=20, t=60),
                                 font={'size': 16})
            st.plotly_chart(fig_c1, use_container_width=True)
        with col2:
            v_min = st.session_state.cultures[st.session_state.culture]['Влажность_min']
            v_max = st.session_state.cultures[st.session_state.culture]['Влажность_max']
            v_place = st.session_state.places[st.session_state.place]['Влажность']
            fig_c2 = go.Figure(go.Indicator(
                mode="gauge+number",
                value=v_place,
                domain={'x': [0, 1], 'y': [0, 1]},
                title={'text': "Влажность"},
                gauge={'axis': {'range': [None, 1]},
                       'bar': {'thickness': 0},
                       'steps': [
                           {'range': [0, 1], 'color': "lightgray"},
                           {'range': [v_min , v_max], 'color': "green"}],
                       'threshold': {'line': {'color': "red", 'width': 6}, 'thickness': 0.75, 'value': v_place}}))

            fig_c2.update_layout(autosize=False, width=200, height=200, margin=dict(l=20, r=20, b=20, t=60),
                                 font={'size': 16})
            st.plotly_chart(fig_c2, use_container_width=True)
        with col3:
            fig_c3 = go.Figure(go.Indicator(
                mode="gauge+number",
                value=500,
                domain={'x': [0, 1], 'y': [0, 1]},
                title={'text': "Осадки"}))
            fig_c3.update_layout(autosize=False, width=200, height=200, margin=dict(l=20, r=20, b=20, t=60),
                                 font={'size': 18})
            st.plotly_chart(fig_c3, use_container_width=True)
        with col4:
            fig_c4 = go.Figure(go.Indicator(
                mode="gauge+number",
                value=500,
                domain={'x': [0, 1], 'y': [0, 1]},
                title={'text': "pH"}))
            fig_c4.update_layout(autosize=False, width=200, height=200, margin=dict(l=20, r=20, b=20, t=60),
                                 font={'size': 18})
            st.plotly_chart(fig_c4, use_container_width=True)

    st.button("ДАЛЕЕ", on_click=next_step)


def select_calc():
    st.title("Расчет прибыли")
    df = pd.read_csv('calc2.csv')
    st.dataframe(df)

    st.bar_chart(df.groupby('Этап')['Сумма'].sum(), )

    st.button("ДАЛЕЕ", on_click=next_step)


pages = {
    'Описание сервиса': {'id': 0, 'func': main_page},
    'Выбор сельхозкультуры': {'id': 1, 'func': select_culture},
    'Выбор месторасположения': {'id': 2, 'func': select_place},
    'Выбор варианта возделывания': {'id': 3, 'func': select_gr_type},
    'Рекомендация': {'id': 4, 'func': select_recomend},
    'Расчет энергозатрат на год': {'id': 5, 'func': select_culture},
    'Комплексный расчет затрат': {'id': 6, 'func': select_culture},
    'Планирование прибыли': {'id': 7, 'func': select_calc},
    'Оценка рисков': {'id': 8, 'func': select_culture},
    'Изменение данных': {'id': 9, 'func': select_culture},
    'Меры господдержки в Марий Эл': {'id': 10, 'func': select_culture},
}

st.sidebar.title(f"Меню")
if "page" not in st.session_state:
    st.session_state.pages = pages
    st.session_state.page = list(pages.keys())[0]
page = st.sidebar.radio("", pages, pages[st.session_state.page]['id'])
st.session_state.page = page

with st.sidebar.expander("О сервисе"):
    st.write("## ЦИФРОВОЙ ПРОРЫВ 2021 \n Команда DST-OFF")
    st.write("Разработка системы контроля энергетических ресурсов крестьянско-фермерских хозяйств в проактивном режиме")
    st.caption("Сервис разработан в рамках конкурса [Цифровой прорыв 2021. Агротех]"
               "(https://leadersofdigital.ru/event/63012/case/1079464) по заказу "
               "[Министерства сельского хозяйства и продовольствия Республики Марий Эл]"
               "(http://mari-el.gov.ru/Pages/main.aspx)")
    st.image("http://mari-el.gov.ru/PublishingImages/republic_map.jpg")
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.image("http://mari-el.gov.ru/PublishingImages/gerb_title.gif")

pages[page]['func']()
