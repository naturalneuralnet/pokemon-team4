import streamlit as st
from data_processing import load_and_clean_data
from input import get_image, get_input
from visualisation import display_details
from graphs import calculate_bmi, display_graph
import pandas as pd


def main():
    """Main function to run the Streamlit app."""
    st.set_page_config(
        page_title="Pokédex Dashboard",
        page_icon="⚡️",
        layout="wide",
        initial_sidebar_state="auto"
    )
    # Set the title of the app
    st.title("Pokédex")

    # Load and clean the data
    df = load_and_clean_data("./pokemon.csv")

    # get input and display pokemon name
    pokedex_numb = get_input()
    image_url = get_image(pokedex_numb)

    # display pokemon details
    display_details(pokedex_numb, df, image_url)

    # display graphs
    st.title("Comparing BMI and HP")
    df_bmi = calculate_bmi(df)
    display_graph(df=df_bmi)
    # display table
    st.title("Pokemon and their BMI:")
    st.write("The full dataset with the BMI calculated for each Pokemon.")
    st.dataframe(df_bmi)


if __name__ == "__main__":
    main()
