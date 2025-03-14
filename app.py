import streamlit as st
import requests
from datetime import datetime
import pandas as pd

st.title('TaxiFareModel front')

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

# Here we would like to add some controllers in order to ask the user to select the parameters of the ride
date_time = st.date_input("Date and Time", datetime.now())
pickup_longitude = st.number_input("Pickup Longitude", value=-73.98)
pickup_latitude = st.number_input("Pickup Latitude", value=40.75)
dropoff_longitude = st.number_input("Dropoff Longitude", value=-73.98)
dropoff_latitude = st.number_input("Dropoff Latitude", value=40.75)
passenger_count = st.number_input("Passenger Count", min_value=1, max_value=8, value=1, step=1)

# API call
if st.button('Get Prediction'):
    url = 'https://taxifare.lewagon.ai/predict'  # Replace with your API URL if available

    params = {
        "pickup_datetime": date_time.isoformat(),
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        prediction = response.json()['fare']
        st.success(f"The predicted fare is ${prediction:.2f}")
    else:
        st.error("Failed to get prediction from the API")

# Add a map
st.subheader("Ride Map")
df = pd.DataFrame({
    'lat': [pickup_latitude, dropoff_latitude],
    'lon': [pickup_longitude, dropoff_longitude]
})
st.map(df)
