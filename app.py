import streamlit as st
import datetime
import requests
from PIL import Image
import pandas as pd

# page conf
st.set_page_config(
    page_title="NY Taxi Fare Prediction",
    page_icon=":snake:",
    layout="centered", # wide
    initial_sidebar_state="auto") # collapsed

'''
# New York City Taxi Fare Predictor

This application was built by Raphaël Voortman

'''
pickup_time = st.sidebar.time_input('Insert a pickup time')
pickup_date = st.sidebar.date_input('Insert a pickup day')
pickup_longitude = st.sidebar.number_input('Insert a pickup longitude', value=-74.01)
pickup_latitude = st.sidebar.number_input('Insert a pickup latitude', value=40.78)
dropoff_longitude = st.sidebar.number_input('Insert a dropoff longitude', value=-73.94)
dropoff_latitude = st.sidebar.number_input('Insert a dropoff latitude', value=40.65)
passenger_count = st.sidebar.number_input('Insert a passenger count', step=1, value=1)
pickup_datetime = str(pickup_date) + " " + str(pickup_time)

url = f'https://taxifare.lewagon.ai/predict?pickup_datetime={pickup_datetime}&pickup_longitude={pickup_longitude}&pickup_latitude={pickup_latitude}&dropoff_longitude={dropoff_longitude}&dropoff_latitude={dropoff_latitude}1&passenger_count={passenger_count}'

response = requests.get(url)

st.write('The estimated cost of your ride is: ', round(response.json()['prediction'],2), '$')

dict = {'lat': [pickup_latitude, dropoff_latitude],'lon': [pickup_longitude, dropoff_longitude]}

df = pd.DataFrame(dict)

st.map(df)