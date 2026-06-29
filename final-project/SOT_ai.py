import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
  api_key=os.getenv("AI_API_KEY")
)

def evidence_dataframe_to_text(evidence_df):
  if evidence_df.empty:
    return ""
  
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
  return evidence_df.to_string(index=False)

def build_training_summary_prompt(evidence_text: str) -> str:
  return (
    f"""
    You are assisting a Unit Training Manager.

    Use only the database evidence provided below.
    Summarize only the information provided.
    If information is missing, state what is missing.

    Produce output in this format:

    Individual's rank and name:
    Supervisor's name:
    Summary:

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