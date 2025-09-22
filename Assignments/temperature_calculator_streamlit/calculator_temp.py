import streamlit as st

st.title("Fahad Calculte temperature")

temp=st.text_input('Enter temperature')
st.write(f'your provided temp: {temp}')
# temp=float(temp)
# print(type(temp))
# print(temp)

selected_form=st.radio('K/F/C')