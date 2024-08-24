import streamlit as st
import pandas as pd
from utils import *

st.set_page_config(
        page_title="Data set",
        layout="wide"
)

tab1, tab2, tab3 = st.tabs(["Bumbuna , Sierra Leon", "Dapaong  Togo", "Malanville , Benin "])

with tab1:
    st.header("Bumbuna , Sierra Leon EDA")
    df=DataFrameLoader("../data/sierraleone-bumbuna.csv").load().describe()
    st.dataframe(df)
with tab2:
    st.header("Dapaong  Togo Data EDA")
    df=DataFrameLoader("../data/togo-dapaong_qc.csv").load().describe()
    st.dataframe(df)
with tab3:
    st.header("Malanville , Benin EDA")
    df=DataFrameLoader("../data/togo-dapaong_qc.csv").load().describe()
    st.dataframe(df)
    HistogramVisualizer(df).plot_histogram()
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