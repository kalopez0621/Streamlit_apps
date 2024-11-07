import streamlit as st

# Title
st.title('My First Streamlit App')

# Select Box
options = ["Option 1", "Option 2", "Option 3"]
selection = st.selectbox("Choose an option:", options)
st.write("You selected:", selection)

# Button
if st.button("Click Me"):
    st.write("Button was clicked!")

