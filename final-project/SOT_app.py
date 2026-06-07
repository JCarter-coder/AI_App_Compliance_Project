import streamlit as st

from SOT_db import get_rank, get_TSC, get_workcenter, get_personnel

st.set_page_config(
  page_title="Database-Backed AI Application",
  page_icon="🗄️",
  layout="wide"
)

st.title("Status of Training App")

st.write(
  """
  This Streamlit application is now reading data from a local SQLite database.
  Iterations will be expanded to support this application. 
  """
)

try:
  st.subheader("Personnel")
  items = get_personnel()
  st.dataframe(items, use_container_width=True)

  st.subheader("Enlisted Ranks")
  items = get_rank()
  st.dataframe(items, use_container_width=True)

  st.subheader("Training Status Codes")
  items = get_TSC()
  st.dataframe(items, use_container_width=True)

  st.subheader("Work Centers")
  items = get_workcenter()
  st.dataframe(items, use_container_width=True)

except Exception as error:
  st.error("The application could not load database records.")
  st.exception(error)
