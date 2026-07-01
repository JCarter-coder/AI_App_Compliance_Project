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
  Dependency problems.
*Where does it occur in the system?*
  Python application.
*Why does it matter?*
  Cyber threats and attack vectors must be mitigated to safeguard data. 
*What evidence from testing or development revealed this risk?*
  This risk is inherent is software development. Over tiem, decisions must be made whether to continue supporting systems or migrate them to new systems.
*What mitigation would reduce the risk?*
  CI/CD automated pipelines can be used with auditing tools to check for vulnerabilities within the app's dependency trees.
*What limitation remains after mitigation?*
  Developers will need to review the flagged dependencies to determine if changes are required or if the known risks are acceptable.

### Risk 2
*What is the risk?*
  AI hallucination.
*Where does it occur in the system?*
  AI-output.
*Why does it matter?*
  When Air Force Instructions and policies are added to the context of the prompts, there will be hundreds of pages of material. It could be easy accept summaries if the references provided by the output don't seem too outlandish.
*What evidence from testing or development revealed this risk?*
  As more context was provided to the AI prompt, more information was referenced within the output. This increase in output should be expected as larger context is provided and until more refinement of the prompting is addressed.
*What mitigation would reduce the risk?*
  Verification by the user of the references the AI provides will provide a validation check to the output. Collected user feedback can be utilized to better address the prompts and context provided.
*What limitation remains after mitigation?*
  Continuous verification will required by the user. The time saved by the AI summaries should still be a positive offset to this verification process.

### Risk 3
*What is the risk?*
  Lack of access controls.
*Where does it occur in the system?*
  Streamlit frontend.
*Why does it matter?*
  Without user controls, anyone can manipulate data. 
*What evidence from testing or development revealed this risk?*
  This is a known risk. All database information was presented within the prototype to check functionality. Now screens need to be compartmentalized dependent on roles.
*What mitigation would reduce the risk?*
  Implementing roles and user authentication will ensure least privileges as applicable.
*What limitation remains after mitigation?*
  Changes to data from roles that have many users could make it difficult to determine who made changes unless logging is implemented too.

## Highest-Priority Risks

- Dependency Problems: High priority because attack vectors could be present without user knowledge unless systems are in place to analyze the dependency trees with known vulnerabilities.
- AI Hallucination: High priority because compliance may be failing if the AI is not properly referencing Air Force Instructions and policies.
- Lack of Access Controls: High priority because all information is currently obtainable. Access should be granted based on roles through least privileges required.

## Mitigation Plan

1. Establish user role screens (e.g. UTM, Workcenter Supervisor)
2. Implement a user authentication method
3. Ensure all AI output provides applicable references for user verifications
4. Setup CI/CD automated pipelines to scan for vulnerabilities of dependencies
5. Address data discrepancies found within AI summaries to improve data quality

| **Mitigation** | **Status** | **Risk Reduced** |
| :-------: | :------: | :---------- |
| Compartmentalize user dashboards by role | In Progress | Lack of access controls |
| Create roles and authenticate users | Not Yet Started | Lack of access controls |
| Validate references provided by AI output | Planned | AI hallucination |
| Use CI/CD automated pipelines | Not Yet Started | Dependency problems |
| Correct data discrepancies from AI output | In Progress | Data quality problems |

## Remaining Limitations

In addition to the noted mitigations above, Air Force Instructions and policies update periodically. Ensuring the most current instructions are used within this app is imperative for this app to provide a useful AI assistant for Air Force training purposes. Lastly, updates to the database structures could be necessary when uncommon and unique personnel training status situations occur. These nuances will need to be explored carefully so that proper changes are made as applicable.