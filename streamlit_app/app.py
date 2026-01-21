import sys
from pathlib import Path

root_path = Path(__file__).resolve().parent.parent
if str(root_path) not in sys.path:
    sys.path.append(str(root_path))

import streamlit as st
import  pandas as pd
import matplotlib.pyplot as plt

from src.utils import load_data
from src.eda import *

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
    st.write(df.info())
with tab1:
    st.title("Exploratory Data Analysis (EDA)")
    st.dataframe(df.head())
    # Diagramme en barres
    #distributions des âges
    st.write("### Distribution des données")
    cols = st.columns(3)
    for i, col in enumerate(df.columns):
        with cols[i % 3]:
            display_column_distribution(col)

