import sqlite3
from pathlib import Path

from seeds.rank_seed import seed_rank
from seeds.workcenter_seed import seed_WC
from seeds.training_status_code_seed import seed_TSC
from seeds.personnel_seed import seed_personnel
from seeds.master_training_plan_seed import seed_MTP
from seeds.master_task_list_seed import seed_MTL
from seeds.individual_training_plan_seed import seed_ITP
from seeds.career_dev_course_seed import seed_CDC

BASE_DIR = Path(__file__).resolve().parent
DATABASE_PATH = BASE_DIR / "data" / "statusOfTrainingV2.db"
SCHEMA_PATH = BASE_DIR / "SOTschemaV2.sql"

def initialize_database() -> None:
  """Create the starter database and insert sample records."""
  DATABASE_PATH.parent.mkdir(exist_ok=True)

  with sqlite3.connect(DATABASE_PATH) as conn:
    schema_sql = SCHEMA_PATH.read_text()
    conn.executescript(schema_sql)

    seed_rank(conn)
    seed_WC(conn)
    seed_TSC(conn)
    seed_personnel(conn)
    seed_MTP(conn)
    seed_MTL(conn)
    seed_ITP(conn)
    seed_CDC(conn)

    conn.commit()

if __name__ == "__main__":
  initialize_database()
  print(f"Database created at: {DATABASE_PATH}")