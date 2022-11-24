import streamlit
import pandas as pd
import requests

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
my_fruit_list = my_fruit_list.set_index('Fruit')


# Let's put a pick list here so they can pick the fruit they want to include 

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])




fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page.


streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")


fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response.json())


# normalizes the above json output

fruityvice_normalized = pd.json_normalize(fruityvice_response.json())

# displays the normaized json output in a dataframe

streamlit.dataframe(fruityvice_normalized)
