import streamlit as st
import pandas as pd
import numpy as np
import joblib


#State Variables
dist_api_key = 'DemoOnly00DgssZhqQQdtOzNGg7AUs00FFUrPmeLyHHuit4lRMvyeEZsu7jiAhSd'

model = joblib.load

gross_model_dir = "./all_models/1000mi/v1/gross"
freight_model_dir = "./all_models/1000mi/v1/freight"
transformer_file = "./boxcox_transformers/transformer_1000mi_v1.joblib"



#UI Variables
pick_up_zip = st.text_input("Pickup ZIP Code")
delivery_zip = st.text_input("Delivery ZIP Code")
load_wgt = st.text_input(f"Load Weight (lbs)")
pick_up_zip = st.selectbox("Shipping type",("Drayage","Truckload"),index=None,placeholder="Choose Shipping Type...")

#Functions
def clear_form():
    st.pick_up_zip = st.empty()
    st.delivery_up_zip = st.empty()
    st.load_wgt = st.empty()
    st.button("Clear", on_click=clear_form)

clear_btn = st.button("Clear")

freight_charge = st.text_input("Freight charge")
total_charge = st.text_input("Total Charge")

sumbit_btn = st.button("Apply Quote")