import streamlit as st

#UI Variables
pick_up_zip = st.text_input("Pickup ZIP Code")
delivery_up_zip = st.text_input("Delivery ZIP Code")
load_wgt = st.text_input(f"Load Weight (lbs)")
pick_up_zip = st.selectbox("Shipping type",("Drayage","Truckload"),index=None,placeholder="Choose Shipping Type...")

