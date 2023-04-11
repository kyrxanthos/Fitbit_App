import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from pre_process_steps import get_dataframes

# Enable the dark theme
alt.themes.enable("dark")

# Define function for page 1
def page1():
    st.title("Steps")
    st.write("This is the first page of the app.")

    df, df_weekly = get_dataframes()

    line_chart = alt.Chart(df).mark_line().encode(
        x='dateTime:T',
        y='value:Q',
        tooltip=['dateTime:T', 'value:Q']
    ).properties(
        title='Line Chart of My Data'
    )

    bar_chart = alt.Chart(df).mark_bar().encode(
        x='dateTime:T',
        y='value:Q'
    ).properties(
        title='Bar Chart of My Data'
    )

    line_chart_week = alt.Chart(df_weekly).mark_line().encode(
        x='week:N',
        y='value:Q'
    ).properties(
        title='Line Chart of My Data (Aggregated by Week)'
    )

    st.altair_chart(line_chart, use_container_width=True)
    st.altair_chart(bar_chart, use_container_width=True)
    st.altair_chart(line_chart_week, use_container_width=True)

# Define function for page 2
def page2():
    st.title("Sleep")
    st.write("This is the second page of the app.")

    # Show some text
    st.write("Here's some text on page 2.")

    # Show an image
    st.image("https://streamlit.io/images/brand/streamlit-mark-color.png")

# Define function to switch between pages
def main():
    st.set_page_config(page_title="Simple Multipage App")
    pages = {
        "Steps": page1,
        "Sleep": page2
    }

    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(pages.keys()))

    page = pages[selection]
    page()

if __name__ == "__main__":
    main()
