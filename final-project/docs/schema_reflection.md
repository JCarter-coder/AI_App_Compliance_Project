# Schema Reflection

1. *What changes, if any, did you make from your ERDC Proposal?*

I added a workcenter table as well as a Master Task List that will connect to MTPs. This will be important when adding more complexity to groups that have more than one AFSC in their workcenter. Additionally, a table that seemed unnecessary was my Upgrade Training (UGT) table. TSC annotations applied to individuals will allow filtering of those in UGT from the personnel table.

2. *Which constraints did you include, and why?*

My understanding is SQLite does not have boolean data types by default so I used integers that check to values of either 0 or 1. In addition, there are specific AFSCs that are referenced in this database, so I ensured to check values that only allow for select choices.

3. *How does your seed data support future SQL queries?*

Right now, my seed data incorporates some tables that are rather static in nature that will be used for referencing proper values with accompanying information (e.g. ranks, TSCs). Other tables require a nesting of values that form relationships to each other. Since several of their primary keys are autoincremented (their values are arbitrary), it will be easier to ensure intended functionality by incorporating a GUI to add data to these tables as intended.

4. *Which table or field will be most important for your AI features?*

The personnel table will be the most important to incorporate AI features, as this links all relevant data from ranks, workcenters, master training plans, and master task listings and references relevant Air Force Instructions to ensure compliance.

5. *What part of your schema may need revision later?*

There may need to be adjustments to relationships to ensure effective record keeping between master training plans, master task listings, and personnel. This will likely evolve to better solutions after connecting the needed functionality of the GUI to the database.