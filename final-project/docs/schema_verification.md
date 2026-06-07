# Basic Verification Queries

### Ranks

This will display all 9 enlisted ranks in this table.

```sql
SELECT * 
FROM rank;
```

![rank query](./images/rankQuery.png)

### Status Training Codes

This will display all 16 training status codes in this table.

```sql
SELECT * 
FROM training_status_code;
```

![TSC query](./images/TSCquery.png)

### Work Centers

This will display all 3 work centers in this table.

```sql
SELECT * 
FROM workcenter;
```

![work center query](./images/workcenterQuery.png)

### Master Training Tasks

This will display all 9 training tasks list so far in this table.

```sql
SELECT * 
FROM master_task_list;
```

![master task list query](./images/MTLquery.png)

### Remaining Tables

Due to the interrelationships between the remaining tables and arbitrary record id values created via autoincrementation, I believe it will be more productive to connect the GUI to the database to add records to these fields. Functionality will be adjusted as required. 

![tables view](./images/tables.png)