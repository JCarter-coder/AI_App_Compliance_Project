import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
  api_key=os.getenv("AI_API_KEY")
)

response = client.responses.create(
  model="gpt-5.4-mini",
  input="write a haiku about ai",
  store=True,
)

print(response.output_text)

# def built_training_summary_prompt(evidence_text: str) -> str:
#   return (
#     f"""
#     You are assisting a Unit Training Manager.

#     Use only the database evidence provided below.
#     Summarize only the information provided.
#     Focus on the personnel that are not in Training Status Code (TSC) 'R'.
#     Individuals not marked 'R' indicate training actions are required.
#     If information is missing, state what is missing.

#     Produce output in this format:

#     Individual's name:
#     Supervisor's name:
#     Summary:

#     Database Evidence:
#     {evidence_text}
#     """
#   )

# def generate_ai_response(evidence_text: str) -> str:
#   if not evidence_text:
#     return "No database evidence was provided."
  
#   prompt = built_training_summary_prompt(evidence_text)

#   response_text = call_approved_ai_model(prompt)

#   return response_text