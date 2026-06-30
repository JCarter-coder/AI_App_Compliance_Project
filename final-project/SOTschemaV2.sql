PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS career_dev_courses;
DROP TABLE IF EXISTS individual_training_plan;
DROP TABLE IF EXISTS master_task_list;
DROP TABLE IF EXISTS master_training_plan;
DROP TABLE IF EXISTS personnel;
DROP TABLE IF EXISTS training_status_code;
DROP TABLE IF EXISTS workcenter;
DROP TABLE IF EXISTS rank;

CREATE TABLE rank (
  pay_grade TEXT PRIMARY KEY,
  rank_name TEXT NOT NULL,
  rank_abbr TEXT NOT NULL,
  time_in_grade INTEGER NOT NULL,
  time_in_service INTEGER NOT NULL,
  high_year_tenure INTEGER NOT NULL
);

CREATE TABLE workcenter (
  WC_id INTEGER PRIMARY KEY AUTOINCREMENT,
  office_name TEXT NOT NULL,
  office_symbol TEXT NOT NULL
);

CREATE TABLE training_status_code (
  TSC TEXT PRIMARY KEY,
  defined TEXT NOT NULL
);

CREATE TABLE personnel (
  DOD_id TEXT PRIMARY KEY,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  rank TEXT NOT NULL CHECK (rank IN ("AB", "Amn", "A1C", "SrA", "SSgt", "TSgt", "MSgt", "SMSgt", "CMSgt")),
  date_of_enlistment DATE NOT NULL, --YYYY-MM-DD
  date_of_rank DATE NOT NULL,
  date_arrived_station DATE NOT NULL,
  date_of_separation DATE NOT NULL,
  AFSC TEXT NOT NULL CHECK (AFSC IN ("2M0X1", "2M0X2", "2M0X3")),
  TSC TEXT NOT NULL CHECK (TSC IN ("A", "B", "C", "R")),
  TSC_date DATE NOT NULL,
  supervisor_name TEXT NOT NULL DEFAULT 'TBD',
  office_symbol TEXT NOT NULL CHECK (office_symbol IN ("EMT", "MHT", "FMS"))
);

CREATE TABLE master_training_plan (
  MTP_id INTEGER PRIMARY KEY AUTOINCREMENT,
  WC_id INTEGER NOT NULL,
  plan_title TEXT NOT NULL,
  AFSC TEXT NOT NULL CHECK (AFSC IN ("2M0X1", "2M0X2", "2M0X3")),
  FOREIGN KEY (WC_id) REFERENCES workcenter(WC_id)
);

CREATE TABLE master_task_list (
  MTL_id INTEGER PRIMARY KEY AUTOINCREMENT, --changed in V2
  MTP_id INTEGER NOT NULL,
  AFSC TEXT NOT NULL CHECK (AFSC IN ("2M0X1", "2M0X2", "2M0X3")),
  skill_lvl TEXT NOT NULL CHECK (skill_lvl IN ("3", "5", "7", "")),
  task_id TEXT NOT NULL,
  task_name TEXT NOT NULL,
  FOREIGN KEY (MTP_id) REFERENCES master_training_plan(MTP_id)
);

CREATE TABLE individual_training_plan (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  DOD_id TEXT NOT NULL,
  MTP_id INTEGER NOT NULL, --changed in V2
  MTL_id INTEGER NOT NULL, --added into V2
  --AFSC TEXT NOT NULL, --removed in V2
  skill_lvl TEXT NOT NULL CHECK (skill_lvl IN ("3", "5", "7", "")), --added into V2
  task_id TEXT NOT NULL, --added into V2
  task_name TEXT NOT NULL, --added into V2
  task_start_date DATE, --added into V2
  is_task_complete INTEGER NOT NULL DEFAULT 0 CHECK (is_task_complete IN (0, 1)), --added into V2
  FOREIGN KEY (DOD_id) REFERENCES personnel(DOD_id),
  FOREIGN KEY (MTP_id) REFERENCES master_training_plan(MTP_id), --added into V2
  FOREIGN KEY (MTL_id) REFERENCES master_task_list(MTL_id) --added into V2
);

CREATE TABLE career_dev_courses (
  CDC_order_id INTEGER PRIMARY KEY AUTOINCREMENT,
  DOD_id TEXT NOT NULL,
  order_date DATE NOT NULL,
  CDC_version TEXT NOT NULL,
  is_received INTEGER NOT NULL DEFAULT 0 CHECK (is_received IN (0, 1)),
  is_EOC_scheduled INTEGER NOT NULL DEFAULT 0 CHECK (is_EOC_scheduled IN (0, 1)),
  is_completed INTEGER NOT NULL DEFAULT 0 CHECK (is_completed IN (0, 1)),
  trainer_notes TEXT NOT NULL DEFAULT "", --added into V2
  FOREIGN KEY (DOD_id) REFERENCES personnel(DOD_id)
);
