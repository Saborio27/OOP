import streamlit as streamlit
#create my resume

st.tittle("Andres Saborio")
st.header("Student, CS")

st.markdown("About me")
st.text("I am a student at JBU")
st.diviser()

st.markdown("Qualifications")
st.text("I am currently in OOP class")
st.text("I am in Network Security class")
st.diviser()

st.markdown("Work Experience")
st.text("I am a cafeteria worker at JBU")
st.text("I worked at landscaping")

st.markdown("Contact me")
userName = st.text_input("Your Name: Andres Saborio")
userPhone = st.text_input("Phone Number: 828-590-7369")
userEmailId = st.text_input("Email Address: saborioruia@jbu.edu")
st.button("Send message")




