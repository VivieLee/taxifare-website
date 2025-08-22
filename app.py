import streamlit as st
import datetime
import requests

st.markdown('## Get a taxi fare quote')

# Selects today's date by default
pickup_date = st.date_input("Select Pickup Date", datetime.date.today())

# Selects current time by default
pickup_time = st.time_input("Select Pickup Time", datetime.datetime.now().time())

pickup_datetime = datetime.datetime.combine(pickup_date, pickup_time)

pickup_datetime_str = pickup_datetime.strftime("%Y-%m-%d %H:%M:%S.%f")[:-4]

st.write("Your pickup datetime is:", pickup_datetime)

# Sets the other params to default values
pickup_longitude = st.number_input("Pickup Longitude", value=-73.985428)
pickup_latitude = st.number_input("Pickup Latitude", value=40.748817)
dropoff_longitude = st.number_input("Dropoff Longitude", value=-73.985428)
dropoff_latitude = st.number_input("Dropoff Latitude", value=40.748817)
passenger_count = st.number_input("Passenger Count", value=1)

params = {
    "pickup_datetime": pickup_datetime_str,
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count
}

# Call API
url = "https://taxifare-new-428752380854.asia-east1.run.app/predict"
res = requests.get(url=url, params=params).json()


# Show the prediction
if isinstance(res, dict) and "fare" in res:
    prediction = res["fare"]
    st.markdown(f"# Your taxi fare is: ${prediction:.2f}")
else:
    st.error("Could not retrieve 'fare' from API. Check the response above.")
    
