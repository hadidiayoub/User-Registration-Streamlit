import streamlit as st


#this is a User Registration form
st.markdown("<h1>User Registration</h1>",unsafe_allow_html=True)
with st.form("Form 2", clear_on_submit=True):
    col1,col2=st.columns(2)
    f_name=col1.text_input("First Name")
    l_name=col2.text_input("Last Name")
    st.text_input("Email Address")
    st.text_input("Password")
    st.text_input("Confirm Password")
    day,month,year=st.columns(3)
    day.text_input("Day")
    month.text_input("month")
    year.text_input("year")
    s_state=st.form_submit_button("Register")
    if s_state:
        if f_name == "" and l_name=="":
            st.warning("Please Fill above fields")
        else:
            st.success("Submitted Successfully")
