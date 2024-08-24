import streamlit as st
#config 
import os 
import sys
root_path = os.path.abspath('..')
if root_path not in sys.path:
    sys.path.insert(0, root_path)
script_path=os.path.abspath(os.path.join('..', 'app'))
if script_path not in sys.path:
    sys.path.append(script_path)
st.set_page_config(
    page_title="Solar Radiation Measurement Data",
    # page_icon=''
    layout="wide"
)
st.header("Solar Radiation Measurement Data")
st.subheader("Introduction")
st.markdown("The purpose of this report is to explore and understand the Solar Radiation Measurement dataset of one year observation from two cities and one town from different West African countries: Bumbuna town from northern Sierra Leone, Dapaong city in northern Togo and Malanville city in northern Benin. The dataset consists of various parameters that influence solar radiation, and through this analysis, I aim to gain insights into the data distribution, relationships between variables, and potential trends.")
st.subheader("Data Overview")
st.markdown("The dataset contains measurements of solar radiation along with the following meteorological parameters ")
st.write("•  Timestamp (yyyy-mm-dd hh:mm): Date and time of each observation.")
st.write("•	GHI (W/m²): Global Horizontal Irradiance, the total solar radiation received per square meter on a horizontal surface.")
st.write("•	DNI (W/m²): Direct Normal Irradiance, the amount of solar radiation received per square meter on a surface perpendicular to the rays of the sun.")
st.write("•	DHI (W/m²): Diffuse Horizontal Irradiance, solar radiation received per square meter on a horizontal surface that does not arrive on a direct path from the sun.")
st.write("•	ModA (W/m²): Measurements from a module or sensor (A), similar to irradiance.")
st.write("•	ModB (W/m²): Measurements from a module or sensor (B), similar to irradiance.")
st.write("•	Tamb (°C): Ambient Temperature in degrees Celsius.")
st.write("•	RH (%): Relative Humidity as a percentage of moisture in the air.")
st.write("•	WS (m/s): Wind Speed in meters per second.")
st.write("•	WSgust (m/s): Maximum Wind Gust Speed in meters per second.")
st.write("•	WSstdev (m/s): Standard Deviation of Wind Speed, indicating variability.")
st.write("•	WD (°N (to east)): Wind Direction in degrees from north.")
st.write("•	WDstdev: Standard Deviation of Wind Direction, showing directional variability.")
st.write("•	BP (hPa): Barometric Pressure in hectopascals.")
st.write("•	Cleaning (1 or 0): Signifying whether cleaning (possibly of the modules or sensors) occurred.")
st.write("•	Precipitation (mm/min): Precipitation rate measured in millimeters per minute.")
st.write("•	TModA (°C): Temperature of Module A in degrees Celsius.")
st.write("•	TModB (°C): Temperature of Module B in degrees Celsius")

st.subheader("Data cleaning")

st.write("There is no missing values except that of comments which has no impact on measurements.  ")
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
