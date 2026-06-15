import sqlite3

def seed_TSC(conn: sqlite3.Connection) -> None:
  """ Training Status Codes and Definitions
  dafman36-2689, Table A2.1 """
  conn.executemany(
    """ 
    INSERT INTO training_status_code (
      TSC, 
      defined
    )
    VALUES (?, ?)
    """,
    [
      ("A", "The service member is in upgrade training for the initial award of a 3-skill level AFSC."),
      ("B", "The service member is in upgrade training for the initial award of a 5-skill level AFSC."),
      ("C", "The service member is in upgrade training for the initial award of a 7-skill level AFSC. The member must be an E-5 select or above."),
      ("D", "AFR member awaiting reassingment to the Inactive Ready Reserve. Use only when member is within 6 months of the reassignment to the Inactive Ready Reserve. Not to be used for discharge."),
      ("E", "The service member is retraining from an AFSC awarded at the 3- or higher skill level and is in upgrade training for subsequent award of a 3-skill level AFSC."),
      ("F", "The service member is retraining from an AFSC awarded at the 5- or higher skill level and is in upgrade training for subsequent award of a 5-skill level AFSC. This includes 3-skill level AFSCs having no 5-skill level (see AFMAN 36-2100)."),
      ("G", "The service member is retraining from an AFSC awarded at the 7- or higher skill-level and is in upgrade training for subsequent award of a 7-skill level AFSC. The service member must be a E-5 select or above."),
      ("I", "The service member is in re-qualification training and meets the following criteria: Is a #-4 (Senior Airman/Specialist 4), E-5 (Staff Sergeant/Sergeant), or #-6 (Technical Sergeant) and is returned to an AFSC at the highest skill level for their current grade from an AFSC, reporting identifier, or special duty identifier; and has not performed in the AFSC for at least the past 6 months. Do not use this code for prior service members or former officers."),
      ("K", "The service member is attending Basic Military Training or a skill-level awarding technical school. This code also applies to those in follow-on training."),
      ("M", "The service member has approved retraining via a formal school, the control AFSC has changed to the ratraining AFSC, and the member is waiting to attend class, ANG personnel with a control AFSC of a 1-skill level awaiting entry into a formal school, not to exceed 12 months if there are dates of availability for scheduling. If there are no dates available for scheduling out of cycle request will be placed in the training system. (T-2) Documentation will be completed every 90 calendar days. (T-2) Refer to ANG supplement for further guidance."),
      ("P", "The service member cannot enter or continue in upgrade training due to the lack of a training capability or because of duty status (Examples: AFSC withdrawn, in confinement, absent without leave, hospitalized, officer trainee or selectee, assigned out of the control AFSC, decertified from the personnel reliability program, pregnancy, and elimination from formal training course pending reclassification or separation, attending DLI, and awaiting security clearance when no unclassified upgrade training is available). Submit an explanation of circumstances surrounding a lack of upgrade training capability through applicable channels to the MAJCOM functional manager for action. This TSC does not permit waiving the dislocation allowance or other permanent change of station restrictions (see DAFI 36-2110). Return service members out of their control AFSC for more than 130 calendar days (270 calendar days for temporary PRP decertification) to duty immediately and reenter them into training in the control AFSC or recommend for retraining according to AFMAN 36-2100, whichever is appropriate."),
      ("Q", "The service member is not in upgrade training, has received the highest skill-level possible at the current grade, and is in qualification training for an assigned duty position. Supervisors evaluate enlisted members in this TSC monthly until fully qualified in the duty position. This TSC is optional for active duty unless directed by another regulation or authoritative guidance."),
      ("R", "The service member is fully qualified. Use this code when personnel complete upgrade training."),
      ("S", "The service member is directly or indirectly changing to another AFSC at the same skill-level of their previous AFSC. Only AFPC will update this code."),
      ("T", "The commander is not recommending the service member for entry into training or withdraws the member from training for failure to progress. This code includes personnel who fail to complete formal training mandatory for award of a skill-level. This code also applies to personnel who fail to complete qualification training and/or upgrade training requirements levied by the CFMs (i.e., CDCs, transition, and multi-skills training). See the TSC P and T management procedures PSD guide."),
      ("Y", "The service member The applicable TSC has not been assigned or the gaining Personnel Flight has not processed the member. Use this code for ARC personnel awaiting the start of BMT.")
    ],
  )