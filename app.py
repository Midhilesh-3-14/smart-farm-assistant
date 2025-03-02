import streamlit as st
import requests

# Configuration
api_key = "1163515f43c8c06d7c2d6530ed8e71e8"  # Replace with your API key from openweathermap.org
location = "London"  # Replace with your city

st.title("AI-Powered Smart Farm Assistant")

# Weather Section
st.header("Weather Forecast")
try:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    st.write(f"Temperature: {data['main']['temp']}°C")
    st.write(f"Humidity: {data['main']['humidity']}%")
    st.write(f"Conditions: {data['weather'][0]['description']}")
except:
    st.write("Weather data unavailable (please add a valid API key)")

# Inventory Section
st.header("Inventory Management")
item = st.text_input("Enter item name")
quantity = st.number_input("Quantity", min_value=0)
if st.button("Add Item"):
    st.write(f"Added: {item} - {quantity} units")

# Crop Health Placeholder
st.header("Crop Health")
st.write("Upload an image (feature not fully implemented yet)")
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "png"])
if uploaded_file:
    st.write("Image uploaded (processing not available in this version)")