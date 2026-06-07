# Basic Verification Queries

### Ranks

This will display all 9 enlisted ranks in this table.

```sql
SELECT COUNT(*) AS Ranks
FROM rank;
```

### Status Training Codes

This will display all 16 training status codes in this table.

```sql
SELECT COUNT(*) AS 'Status Training Codes'
FROM training_status_code;
```

### Work Centers

This will display all 3 work centers in this table.

```sql
SELECT COUNT(*) AS 'Work Centers'
FROM workcenter;
```

### Master Training Tasks

This will display all 9 training tasks list so far in this table.

```sql
SELECT COUNT(*) AS 'Master Training Tasks'
FROM master_training_tasks;
```