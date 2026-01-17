import sys
from pathlib import Path

# Ajoute le dossier racine (HEART_PROJECT) au chemin de recherche de Python
root_path = Path(__file__).resolve().parent.parent
if str(root_path) not in sys.path:
    sys.path.append(str(root_path))

import streamlit as st
import  pandas as pd
from src.utils import load_data
import matplotlib.pyplot as plt

# Load data
df = load_data('data/heart.csv')
st.set_page_config(page_title="Exploratory Data Analysis", layout="wide")
tab1, tab2, tab3 = st.tabs(["Données", "Overview", "Statistiques"])

with tab2:
    st.title("Overview")
    st.subheader("Aperçu des données")
    st.write(df.describe())

    
    

with tab3:
    st.title("Données")
    st.subheader("Visualisation des données")

with tab1:
    st.title("Exploratory Data Analysis (EDA)")
    st.dataframe(df.head())
    # Diagramme en barres
    #distributions des âges
    var = st.selectbox("Sélectionnez une variable pour le diagramme en barres", df.columns)
    