# Basic Verification Queries

### Ranks

This will display all 9 enlisted ranks in this table.

```sql
SELECT * AS Ranks
FROM rank;
```

![rank query](./images/rankQuery.png)

### Status Training Codes

This will display all 16 training status codes in this table.

```sql
SELECT * AS 'Status Training Codes'
FROM training_status_code;
```

![TSC query](./images/TSCquery.png)

### Work Centers

This will display all 3 work centers in this table.

```sql
SELECT COUNT(*) AS 'Work Centers'
FROM workcenter;
```

![work center query](./images/workcenterQuery.png)

### Master Training Tasks

This will display all 9 training tasks list so far in this table.

```sql
SELECT COUNT(*) AS 'Master Task List'
FROM master_task_list;
```

![master task list query](./images/MTLquery.png)