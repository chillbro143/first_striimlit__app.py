import streamlit
import pandas
streamlit.title("🥗 My parents new healthy diner 🐔 ")
streamlit.header('breakfast menu')
streamlit.text('omega 3 and Blueberry ooatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
