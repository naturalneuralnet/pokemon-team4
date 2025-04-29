import streamlit as st
from data_processing import load_and_clean_data
from input import get_image, get_input
from visualisation import display_details
import pandas as pd
# from app.data_processing import load_and_clean_data
# from app.filters import apply_filters
# from app.metrics_visuals import (
#     display_metrics,
#     display_visualizations,
# )


def main():
    """Main function to run the Streamlit app."""
    st.set_page_config(
        page_title="Titanic Dashboard",
        page_icon="🚢",
        layout="wide",
        initial_sidebar_state="auto",
    )
    # Set the title of the app
    st.title("Pokédex")

    # Load and clean the data
    df = load_and_clean_data("pokemon.csv")

    # get input and display pokemon name
    pokedex_numb = get_input()
    image_url = get_image(pokedex_numb)

    display_details(pokedex_numb, df, image_url)

    st.title("Pokémon Dataset")
    st.write("This dataset contains information about various Pokémon, including their types, abilities, and base stats.")
    st.dataframe(df)
    # # Apply filters
    # filtered_df = apply_filters(df)

    # # Display metrics
    # display_metrics(filtered_df)

    # # Display visualizations
    # display_visualizations(filtered_df)


if __name__ == "__main__":
    main()
