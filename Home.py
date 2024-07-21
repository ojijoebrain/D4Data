import streamlit as st

st.set_page_config(
    page_title='My Portfolio'
)

st.sidebar.success('Menu')
st.title('D4D')
st.header('Dashboard For Data Driven Decisions')
st.image("luke-chesser-JKUTrJ4vK00-unsplash.jpg", use_column_width=True)

st.write("""This project was inspired by my facination for the Data 
         and AI field.""")

st.image('feature.PNG')
st.write(""" This is the sidebar for the visualization app created
         with streamlit displaying a Histogram with a dropdown to select
         the feature to visualize and the number of bins for the plot""")

st.markdown("**Connect With Me**")

st.markdown("[LinkedIn](https://www.linkedin.com/in/oji-joseph-oji-b41023168/)")

st.markdown("[X-Twitter](https://x.com/ojijoebrain)")

st.markdown("[Github](https://github.com/ojijoebrain)")

st.write("© 2024 oji joseph oji All rights reserved.")