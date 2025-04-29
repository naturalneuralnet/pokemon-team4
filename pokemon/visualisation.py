import streamlit as st
from input import get_image


# display details
def display_details(pokedex_numb, df, image_url):
    df_row = df[['name', 'height_m', 'weight_kg']
                ].loc[df["pokedex_number"] == int(pokedex_numb)]

    st.subheader("Pokemon Details")
    for i in range(len(df_row)):
        height = df_row['height_m'].values[i]
        name = df_row['name'].values[i]
        weight = df_row['weight_kg'].values[i]

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.image(image=image_url)

        with col2:
            st.metric(
                label="Name", value=name)

        with col3:
            st.metric(label="Weight", value=weight)

        with col4:
            st.metric(label="Height", value=height)

    st.subheader("Pokemon Full Details")
    df_full_row = df.loc[df["pokedex_number"] == int(pokedex_numb)]
    st.write(df_full_row)
