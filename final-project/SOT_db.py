import sqlite3
from pathlib import Path

import pandas as pd

DATABASE_PATH = Path("data/statusOfTraining.db")

def get_connection() -> sqlite3.Connection:
  """Return a connection to the local SQLite database."""
  return sqlite3.connect(DATABASE_PATH)

def get_rank() -> pd.DataFrame:
  """Return all records from the rank table."""
  query = """ 
    SELECT 
    pay_grade AS 'Pay Grade', 
    rank_name AS 'Rank', 
    rank_abbr AS 'Abbr'
    FROM rank
    ORDER BY 'Pay Grade';
  """

  with get_connection() as conn:
    return pd.read_sql_query(query, conn)
  
def get_TSC() -> pd.DataFrame:
  """Return all records from the rank table."""
  query = """ 
    SELECT 
    TSC, 
    defined AS 'Definition'
    FROM training_status_code
    WHERE TSC = 'A' OR TSC = 'B' OR TSC = 'C' OR TSC = 'R';
  """

  with get_connection() as conn:
    return pd.read_sql_query(query, conn)
  
def get_workcenter() -> pd.DataFrame:
  """Return all records from the workcenter table."""
  query = """ 
    SELECT 
    office_name AS 'Work Center', 
    office_symbol AS 'Office Symbol'
    FROM workcenter;
  """

  with get_connection() as conn:
    return pd.read_sql_query(query, conn)
  
def get_personnel() -> pd.DataFrame:
  """Return all records from the personnel table."""
  query = """ 
    SELECT 
      DOD_id AS 'DoD ID',
      first_name AS 'First Name', 
      last_name AS 'Last Name',
      rank AS 'Rank',
      AFSC,
      TSC,
      supervisor_name AS 'Supervisor',
      WC_id AS 'Workcenter',
      date_of_enlistment AS 'DOE',
      date_of_rank AS 'DOR',
      date_of_separation AS 'DOS'
    FROM personnel;
  """

  with get_connection() as conn:
    return pd.read_sql_query(query, conn)