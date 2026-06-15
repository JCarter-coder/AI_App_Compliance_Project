# Database Access Notes

1. *Which database access functions did you create, and what does each function do?*

I created several functions that get all records from their applicable tables. For instance, the database can get records related to rank, training status code, work center, personnel, and master training plan. It can also get records from parameterized queries which I explain in the next question.

2. *Which function uses a parameterized query? Why is that important?*

I created at least three parameterized queries. One can get the master task list by providing the office symbol. Another retrieves an individual training plan when the individual's DoD ID number is provided. Lastly, CDC status records can be retrieved by providing the individual's DoD ID number.

3. *Which function uses a JOIN? What relationship does it rely on?*

The parameterized queries above all utilize joins. For the get_MTL_by_WC(), the relationship is established across three tables: workcenter, master_training_plan, and master_task_list. The first two tables mentioned are linked across the WC_id and the last two tables are linked across the MTP_id. Both the get_ITP_by_DOD_id() and get_CDC_by_DOD_id() join the personnel table to the ITP and CDC tables, respectively.

4. *Which function supports your future AI feature? What database evidence does it retrieve?*

The get_overdue_cdcs() function is a good example of a future AI feature query. This joins the personnel table to the CDC table to find CDCs that are over a year old. They should be completed no later than a year. I reseeded the CDC table to ensure someone would flag in this function. The orderdate is compared to the current date minus 365 days.

5. *What problems did you encounter while connecting Python to the database, if any?*

I didn't encounter problems connecting the Python app to the database, as much as ensuring I had enough examples records seeded to begin to create meaningful data to analyze. Because of the relationships between several of the tables, I had to ensure data was seeded in a specific order to ensure parent tables were established before their children tables. I quickly realized it would be more efficient to build separate seed files for each table and build the tables one at a time. This allowed for more efficient troubleshooting when there were errors, usually attributed to syntax.