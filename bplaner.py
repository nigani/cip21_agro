import plotly.graph_objects as go
import plotly.express as px

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
        'Влажность_max': 0.8,
        'Осадки_min': 300,
        'Осадки_max': 450,
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
        'Осадки_max': 450,
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
        'Осадки_max': 450,
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
        'Осадки_max': 450,
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
        'Осадки_max': 400,
        'Почва': ['Супесчаные', 'Легкосуглинистые', 'Среднесуглинистые'],
        'pH_min': 6.5,
        'pH_max': 7.4,
    },
    'Дыня': {
        'id': 5,
        't_min': 25,
        't_max': 30,
        'Влажность_min': 0.6,
        'Влажность_max': 0.8,
        'Осадки_min': 300,
        'Осадки_max': 450,
        'Почва': ['Легкосуглинистые'],
        'pH_min': 6.5,
        'pH_max': 7.0,
    },
    'Арбуз': {
        'id': 6,
        't_min': 25,
        't_max': 30,
        'Влажность_min': 0.6,
        'Влажность_max': 0.8,
        'Осадки_min': 300,
        'Осадки_max': 450,
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
        'Осадки_max': 500,
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

if "culture" not in st.session_state:
    st.session_state.cultures = cultures
    st.session_state.culture = list(cultures.keys())[0]

if "place" not in st.session_state:
    st.session_state.places = places
    st.session_state.place = list(places.keys())[0]

if "gr_type" not in st.session_state:
    st.session_state.gr_types = ['Открытый грунт', 'Теплица']
    st.session_state.gr_type = st.session_state.gr_types[0]

def next_step():
    save_pages = st.session_state.pages
    next_page_id = pages[st.session_state.page]['id'] + 1
    if next_page_id > 10:
        next_page_id = 0
    st.session_state.page = list(save_pages.keys())[next_page_id]
    st.experimental_rerun()


def to_select_culture():
    st.session_state.page = 'Выбор сельхозкультуры'
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
    return np.where(x.index == idx, 'background-color: #e6ffe6; color: #000000;', None)

def highlight_flags(x, flags):
    return np.where(flags, 'background-color: #e6ffe6; color: #000000;', None)

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

    st.button("Получить рекомендацию", on_click=next_step)

    with st.expander("Варианты возделывания", expanded=True):
        st.image("Варианты возделывания.jpg")


def select_recomend():
    st.title("Рекомендация")
    st.write("## " + st.session_state.culture + " / Место: " + st.session_state.place +
             " / Тип возделывания: " + st.session_state.gr_type)
    st.write("---")

    with st.container():
        st.write("## Анализ возможности выращивания в открытом грунте")
        result = True
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            v_min = st.session_state.cultures[st.session_state.culture]['t_min']
            v_max = st.session_state.cultures[st.session_state.culture]['t_max']
            v_place = st.session_state.places[st.session_state.place]['t_лето']
            fig_c1 = go.Figure(go.Indicator(
                mode="gauge+number",
                value=v_place,
                domain={'x': [0, 1], 'y': [0, 1]},
                title={'text': "Температура"},
                gauge={'axis': {'range': [None, 50]},
                       'bar': {'thickness': 0},
                       'steps': [
                           {'range': [0, 50], 'color': "lightgray"},
                           {'range': [v_min , v_max], 'color': "green"}],
                       'threshold': {'line': {'color': "red", 'width': 6}, 'thickness': 0.75, 'value': v_place}}))

            fig_c1.update_layout(autosize=False, width=200, height=200, margin=dict(l=30, r=30, b=20, t=60),
                                 font={'size': 16})
            st.plotly_chart(fig_c1, use_container_width=True)
            if v_min <= v_place <= v_max:
                st.success("**Хорошо**")
            else:
                st.error("**Плохо**")
                result = False
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
            fig_c2.update_layout(autosize=False, width=200, height=200, margin=dict(l=30, r=30, b=20, t=60),
                                 font={'size': 16})
            st.plotly_chart(fig_c2, use_container_width=True)
            if v_min <= v_place <= v_max:
                st.success("**Хорошо**")
            else:
                st.error("**Плохо**")
                result = False
        with col3:
            v_min = st.session_state.cultures[st.session_state.culture]['Осадки_min']
            v_max = st.session_state.cultures[st.session_state.culture]['Осадки_max']
            v_place = st.session_state.places[st.session_state.place]['Осадки']
            fig_c3 = go.Figure(go.Indicator(
                mode="gauge+number",
                value=v_place,
                domain={'x': [0, 1], 'y': [0, 1]},
                title={'text': "Осадки"},
                gauge={'axis': {'range': [None, 500]},
                       'bar': {'thickness': 0},
                       'steps': [
                           {'range': [0, 500], 'color': "lightgray"},
                           {'range': [v_min, v_max], 'color': "green"}],
                       'threshold': {'line': {'color': "red", 'width': 6}, 'thickness': 0.75, 'value': v_place}}))

            fig_c3.update_layout(autosize=False, width=200, height=200, margin=dict(l=30, r=30, b=20, t=60),
                                 font={'size': 16})
            st.plotly_chart(fig_c3, use_container_width=True)
            if v_min <= v_place <= v_max:
                st.success("**Хорошо**")
            else:
                st.error("**Плохо**")
                result = False
        with col4:
            v_min = st.session_state.cultures[st.session_state.culture]['pH_min']
            v_max = st.session_state.cultures[st.session_state.culture]['pH_max']
            v_place = st.session_state.places[st.session_state.place]['pH']
            fig_c4 = go.Figure(go.Indicator(
                mode="gauge+number",
                value=v_place,
                domain={'x': [0, 1], 'y': [0, 1]},
                title={'text': "pH"},
                gauge={'axis': {'range': [None, 10]},
                       'bar': {'thickness': 0},
                       'steps': [
                           {'range': [0, 10], 'color': "lightgray"},
                           {'range': [v_min, v_max], 'color': "green"}],
                       'threshold': {'line': {'color': "red", 'width': 6}, 'thickness': 0.75, 'value': v_place}}))

            fig_c4.update_layout(autosize=False, width=200, height=200, margin=dict(l=30, r=30, b=20, t=60),
                                 font={'size': 16})
            st.plotly_chart(fig_c4, use_container_width=True)
            if v_min <= v_place <= v_max:
                st.success("**Хорошо**")
            else:
                st.error("**Плохо**")
                result = False
    if result:
        st.success("## РЕКОМЕНДОВАНО")
    elif st.session_state.gr_type == 'Теплица':
        st.success("## РЕКОМЕНДОВАНО ДЛЯ ТЕПЛИЦЫ")
    else:
        st.error("## НЕ РЕКОМЕНДОВАНО", )
        st.write("---")
        with st.expander("Рекомендация культуры", expanded=True):
            st.write("Вы можете выращивать выбранную культуру в защищенном грунте (теплице)"
                     " или выбрать другую культуру")
            flags = pd.DataFrame(st.session_state.cultures).T.t_min <=\
                    st.session_state.places[st.session_state.place]['t_лето']
            st.dataframe(pd.DataFrame(st.session_state.cultures).astype(str).T.style.apply(
                highlight_flags, flags=flags))
            st.button("Вернуться к выбору культуры", on_click=to_select_culture)

    st.button("ДАЛЕЕ", on_click=next_step)


def select_calc_energo():
    st.title("Расчет энергозатрат")
    df = pd.read_csv('calc2.csv')
    df = df[df['Вид затрат']=='Энергозатраты'].groupby('Статья').sum()
    st.dataframe(df)

    fig = px.bar(df['Сумма'], x='Сумма', orientation='h')
    st.write(fig)

    st.write('Изменить цены можно в разделе Изменение данных')

    st.button("ДАЛЕЕ", on_click=next_step)


def select_calc():
    st.title("Планирование прибыли")
    df = pd.read_csv('calc2.csv')
    st.dataframe(df)

    st.bar_chart(df.groupby('Этап')['Сумма'].sum(), )

    st.button("ДАЛЕЕ", on_click=next_step)


def select_risk():
    st.title("Оценка рисков")

    st.write('Необходимо обратить внимание на возможность страхования от неурожая, '
             'принятие защитных мер от вредителей, другие факторы.')

    st.button("ДАЛЕЕ", on_click=next_step)


def select_change():
    st.title("Изменение данных")

    @st.cache
    def convert_df(df):
        return df.to_csv(index=False).encode('utf-8')

    csv = convert_df(pd.read_csv('calc2.csv'))

    st.download_button(
        label="Выгрузить данные",
        data=csv,
        file_name='calc.csv',
        mime='text/csv',
    )

    spectra = st.file_uploader("Загрузить измененные данные", type={"csv"})
    if spectra is not None:
        spectra_df = pd.read_csv(spectra)
        st.write(spectra_df)
        spectra_df.to_csv('calc2.csv')

    st.button("ДАЛЕЕ", on_click=next_step)


def select_help():
    st.title("Меры господдержки в Марий Эл")

    st.write("[Государственная поддержка агропромышленного комплекса]"
             "(http://mari-el.gov.ru/minselhoz/Pages/budjet.aspx)")

    st.button("ДАЛЕЕ", on_click=next_step)


pages = {
    'Описание сервиса': {'id': 0, 'func': main_page},
    'Выбор сельхозкультуры': {'id': 1, 'func': select_culture},
    'Выбор месторасположения': {'id': 2, 'func': select_place},
    'Выбор варианта возделывания': {'id': 3, 'func': select_gr_type},
    'Рекомендация': {'id': 4, 'func': select_recomend},
    'Расчет энергозатрат на год': {'id': 5, 'func': select_calc_energo},
    'Планирование прибыли': {'id': 6, 'func': select_calc},
    'Оценка рисков': {'id': 7, 'func': select_risk},
    'Изменение данных': {'id': 8, 'func': select_change},
    'Меры господдержки в Марий Эл': {'id': 9, 'func': select_help},
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
