# Final Scope Report

## Application Vision

This application employs a database connected AI Assistant for Unit Training Management within a USAF unit. The Unit Training Manager is responsible for gathering metrics and ensuring personnel progress through their training requirements in a timely manner consistent with Air Force Instructions and policies. This AI Assistant will summarize personnel training data, addressing discrepancies or potential concerns.

## Intended Users

- Unit Training Manager (UTM): The primary user. Through this system, the AI augments the UTM's workflow to gather metrics and address compliance concerns as needed.
- Workcenter Supervisor (WC): Secondary users. They will be able to create and update their workcenter Master Training Plan (MTP), needed for training plan reviews.
- Supervisor: Secondary users. They will be able to update Individual Training Plans (ITP) and training notes for their direct reports, needed for training progress reports.

## Core User Problem

UTMs report all training status of personnel within their units. Typically, there may be only one UTM per squadron and squadrons could contain hundreds of people. This AI Compliance app augments the workflow of the UTM so that they can identify and address training concerns quickly and effectively.

## Final In-Scope Functionality

The final application allows users to see:
- all personnel information
- data related to enlisted ranks
- work center lists
- TSC definitions for clarity
- existing MTPs and ITPs
- status of Career Development Courses (CDCs)
- training status filtered by workcenter
- overdue CDCs
- evidence used by AI
- AI training summary of all personnel

## Out-of-Scope Functionality

The application does not guarantee compliance. It is incumbent upon the user to validate references cited. Additionally, the AI does not make changes to the database.

## Database Role

The database contains personnel information to account for rank, AFSC, TSC, DOE, DOR, DAS, etc. to training and career progression requirements. Workcenters create Master Training Plans within the database. These tasks can then be added to the Individual Training Plans to track individual training qualifications. Additionally, CDCs are attached to individuals as applicable.

## AI Feature Role

This AI feature utilizes an OpenAI client connected database allowing a Unit Training Manager in the United States Air Force to obtain better insight into the training health of their unit, ensuring compliance with instructions and policies, and reporting this to their commander.

## End-State User Workflow

1. The user selects a role (e.g. UTM)
2. The UTM views the available database records throughout the unit
3. The UTM reviews the database evidence used for the AI feature
4. The UTM generates the AI summary
5. The UTM reviews the summary
6. The UTM verifies any references provided within the summary to validate
7. The UTM reports training status as applicable

## Current Implementation Status

| **Component** | **Status** | **Notes** |
| :------- | :------: | :---------- |
| Schema | Complete | `SOTschemaV2.sql` creates eight tables |
| Seed data | Complete | `SOTseedV2.sql` plus files within `/seed` |
| Query portfolio | Complete | Includes several fundamental queries to connect data across tables |
| Python database layer | Mostly complete | `SOT_db.py` includes at least 11 functions |
| Streamlit interface | In Progress | Displays all records in database, working on dashboards based on roles |
| AI feature | In Progress | Training summaries are created, needing to add more data fields and AFI/policy references within the prompt |
| Testing | Complete | Static Reviews were conducted (see `ai_test_report.md`). As noted issues are addressed, new testing will be required on future app iterations |
| Risk analysis | Complete | Major risks are captured in the `risk_failure_analysis.md` |

## Final Improvement Plan

| **Improvement** | **Priority** | **Reason** |
| :------- | :------: | :---------- |
| Compartmentalize user dashboards by role | High | Lack of access controls |
| Create roles and authenticate users | High | Lack of access controls |
| Validate references provided by AI output | Medium | AI hallucination |
| Use CI/CD automated pipelines | High | Dependency problems |
| Correct data discrepancies from AI output | Medium | Data quality problems |