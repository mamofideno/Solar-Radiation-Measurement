import streamlit as st
import pandas as pd
from utils import DataFrameLoader

st.set_page_config(
        page_title="Data set",
        layout="wide"
)

tab1, tab2, tab3 = st.tabs(["Bumbuna , Sierra Leon", "Dapaong  Togo", "Malanville , Benin "])

with tab1:
    st.header("Bumbuna , Sierra Leon Data set Data set")
    df=DataFrameLoader("data/sierraleone-bumbuna.csv").load()
    st.dataframe(df)
with tab2:
    st.header("Dapaong  Togo Data set")
    df=DataFrameLoader("data/togo-dapaong_qc.csv").load()
    st.dataframe(df)
with tab3:
    st.header("Malanville , Benin ")
    df=DataFrameLoader("data/togo-dapaong_qc.csv").load()
    df = pd.read_csv("data/benin-malanville.csv")
    st.dataframe(df)

st.markdown("""
    <style>
        .reportview-container {
            margin-top: -2em;
        }
        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""", unsafe_allow_html=True)   