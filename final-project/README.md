# Final Project Starter Environment

## Project Description

This project is the starter environment for a database-backed AI application built with Python, SQL, and Streamlit.

## Current Features

- Python virtual environment
- Streamlit starter application
- SQLite starter database
- SQL schema file
- Seed script
- Database access module

## How to Run

1. Activate your virtual environment.

   ### macOS / Linux

   ```bash
   python3 - m venv .venv
   source .venv/bin/activate

2. Install dependencies:

   ```bash
   pip install -r requirements.txt

3. Create the starter database:

   ```bash
   python seed.py

4. Run the Streamlit app:

   ```bash
   streamlit run app.py