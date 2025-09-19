import streamlit as st

st.title("My First Streamlit App")

name = st.text_input("Enter your name:")

if name:
    st.write(f"Hello, {name}!")

age = st.slider("Select your age:", 0, 100, 25)
st.write(f"You are {age} years old.")

if st.button("Click me!"):
    st.success("Button clicked!")