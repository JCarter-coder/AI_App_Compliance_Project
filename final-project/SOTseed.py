import sqlite3
from pathlib import Path

DATABASE_PATH = Path("data/statusOfTraining.db")
SCHEMA_PATH = Path("SOTschema.sql")

def initialize_database() -> None:
  """Create the starter database and insert sample records."""
  DATABASE_PATH.parent.mkdir(exist_ok=True)

  with sqlite3.connect(DATABASE_PATH) as conn:
    schema_sql = SCHEMA_PATH.read_text()
    conn.executescript(schema_sql)

    # FIXME: Add my on sample records here for each table in the schema as needed

    # Rank Table
    # Minimum Eligibility Requirements for Promotion: 
    # afi36-2502, Table 2.1
    # SrA -> (TIG: 20 and TIS: 36) OR TIG: 28
    # Numerical values -> TIG: months, TIS: months, HYT: years
    # FIXME: include EPME and cutoff? -> afi36-2502, Table 1.1,
    # Promotion Eligibility Cutoff Date Table 1.4
    conn.executemany(
      """ 
      INSERT INTO rank (pay_grade, rank_name, rank_abbr, time_in_grade, time_in_service, high_year_tenure)
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
        ("E-9", "Chief Master Sergeant", "CMSgt", 21, 168, 30),
      ],
    )

    # Personnel (empty)

    conn.executemany(
      """ 
      INSERT INTO personnel (
        DOD_id, 
        first_name, 
        last_name, 
        rank,
        date_of_enlistment, 
        date_of_rank, 
        date_of_separation,
        AFSC,
        TSC,
        supervisor_name,
        WC_id
      )
      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
      """,
      [],
    )

    # Training Status Codes and Definitions
    # dafman36-2689, Table A2.1

    conn.executemany(
      """ 
      INSERT INTO training_status_code (TSC, defined)
      VALUES (?, ?)
      """,
      [
        ("A", "The service member is in upgrade training for the initial award of a 3-skill level AFSC."),
        ("B", "The service member is in upgrade training for the initial award of a 5-skill level AFSC."),
        ("C", "The service member is in upgrade training for the initial award of a 7-skill level AFSC. The member must be an E-5 select or above."),
        ("D", "The service member..."),
        ("E", "The service member..."),
        ("F", "The service member..."),
        ("G", "The service member..."),
        ("I", "The service member..."),
        ("K", "The service member..."),
        ("M", "The service member..."),
        ("P", "The service member..."),
        ("Q", "The service member..."),
        ("R", "The service member is fully qualified. Use this code when personnel complete upgrade training."),
        ("S", "The service member..."),
        ("T", "The service member..."),
        ("Y", "The service member..."),
      ],
    )

    # Workcenter Table (sample)

    conn.executemany(
      """ 
      INSERT INTO workcenter (office_name, office_symbol)
      VALUES (?, ?)
      """,
      [
        ("Electronic Maintenance Team", "EMT"),
        ("Missile Handling Team", "MHT"),
        ("Facilities Maintenance Section", "FMS"),
      ],
    )

    # Master Training Plan (empty)

    conn.executemany(
      """ 
      INSERT INTO master_training_plan (AFSC)
      VALUES (?)
      """,
      [],
    )

    # Master Training Tasks (sample)

    conn.executemany(
      """ 
      INSERT INTO master_training_tasks (AFSC, task_id, task_name)
      VALUES (?, ?, ?)
      """,
      [
        ("2M0X1", "EMT-001", "Remove Electronic Item"),
        ("2M0X1", "EMT-002", "Install Electronic Item"),
        ("2M0X1", "EMT-003", "Electrical Checkout"),
        ("2M0X2", "MHT-001", "Remove Missile"),
        ("2M0X2", "MHT-002", "Install Missile"),
        ("2M0X2", "MHT-003", "Mechanical Checkout"),
        ("2M0X3", "FMS-001", "Remove Component"),
        ("2M0X3", "FMS-002", "Install Component"),
        ("2M0X3", "FMS-003", "Facility Checkout"),
      ],
    )

    # Individual Training Plan (empty)

    conn.executemany(
      """ 
      INSERT INTO individual_training_plan (AFSC, training_tasks)
      VALUES (?, ?)
      """,
      [],
    )

    conn.commit()

if __name__ == "__main__":
  initialize_database()
  print(f"Database created at: {DATABASE_PATH}")