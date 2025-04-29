import plotly.express as px
import streamlit as st

# transform height and weight


def calculate_bmi(df):
    hsquared = (df["height_m"] ** 2)
    bmi = (df["weight_kg"]) / hsquared
    df['bmi'] = bmi
    return df


def display_graph(df):
    fig = px.scatter(
        df,
        x='bmi',
        y='hp',
        color='bmi',
        title='Original BMI vs HP Scatter Plot'
    )
    st.write(fig)

    df_normal = df.drop(index=923)
    fig2 = px.scatter(
        df_normal,
        x='bmi',
        y='hp',
        color='bmi',
        title='Normalised BMI vs HP Scatter Plot'
    )
    st.write(fig2)
