PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS rank;
DROP TABLE IF EXISTS personnel;
DROP TABLE IF EXISTS training_status_code;
DROP TABLE IF EXISTS workcenter;
DROP TABLE IF EXISTS master_training_plan;
DROP TABLE IF EXISTS master_training_tasks;
DROP TABLE IF EXISTS individual_training_plan;

CREATE TABLE rank (
  pay_grade TEXT PRIMARY KEY,
  rank_name TEXT NOT NULL,
  rank_abbr TEXT NOT NULL,
  time_in_grade INTEGER NOT NULL,
  time_in_service INTEGER NOT NULL,
  high_year_tenure INTEGER NOT NULL
);

CREATE TABLE personnel (
  DOD_id INTEGER PRIMARY KEY,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  rank TEXT NOT NULL,
  date_of_enlistment DATE NOT NULL, --YYYY-MM-DD
  date_of_rank DATE NOT NULL,
  date_of_separation DATE NOT NULL,
  AFSC TEXT NOT NULL CHECK (AFSC IN ("2M0X1", "2M0X2", "2M0X3")),
  --time_in_service INTEGER NOT NULL,
  --time_in_grade INTEGER NOT NULL,
  --high_year_tenure INTEGER NOT NULL,
  TSC TEXT NOT NULL,
  supervisor_name TEXT DEFAULT 'TBD',
  WC_id INTEGER NOT NULL,
  FOREIGN KEY (rank) REFERENCES rank(pay_grade),
  FOREIGN KEY (TSC) REFERENCES training_status_code(TSC),
  FOREIGN KEY (WC_id) REFERENCES workcenter(WC_id)
);

CREATE TABLE training_status_code (
  TSC TEXT PRIMARY KEY,
  defined TEXT NOT NULL
);

CREATE TABLE workcenter (
  WC_id INTEGER PRIMARY KEY AUTOINCREMENT,
  office_name TEXT NOT NULL,
  office_symbol TEXT NOT NULL
);

CREATE TABLE master_training_plan (
  MTP_id INTEGER PRIMARY KEY AUTOINCREMENT,
  --FOREIGN KEY (workcenter_id) REFERENCES workcenter(WC_id),
  AFSC TEXT NOT NULL
  --FOREIGN KEY (master_training_tasks) REFERENCES master_training_tasks(MTT_id),
);

CREATE TABLE master_training_tasks (
  MTT_id INTEGER PRIMARY KEY AUTOINCREMENT,
  AFSC TEXT NOT NULL,
  task_id TEXT NOT NULL,
  task_name TEXT NOT NULL
);

CREATE TABLE individual_training_plan (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  --FOREIGN KEY (DOD_id) REFERENCES personnel (DOD_id),
  --FOREIGN KEY (workcenter_id) REFERENCES workcenter(WC_id),
  AFSC TEXT NOT NULL,
  training_tasks TEXT NOT NULL
);