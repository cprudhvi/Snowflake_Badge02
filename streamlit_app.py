import streamlit
import pandas

streamlit.title('Test application - Healthy Diner')


#streamlit.header('Breakfast Menu')
#streamlit.text('Masala Dosa, Palli chutney')
#streamlit.text('Ugani, Bajji')
#streamlit.text('Chai, Coffee')

streamlit.header('Breakfast Menu')
streamlit.text(' 🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text(' 🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avovado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')

#adding multiselect feature so that the user can pick the fruit from the list.
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)


streamlit.header("Fruityvice Fruit Advice!")


fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/ + fruit_choice")
#streamlit.text(fruityvice_response.json()) #just writes the data to the screen


# making the json response data look good on screen by normalizing it !! 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# outputing the normalized data on to the streamlit app page !!
streamlit.dataframe(fruityvice_normalized)
