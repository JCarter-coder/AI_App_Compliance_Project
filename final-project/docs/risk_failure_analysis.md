# Risk Failure Analysis

## Project Overview

This project establishes a database connected to an OpenAI client allowing a Unit Training Manager in the United States Air Force to obtain better insight into the training health of their unit, ensuring compliance with instructions and policies, and reporting this to their commander.

## System Data Flow Summary

User -> Streamlit -> SOT_db.py -> SQLite database -> evidence display -> SOT_ai.py -> OpenAI output

## Risk Analysis Table

| **Risk** | **Category** | **Example** | **Likelihood** | **Impact** | **Mitigation** |
| :-------: | :------: | :---------- | :----: | :----: | :--------------- |
| data quality problems | Database | discrepancies of dates within records | Low | Medium | through continued use of the AI feature, these discrepancies will be highlighted in summaries and easily corrected |
| dependency problems | App | security vulnerabilities may be present within the app | Low | High | Use CI/CD automated pipelines and Software Composition Analysis tools to scan against known vulnerabities |
| AI output without context | Streamlit | summaries created without seeing the database records used | Low | Low | display the database records within the app before the user submits for AI summaries |
| AI hallucination | AI-output | fictitious references generated during summaries | Medium | High | list the references utilized for the summaries so the user may verify accuracy before reporting training status |
| AI ignores output instructions | Prompt/Input | not presenting record summaries as expected | Medium | Low | obtain user feedback to refine prompting within the app |
| lack of access controls | Exposure | users accessing or manipulating database information outside of their role | High | High | create roles and implement authentication to restrict user access as applicable |

## Detailed Risk Discussion

### Risk 1
*What is the risk?*
  Database
*Where does it occur in the system?*
*Why does it matter?*
*What evidence from testing or development revealed this risk?*
*What mitigation would reduce the risk?*
*What limitation remains after mitigation?*

### Risk 2
*What is the risk?*
  AI
*Where does it occur in the system?*
*Why does it matter?*
*What evidence from testing or development revealed this risk?*
*What mitigation would reduce the risk?*
*What limitation remains after mitigation?*

### Risk 3
*What is the risk?*
  Exposure
*Where does it occur in the system?*
*Why does it matter?*
*What evidence from testing or development revealed this risk?*
*What mitigation would reduce the risk?*
*What limitation remains after mitigation?*

## Highest-Priority Risks

## Mitigation Plan

## Remaining Limitations