import streamlit as st

st.text("This is the Title")
st.title("This is the Title")
st.header("This is the HEADER")
st.subheader("This is the SUBHEADER")
st.write("This is the WRITE SUPER FXN")
st.markdown("""This is THE *MARKDOWN* """)
st.latex("\int")
st.json(""" {
        "data":12
}""")
st.code(
""" 
    print("hello world")
    a = 40
"""
,language="python",line_numbers=True)


#Error Element
st.success("This was successful")
st.error("This is an error")
st.exception("TypeError")
st.warning("Warning")

# input Widget
First_name = st.text_input("FIRST NAME")
password = st.text_input("Password", type="password")
message = st.text_area("Message")
date = st.date_input("Date")
appointment_time = st.time_input("Appointment Time")
age = st.number_input("Age",min_value=0,max_value=120)
gender = st.radio("Gender",["Male","Female"])
enable = st.toggle("Enable Picker")
level = st.checkbox("Level")

# Sliders
countries = st.selectbox("Countries",["Ghana","USA","Germany","Spain","Italy"])