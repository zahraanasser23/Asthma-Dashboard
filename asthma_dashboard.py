# -*- coding: utf-8 -*-
"""Asthma_Dashboard.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12tmTccbaNgt7Sn5EqmBuXDZtutyCUYDi
"""

import streamlit as st
import pandas as pd
import plotly.express as px

# Function to load data set
def load_data(file):
    df = pd.read_csv(file)
    return df

# Function to plot bar chart
def plot_bar_chart(df, column):
    fig = px.bar(df, x=column)
    st.plotly_chart(fig)

# Function to plot scatter plot
def plot_scatter_plot(df, x_column, y_column):
    fig = px.scatter(df, x=x_column, y=y_column, color='Asthma', color_continuous_scale='RdBu')
    st.plotly_chart(fig)

# Set the app title
st.title("Asthma Data Set Dashboard")

# Create file uploader for each data set
file_1 = st.file_uploader("asthma-deaths-by-county-1.csv", type="csv")
file_2 = st.file_uploader("asthma-prevalence-2.csv", type="csv")
file_3 = st.file_uploader("asthma-ed-visit-rates-lghc-indicator-07-.csv", type="csv")

# Load and process the selected data sets
if st.button("Load Data Set"):
    if file_1 and file_2 and file_3:
        st.write("Loading data sets...")
        df_1 = load_data(file_1)
        df_2 = load_data(file_2)
        df_3 = load_data(file_3)
        st.write("Data sets loaded successfully!")

        # Display the data sets
        st.subheader("Data Set 1")
        st.dataframe(df_1)

        st.subheader("Data Set 2")
        st.dataframe(df_2)

        st.subheader("Data Set 3")
        st.dataframe(df_3)

        # Process and visualize the data sets as desired
        # Add your code here for data analysis and visualization using pandas, plotly, and streamlit
        # For example, you can call the plot_bar_chart and plot_scatter_plot functions on the loaded data sets

