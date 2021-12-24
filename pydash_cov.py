import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt

df = pd.read_csv("D:\PyDash\state_level_latest.csv")

st.title("Covid-19 Dashboard For India \nBy Aditya Gupta COE6 101953010")
st.markdown('The dashboard will visualize the Covid-19 Situation in India')
st.markdown('Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus. Most people infected with the COVID-19 virus will experience mild to moderate respiratory illness and recover without requiring special treatment.')
st.sidebar.title("Visualization Selector")

st.sidebar.checkbox("Show Analysis by State", True, key=1)
select = st.sidebar.selectbox('Select a State',df['State'])

#get the state selected in the selectbox
state_data = df[df['State'] == select]
select_status = st.sidebar.radio("Covid-19 patient's status", ('Confirmed', 'Active', 'Recovered', 'Deceased'))

def get_total_dataframe(dataset):
    total_dataframe = pd.DataFrame({
    'Status':['Confirmed', 'Recovered', 'Deaths','Active'],
    'Number of cases':(dataset.iloc[0]['Confirmed'],
    dataset.iloc[0]['Recovered'],
    dataset.iloc[0]['Deaths'],dataset.iloc[0]['Active'])})
    return total_dataframe

state_total = get_total_dataframe(state_data)

if st.sidebar.checkbox("Show Analysis by State", True, key=2):
    st.markdown("## **State level analysis**")
    st.markdown("### Overall Confirmed, Active, Recovered and " +
    "Deceased cases in %s yet" % (select))
    if not st.checkbox('Hide Graph', False, key=1):
        state_total_graph = px.bar(
        state_total,
        x='Status',
        y='Number of cases',
        labels={'Number of cases':'Number of cases in %s' % (select)},
        color='Status')
        st.plotly_chart(state_total_graph)


st.sidebar.markdown("Select the Charts/Plots accordingly:")


select = st.sidebar.selectbox('Visualization type', ['Bar plot', 'Pie chart'], key='1')
if st.sidebar.checkbox("Hide", True, key='1'):
     if select == 'Pie chart':
         st.title("Selected top 5 cities")
         fig = px.pie(df, values=df['Confirmed'][:5], names=df['State'][:5], title='Total Confirmed Cases')
         st.plotly_chart(fig)

     if select=='Bar plot':
         st.title("Selected Top 5 Cities")
         fig = go.Figure(data=[
         go.Bar(name='Confirmed', x=df['State'][:5], y=df['Confirmed'][:5]),
         go.Bar(name='Recovered', x=df['State'][:5], y=df['Recovered'][:5]),
         go.Bar(name='Active', x=df['State'][:5], y=df['Active'][:5])])
         st.plotly_chart(fig)

df2 = pd.read_csv('D:\PyDash\case_time_series.csv')
df2['Date'] =  df2['Date'].astype('datetime64[ns]')
select1 = st.sidebar.selectbox('Select', ['Confirmed', 'Recovered'], key='3')
if not st.sidebar.checkbox("Hide", True, key='3'):
    if select1 == 'Confirmed':
        fig = px.line(df2, x="Date", y="Daily Confirmed")
        st.plotly_chart(fig)
    elif select1 == 'Recovered':
        fig = px.line(df2, x="Date", y="Daily Recovered")
        st.plotly_chart(fig)

select2 = st.sidebar.selectbox('Select', ['Confirmed', 'Recovered'], key='4')
if not st.sidebar.checkbox("Hide", True, key='4'):
    if select2 == 'Confirmed':
        fig = px.area(df2, x="Date", y="Daily Confirmed")
        st.plotly_chart(fig)
    elif select1 == 'Recovered':
        fig = px.area(df2, x="Date", y="Daily Recovered")
        st.plotly_chart(fig)

