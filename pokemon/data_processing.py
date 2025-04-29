import streamlit as st
import pandas as pd


file_path = "./pokemon.csv"


def load_data(filepath):
    """Load the Titanic dataset from a CSV file."""
    return pd.read_csv(filepath)


def clean_numerical_columns(df):
    """Clean numerical columns by filling missing values."""
    df["base_friendship"] = df["base_friendship"].fillna(
        df["base_friendship"].mode()[0])
    df["base_experience"] = df["base_experience"].fillna(
        df["base_experience"].mode()[0])
    df["percentage_male"] = df["percentage_male"].fillna(
        df["percentage_male"].mode()[0])
    return df


def clean_categorical_columns(df):
    """Clean categorical columns by filling missing values."""
    df["ability_2"] = df["ability_2"].fillna("None")
    df["ability_hidden"] = df["ability_hidden"].fillna("None")
    return df


def drop_unnecessary_columns(df):
    """Drop unnecessary columns and duplicates."""
    df.drop(columns=["egg_type_number"], inplace=True)
    df.drop(columns=["german_name"], inplace=True)
    df.drop(columns=["japanese_name"], inplace=True)
    df.drop(columns=["egg_cycles"], inplace=True)
    df.drop_duplicates(inplace=True)
    return df


def load_and_clean_data(filepath):
    """Load and clean the Pokemon dataset."""
    df = load_data(filepath)
    df = clean_numerical_columns(df)
    df = clean_categorical_columns(df)
    df = drop_unnecessary_columns(df)
    return df
