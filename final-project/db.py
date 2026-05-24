import sqlite3
from pathlib import Path

import pandas as pd

DATABASE_PATH = Path("data/starter.db")

def get_connection() -> sqlite3.Connection:
  """Return a connection to the local SQLite database."""
  return sqlite3.connect(DATABASE_PATH)

def get_sample_items() -> pd.DataFrame:
  """Return all records from the sample_items table."""
  query = """ 
    SELECT id, name, status
    FROM sample_items
    ORDER BY id;
  """

  with get_connection() as conn:
    return pd.read_sql_query(query, conn)