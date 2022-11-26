import streamlit
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

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

##streamlit.header("Fruityvice Fruit Advice!")

##fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
##streamlit.write('The user entered: ', fruit_choice)


##fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text(fruityvice_response.json())


# normalizes the above json output

##fruityvice_normalized = pd.json_normalize(fruityvice_response.json())

# displays the normaized json output in a dataframe

##streamlit.dataframe(fruityvice_normalized)

def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
#New Section to display fruityvice api response 

streamlit.header ('Fruityvice Fruit Advice!')

try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()
  


#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#my_cur.execute("SELECT * FROM fruit_load_list")
#my_data_row = my_cur.fetchone()

#my_data_row = my_cur.fetchall()

#streamlit.text("Hello from Snowflake:")
streamlit.header("The fruit load list contains:")
#snowflake related functions
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("SELECT * FROM fruit_load_list")
        return my_cur.fetchall()
#add a button to show fruit list
if streamlit.button('Get fruit load list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    streamlit.dataframe(my_data_rows)

# Allow the end user to add a fruit to the list
def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        #my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('from streamlit')")
        my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('"+new_fruit+"')")
        return "Thanks for adding " + new_fruit
    
add_my_fruit = streamlit.text_input('What fruit would you like to add')
if streamlit.button('Add a fruit to the list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function = insert_row_snowflake(add_my_fruit)
    streamlit.text(back_from_function)
#streamlit.write('Thanks for adding', add_my_fruit)

streamlit.stop()

my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('from streamlit')")
