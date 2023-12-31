import streamlit

 

streamlit.header('My Moms New Healthy Diner')
streamlit.title('Breakfast Favorites')
streamlit.text('🥣 Omega 3 and Blueberry Oatmeal')
streamlit.text('🥗 Kale,Spinach and Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

 

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

 

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

 

# Display the table on the page.
streamlit.dataframe(my_fruit_list)

 

 

streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

 

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+"kiwi")

 

 

#Take the json version of the response and normalise it 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# Output it  the screen as a table
streamlit.dataframe(fruityvice_normalized)


