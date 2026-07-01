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
  get_overdue_cdcs,
  get_personnel_for_ai
)

from SOT_ai import (
  evidence_dataframe_to_text,
  generate_ai_response
)

st.set_page_config(
  page_title="Database-Backed AI Application",
  page_icon="🗄️",
  layout="wide"
)

if "role" not in st.session_state:
  st.session_state.role = None

st.title("Status of Training App")

st.write(
  """
  This Streamlit application is now reading data from a local SQLite database.
  Iterations will be expanded to support AI features connecting to this application. 
  """
)

try:

  # This is used to display the selected role at the top of the screen
  placeholder = st.empty()
  placeholder.write("No role has been selected.")

  st.sidebar.title("Training Menu")
  sidebar_input = st.sidebar.selectbox(
    "Select Role", 
    ["Unit Training Manager", "Work Center Supervisor", "Supervisor"]
  )

  if st.sidebar.button("Submit"):
    st.session_state.role = sidebar_input
    placeholder.write(st.session_state.role + " Screen")

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
  work_center = st.selectbox("Work Center:", ["EMT", "MHT", "FMS"], index=None, placeholder="Select...")
  items = get_MTL_by_WC(work_center)
  st.dataframe(items, use_container_width=True)

  st.subheader("Individual Training Plans")
  DOD_ID_for_ITP = st.text_input("DoD ID:", "", placeholder="Enter DoD ID Number...")
  items = get_ITP_by_DOD_id(DOD_ID_for_ITP)
  st.dataframe(items, use_container_width=True)

  st.subheader("Career Development Course Status")
  items = get_CDC_by_DOD_id("863287637")
  st.dataframe(items, use_container_width=True)

  st.subheader("Training Status by Work Center")
  items = get_training_status_by_WC()
  st.dataframe(items, use_container_width=True)

  st.subheader("Get Overdue CDCs")
  items = get_overdue_cdcs()
  st.dataframe(items, use_container_width=True)

  st.subheader("Database Evidence Used")
  evidence_df = get_personnel_for_ai()
  if evidence_df.empty:
    st.warning("No database evidence.")
  else:
    st.dataframe(evidence_df, use_container_width=True)

    evidence_text = evidence_dataframe_to_text(evidence_df)

    st.warning(
      "AI output is generated from the database evidence shown above. "
      "Verify the response against the source records."
    )
    if st.button("Generate AI Summary"):
      with st.spinner("Generating AI response..."):
        ai_output = generate_ai_response(evidence_text)

      st.subheader("AI Generated Output")
      st.write(ai_output)

except Exception as error:
  st.error("The application could not load database records.")
  st.exception(error)