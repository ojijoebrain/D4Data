# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io
import matplotlib as mpl
import plotly.express as px


# Page Configuration
st.set_page_config(
    page_title="Data Driven Decisions Visualization App", # Title of the app
    layout="wide", # Wide layout for better use of space
    initial_sidebar_state="expanded", # Sidebar is expanded by default
)

# Disable the toolbar for all plots
mpl.rcParams['toolbar'] = 'none'


sns.set_style('darkgrid')


def load_data():
    """ Load the dataset and returns a dataframe"""
    df = pd.read_csv("data/clean_auto_mpg.csv")
    return df

# Select numeric columns for visualization
df = load_data()
int_columns = df.select_dtypes(['float64', 'float32', 'int32', 'int64']).columns



# Sidebar
st.sidebar.title("Menu")
options = st.sidebar.radio("Go to", ["Home", "Data Exploration", "Visualization",])

# Home Page
if options == "Home":
    st.title("Data Driven Decisions Visualization App")
    st.image("luke-chesser-JKUTrJ4vK00-unsplash.jpg", use_column_width=True)
    st.write("This app allows you to visualize data and make data-driven decisions.")
    
# File Uploader
st.sidebar.title("Upload Data")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = load_data(uploaded_file)
    int_columns = df.select_dtypes(['float64', 'float32', 'int32', 'int64']).columns
    
    # Data Exploration
elif options == "Data Exploration":
    st.title("Data Exploration")
    st.write("### Data Preview")
    st.dataframe(df.head())

    st.write("### Data Summary")
    st.write(df.describe())

    st.write("### Data Info")
    buffer = io.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)


# load dataset
df = load_data()
int_columns = df.select_dtypes(
    ['float64', 'float32', 'int32', 'int64']).columns

# checkbox and sidebar
checkbox = st.sidebar.checkbox('Display Data')
if checkbox:
    st.dataframe(data=df)

# Create Plots
# histogram plots
st.sidebar.subheader('Histogram')
uni_variate = st.sidebar.selectbox(label='Feature', options=int_columns)
option = [i for i in range(3, 100)]
bins = st.sidebar.selectbox(label='Bins', options=option)
fig, ax = plt.subplots()
sns.histplot(data=df, x=uni_variate, bins=bins, ax=ax)
st.pyplot(fig)

    
# scatter plots
st.sidebar.subheader('Scatter Plot')
xAxis = st.sidebar.selectbox(label='X axis', options=int_columns)
yAxis = st.sidebar.selectbox(label='Y axis', options=int_columns)

scatter = sns.relplot(x=xAxis, y=yAxis, data=df)
st.pyplot(scatter)

# Footer
st.markdown("[LinkedIn](https://www.linkedin.com/in/oji-joseph-oji-b41023168/)")
st.markdown("[X-Twitter](https://x.com/ojijoebrain)")
st.write("© 2024 oji joseph oji . All rights reserved.")  