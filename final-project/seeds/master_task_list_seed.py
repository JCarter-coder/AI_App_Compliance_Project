import sqlite3

def seed_MTL(conn: sqlite3.Connection) -> None:
  # Master Training Tasks (sample)
  conn.executemany(
    """ 
    INSERT INTO master_task_list (
      MTP_id,
      AFSC,
      skill_lvl,
      task_id,
      task_name
    )
    VALUES (?, ?, ?, ?, ?)
    """,
    [
      (1, "2M0X1", 5, "EMT-001", "Remove Electronic Item"),
      (1, "2M0X1", 7, "EMT-002", "Install Electronic Item"),
      (1, "2M0X1", 5, "EMT-003", "Electronic Checkout"),
      (2, "2M0X2", 5, "MHT-001", "Remove Missile"),
      (2, "2M0X2", 7, "MHT-002", "Install Missile"),
      (2, "2M0X2", 5, "MHT-003", "Inspect Missile"),
      (3, "2M0X3", 5, "FMS-001", "Remove Facility Component"),
      (3, "2M0X3", 7, "FMS-002", "Install Facility Component"),
      (3, "2M0X3", 5, "FMS-003", "Facility Checkout")
    ],
  )