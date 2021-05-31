import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px


@st.cache
def load_data():
    df = pd.read_csv('./data/data.csv')
    df_month_median = df.groupby('month')['duration_days'].median().reset_index()
    df_year_median = df.groupby('year')['duration_days'].median().reset_index()
    df_month_mean = df.groupby('month')['duration_days'].mean().reset_index()
    df_year_mean = df.groupby('year')['duration_days'].mean().reset_index()
    depart_tth = df.groupby('department_id')['duration_days'].median().reset_index()
    depart_tth = depart_tth[(depart_tth.duration_days > 1) & (depart_tth.duration_days < 50)]
    return df, df_month_median, df_year_median, df_month_mean, df_year_mean, depart_tth


df, df_month_median, df_year_median, df_month_mean, df_year_mean, depart_tth = load_data()
df_1 = df.copy()
st.dataframe(df_1)

st.sidebar.header('Time to Hire')
date_aggr_radio = st.sidebar.radio(label='Агрегация по времени:', options=['Месяц', 'Год'])
type_aggr_radio = st.sidebar.radio(label='Тип агрегации:', options=['Медиана', 'Среднее'])

if date_aggr_radio == 'Месяц':
    if type_aggr_radio == 'Медиана':
        st.plotly_chart(px.line(df_month_median, x='month', y='duration_days'))
    else:
        st.plotly_chart(px.line(df_month_mean, x='month', y='duration_days'))
else:
    if type_aggr_radio == 'Медиана':
        st.plotly_chart(px.line(df_year_median, x='year', y='duration_days'))
    else:
        st.plotly_chart(px.line(df_year_mean, x='year', y='duration_days'))


st.plotly_chart(px.histogram(depart_tth, 'duration_days'))
