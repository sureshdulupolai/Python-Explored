import streamlit as st

st.title("Hello Streamlit App")
st.subheader("Brewed with streamlit")
st.text("Welcome to your first interative app")
st.write("Choose your fav. variety of chai")

chai = st.selectbox(
    'your fav chai:', 
    ['Masala Chai', 'Lemon Tea', 'Adrak Chai', 'Kesar Chai']
)

st.write(f"Your Choose {chai}. Excellent Choise")
st.success("Your Chai Has Been Success")