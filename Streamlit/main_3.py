import streamlit as st

st.title("Chai Taste Poll")

# Create 2 Column
col1, col2 = st.columns(2)

with col1:
    st.header("Masala Chai")
    # st.image("https://www.thespicehouse.com/cdn/shop/articles/Chai_Masala_Tea_1200x1200.jpg?v=1606936195", width=100)
    # st.image(
    # "https://www.thespicehouse.com/cdn/shop/articles/Chai_Masala_Tea_1200x1200.jpg?v=1606936195", 
    # use_column_width=True
    # )

    st.markdown(
    """
    <img src="https://www.thespicehouse.com/cdn/shop/articles/Chai_Masala_Tea_1200x1200.jpg?v=1606936195" width="200" height="150">
    """,
    unsafe_allow_html=True
    )

    vote1 = st.button("Vote Masala Chai")

with col2:
    st.header("Adrak Chai")
    # st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSpBYuPv4s8IannX9AIfAQQ6DUIW6Venc7HYg&s", width=100)
    st.markdown(
    """
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSpBYuPv4s8IannX9AIfAQQ6DUIW6Venc7HYg&s" width="200" height="150">
    """,
    unsafe_allow_html=True
    )
    vote2 = st.button("Vote Adrak Chai")

if vote1:
    st.success("Thanks For Voting Masala Chai")
elif vote2:
    st.success("Thanks For Voting Adrak Chai")

name = st.sidebar.text_input("Enter Your Name: ")
tea = st.sidebar.selectbox("Choose Your Chai", ['Choose-Chai', 'Masala', 'Kesar', 'Adrak'])

if name:
    st.sidebar.write(f"Your Name : {name}")
if tea != 'Choose-Chai':
    st.sidebar.write(f"Select Chai : {tea}")


with st.expander("Show Chai Making Instruction"):
    st.write("""
    1. Boil Water With Tea Leaves
    2. Add Milk and Spices
    3. Serve Hot
""")
    

st.markdown("### Welcome to Chai App")
st.markdown("# Welcome to Chai App With Big Letter")
st.markdown("> Blockquote")