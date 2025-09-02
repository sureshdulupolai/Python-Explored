import streamlit as st
import requests

st.title("Live Currency Converter")
amount = st.number_input("Enter The Amount in INR: ", min_value=1)
target_currency = st.selectbox("Conver to: ", ['USD', 'EUR', 'GBP', 'JPY'])

if st.button("Convert"):
    url = "https://api.exchangerate-api.com/v4/latest/INR"
    respone = requests.get(url)
    if respone.status_code == 200:
        data = respone.json()
        rate = data['rates'][target_currency]
        converted = rate * amount
        st.success(f"{amount} INR = {converted:.2f} {target_currency}")
    else:
        st.error("Failed to fetch conversion rate")