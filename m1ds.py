import streamlit as st
import pandas as pd

# Initialize session state to store data
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=['Name', 'Age', 'Email'])

st.title("User Registration Form")

# Streamlit form
with st.form("user_form"):
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, max_value=120, step=1)
    email = st.text_input("Email")
    tel = st.text_input("Tel")
    
    submitted = st.form_submit_button("Submit")
    
    if submitted:
        # Add the new row to the DataFrame
        new_data = pd.DataFrame([[name, age, email]], columns=['Name', 'Age', 'Email'])
        st.session_state.data = pd.concat([st.session_state.data, new_data], ignore_index=True)
        st.success("Data submitted successfully!")

# Display the updated DataFrame
st.subheader("Submitted Data")
st.dataframe(st.session_state.data)
