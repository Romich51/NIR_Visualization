import streamlit as st
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
    stages_duration = pd.read_csv('./data/stages_duration.csv')
    stage_act_duration = pd.read_csv('./data/stage_act_duration.csv')
    return df, df_month_median, df_year_median, df_month_mean, df_year_mean, depart_tth, stages_duration, stage_act_duration


@st.cache(hash_funcs={dict: lambda _: None})
def get_dict_of_plots(list_of_params):
    dict_of_plots = {}
    for param in list_of_params:
        plotly_fig = px.line(param['df'], x=param['date'], y='duration_days')
        dict_of_plots[param['df_name']+'_'+param['date']] = plotly_fig
    return dict_of_plots
