import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from utils import load_data, get_dict_of_plots


df, df_month_median, df_year_median, df_month_mean, df_year_mean, depart_tth, stages_duration, stage_act_duration, hire_qty_by_month = load_data()
list_of_params = [{'df': df_month_mean, 'df_name': 'df_month_mean', 'date': 'month'},
                  {'df': df_month_median, 'df_name': 'df_month_median', 'date': 'month'},
                  {'df': df_year_mean, 'df_name': 'df_year_mean', 'date': 'year'},
                  {'df': df_year_median, 'df_name': 'df_year_median', 'date': 'year'}]
dict_of_plots = get_dict_of_plots(list_of_params)
#st.sidebar.image('./data/misis_logo.png')
st.sidebar.header('Выберите необходимые графики: ')
tth_checkbox = st.sidebar.checkbox('TTH', value=True)
depart_checkbox = st.sidebar.checkbox('Анализ по департаментам', value=False)
stages_checkbox = st.sidebar.checkbox('Анализ по стадиям', value=False)
hire_qty_checkbox = st.sidebar.checkbox('Кол-во нанимаемых в динамике', value=False)

if tth_checkbox:
    st.sidebar.header('Time to Hire')
    date_aggr_radio = st.sidebar.radio(label='Агрегация по времени:', options=['Месяц', 'Год'])
    type_aggr_radio = st.sidebar.radio(label='Тип агрегации:', options=['Медиана', 'Среднее'])
    st.title('Анализ TTH')
    st.markdown("Медианный TTH: {} дней".format(np.round(df.duration_days.median(), 1)))
    if date_aggr_radio == 'Месяц':
        if type_aggr_radio == 'Медиана':
            st.plotly_chart(dict_of_plots['df_month_median_month'])
        else:
            st.plotly_chart(dict_of_plots['df_month_mean_month'])
    else:
        if type_aggr_radio == 'Медиана':
            st.plotly_chart(dict_of_plots['df_year_median_year'])
        else:
            st.plotly_chart(dict_of_plots['df_year_mean_year'])

if depart_checkbox:
    st.title('Распределение TTH по департаментам')
    st.plotly_chart(px.histogram(depart_tth, 'duration_days'))

if stages_checkbox:
    st.title('Медианное время, затраченное на стадию/активность')
    st.sidebar.header('Анилиз стадий и активностей')
    stage_act_radio = st.sidebar.radio(label='Стадии/активности: ', options=['Стадии', 'Активности'])
    if stage_act_radio == 'Стадии':
        st.plotly_chart(px.bar(stages_duration, x='stage_name', y='duration_hours'))
    else:
        st.plotly_chart(px.bar(stage_act_duration, x='stage_activity', y='duration_hours'))

if hire_qty_checkbox:
    st.title('Количество нанимаемых в динамике')
    st.plotly_chart(px.line(hire_qty_by_month, x='month', y='hire_qty'))
