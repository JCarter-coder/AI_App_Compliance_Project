import sqlite3
from pathlib import Path

import pandas as pd

DATABASE_PATH = Path("data/statusOfTrainingV2.db")

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
    FROM training_status_code;
  """
    #WHERE TSC = 'A' OR TSC = 'B' OR TSC = 'C' OR TSC = 'R';
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
      office_symbol AS 'Workcenter',
      date_of_enlistment AS 'DOE',
      date_of_rank AS 'DOR',
      date_arrived_station AS 'DAS',
      date_of_separation AS 'DOS'
    FROM personnel;
  """

  with get_connection() as conn:
    return pd.read_sql_query(query, conn)
  
def get_training_status_by_WC() -> pd.DataFrame:
  """Return all personnel records by Training Status Code."""
  query = """ 
    SELECT
      office_symbol AS 'Workcenter',
      TSC,
      COUNT(TSC) AS "Amount"
    FROM personnel
    GROUP BY office_symbol, TSC;
  """

  with get_connection() as conn:
    return pd.read_sql_query(query, conn)
  
def get_MTP() -> pd.DataFrame:
  """Return all master training plans."""
  query = """ 
    SELECT 
    plan_title AS 'MTP Title', 
    AFSC
    FROM master_training_plan;
  """

  with get_connection() as conn:
    return pd.read_sql_query(query, conn)
  
def get_MTL_by_WC(office_symbol: str) -> pd.DataFrame:
  """Return all master tasks lists by work center."""
  query = """ 
    SELECT 
      w.office_symbol AS "Work Center",
      mtp.plan_title AS "MTP Title",
      mtp.AFSC,
      mtl.task_id AS "Task ID",
      mtl.skill_lvl AS "Skill Lvl",
      mtl.task_name AS "Task"
    FROM workcenter AS w
    JOIN master_training_plan AS mtp ON w.WC_id = mtp.WC_id
    JOIN master_task_list AS mtl ON mtp.MTP_id = mtl.MTP_id
    WHERE w.office_symbol = ?;
  """

  with get_connection() as conn:
    return pd.read_sql_query(query, conn, params=(office_symbol,))
  
def get_ITP_by_DOD_id(DOD_id: str) -> pd.DataFrame:
  """Return all individual training plans by DOD ID."""
  query = """ 
    SELECT 
      p.rank AS "Rank",
      p.last_name AS "Last Name",
      p.first_name AS "First",
      p.office_symbol AS "Work Center",
      itp.skill_lvl AS "Skill Lvl",
      itp.task_id AS "Task ID",
      itp.task_name AS "Task",
      itp.task_start_date AS "Start Date",
      CASE itp.is_task_complete
        WHEN itp.is_task_complete = 0 THEN "No"
        ELSE "Yes"
      END AS "Complete?"
    FROM personnel AS p
    JOIN individual_training_plan AS itp ON p.DOD_id = itp.DOD_id
    WHERE p.DOD_id = ?;
  """

  with get_connection() as conn:
    return pd.read_sql_query(query, conn, params=(DOD_id,))
  

def get_CDC_by_DOD_id(DOD_id: str) -> pd.DataFrame:
  """Return all career development courses status by DOD ID."""
  query = """ 
    SELECT 
      p.rank AS "Rank",
      p.last_name AS "Last Name",
      p.first_name AS "First",
      p.office_symbol AS "Work Center",
      p.supervisor_name AS "Supervisor",
      cdc.CDC_version AS "CDC Version",
      cdc.order_date AS "Order Date",
      CASE cdc.is_received
        WHEN cdc.is_received = 0 THEN "No"
        ELSE "Yes"
      END AS "Received?",
      CASE cdc.is_EOC_scheduled
        WHEN cdc.is_EOC_scheduled = 0 THEN "No"
        ELSE "Yes"
      END AS "Test Scheduled?",
      CASE cdc.is_completed
        WHEN cdc.is_completed = 0 THEN "No"
        ELSE "Yes"
      END AS "Complete?"
    FROM personnel AS p
    JOIN career_dev_courses AS cdc ON p.DOD_id = cdc.DOD_id
    WHERE p.DOD_id = ?;
  """

  with get_connection() as conn:
    return pd.read_sql_query(query, conn, params=(DOD_id,))
  
def get_overdue_cdcs() -> pd.DataFrame:
  """Return all overdue CDCs."""
  query = """ 
    SELECT 
      p.rank AS "Rank",
      p.last_name AS "Last Name",
      p.first_name AS "First",
      p.office_symbol AS "Work Center",
      p.supervisor_name AS "Supervisor",
      cdc.CDC_version AS "CDC Version",
      cdc.order_date AS "Order Date",
      CASE cdc.is_received
        WHEN cdc.is_received = 0 THEN "No"
        ELSE "Yes"
      END AS "Received?",
      CASE cdc.is_EOC_scheduled
        WHEN cdc.is_EOC_scheduled = 0 THEN "No"
        ELSE "Yes"
      END AS "Test Scheduled?",
      CASE cdc.is_completed
        WHEN cdc.is_completed = 0 THEN "No"
        ELSE "Yes"
      END AS "Complete?"
    FROM personnel AS p
    JOIN career_dev_courses AS cdc ON p.DOD_id = cdc.DOD_id
    WHERE cdc.order_date <= date('now', '-365 days');
  """

  with get_connection() as conn:
    return pd.read_sql_query(query, conn)