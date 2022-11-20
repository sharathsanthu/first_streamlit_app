import streamlit
import pandas as pd

streamlit.title("My Parents New Healthy Diner")

streamlit.header("Breakfast Menu")

streamlit.text("Aloo Paratha")

streamlit.text("Gobi Paratha")

streamlit.text("🍲 Idly & Coconut Chutney")

streamlit.text("Idly & Sambar")

streamlit.text("Roti & Aloo Bhujiya")

streamlit.text("Dosa & Peanut Chutney")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Select fruits:", list(my_fruit_list.fruit))

# Display the table on the page.

streamlit.dataframe(my_fruit_list)


