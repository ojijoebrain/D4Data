import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Dashboard 4 Data')
sns.set_style('darkgrid')


def load_data(path):
    """ Load the dataset and returns a dataframe"""
    df = pd.read_csv(path)
    return df


# load dataset
df = load_data('clean_auto_mpg.csv')
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
