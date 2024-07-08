import streamlit as sl

sl.set_page_config(
    page_title='My Portfolio'
)

sl.sidebar.success('MENU')
sl.title('D4D')
sl.header('Dashboard For Data Driven Decisions')
sl.image("luke-chesser-JKUTrJ4vK00-unsplash.jpg", use_column_width=True)

sl.write("""This project was inspired by my facination for the Data 
         and AI field.""")

sl.image('feature.PNG')
sl.write(""" This is the sidebar for the visualization app created
         with streamlit displaying a Histogram with a dropdown to select
         the feature to visualize and the number of bins for the plot""")

sl.markdown("**Connect With Me**")

sl.markdown("[LinkedIn](https://www.linkedin.com/in/oji-joseph-oji-b41023168/)")

sl.markdown("[X-Twitter](https://x.com/ojijoebrain)")

sl.markdown("[Github](https://github.com/ojijoebrain)")

sl.write("© 2024 oji joseph oji All rights reserved.")