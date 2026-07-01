import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
  api_key=os.getenv("AI_API_KEY")
)

UTM_directions = """
5.2.8.25.2. Ensure 3-skill level is awarded as of technical school graduation date unless the CFETP mandates otherwise.
5.2.8.25.3. Enter personnel into 5-skill level upgrade training as of the date arrived station (ARC: upon return from technical training) unless the CFETP mandates otherwise.
5.2.8.25.4. Enter stripes for exceptional personnel (STEP) promotees and ARC personnel into 7-skill level upgrade training upon the date of promotion to E-5.
40 DAFMAN36-2689 31 MARCH 2023
5.2.8.25.5. Ensure retrainees, E-5 and above, are entered into 7-skill level upgrade training upon award of the 5-skill level. For DAF specialty codes without a 5-skill level, enter trainees into 7-skill level upgrade training upon award of the 3-skill level.
5.2.8.25.6. Ensure personnel selected for promotion to E-5 enter 7-level upgrade training the first day of the promotion cycle (1 September each year) except for STEP promotes and retrainees.
5.2.8.25.7. Ensure personnel selected for “out-of-cycle” promotion to E-5 will enter 7-level upgrade training the first day of the following month that AFPC announces the promotions. (T-1)
"""

def evidence_dataframe_to_text(evidence_df):
  if evidence_df.empty:
    return ""
  
  formatted_records = []

  for index, (_, row) in enumerate(evidence_df.iterrows(), start=0):
    formatted_records.append(
      f"""
      Record {index}:
      - Name: {row['Rank']} {row["Last Name"]}, {row["First Name"]}
      - Office Symbol: {row["Workcenter"]}
      - Supervisor: {row["Supervisor"]}
      - TSC: {row["TSC"]}
      - TSC Date: {row["TSC Date"]}
      - TSC Note: {row["defined"]}
      - Date Arrived Station: {row["DAS"]}
      - Date of Rank: {row["DOR"]}
      """
    )

  return "\n".join(formatted_records)
  # row = evidence_df.iloc[0]

  # return (
  #   f"""
  #     First Name: {row.get('first_name')}
  #     Last Name: {row.get('last_name')}
  #     Rank: {row.get('rank')}
  #     AFSC: {row.get('AFSC')}
  #     TSC: {row.get('TSC')}
  #     Workcenter: {row.get('office_symbol')}
  #     Supervisor: {row.get('supervisor_name')}
  #   """
  # )
  #return evidence_df.to_string(index=False)

def build_training_summary_prompt(evidence_text: str) -> str:
  return (
    f"""
    You are assisting a Unit Training Manager (UTM).

    These are some UTM's directions: {UTM_directions}
    'ARC' is not applicable to this unit so do not reference it.

    Use the database evidence provided below.
    Summarize only the personnel training data provided below.
    Do not skip records. 
    If multiple records are included, summarize patterns across all records.
    Mention any notable individual issues.
    If information is missing, state what is missing.

    Summarize grouping by TSC (alphabetically) then Name (alphabetically). 
    Conclude with the Database Evidence.

    Database Evidence:
    {evidence_text}
    """
  )

# response = client.responses.create(
#   model="gpt-5.4-mini",
#   input=build_training_summary_prompt(),
#   store=True,
# )

# print(response.output_text)



def generate_ai_response(evidence_text: str) -> str:
  if not evidence_text:
    return "No database evidence was provided."
  
  prompt = build_training_summary_prompt(evidence_text)

  response = client.responses.create(
    model="gpt-5.4-mini",
    input=prompt,
    store=True,
  )

  return response.output_text