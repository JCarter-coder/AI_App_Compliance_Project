# Streamlit Prototype Notes

1. *What database-backed information does your Streamlit app display?*

The Streamlit app displays Enlisted Ranks, Work Centers, Training Status Codes, Personnel, Master Training Plans, Master Task List by Work Center, Individual Training Plans, Career Development Course Status, Training Status by Work Center, and Get Overdue CDCs. Over the next few iterations, I may add applicable interfaces and adjustments for effective interaction from various roles.

2. *What user-controlled filter or selection did you implement?*

I implemented a selection box to filter Master Task Lists by the loaded work centers. Additionally, Individual Training Plans can be retrieved by entering the DoD ID number.

3. *Which JOIN query result is displayed in your app, and why is it useful?*

The Individual Training Plans have relationships to the Master Training Plan which has a relationship to the work center. This is important to setup in this way, as work centers can have multiple AFSCs needing MTPs with the applicable AFSC tasks to ensure personnel are trained within their unique roles.

4. *Which aggregation or summary result is displayed in your app?*

Training Status Codes are aggregated with a count() function. The output is grouped by work center, then TSC. This view allows leadership to know how many individuals are in training in each work center, broken down by the level of training.

5. *What data does your detail view retrieve?*

Detail on CDC status can be retrieved from an individual trainee using their DoD ID number.

6. *Where will the future AI feature be added, and what database-resident data will it use?*

Dates are important to ensure timelines aren't exceeded for those in training. Anywhere dates are utilized, the AI could be used to analyze and summarize details. Currently, there is a function to see if CDCs are over one year since ordering. This would indicate an issue with completing them in time or a lack of paperwork to update the status.

7. *What is one improvement you plan to make before the final project submission?*

I would like to add more filtering options for the data as well add or format some of the details within tables as applicable for better insight. For instance, the order_date of the CDC table should either be changed to member_received_date or this should be added (to more accurately track the one year deadline).