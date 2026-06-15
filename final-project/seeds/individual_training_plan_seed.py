import sqlite3

def seed_ITP(conn: sqlite3.Connection) -> None:
  # Individual Training Plan (empty)
  conn.executemany(
    """ 
    INSERT INTO individual_training_plan (
      DOD_id,
      MTP_id,
      MTL_id,
      skill_lvl,
      task_id,
      task_name,
      task_start_date,
      is_task_complete
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """,
    [
      ("863287637", 1, 1, "5", "EMT-001", "Remove Electronic Item", "2026-01-14", 0),
      ("863287637", 1, 3, "5", "EMT-003", "Electronic Checkout", "2026-01-14", 0),
      ("073043247", 1, 1, "5", "EMT-001", "Remove Electronic Item", "2026-01-14", 0),
      ("073043247", 1, 3, "5", "EMT-003", "Electronic Checkout", "2026-01-14", 1),
      ("523983673", 2, 4, "5", "MHT-001", "Remove Missile", "2026-04-30", 0),
      ("523983673", 2, 6, "5", "MHT-003", "Inspect Missile", "2026-04-30", 0),
      ("818488687", 2, 4, "5", "MHT-001", "Remove Missile", "2026-01-11", 0),
      ("818488687", 2, 6, "5", "MHT-003", "Inspect Missile", "2026-01-11", 1),
      ("926397272", 3, 7, "5", "FMS-001", "Remove Facility Component", "2026-05-25", 0),
      ("926397272", 3, 9, "5", "FMS-003", "Facility Checkout", "2026-05-25", 0),
      ("698254635", 3, 7, "5", "FMS-001", "Remove Facility Component", "", 0),
      ("698254635", 3, 9, "5", "FMS-003", "Facility Checkout", "", 0),
      ("600621209", 1, 2, "7", "EMT-002", "Install Electronic Item", "2025-09-15", 1),
      ("114329124", 1, 2, "7", "EMT-002", "Install Electronic Item", "2025-09-15", 1),
      ("131875645", 3, 8, "7", "FMS-002", "Install Facility Component", "2025-09-30", 0),
    ],
  )