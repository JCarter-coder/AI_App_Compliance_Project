import sqlite3

def seed_CDC(conn: sqlite3.Connection) -> None:
  # Career Development Courses (sample)

  conn.executemany(
    """ 
    INSERT INTO career_dev_courses (
      DOD_id,
      order_date,
      CDC_version,
      is_received,
      is_EOC_scheduled,
      is_completed
    )
    VALUES (?, ?, ?, ?, ?, ?)
    """,
    [
      ("863287637", "2025-12-18", "2M0X1-2402", 1, 0, 0),
      ("523983673", "2026-03-01", "2M0X2-2501", 1, 0, 0),
      ("926397272", "2026-04-18", "2M0X3-2501", 0, 0, 0),
      ("073043247", "2025-12-18", "2M0X1-2402", 1, 0, 0),
      ("818488687", "2025-11-20", "2M0X2-2501", 1, 1, 0),
      ("698254635", "2026-05-30", "2M0X3-2501", 0, 0, 0),
      ("600621209", "2025-09-01", "2M0X1-2601", 1, 1, 1),
      ("114329124", "2025-09-01", "2M0X1-2601", 1, 1, 1),
      ("131875645", "2025-09-01", "2M0X3-2601", 1, 1, 0),
    ],
  )