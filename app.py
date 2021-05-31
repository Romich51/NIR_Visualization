import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from utils import load_data, get_dict_of_plots


df, df_month_median, df_year_median, df_month_mean, df_year_mean, depart_tth = load_data()
list_of_params = [{'df': df_month_mean, 'df_name': 'df_month_mean', 'date': 'month'},
                  {'df': df_month_median, 'df_name': 'df_month_median', 'date': 'month'},
                  {'df': df_year_mean, 'df_name': 'df_year_mean', 'date': 'year'},
                  {'df': df_year_median, 'df_name': 'df_year_median', 'date': 'year'}]
dict_of_plots = get_dict_of_plots(list_of_params)

st.sidebar.header('Выберите необходимые графики: ')
tth_checkbox = st.sidebar.checkbox('TTH', value=True)
depart_checkbox = st.sidebar.checkbox('Анализ по департаментам', value=False)


if tth_checkbox:
    st.sidebar.header('Time to Hire')
    date_aggr_radio = st.sidebar.radio(label='Агрегация по времени:', options=['Месяц', 'Год'])
    type_aggr_radio = st.sidebar.radio(label='Тип агрегации:', options=['Медиана', 'Среднее'])
    st.title('Анализ TTH')
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
