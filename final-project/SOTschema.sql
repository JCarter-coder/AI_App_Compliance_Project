PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS rank;
DROP TABLE IF EXISTS personnel;
DROP TABLE IF EXISTS training_status_code;
DROP TABLE IF EXISTS workcenter;
DROP TABLE IF EXISTS master_training_plan;
DROP TABLE IF EXISTS master_task_list;
DROP TABLE IF EXISTS individual_training_plan;
DROP TABLE IF EXISTS career_dev_courses;

CREATE TABLE rank (
  pay_grade TEXT PRIMARY KEY,
  rank_name TEXT NOT NULL,
  rank_abbr TEXT NOT NULL,
  time_in_grade INTEGER NOT NULL,
  time_in_service INTEGER NOT NULL,
  high_year_tenure INTEGER NOT NULL
);

CREATE TABLE personnel (
  DOD_id TEXT PRIMARY KEY,
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
  supervisor_name TEXT NOT NULL DEFAULT 'TBD',
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
  WC_id INTEGER NOT NULL,
  AFSC TEXT NOT NULL CHECK (AFSC IN ("2M0X1", "2M0X2", "2M0X3")),
  FOREIGN KEY (WC_id) REFERENCES workcenter(WC_id)
  --FOREIGN KEY (master_training_tasks) REFERENCES master_training_tasks(MTT_id),
);

CREATE TABLE master_task_list (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  --MTP_id INTEGER NOT NULL,
  AFSC TEXT NOT NULL CHECK (AFSC IN ("2M0X1", "2M0X2", "2M0X3")),
  skill_lvl TEXT NOT NULL CHECK (skill_lvl IN ("3", "5", "7", "")),
  task_id TEXT NOT NULL,
  task_name TEXT NOT NULL
  --FOREIGN KEY (MTP_id) REFERENCES master_training_plan(MTP_id)
);

CREATE TABLE individual_training_plan (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  DOD_id TEXT NOT NULL,
  WC_id INTEGER NOT NULL,
  AFSC TEXT NOT NULL,
  training_task TEXT NOT NULL,
  FOREIGN KEY (DOD_id) REFERENCES personnel(DOD_id)
  --FOREIGN KEY (WC_id) REFERENCES personnel(WC_id)
  --FOREIGN KEY (AFSC) REFERENCES personnel(AFSC)
);

CREATE TABLE career_dev_courses (
  CDC_order_id INTEGER PRIMARY KEY AUTOINCREMENT,
  DOD_id TEXT NOT NULL,
  CDC_version TEXT NOT NULL,
  is_received INTEGER NOT NULL DEFAULT 0 CHECK (is_received IN (0, 1)),
  is_completed INTEGER NOT NULL DEFAULT 0 CHECK (is_completed IN (0, 1)),
  FOREIGN KEY (DOD_id) REFERENCES personnel(DOD_id)
);
