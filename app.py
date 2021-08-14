import streamlit as st
import datetime
import requests
from PIL import Image
import pandas as pd

'''
# TaxiFareModel front
'''
pickup_time = st.sidebar.time_input('Insert a pickup time')
pickup_date = st.sidebar.date_input('Insert a pickup day')
pickup_longitude = st.sidebar.number_input('Insert a pickup longitude')
pickup_latitude = st.sidebar.number_input('Insert a pickup latitude')
dropoff_longitude = st.sidebar.number_input('Insert a dropoff longitude')
dropoff_latitude = st.sidebar.number_input('Insert a dropoff latitude')
passenger_count = st.sidebar.number_input('Insert a passenger count', step=1)

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''

pickup_datetime = str(pickup_date) + " " + str(pickup_time)

data = {"pickup_datetime" : pickup_datetime,
    "pickup_longitude" : pickup_longitude,
    "pickup_latitude" : pickup_latitude,
    "dropoff_longitude" : dropoff_longitude,
    "dropoff_latitude" : dropoff_latitude,
    "passenger_count" : passenger_count}


url = f'https://taxifare.lewagon.ai/predict?pickup_datetime={pickup_datetime}&pickup_longitude={pickup_longitude}&pickup_latitude={pickup_latitude}&dropoff_longitude={dropoff_longitude}&dropoff_latitude={dropoff_latitude}1&passenger_count={passenger_count}'

response = requests.get(url)

prediction = round(response.json()['prediction'], 2)

st.markdown(f'The predict price is {prediction} dollars')

dict = {'lat': [pickup_latitude, dropoff_latitude],'lon': [pickup_longitude, dropoff_longitude]}

df = pd.DataFrame(dict)

st.map(df)