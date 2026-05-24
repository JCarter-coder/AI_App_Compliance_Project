import streamlit as st

from db import get_sample_items

st.set_page_config(
  page_title="Database-Backed AI Application",
  page_icon="🗄️",
  layout="wide"
)

st.title("Final Project Starter App")

st.write(
  """
  This Streamlit application is now reading data from a local SQLite database.
  Later in the course, this pattern will be expanded to support your final project. 
  """
)

st.subheader("Database Records")

try:
  items = get_sample_items()
  st.dataframe(items, use_container_width=True)

except Exception as error:
  st.error("The application could not load database records.")
  st.exception(error)
