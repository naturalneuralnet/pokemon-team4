import streamlit as st
import requests
import pandas as pd


def get_input():
    pokemon_num = st.text_input("Enter a pokedex number:", "1")
    st.write("You gave this pokemon number:", pokemon_num)
    return pokemon_num


def get_image(pokemon_num):
    res = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_num}")
    res_json = res.json()
    image_url = res_json['sprites']['front_default']

    return (image_url)
