import streamlit as st

st.title("📝 User Registration Form")

with st.form("user_form"):

    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    username = st.text_input("Username")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    age = st.number_input("Age", min_value=1, max_value=120)
    gender = st.selectbox(
        "Gender",
        ["Male", "Female", "Other"]
    )

    submitted = st.form_submit_button("Submit")

if submitted:
    st.success("Form Submitted Successfully!")

    st.subheader("User Details")

    st.write("**First Name:**", first_name)
    st.write("**Last Name:**", last_name)
    st.write("**Username:**", username)
    st.write("**Email:**", email)
    st.write("**Phone Number:**", phone)
    st.write("**Age:**", age)
    st.write("**Gender:**", gender)