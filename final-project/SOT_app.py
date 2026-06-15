import streamlit as st

from SOT_db import (
  get_rank, 
  get_TSC, 
  get_workcenter, 
  get_personnel, 
  get_training_status_by_WC, 
  get_MTP,
  get_MTL_by_WC,
  get_ITP_by_DOD_id,
  get_CDC_by_DOD_id,
  get_overdue_cdcs
)

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
  st.subheader("Enlisted Ranks")
  items = get_rank()
  st.dataframe(items, use_container_width=True)

  st.subheader("Work Centers")
  items = get_workcenter()
  st.dataframe(items, use_container_width=True)

  st.subheader("Training Status Codes")
  items = get_TSC()
  st.dataframe(items, use_container_width=True)

  st.subheader("Personnel")
  items = get_personnel()
  st.dataframe(items, use_container_width=True)

  st.subheader("Master Training Plans")
  items = get_MTP()
  st.dataframe(items, use_container_width=True)

  st.subheader("Master Task List by Work Center")
  items = get_MTL_by_WC("EMT")
  st.dataframe(items, use_container_width=True)

  st.subheader("Individual Training Plans")
  items = get_ITP_by_DOD_id("863287637")
  st.dataframe(items, use_container_width=True)

  st.subheader("Career Development Course Status")
  items = get_CDC_by_DOD_id("863287637")
  st.dataframe(items, use_container_width=True)

  st.subheader("Training Status by Work Center")
  items = get_training_status_by_WC()
  st.dataframe(items, use_container_width=True)

except Exception as error:
  st.error("The application could not load database records.")
  st.exception(error)

if __name__ == "__main__":
  print("Testing database access functions...\n")

  print("Work Centers:")
  print(get_workcenter())

  print("Personnel:")
  print(get_personnel())

  print("Amn Vance's ITP:")
  print(get_ITP_by_DOD_id("863287637"))

  print("Overdue CDCs (AI Possible Feature)")
  print(get_overdue_cdcs())