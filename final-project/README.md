# Final Project SOT Application Environment

## Project Description

This project is the SOT environment for a database-backed AI application built with Python, SQL, and Streamlit.

## Current Features

- Python virtual environment
- Streamlit SOT application
- SQLite SOT database
- SQL SOT schema file
- SOT Seed script
- Database access module

## How to Run

1. Activate your virtual environment.

   ### macOS / Linux

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   ### Windows PowerShell

   ```bash
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

   ### Windows Command Prompt

   ```bash
   python -m venv .venv
   .venv\Scripts\Activate.bat
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create the starter database:

   ```bash
   python3 SOTseedV2.py
   ```

4. Run the Streamlit app:

   ```bash
   streamlit run SOT_app.py
   ```