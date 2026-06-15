import sqlite3

def seed_rank(conn: sqlite3.Connection) -> None:
  """ Rank Table
  Minimum Eligibility Requirements for Promotion: 
  afi36-2502, Table 2.1
  SrA -> (TIG: 20 and TIS: 36) OR TIG: 28
  Numerical values -> TIG: months, TIS: months, HYT: years
  include EPME and cutoff? -> afi36-2502, Table 1.1,
  Promotion Eligibility Cutoff Date Table 1.4 """
  conn.executemany(
    """ 
    INSERT INTO rank (
      pay_grade,
      rank_name,
      rank_abbr,
      time_in_grade,
      time_in_service,
      high_year_tenure
    )
    VALUES (?, ?, ?, ?, ?, ?)
    """,
    [
      ("E-1", "Airman Basic", "AB", 0, 0, 2),
      ("E-2", "Airman", "Amn", 6, 0, 2),
      ("E-3", "Airman First Class", "A1C", 10, 0, 4),
      ("E-4", "Senior Airman", "SrA", 20, 36, 10),
      ("E-5", "Staff Sergeant", "SSgt", 6, 36, 15),
      ("E-6", "Technical Sergeant", "TSgt", 23, 60, 20),
      ("E-7", "Master Sergeant", "MSgt", 24, 96, 24),
      ("E-8", "Senior Master Sergeant", "SMSgt", 20, 132, 26),
      ("E-9", "Chief Master Sergeant", "CMSgt", 21, 168, 30)
    ],
  )