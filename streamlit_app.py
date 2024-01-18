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
#adding multiselect feature so that the user can pick the fruit from the list.
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

streamlit.dataframe(my_fruit_list)
