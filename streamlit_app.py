import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Parents New Healthy Diner')


streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

streamlit.title('Build Your Own Fruit Smoothie')

#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
#streamlit.dataframe(my_fruit_list)

# This line to show selection of fruits from the table
streamlit.dataframe(fruits_to_show)

################# comment the line below and use the if else statement ################
# This section to display fruityvice response
#streamlit.header("Fruityvice Fruit Advice!")

#import requests
##fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
##streamlit.text(fruityvice_response.json()) # this line just writes data on the screen
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")

# take json version of the response and normalize it 

#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it as a table
##streamlit.dataframe(fruityvice_normalized)
#
###### this is from exercise lesson 9 last part ####

##fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
##streamlit.write('The user entered ', fruit_choice)

#import requests
##fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
##streamlit.text(fruityvice_response.json()) # this line just writes data on the screen
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# take json version of the response and normalize it 
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it as a table
#streamlit.dataframe(fruityvice_normalized)

############## comment the line above and using the if else statement ###########

#create the repeatable code block (called a function)
def get_fruitvice_data(this_fruit_choice):
      fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
      fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
      return fruityvice_normalized
  
# New section to display fruityvice response
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
#    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#    streamlit.dataframe(fruityvice_normalized)  
    back_from_function = get_fruitvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)    

except URLError as e:
  streamlit.error()
  
#adding stop function for debugging frm this line onwards
#streamlit.stop()

# This section to display snowflake connector
#streamlit.header("chapter 12 from the training material adding snowflake connector")
#import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("chapter 12 from the training material adding snowflake connector")
#streamlit.text("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

#
###### this is from exercise lesson 12 streamlit challenge ####

add_my_fruit = streamlit.text_input('What fruit would you like to add?','jackfruit')
streamlit.write('Thanks for adding ', add_my_fruit)

#this will not work correctly, but just go with it for now
my_cur.execute("insert into fruit_load_list values ('from streamlit')")
