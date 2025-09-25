import streamlit as st

# Title
st.title(" Fahad Temperature Calculator")

# Step 1: Enter temperature value
temp_value = st.number_input("Enter Temperature:", step=0.1)

# Step 2: Select "Convert From" unit
convert_from = st.radio("Convert From:", ("Kelvin (K)", "Fahrenheit (F)", "Celsius (C)"))

# Step 3: Select "Convert To" unit
convert_to = st.radio("Convert To:", ("Kelvin (K)", "Fahrenheit (F)", "Celsius (C)"))


# Function to handle conversion
def convert_temperature(value, from_unit, to_unit):
    # First, convert everything to Celsius
    if from_unit == "Celsius (C)":
        celsius = value
    elif from_unit == "Kelvin (K)":
        celsius = value - 273.15
    elif from_unit == "Fahrenheit (F)":
        celsius = (value - 32) * 5 / 9
    else:
        return None

    # Then convert Celsius to target unit
    if to_unit == "Celsius (C)":
        return celsius
    elif to_unit == "Kelvin (K)":
        return celsius + 273.15
    elif to_unit == "Fahrenheit (F)":
        return (celsius * 9 / 5) + 32
    else:
        return None


# Step 4: Convert button
if st.button("Convert Temperature"):
    if convert_from == convert_to:
        st.warning(" 'Convert From' and 'Convert To' units are the same. Please select different units.")
    else:
        converted_value = convert_temperature(temp_value, convert_from, convert_to)

        # Display result in success box
        st.success(
            f"**{convert_from}:** {temp_value:.2f}\n\n"
            f"**{convert_to}:** {converted_value:.2f}"
        )
