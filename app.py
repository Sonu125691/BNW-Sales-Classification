import pickle
import streamlit as st
import pandas as pd


with open("final_encoder.pkl", "rb") as file:
    encoder = pickle.load(file)
with open("final_scaler.pkl", "rb") as file:
    scaler = pickle.load(file)
with open("final_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("BMW Car Sales Prediction (2010 - 2024)")
         
st.write(""" This app is for predicting BMW car sales class prediction from 2010 - 2024.
         This app will predict the sales classification as "High" or "Low"
         """)


car_model = st.selectbox("Model", ['5 Series', 'i8', 'X3', '7 Series', 'M5', '3 Series', 'X1', 'M3',
       'X5', 'i3', 'X6'])
year = st.selectbox("Year", [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024])
region = st.selectbox("Region", ['Asia', 'North America', 'Middle East', 'South America', 'Europe',
       'Africa'])
color = st.selectbox("Color", ['Red', 'Blue', 'Black', 'Silver', 'White', 'Grey'])
fuel_type = st.selectbox("Fuel Type", ['Petrol', 'Hybrid', 'Diesel', 'Electric'])
transmission = st.radio("Transmission", ['Manual', 'Automatic'])
engine_size = st.number_input("Engine Size in Litre", 1.0, 10.0, 1.0, format = "%.1f")
milage = st.number_input("Mileage in KM", 0, 1000000, 50000)
price = st.number_input("Price in USD", 10000, 1000000, 50000)
volume = st.number_input("Sales Volume", 0, 1000000, 1000)

user_input = {'Model': car_model,
              'Year': year,
              'Region': region,
              'Color': color,
              'Fuel_Type': fuel_type, 
              'Transmission': transmission,
              'Engine_Size_L': engine_size,
              'Mileage_KM': milage, 
              'Price_USD': price,
              'Sales_Volume': volume
}

user_df = pd.DataFrame([user_input])


if st.button("Predict"):
    
    user_df_encoded = encoder.transform(user_df[["Model","Region","Color","Fuel_Type","Transmission"]])
    user_df_encoded = pd.DataFrame(user_df_encoded, columns = encoder.get_feature_names_out(["Model","Region","Color","Fuel_Type","Transmission"]))
    user_df = user_df.drop(columns = ["Model","Region","Color","Fuel_Type","Transmission"])
    user_df_final = pd.concat([user_df,user_df_encoded], axis = 1)

    scaled = scaler.transform(user_df_final)

    prediction = model.predict(scaled)

    if prediction[0] == 1:
        st.info("Predicted Sales Classification: HIGH 🚀")
    else:
        st.info("Predicted Sales Classification: LOW 📉")