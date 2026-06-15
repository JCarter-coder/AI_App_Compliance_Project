import sqlite3

def seed_WC(conn: sqlite3.Connection) -> None:
  # Workcenter Table (sample)
  conn.executemany(
    """ 
    INSERT INTO workcenter (
      office_name,
      office_symbol
    )
    VALUES (?, ?)
    """,
    [
      ("Electronic Maintenance Team", "EMT"),
      ("Missile Handling Team", "MHT"),
      ("Facilities Maintenance Section", "FMS")
    ],
  )