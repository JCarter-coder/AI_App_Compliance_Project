import sqlite3

def seed_MTP(conn: sqlite3.Connection) -> None:
  # Master Training Plan (empty)
  conn.executemany(
    """ 
    INSERT INTO master_training_plan (
      WC_id,
      plan_title,
      AFSC
    )
    VALUES (?, ?, ?)
    """,
    [
      (1, "EMT MTP", "2M0X1"),
      (2, "MHT MTP", "2M0X2"),
      (3, "FMS MTP", "2M0X3")
    ],
  )