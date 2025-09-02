import streamlit as st

st.title("Chai Maker App")

if st.button("Make Chai"):
    st.success("Your Chai is being Brewed")

add_masala = st.checkbox("Add Masala")
if add_masala:
    st.success('Masala Added to Chai')

tea_type = st.radio("Pick Your Chai base: ", ['Milk', 'Water', 'Honey'])
st.write(f"Selected : {tea_type}")

flavour = st.selectbox("Choose flavour: ", ['Adrak', 'Kesar', 'Tulsi'])
st.write(f'Selected Flavour: {flavour}')

sugar = st.slider("Sugar Level (Spoon)", 0, 5, 2)
st.write(f'Selected Sugar Level is : {sugar}')

cups = st.number_input("How many cups", min_value=1, max_value=10, step=1)
st.write(f'Selected Cups : {cups}')


name = st.text_input("Enter your name")
if name:
    st.write(f"Welcome, {name} ! Your Chai is on the way...")

dob = st.date_input("Select Your Date Of Birth")
if dob:
    st.write(f"Your Date of Birth is : {dob}")