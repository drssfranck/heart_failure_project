import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

# Permet d'importer src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.utils import load_data

data = load_data("data/heart.csv")

def display_column_distribution(column):
    fig, ax = plt.subplots(figsize=(4, 3))
    if column == "Age":
        st.subheader("Distribution de l'âge")
        # Utilisation de Seaborn pour un rendu plus moderne
        import seaborn as sns
        sns.histplot(data["Age"], bins=15, kde=True, ax=ax, color='skyblue')
        ax.set_xlabel("Âge")
        ax.set_ylabel("Nombre de patients")
        st.pyplot(fig)

    elif column == "Sex":
        st.subheader("Distribution du sexe")
        sex_count = data["Sex"].value_counts()
        labels = sex_count.index.map({'F': "Femme", 'M': "Homme"})
        ax.pie(sex_count, labels=labels, autopct="%1.1f%%", startangle=90)
        st.pyplot(fig)
    elif column in [
        "ChestPainType",
        "RestingECG",
        "ExerciseAngina",
        "ST_Slope",
        "HeartDisease"
    ]:
        st.subheader(f"Distribution de {column}")
        data[column].value_counts().plot(kind="bar", ax=ax)
        st.pyplot(fig)

    elif column in [
        "RestingBP",
        "Cholesterol",
        "MaxHR",
        "Oldpeak"
    ]:
        st.subheader(f"Distribution de {column}")
        ax.hist(data[column], bins=20)
        st.pyplot(fig)
