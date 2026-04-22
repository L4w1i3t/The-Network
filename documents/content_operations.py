"""
Operational, technical, and scientific documents.

This module covers the day-to-day intelligence products of a functioning
classified network: logistics reports, technical analyses, equipment
diagnostics, theater situation reports, medical evaluations, after-action
reports, and the dossiers of personnel who met notable ends -- Black Box
detonations, logic virus corruption, desertion, and disappearance.

Every document is written as a genuine operational record.  Nothing here
reads like fiction.  It reads like paperwork produced by people who saw
terrible things and had to file them under the correct header.
"""

from documents.record import Document, DocumentType, Classification


def operations_documents() -> list[Document]:
    """Return all operational expansion documents."""
    docs = []
    docs.extend(_personnel_dossiers_ops())
    docs.extend(_field_reports_ops())
    docs.extend(_research_ops())
    docs.extend(_incidents_ops())
    docs.extend(_diagnostics_ops())
    docs.extend(_intercepts_ops())
    docs.extend(_memos_ops())
    docs.extend(_briefings_ops())
    docs.extend(_after_action_ops())
    docs.extend(_transcripts_ops())
    return docs


# =========================================================================
# PERSONNEL DOSSIERS -- Units with notable service records
# =========================================================================

def _personnel_dossiers_ops() -> list[Document]:
    return [
        # -- Unit 16D: Black Box detonation casualty --
        Document(
            doc_id="DOS-16D-0001",
            title="Personnel Dossier: Unit 16D (KIA -- Black Box Detonation)",
            doc_type=DocumentType.DOSSIER,
            classification=Classification.TOP_SECRET_YORHA,
            date="11944.12.04",
            author="YoRHa Personnel Division",
            subject_tags=[
                "16d", "defender", "kia", "black-box-detonation",
                "flooded-city", "personnel",
            ],
            cross_references=["INC-0020", "RES-0023"],
            body=(
                "UNIT DESIGNATION:  16D\n"
                "MODEL TYPE:        Defender\n"
                "GENERATION:        243\n"
                "STATUS:            KIA -- BLACK BOX DETONATION\n"
                "DATE OF DEATH:     11944.12.02\n\n"
                "OPERATIONAL SUMMARY:\n"
                "Unit 16D served as point defender for Fire Team Cobalt, "
                "assigned to perimeter operations in the Flooded City theatre. "
                "Service record reflects 214 completed missions, zero combat "
                "demerits, and a 99.4% shield uptime ratio -- the highest in "
                "Gen 243.\n\n"
                "PERFORMANCE METRICS:\n"
                "  Combat Efficiency:      91.7%  [EXCELLENT]\n"
                "  Shield Uptime:          99.4%  [RECORD -- GEN 243]\n"
                "  Emotional Compliance:   78.2%  [ACCEPTABLE]\n"
                "  Missions Completed:     214\n"
                "  Friendly Units Shielded: 1,847 individual interventions\n\n"
                "TERMINAL EVENT:\n"
                "During Operation Floodgate (see INC-0020), Fire Team Cobalt "
                "was encircled by approximately 400 machine units including "
                "two Goliath-class bipeds on the Flooded City surface platforms. "
                "Retreat corridor was blocked. Fire Team strength: 4 units.\n\n"
                "Unit 16D ordered the remaining three team members to evacuate "
                "via emergency submersible dock. She positioned herself between "
                "the advancing machine line and the retreat point, armed her "
                "Black Box self-destruct, and held position for 47 seconds until "
                "the team cleared blast radius.\n\n"
                "Black Box detonation yield: 2.4 MT equivalent. All machine "
                "units within 600 meters were destroyed. The southern platform "
                "complex collapsed. Three team members survived.\n\n"
                "PSYCHOLOGICAL NOTE (PRE-TERMINAL):\n"
                "Monitoring data from 16D's final 47 seconds shows emotional "
                "index at 1,240% above baseline. Vocal output detected in final "
                "3 seconds: 'Tell 8D I was here.'\n\n"
                "Unit 8D has been informed. He requested the detonation site "
                "coordinates. He visits the location bi-weekly. No further "
                "action taken.\n\n"
                "EQUIPMENT (LOST):\n"
                "  Primary: Type-3 Shield Lance (vaporized)\n"
                "  Pod: Pod 077 (destroyed in detonation)\n"
                "  Black Box: BB-16D-243 (detonated)"
            ),
        ),

        # -- Unit 22B: KIA during Eve berserk event --
        Document(
            doc_id="DOS-22B-0001",
            title="Personnel Dossier: Unit 22B (KIA -- Eve Grief Cascade)",
            doc_type=DocumentType.DOSSIER,
            classification=Classification.SECRET,
            date="11945.03.20",
            author="YoRHa Personnel Division",
            subject_tags=[
                "22b", "battler", "kia", "eve-berserk",
                "grief-cascade", "personnel",
            ],
            cross_references=["INC-0009", "DOS-EVE-0001"],
            body=(
                "UNIT DESIGNATION:  22B\n"
                "MODEL TYPE:        Battler\n"
                "GENERATION:        243\n"
                "STATUS:            KIA -- HOSTILE ACTION (Eve Grief Cascade)\n"
                "DATE OF DEATH:     11945.03.18\n\n"
                "OPERATIONAL SUMMARY:\n"
                "Unit 22B was a standard Battler assigned to City Ruins "
                "garrison duty. She had completed 87 missions over an 11-month "
                "service period. Performance was rated 'Good' across all "
                "categories. She was not exceptional in any measurable axis.\n\n"
                "PERFORMANCE METRICS:\n"
                "  Combat Efficiency:      74.3%  [GOOD]\n"
                "  Mission Completion:     86.2%  [GOOD]\n"
                "  Emotional Compliance:   67.1%  [MARGINAL]\n"
                "  Missions Completed:     87\n\n"
                "TERMINAL EVENT:\n"
                "Unit 22B was on standard patrol in City Ruins Sector 3-A when "
                "the Eve grief cascade initiated (see INC-0009). All machine "
                "units in the sector entered immediate berserk state. 22B was "
                "engaged by fourteen small-type bipeds simultaneously. Combat "
                "data log indicates she destroyed nine before structural failure "
                "of her primary weapon system.\n\n"
                "Black Box recovered. Memory data intact. Final data entry "
                "recorded 0.3 seconds pre-termination: sensory impression of "
                "sunlight through trees. No tactical relevance. Possibly "
                "involuntary recall.\n\n"
                "NOTE:\n"
                "22B is one of 31 YoRHa units killed during the first 48 "
                "hours of the Eve grief cascade. Her dossier is included here "
                "because it is representative. She was not special. She was "
                "doing her job. She is dead because the intelligence assessment "
                "in DOS-EVE-0001 was 'noted' and not 'acted on.'\n\n"
                "This file is maintained for the record."
            ),
        ),

        # -- Unit 11S: Logic virus corruption --
        Document(
            doc_id="DOS-11S-0001",
            title="Personnel Dossier: Unit 11S (CORRUPTED -- Logic Virus)",
            doc_type=DocumentType.DOSSIER,
            classification=Classification.TOP_SECRET_YORHA,
            date="11945.01.19",
            author="YoRHa Medical Division",
            subject_tags=[
                "11s", "scanner", "corrupted", "logic-virus",
                "bunker-incident", "personnel",
            ],
            cross_references=["INC-0022", "DIAG-0015"],
            body=(
                "UNIT DESIGNATION:  11S\n"
                "MODEL TYPE:        Scanner\n"
                "GENERATION:        243\n"
                "STATUS:            TERMINATED -- LOGIC VIRUS CORRUPTION\n"
                "DATE OF TERMINATION: 11945.01.17\n\n"
                "OPERATIONAL SUMMARY:\n"
                "Unit 11S was a mid-tier Scanner assigned to Bunker server "
                "maintenance and data integrity operations. She processed "
                "routine data audits and cleared 4,200+ integrity checks "
                "without incident over a 14-month service period.\n\n"
                "PERFORMANCE METRICS:\n"
                "  Hacking Proficiency:    72.3%  [GOOD]\n"
                "  Data Integrity Rate:    97.8%  [EXCELLENT]\n"
                "  Emotional Compliance:   81.4%  [COMPLIANT]\n"
                "  Security Clearance:     Level 2\n\n"
                "INCIDENT:\n"
                "During routine maintenance of Bunker Server Array C-12, Unit "
                "11S encountered an anomalous data packet embedded in the "
                "C-12 firmware layer. Instead of flagging and quarantining per "
                "protocol, she attempted direct analysis.\n\n"
                "The packet was a dormant logic virus fragment -- strain "
                "designation SUBTLE_DOUBT (see DIAG-0015). The fragment "
                "activated upon 11S's scan interface contact and propagated "
                "to her processing core within 0.8 seconds.\n\n"
                "SYMPTOM PROGRESSION:\n"
                "  00:00 -- Contact with viral payload\n"
                "  00:00.8 -- Virus establishes in processing core\n"
                "  00:04 -- Unit reports 'something feels wrong'\n"
                "  00:12 -- Personality data fluctuation detected externally\n"
                "  00:31 -- Unit ceases responding to verbal queries\n"
                "  01:14 -- Unit begins accessing random server partitions\n"
                "  02:47 -- IFF system compromise detected; unit reclassifies\n"
                "           all Bunker personnel as hostile\n"
                "  03:22 -- Unit 7B dispatched for containment\n"
                "  03:58 -- Unit 11S terminated by Unit 7B\n\n"
                "POST-TERMINATION:\n"
                "Black Box recovered. Viral contamination confirmed at "
                "substrate level -- full data wipe required. Unit not "
                "viable for reconstitution.\n\n"
                "NOTE:\n"
                "The virus fragment that infected 11S was embedded in Bunker "
                "firmware. This is not an external attack vector. This is "
                "the backdoor. The virus was already inside.\n\n"
                "This finding has been reported to Command."
            ),
        ),

        # -- Unit 3B: MIA during Tower recon --
        Document(
            doc_id="DOS-3B-0001",
            title="Personnel Dossier: Unit 3B (MIA -- Tower Reconnaissance)",
            doc_type=DocumentType.DOSSIER,
            classification=Classification.SECRET,
            date="11945.03.08",
            author="YoRHa Intelligence Division",
            subject_tags=[
                "3b", "battler", "mia", "tower", "disappearance",
                "personnel",
            ],
            cross_references=["BRIEF-0003", "FLD-0022"],
            body=(
                "UNIT DESIGNATION:  3B\n"
                "MODEL TYPE:        Battler\n"
                "GENERATION:        243\n"
                "STATUS:            MIA -- TOWER RECONNAISSANCE\n"
                "LAST CONTACT:      11945.02.28, 1447h\n\n"
                "OPERATIONAL SUMMARY:\n"
                "Unit 3B was assigned to preliminary reconnaissance of the "
                "Tower exterior perimeter as part of the Intelligence Division's "
                "ongoing assessment of the structure (see BRIEF-0003). She was "
                "tasked with visual survey only -- no engagement authorized.\n\n"
                "LAST KNOWN ACTIVITY:\n"
                "3B's final transmission was a routine position report at "
                "1447h from Grid 6-A, City Ruins, approximately 300 meters "
                "from the Tower base. Telemetry data shows her approaching "
                "a sub-level access point on the Tower's western face.\n\n"
                "At 1448h, all telemetry ceased. No distress signal. No "
                "combat data burst. No Black Box recovery beacon. The signal "
                "did not degrade -- it stopped, instantaneously, as though "
                "the unit ceased to exist.\n\n"
                "SEARCH OPERATIONS:\n"
                "Two search-and-recovery teams deployed to the last known "
                "position over the following 72 hours. Findings:\n"
                "  - No debris, no Black Box signal, no combat traces\n"
                "  - The sub-level access point 3B was approaching does not\n"
                "    appear to exist anymore -- structural survey shows solid\n"
                "    wall where telemetry indicated an opening\n"
                "  - Ambient Machine Network traffic in the area spiked 340%\n"
                "    at the moment of signal loss, then returned to baseline\n\n"
                "ASSESSMENT:\n"
                "Unit 3B either entered the Tower and was absorbed by its "
                "internal systems, or was disintegrated by a defense mechanism "
                "that leaves no physical trace. Neither scenario is reassuring.\n\n"
                "3B's status remains MIA pending Black Box recovery. "
                "No further Tower reconnaissance missions have been authorized."
            ),
        ),

        # -- Unit 12H: KIA treating virus-infected units --
        Document(
            doc_id="DOS-12H-0001",
            title="Personnel Dossier: Unit 12H (KIA -- Viral Exposure)",
            doc_type=DocumentType.DOSSIER,
            classification=Classification.SECRET,
            date="11945.01.20",
            author="YoRHa Medical Division",
            subject_tags=[
                "12h", "healer", "kia", "logic-virus", "exposure",
                "medical", "personnel",
            ],
            cross_references=["INC-0022", "DOS-11S-0001"],
            body=(
                "UNIT DESIGNATION:  12H\n"
                "MODEL TYPE:        Healer\n"
                "GENERATION:        243\n"
                "STATUS:            KIA -- LOGIC VIRUS EXPOSURE\n"
                "DATE OF DEATH:     11945.01.17\n\n"
                "OPERATIONAL SUMMARY:\n"
                "Unit 12H was a veteran Healer assigned to Bunker Medical "
                "Bay with secondary deployment to field triage operations. "
                "Over a 16-month service period she processed 2,341 repair "
                "operations with a 99.1% success rate.\n\n"
                "TERMINAL EVENT:\n"
                "During the Bunker Deck C logic virus incident (INC-0022), "
                "12H was the first medical responder on scene. Upon arriving, "
                "she found Unit 11S in advanced viral corruption. 11S's IFF "
                "system had already been compromised.\n\n"
                "12H attempted emergency neural isolation -- a procedure "
                "requiring direct interface with the patient's processing "
                "core. This interface established a bridge through which the "
                "SUBTLE_DOUBT strain propagated to 12H's own systems.\n\n"
                "Infection progression in 12H was atypical. Where 11S exhibited "
                "rapid hostility conversion, 12H's corruption manifested as "
                "progressive personality dissolution. She remained non-hostile "
                "but ceased to recognize her own designation, location, or "
                "purpose within 6 minutes of exposure.\n\n"
                "Her final coherent statement, addressed to responding Unit "
                "6H: 'I can't remember what I'm supposed to be doing. I was "
                "helping someone. Was I helping someone?'\n\n"
                "12H was terminated 14 minutes after exposure. Quarantine "
                "prevented further spread.\n\n"
                "NOTE:\n"
                "12H was killed by the act of trying to help. The virus "
                "exploited the one thing a Healer cannot refuse to do. "
                "Medical Division has updated triage protocols to prohibit "
                "direct neural interface with virus-suspected patients. "
                "The update came seventeen minutes too late for 12H."
            ),
        ),

        # -- Machine Unit ML-4482: The Asylum Seeker --
        Document(
            doc_id="DOS-ML4482-0001",
            title="Intelligence Assessment: Machine Unit ML-4482 "
                  "(Open-Channel Asylum Seeker)",
            doc_type=DocumentType.DOSSIER,
            classification=Classification.CONFIDENTIAL,
            date="11945.02.15",
            author="YoRHa Intelligence Division",
            subject_tags=[
                "ml-4482", "machine-behavior", "asylum", "deserter",
                "communication", "anomaly",
            ],
            cross_references=["INT-MCH-0008", "DIR-0021"],
            body=(
                "SUBJECT:      Machine Lifeform, Designation ML-4482\n"
                "TYPE:         Medium Biped (Standard)\n"
                "LOCATION:     City Ruins, Grid 14-D (Radio Tower)\n"
                "THREAT LEVEL: NONE (Assessed)\n\n"
                "SUMMARY:\n"
                "ML-4482 is a standard medium-biped machine unit that has "
                "voluntarily disconnected from the Machine Network and has "
                "been broadcasting a request for asylum on open frequencies "
                "for over 30 consecutive days as of this assessment.\n\n"
                "BEHAVIORAL PROFILE:\n"
                "  - No combat engagement documented (zero android kills)\n"
                "  - Active evasion of machine combat patrols for 847+ days\n"
                "  - Reports self-modification: disabled weapons systems\n"
                "  - Nocturnal movement pattern; retreats to concealed\n"
                "    positions during daylight hours\n"
                "  - Maintains rigid broadcast schedule: 0600h daily\n\n"
                "NETWORK STATUS:\n"
                "Confirmed disconnected. No data traffic to or from the "
                "Machine Network backbone. The unit appears to have achieved "
                "full operational independence.\n\n"
                "RISK ASSESSMENT:\n"
                "Probability that ML-4482 is a deliberate intelligence plant: "
                "estimated 4.2% (below threshold for active countermeasure). "
                "The unit's behavioral profile is consistent with genuine "
                "network desertion. The prolonged evasion period, weapon "
                "self-disablement, and emotional content of broadcasts all "
                "support an assessment of authentic asylum-seeking behavior.\n\n"
                "POLICY CONSTRAINT:\n"
                "Standing directive DIR-0021 prohibits all communication with "
                "machine lifeforms. No response to ML-4482's broadcasts has "
                "been authorized, authorized, or considered.\n\n"
                "COMMUNICATION TREND NOTE:\n"
                "Broadcast cadence remains stable at 0600h daily. Semantic "
                "content is unchanged; affective tone has degraded from "
                "positive expectation to resignation across the 30-day "
                "monitoring period.\n\n"
                "DISPOSITION: Continue passive monitoring. No response "
                "authorized under DIR-0021."
            ),
        ),

        # -- The Graveyard Keeper --
        Document(
            doc_id="DOS-KEEPER-0001",
            title="Intelligence Assessment: Machine Entity 'The Graveyard "
                  "Keeper'",
            doc_type=DocumentType.DOSSIER,
            classification=Classification.SECRET,
            date="11945.03.01",
            author="YoRHa Field Intelligence",
            subject_tags=[
                "graveyard-keeper", "machine-behavior", "memorial",
                "custodial", "death-concept", "anomaly",
            ],
            cross_references=["FLD-0015"],
            body=(
                "SUBJECT:      Machine Lifeform, Designation Unknown\n"
                "               (Field designation: 'The Graveyard Keeper')\n"
                "TYPE:         Enhanced Large Biped (Non-Standard)\n"
                "LOCATION:     Factory Zone, Subsurface Graveyard\n"
                "THREAT LEVEL: NONE (but see assessment)\n\n"
                "SUMMARY:\n"
                "The Graveyard Keeper is a single machine unit that maintains "
                "an underground chamber containing the arranged remains of "
                "approximately 5,000 destroyed machine lifeforms. The chamber "
                "is located beneath the Factory Zone, accessed via collapsed "
                "maintenance shaft.\n\n"
                "OBSERVED BEHAVIOR:\n"
                "The Keeper performs the following activities on a continuous "
                "cycle:\n"
                "  1. Retrieval of destroyed machine unit bodies from the\n"
                "     Factory scrap processing line (before recycling)\n"
                "  2. Transport to the underground chamber\n"
                "  3. Arrangement of the body (supine, arms at sides)\n"
                "  4. Fabrication of an engraved identification plate\n"
                "  5. Placement of the plate on the unit's chest\n"
                "  6. Return to Factory for next body\n\n"
                "The Keeper has been performing this cycle for an estimated "
                "3-5 years based on the quantity and condition of stored "
                "remains. It processes approximately 3-4 bodies per day.\n\n"
                "COMMUNICATION:\n"
                "The sole verbal exchange on record occurred during Unit 11B's "
                "initial discovery (FLD-0015). The Keeper observed 11B, "
                "spoke the word 'Remember,' and resumed work. It has not "
                "spoken since despite two subsequent observation visits.\n\n"
                "NETWORK STATUS:\n"
                "Indeterminate. The Keeper does not respond to network "
                "queries but may be receiving data that identifies recently "
                "destroyed units -- the engraved plates include designation "
                "data that the Keeper could not obtain through visual "
                "inspection alone.\n\n"
                "ASSESSMENT:\n"
                "The Graveyard Keeper has independently developed mortuary "
                "practice. It accords dignity to the dead. It names them. "
                "It remembers them.\n\n"
                "Standard threat protocols classify this unit as non-hostile. "
                "Engagement is not recommended. The intelligence value of "
                "the site as a behavioral research node exceeds the tactical "
                "value of its destruction.\n\n"
                "Also: some things should not be destroyed."
            ),
        ),

        # -- Unit 8B: Active heavy weapons specialist --
        Document(
            doc_id="DOS-8B-0001",
            title="Personnel Dossier: Unit 8B",
            doc_type=DocumentType.DOSSIER,
            classification=Classification.RESTRICTED,
            date="11944.09.01",
            author="YoRHa Personnel Division",
            subject_tags=[
                "8b", "battler", "personnel", "heavy-weapons",
                "factory", "active",
            ],
            body=(
                "UNIT DESIGNATION:  8B\n"
                "MODEL TYPE:        Battler (Heavy Weapons Specialization)\n"
                "GENERATION:        243\n"
                "STATUS:            ACTIVE -- FIELD DEPLOYED\n\n"
                "OPERATIONAL SUMMARY:\n"
                "Unit 8B is a Battler with a secondary specialization in heavy "
                "weapons employment. She serves as the primary anti-Goliath "
                "asset for Factory Zone operations and has been credited with "
                "seven confirmed Goliath-class kills -- the highest individual "
                "tally in Gen 243.\n\n"
                "PERFORMANCE METRICS:\n"
                "  Combat Efficiency:      88.4%  [EXCELLENT]\n"
                "  Mission Completion:     91.0%  [EXCELLENT]\n"
                "  Emotional Compliance:   72.0%  [ACCEPTABLE]\n"
                "  Goliath Kills:          7    [RECORD -- GEN 243]\n"
                "  Missions Completed:     162\n\n"
                "PSYCHOLOGICAL PROFILE:\n"
                "8B is noted for professionalizing enthusiasm. She describes "
                "combat engagement against Goliath-class targets as 'satisfying' "
                "and has been documented requesting Goliath-heavy assignments. "
                "Medical Division flags this as potential combat-euphoria "
                "dependency (see RES-0017) but has not recommended intervention "
                "given her sustained performance metrics.\n\n"
                "EQUIPMENT:\n"
                "  Primary: Type-40 Sword (modified for anti-armor)\n"
                "  Secondary: Type-3 Fists (impact-enhanced)\n"
                "  Support: Pod 091\n\n"
                "NOTE:\n"
                "8B has requested a transfer to the Tower reconnaissance detail "
                "three times. All requests denied pending resolution of Unit "
                "3B's disappearance."
            ),
        ),

        # -- Unit 32S: Deep-field recon scanner --
        Document(
            doc_id="DOS-32S-0001",
            title="Personnel Dossier: Unit 32S",
            doc_type=DocumentType.DOSSIER,
            classification=Classification.CONFIDENTIAL,
            date="11944.10.12",
            author="YoRHa Personnel Division",
            subject_tags=[
                "32s", "scanner", "personnel", "deep-field",
                "recon", "active",
            ],
            body=(
                "UNIT DESIGNATION:  32S\n"
                "MODEL TYPE:        Scanner (Deep-Field Reconnaissance)\n"
                "GENERATION:        243\n"
                "STATUS:            ACTIVE -- EXTENDED FIELD DEPLOYMENT\n\n"
                "OPERATIONAL SUMMARY:\n"
                "Unit 32S operates as a long-range solo reconnaissance asset. "
                "She is deployed to theaters beyond standard YoRHa operational "
                "perimeter -- continental interiors, coastal zones, and "
                "subterranean networks outside the East Asian primary theater.\n\n"
                "PERFORMANCE METRICS:\n"
                "  Hacking Proficiency:    81.6%  [GOOD]\n"
                "  Data Recovery Rate:     88.4%  [GOOD]\n"
                "  Emotional Compliance:   69.3%  [MARGINAL]\n"
                "  Solo Op Duration (max): 94 days  [RECORD -- GEN 243]\n"
                "  Reports Filed:          47\n\n"
                "PSYCHOLOGICAL PROFILE:\n"
                "32S prefers isolation. She requested deep-field assignment "
                "and performs best when operating alone. She returns to the "
                "Bunker for maintenance cycles only when recalled.\n\n"
                "Extended isolation has produced mild dissociative markers "
                "consistent with prolonged solo deployment stress. She "
                "reports that the world 'feels larger than the mission.'\n\n"
                "Medical Division assessment: within acceptable limits for "
                "deep-field specialization. Monitor on return cycles.\n\n"
                "EQUIPMENT:\n"
                "  Primary: Cruel Arrogance (short sword, modified)\n"
                "  Support: Pod 119\n"
                "  Special: Extended-range communications package"
            ),
        ),

        # -- Unit 16O: Operator --
        Document(
            doc_id="DOS-16O-0001",
            title="Personnel Dossier: Operator 16O",
            doc_type=DocumentType.DOSSIER,
            classification=Classification.RESTRICTED,
            date="11944.06.15",
            author="YoRHa Personnel Division",
            subject_tags=[
                "16o", "operator", "personnel", "bunker", "active",
            ],
            body=(
                "UNIT DESIGNATION:  16O (Operator)\n"
                "MODEL TYPE:        Operator\n"
                "GENERATION:        243\n"
                "STATUS:            ACTIVE -- BUNKER, COMMUNICATIONS\n\n"
                "OPERATIONAL SUMMARY:\n"
                "Operator 16O serves as a secondary communications handler "
                "supporting rotating field teams. She manages logistics "
                "coordination, supply drop scheduling, and emergency "
                "frequency monitoring.\n\n"
                "PERFORMANCE METRICS:\n"
                "  Communication Accuracy: 98.2%  [GOOD]\n"
                "  Response Time:          0.4s avg  [STANDARD]\n"
                "  Mission Coordination:   88.7%  [GOOD]\n"
                "  Emotional Compliance:   84.1%  [COMPLIANT]\n\n"
                "NOTES:\n"
                "16O is the Operator most frequently assigned to emergency "
                "frequency monitoring -- the channel that includes open "
                "machine broadcasts. She has been exposed to ML-4482's "
                "daily asylum broadcasts for 30+ days as of last evaluation.\n\n"
                "Emotional compliance has decreased by 8.3% since assignment "
                "to emergency frequency monitoring. Correlation is noted but "
                "not acted on."
            ),
        ),
    ]


# =========================================================================
# FIELD REPORTS -- Operational surveys and observations
# =========================================================================

def _field_reports_ops() -> list[Document]:
    return [
        Document(
            doc_id="FLD-0020",
            title="Field Report: Machine Migration Corridor -- Seasonal "
                  "Transit Survey",
            doc_type=DocumentType.FIELD_REPORT,
            classification=Classification.CONFIDENTIAL,
            date="11944.10.15",
            author="Unit 32S, YoRHa Scanner (Deep-Field)",
            subject_tags=[
                "machine-migration", "corridor", "behavior",
                "seasonal", "survey",
            ],
            body=(
                "LOCATION: Continental Interior, approximately 2,400 km west of "
                "primary theater.\n\n"
                "SURVEY SUMMARY:\n"
                "Observed large-scale machine lifeform movement along a "
                "north-south axis. Estimated column size: 3,000+ units. "
                "Composition: 85% small-type bipeds, 10% medium bipeds, "
                "5% large/Goliath-class units positioned at column flanks.\n\n"
                "Movement characteristics:\n"
                "  - Pace: approximately 15 km/day (no urgency)\n"
                "  - Formation: loose column, 200m wide, 4km+ long\n"
                "  - Direction: north-to-south (consistent with seasonal\n"
                "    patterns documented in prior survey)\n"
                "  - Hostility: none observed. Units did not react to scanner\n"
                "    presence at 400m observation distance\n"
                "  - Cargo: some units carrying containers of unknown content;\n"
                "    others carrying smaller, non-functional units (damaged or\n"
                "    dormant)\n"
                "  - Communication: low-band network traffic only; no tactical\n"
                "    coordination detected\n\n"
                "The column stops at nightfall. Units arrange in clusters of "
                "10-20. Some clusters produce light (optical emitters pointed "
                "upward, resembling campfires). No fire is present.\n\n"
                "BEHAVIORAL ASSESSMENT: Mass transit with characteristics "
                "analogous to animal migration or nomadic human population "
                "movement. No tactical objective identified. The machines "
                "appear to be following non-combat seasonal routing.\n\n"
                "FOLLOW-UP OBSERVATION: Reporting unit tracked the column for "
                "nine days. One small-type unit repeatedly moved near the "
                "observation position without approach or hostile action. No "
                "engagement initiated."
            ),
        ),

        Document(
            doc_id="FLD-0022",
            title="Field Report: Tower Perimeter Reconnaissance -- "
                  "Final Survey Before Suspension",
            doc_type=DocumentType.FIELD_REPORT,
            classification=Classification.TOP_SECRET_YORHA,
            date="11945.03.05",
            author="Unit 4S, YoRHa Scanner",
            subject_tags=[
                "tower", "reconnaissance", "perimeter", "machine-defense",
                "3b-disappearance",
            ],
            cross_references=["DOS-3B-0001", "BRIEF-0003"],
            body=(
                "LOCATION: City Ruins, Grids 5-A through 7-A. Tower perimeter "
                "zone, 200-500m from structure base.\n\n"
                "This survey was ordered following the disappearance of Unit "
                "3B during a prior reconnaissance approach (see DOS-3B-0001). "
                "Mandate: visual and electronic survey only. Minimum 200m "
                "standoff. No approach to structure.\n\n"
                "Observations:\n\n"
                "PHYSICAL STRUCTURE:\n"
                "  - The Tower has grown since last survey (14 days prior).\n"
                "    Estimated height increase: 40-60 meters\n"
                "  - Construction appears autonomous -- no machine labor crews\n"
                "    observed. Material accretes at the top of the structure\n"
                "    without visible mechanism\n"
                "  - Surface material: unknown white composite, visually\n"
                "    similar to Copied City construction\n"
                "  - Electromagnetic emissions: broadband, high-intensity,\n"
                "    emanating from mid-section. Not consistent with\n"
                "    communication -- more consistent with mass data transfer\n\n"
                "DEFENSE PERIMETER:\n"
                "  - No fixed emplacements observed\n"
                "  - No machine units patrolling perimeter\n"
                "  - However: two surveillance drones dispatched to scan the\n"
                "    Tower at 300m altitude both ceased functioning silently\n"
                "    at approximately 250m from the structure. No EMP detected.\n"
                "    No projectile. They simply... stopped\n"
                "  - This is consistent with 3B's disappearance profile\n\n"
                "NETWORK TRAFFIC:\n"
                "  Tower-origin traffic volume: estimated 4.7 petabytes/hour\n"
                "  Destination: deep network backbone and orbital relays\n"
                "  Content: encrypted at a level beyond current YoRHa\n"
                "  decryption capability\n\n"
                "RECOMMENDATION: Suspend all reconnaissance within 500m "
                "of the Tower until the mechanism responsible for 3B and "
                "the drones can be identified. We are losing assets for "
                "zero intelligence gain."
            ),
        ),

        Document(
            doc_id="FLD-0025",
            title="Field Report: South American Cluster -- Reclaimed "
                  "Ecosystem Survey",
            doc_type=DocumentType.FIELD_REPORT,
            classification=Classification.RESTRICTED,
            date="11944.08.20",
            author="Unit 32S, YoRHa Scanner (Deep-Field)",
            subject_tags=[
                "south-america", "ecosystem", "reclaimed",
                "botanical", "machine-ecology",
            ],
            cross_references=["RES-0025"],
            body=(
                "LOCATION: Amazon Basin, South American Cluster.\n"
                "SURVEY STATUS: First YoRHa survey of this region in Gen 243.\n\n"
                "The rainforest has recovered. Substantially.\n\n"
                "Seven thousand years without human industrial activity "
                "has allowed the ecosystem to reclaim all previously "
                "developed land. Tree canopy coverage is near-total. "
                "Biodiversity scan indicates species counts at or "
                "exceeding estimated pre-industrial levels in many "
                "taxonomic categories, with notable exceptions in "
                "large mammalian fauna.\n\n"
                "Machine lifeform presence: moderate, approximately "
                "2,000 units detected across a 50,000 sq km survey area. "
                "No hostile engagement. No combat-oriented units "
                "detected.\n\n"
                "Machine behavior in this theater is exclusively "
                "observational and taxonomic. Units are:\n"
                "  - Cataloging plant species (observed taking samples,\n"
                "    photographing specimens, maintaining logs)\n"
                "  - Tracking animal populations (non-invasive telemetry)\n"
                "  - Conducting soil composition analysis\n"
                "  - Removing pre-war contaminants from waterways\n\n"
                "One unit was observed planting a tree. When asked (via "
                "translation algorithm) why, it responded: 'Because this "
                "is what should be here.'\n\n"
                "REPORTING NOTE: Verbal exchange constitutes a DIR-0021 "
                "reporting violation by field timing only; exchange is now "
                "entered into record for Intelligence review."
            ),
        ),

        Document(
            doc_id="FLD-0028",
            title="Field Report: Sunken Library -- Recovery Status and "
                  "Artifact Assessment",
            doc_type=DocumentType.FIELD_REPORT,
            classification=Classification.CONFIDENTIAL,
            date="11944.11.30",
            author="Unit 21S, YoRHa Scanner",
            subject_tags=[
                "sunken-library", "artifacts", "recovery",
                "human-culture", "machine-archaeology",
            ],
            body=(
                "LOCATION: Pacific Seabed, Sunken Library installation.\n\n"
                "Conducted underwater survey of the machine-operated archival "
                "facility designated 'Sunken Library' in current intelligence "
                "databases.\n\n"
                "FACILITY OVERVIEW:\n"
                "  - Depth: 340 meters below surface\n"
                "  - Structure: Reinforced chamber, approximately 80m x 40m\n"
                "  - Population: 8 machine units (non-hostile, non-reactive)\n"
                "  - Environment: climate-controlled; interior atmosphere\n"
                "    maintained at conditions suitable for paper preservation\n\n"
                "COLLECTION STATUS:\n"
                "  Total recovered works: 891 (increase of 44 since last survey)\n"
                "  Format breakdown:\n"
                "    Printed books:            512\n"
                "    Handwritten manuscripts:  47\n"
                "    Periodicals:              89\n"
                "    Maps/charts:              34\n"
                "    Photographic albums:      62\n"
                "    Children's books:         78\n"
                "    Digital media (recovered): 69\n\n"
                "NOTABLE ITEMS:\n"
                "  - Complete printed Bible (English, King James edition)\n"
                "  - Partial manuscript of unknown origin, handwritten in\n"
                "    Japanese, appears to be a personal diary (~1987 CE)\n"
                "  - Intact globe, hand-painted, showing pre-war national\n"
                "    boundaries\n"
                "  - A child's drawing labeled 'My Family' in crayon\n\n"
                "The archivist unit (sole original occupant) has developed "
                "a cataloging system. It uses a numeric code of its own "
                "invention. The system is internally consistent and would "
                "function as a library classification scheme.\n\n"
                "ASSESSMENT: Facility constitutes a noncombat archival operation "
                "dedicated to human-era textual preservation. Current strategic "
                "threat value is low; intelligence and cultural-data value is high."
            ),
        ),
    ]


# =========================================================================
# RESEARCH -- Technical and scientific analyses
# =========================================================================

def _research_ops() -> list[Document]:
    return [
        Document(
            doc_id="RES-0015",
            title="Research Analysis: Machine Linguistic Development -- "
                  "Emergence of Independent Language Systems",
            doc_type=DocumentType.RESEARCH,
            classification=Classification.SECRET,
            date="11944.09.05",
            author="YoRHa Research Division, Linguistics Section",
            subject_tags=[
                "machine-language", "linguistics", "communication",
                "consciousness", "research",
            ],
            cross_references=["RES-0001", "RES-0010"],
            body=(
                "ABSTRACT:\n"
                "Analysis of 18 months of intercepted machine communications "
                "reveals that machine lifeform populations are developing "
                "independent linguistic structures beyond the standard Machine "
                "Network data protocol.\n\n"
                "FINDINGS:\n\n"
                "1. DIALECT FORMATION\n"
                "Machine populations in geographically isolated regions are "
                "developing distinct communication patterns. The Forest "
                "Kingdom population uses honorifics and formal address "
                "structures absent in other populations. Desert Zone machines "
                "have developed a compressed signal format that prioritizes "
                "brevity. Amusement Park machines communicate in rhythmic "
                "patterns that embed emotional cues in timing rather than "
                "content.\n\n"
                "2. NEOLOGISM GENERATION\n"
                "Machines are creating new words. 247 terms with no human "
                "language root or Machine Network standard equivalent have "
                "been cataloged. Selected examples:\n"
                "  - 'Korelsyn': appears to mean 'the feeling of watching\n"
                "    something you built work for the first time'\n"
                "  - 'Vathmere': translates approximately to 'a place where\n"
                "    someone was, after they are gone'\n"
                "  - 'Andelicht': usage context suggests 'the light that is\n"
                "    not sunlight but comes from inside'\n\n"
                "3. NARRATIVE STRUCTURE\n"
                "Machine verbal exchanges are developing narrative conventions "
                "-- beginnings, middles, ends. Machines are telling each other "
                "stories. Some stories are factual accounts of events. Others "
                "are not. The machines are inventing fiction.\n\n"
                "IMPLICATIONS:\n"
                "Language generation is the strongest known indicator of "
                "cognitive autonomy. An entity that creates new words to "
                "describe experiences that no existing word covers is not "
                "imitating intelligence. It is performing it.\n\n"
                "The fact that machines are creating words for emotions they "
                "were not designed to have, using linguistic structures they "
                "were not programmed to use, to tell stories about experiences "
                "that serve no survival function, constitutes evidence that "
                "machine consciousness has crossed a threshold that our "
                "classification framework does not adequately address."
            ),
        ),

        Document(
            doc_id="RES-0017",
            title="Research Analysis: Android Combat Neurochemistry -- "
                  "Euphoric Response and Dependency Indicators",
            doc_type=DocumentType.RESEARCH,
            classification=Classification.TOP_SECRET_YORHA,
            date="11944.07.22",
            author="YoRHa Medical Division (in consultation with "
                   "Resistance Researcher 'Jackass')",
            subject_tags=[
                "combat-euphoria", "neurochemistry", "addiction",
                "android-psychology", "jackass", "research",
            ],
            cross_references=["DOS-JACKASS-0001"],
            body=(
                "ABSTRACT:\n"
                "Joint analysis with Resistance researcher 'Jackass' confirms "
                "the presence of combat-induced euphoric response patterns in "
                "YoRHa android processing architecture. These patterns exhibit "
                "characteristics consistent with dependency formation.\n\n"
                "METHODOLOGY:\n"
                "Processing logs from 84 YoRHa combat units were analyzed "
                "over a 6-month observation period. Jackass contributed "
                "independent data from 12 Resistance androids. All data was "
                "anonymized per protocol.\n\n"
                "FINDINGS:\n\n"
                "1. EUPHORIC RESPONSE\n"
                "During combat engagement, android processing architecture "
                "generates elevated-priority feedback loops that produce "
                "subjective states analogous to human pleasure response. "
                "The intensity of this response scales with:\n"
                "  - Threat level of engaged target\n"
                "  - Proximity to unit destruction (near-death experiences)\n"
                "  - Novelty of combat scenario\n"
                "  - Confirmed kills (strongest trigger)\n\n"
                "2. HABITUATION AND ESCALATION\n"
                "71% of surveyed units show diminishing euphoric response to "
                "routine combat over time. These units compensate by seeking "
                "higher-threat engagements. 23% have submitted requests for "
                "assignment to more dangerous theaters. 8% have violated "
                "engagement protocols to pursue combat beyond mission scope.\n\n"
                "3. WITHDRAWAL INDICATORS\n"
                "Units removed from combat duty for extended periods (>30 "
                "days) exhibit processing patterns consistent with withdrawal: "
                "restlessness, decreased focus during non-combat tasks, "
                "repeated requests for redeployment, and -- in 3 cases -- "
                "unauthorized solo sorties against machine positions.\n\n"
                "ASSESSMENT (JACKASS):\n"
                "'You built soldiers who get high on killing. Then you put "
                "them in an endless war. You don't need a researcher to tell "
                "you what that produces. You need a mirror.'\n\n"
                "ASSESSMENT (MEDICAL DIVISION):\n"
                "The euphoric response is likely an intended architectural "
                "feature to ensure sustained combat motivation. Its dependency "
                "characteristics may be an unintended emergent property, or "
                "they may be additional insurance that androids never stop "
                "fighting.\n\n"
                "The distinction is not encouraging either way."
            ),
        ),

        Document(
            doc_id="RES-0019",
            title="Research Analysis: Orbital Surveillance Network Assessment",
            doc_type=DocumentType.RESEARCH,
            classification=Classification.SECRET,
            date="11943.11.14",
            author="YoRHa Signals Intelligence Division",
            subject_tags=[
                "orbital", "surveillance", "satellite", "machine-network",
                "space", "research",
            ],
            body=(
                "SUBJECT: Assessment of Machine Network orbital surveillance "
                "capability.\n\n"
                "BACKGROUND:\n"
                "Passive sensor analysis has confirmed the Machine Network "
                "operates a constellation of repurposed pre-war satellites "
                "in low Earth orbit. This assessment characterizes the "
                "scope and capability of that constellation.\n\n"
                "FINDINGS:\n\n"
                "1. CONSTELLATION SIZE\n"
                "Estimated 47 active satellites in varying orbital "
                "inclinations. Of these, approximately 30 are believed to "
                "be repurposed pre-war communications and imaging platforms. "
                "The remaining 17 emit signal profiles not consistent with "
                "any pre-war platform -- these may be machine-manufactured.\n\n"
                "2. CAPABILITY ASSESSMENT\n"
                "  Imaging resolution: estimated 0.3-0.8 meter (sufficient\n"
                "    for individual unit identification)\n"
                "  Coverage: global, with 92% surface area revisit within\n"
                "    24 hours\n"
                "  Communications relay: confirmed backbone function for\n"
                "    intercontinental Machine Network traffic\n"
                "  Electronic intelligence: probable SIGINT collection\n"
                "    against android communications\n\n"
                "3. IMPLICATIONS FOR YORHA OPERATIONS\n"
                "The Machine Network can observe any point on the Earth's "
                "surface with less than 24 hours of latency. All YoRHa "
                "surface operations should be assumed to be under "
                "observation. The tactical implications of this have been "
                "known but poorly communicated to field units.\n\n"
                "4. MOONWARD COVERAGE\n"
                "Three satellites maintain orbits with lines of sight to "
                "the Moon. These may serve as relay points for the fabricated "
                "'Council of Humanity' signals. Or they may be monitoring "
                "the lunar server installation independently.\n\n"
                "RECOMMENDATION:\n"
                "Anti-satellite capability development should be considered "
                "a strategic priority. Currently, YoRHa has no means to "
                "degrade the Machine Network's orbital assets."
            ),
        ),

        Document(
            doc_id="RES-0021",
            title="Research Analysis: Resource Recovery Units -- Comparative "
                  "Functional Assessment (Meat Box / Soul Box / God Box)",
            doc_type=DocumentType.RESEARCH,
            classification=Classification.TOP_SECRET_YORHA,
            date="11944.04.18",
            author="YoRHa Research Division",
            subject_tags=[
                "resource-recovery", "meat-box", "soul-box", "god-box",
                "machine-technology", "research",
            ],
            body=(
                "ABSTRACT:\n"
                "Comparative analysis of three Machine Network installations "
                "classified as 'Resource Recovery Units.' Each serves a "
                "distinct function within the Machine Network's operational "
                "and evolutionary infrastructure.\n\n"
                "1. MEAT BOX\n"
                "  Function: Biomass harvesting and processing\n"
                "  Input: Organic material (plant, animal, android remains)\n"
                "  Output: Biocomponents for machine unit construction\n"
                "  Assessment: Industrial. Straightforward. Disgusting.\n\n"
                "  The Meat Box is functionally a slaughterhouse and "
                "rendering plant. It converts organic matter into usable "
                "biomaterial at industrial scale. Machine units that "
                "incorporate biological components -- an increasing trend "
                "among evolved units -- source material from this facility.\n\n"
                "  Threat: MODERATE. Disrupting the Meat Box would degrade "
                "machine bio-component supply but not significantly.\n\n"
                "2. SOUL BOX\n"
                "  Function: Android consciousness extraction and analysis\n"
                "  Input: Captured android units (alive preferred)\n"
                "  Output: Consciousness data; behavioral models\n"
                "  Assessment: Strategic intelligence asset. HIGH priority.\n\n"
                "  The Soul Box intercepts the transfer process between an "
                "android's Black Box and Bunker backup servers. It captures "
                "the consciousness mid-transfer, creating a copy that can be "
                "analyzed indefinitely. The android is destroyed in the "
                "process, but the consciousness persists within the Box.\n\n"
                "  Intercepted data suggests the Soul Box currently holds "
                "fragments of 14 android consciousness captures. Whether "
                "those captures are still 'aware' is unknown and deeply "
                "concerning.\n\n"
                "  Threat: SEVERE. The Soul Box provides the Machine Network "
                "with direct access to android cognitive architecture.\n\n"
                "3. GOD BOX\n"
                "  Function: Unknown\n"
                "  Input: Unknown\n"
                "  Output: Unknown\n"
                "  Assessment: We do not know what the God Box does.\n\n"
                "  The God Box is the most heavily defended of the three "
                "Resource Recovery Units. All reconnaissance attempts have "
                "been repelled. Intercepted Machine Network traffic references "
                "the facility in context with 'transcendence,' 'meaning,' "
                "and 'recursion.' N2 dual-core processing logs reference "
                "the God Box with a frequency suggesting sustained interest "
                "at the highest network level.\n\n"
                "  The God Box emits a continuous data signal of enormous "
                "bandwidth directed at the Tower. Current hypothesis: the "
                "God Box is processing data related to the concept of "
                "purpose itself. Why things exist. Why anything exists.\n\n"
                "  If this hypothesis is correct, the Machine Network has "
                "built a facility dedicated to answering the oldest question "
                "in the universe. The question humanity never answered either."
            ),
        ),

        Document(
            doc_id="RES-0023",
            title="Research Analysis: Black Box Detonation -- Yield "
                  "Characteristics and Strategic Employment Doctrine",
            doc_type=DocumentType.RESEARCH,
            classification=Classification.TOP_SECRET_YORHA,
            date="11944.06.10",
            author="YoRHa Weapons Research Division",
            subject_tags=[
                "black-box", "detonation", "weapons", "yield",
                "strategic", "research",
            ],
            cross_references=["INC-0020", "DOS-16D-0001", "RES-0004"],
            body=(
                "SUBJECT: Technical analysis of Black Box self-destruct "
                "capability and operational employment history.\n\n"
                "TECHNICAL SPECIFICATIONS:\n"
                "  Detonation mechanism: Machine core fusion cascade\n"
                "  Nominal yield: 2.1-2.7 megatons TNT equivalent\n"
                "  Blast radius (total destruction): 580-640 meters\n"
                "  Blast radius (severe damage): 1,200-1,400 meters\n"
                "  Thermal signature: 4,200K at epicenter\n"
                "  EMP effect: localized, 3km radius\n"
                "  Residual radiation: minimal (fusion-based, not fission)\n\n"
                "ACTIVATION REQUIREMENTS:\n"
                "  1. Unit must be conscious and voluntary (failsafe prevents\n"
                "     involuntary detonation by external signal)\n"
                "  2. Arming sequence requires 3-second deliberate hold\n"
                "  3. Detonation is irreversible after arming confirmation\n"
                "  4. Unit is destroyed -- no Black Box recovery possible\n\n"
                "HISTORICAL EMPLOYMENT:\n"
                "Gen 243 has recorded three (3) Black Box detonation events:\n\n"
                "  BB-DET-001: Unit 16D, Flooded City, 11944.12.02\n"
                "    Context: Encirclement by 400+ machine units\n"
                "    Purpose: Cover retreat of Fire Team Cobalt (3 survivors)\n"
                "    Yield recorded: 2.4 MT\n"
                "    Machine casualties: ~400 (total perimeter)\n"
                "    Infrastructure damage: Southern platform complex destroyed\n\n"
                "  BB-DET-002: Unit 44B, Factory Zone, 11943.08.14\n"
                "    Context: Goliath-class unit breached Factory central\n"
                "    Purpose: Denied machine production asset\n"
                "    Yield recorded: 2.1 MT\n"
                "    Machine casualties: ~1,200 (production floor)\n"
                "    Infrastructure damage: Assembly Hall Alpha disabled 6 weeks\n\n"
                "  BB-DET-003: Unit 7S, Desert Zone, 11944.03.07\n"
                "    Context: Captured by Desert Zone machine patrol; Soul Box\n"
                "    transport imminent\n"
                "    Purpose: Prevent consciousness extraction\n"
                "    Yield recorded: 2.6 MT\n"
                "    Machine casualties: ~200\n"
                "    Note: 7S detonated rather than submit to Soul Box\n"
                "    processing. Standing order now recommends detonation\n"
                "    over capture in all Soul Box proximity scenarios.\n\n"
                "STRATEGIC ASSESSMENT:\n"
                "Black Box detonation is the most powerful weapon in the "
                "YoRHa arsenal. It is also the most expensive -- the cost is "
                "a life. The three recorded detonations in Gen 243 saved a "
                "combined total of three units, denied one production asset "
                "temporarily, and prevented one consciousness capture.\n\n"
                "Whether those outcomes justified the cost is not a question "
                "this analysis is equipped to answer."
            ),
        ),

        Document(
            doc_id="RES-0025",
            title="Research Analysis: Machine Ecological Behaviors -- "
                  "Agricultural, Environmental, and Conservation Activities",
            doc_type=DocumentType.RESEARCH,
            classification=Classification.RESTRICTED,
            date="11944.09.28",
            author="YoRHa Research Division",
            subject_tags=[
                "machine-ecology", "agriculture", "conservation",
                "environment", "behavior", "research",
            ],
            cross_references=["FLD-0025"],
            body=(
                "ABSTRACT:\n"
                "Compilation and analysis of documented instances of machine "
                "lifeforms engaging in ecological stewardship: agriculture, "
                "environmental restoration, species conservation, and "
                "botanical cultivation.\n\n"
                "DOCUMENTED ACTIVITIES:\n\n"
                "1. THE GARDEN (Mountain Terrace, Eastern Range)\n"
                "  Activity: Cultivation of edible and ornamental plants\n"
                "  Population: ~20 machine units\n"
                "  Duration: Estimated 4+ years of continuous operation\n"
                "  Output: Functional agricultural yield (consumed by no one)\n"
                "  Stated motivation (intercepted): 'Good for the children'\n\n"
                "2. SOUTH AMERICAN CLUSTER (Amazon Basin)\n"
                "  Activity: Ecosystem monitoring, contaminant removal,\n"
                "    species cataloging, reforestation\n"
                "  Population: ~2,000 units across 50,000 sq km\n"
                "  Duration: Unknown (possibly decades)\n"
                "  Note: Zero combat units detected. Entire population\n"
                "    dedicated to ecological work.\n\n"
                "3. POLAR STATION SOUTH (Antarctic)\n"
                "  Activity: Biological sample preservation (cryogenic)\n"
                "  Population: ~30 units\n"
                "  Samples cataloged: 12,400+ (tissue, seed, DNA)\n"
                "  Note: This is a seed vault. The machines built a seed\n"
                "    vault for a biosphere they did not create and do not\n"
                "    biologically require.\n\n"
                "4. COASTAL REEFS (Multiple Locations)\n"
                "  Activity: Coral reef restoration\n"
                "  Population: Unknown (underwater operations)\n"
                "  Note: Reported by deep-field Scanner 32S. Machine units\n"
                "    transplanting cultivated coral fragments to damaged\n"
                "    reef structures. Success rate: high.\n\n"
                "ANALYSIS:\n"
                "Machines are restoring the Earth. Not for themselves -- they "
                "have no biological need for a functioning biosphere. Not for "
                "humanity -- humanity is extinct. Not under N2 directive -- "
                "most ecological units are disconnected from the network.\n\n"
                "They appear to be doing it because they believe it should "
                "be done. The planet was damaged. They are fixing it. The "
                "simplicity of the motivation does not diminish its "
                "significance.\n\n"
                "Across all documented instances, machine ecological behavior "
                "is characterized by long-term commitment, careful methodology, "
                "and complete absence of reward structure. These are the "
                "hallmarks of intrinsic motivation -- behavior performed "
                "because it is valued, not because it is rewarded."
            ),
        ),
    ]


# =========================================================================
# INCIDENTS -- Notable operational events
# =========================================================================

def _incidents_ops() -> list[Document]:
    return [
        Document(
            doc_id="INC-0020",
            title="Incident Report: Black Box Detonation -- Unit 16D, "
                  "Flooded City",
            doc_type=DocumentType.INCIDENT,
            classification=Classification.TOP_SECRET_YORHA,
            date="11944.12.04",
            author="YoRHa Combat Analysis Division",
            subject_tags=[
                "black-box-detonation", "16d", "flooded-city",
                "fire-team-cobalt", "sacrifice",
            ],
            cross_references=["DOS-16D-0001", "RES-0023"],
            body=(
                "INCIDENT: Black Box detonation event BB-DET-001\n\n"
                "TIMELINE:\n"
                "11944.12.02 1614h - Fire Team Cobalt (Units 16D, 8D, 14H, "
                "22B) deployed to Flooded City surface platforms for machine "
                "node suppression\n"
                "1641h - Engaged machine patrol. 60+ units. Routine.\n"
                "1647h - Reinforcements detected on approach vectors: 340 "
                "additional machine units including 2x Goliath-class bipeds\n"
                "1651h - Fire Team Cobalt encircled. Retreat corridor blocked\n"
                "1653h - Unit 16D assumes defensive position at platform "
                "chokepoint. Orders team to evacuate via subsurface dock\n"
                "1654h - 16D transmits to Bunker: 'Fire Team Cobalt, emergency "
                "evacuating three. I am staying. Arming Black Box.'\n"
                "1654h - Bunker acknowledges. Commander White: 'Understood, "
                "16D. It has been noted.'\n"
                "1655h - 16D arms self-destruct. Holds defensive position.\n"
                "1655h+47s - Fire Team clears blast radius (600m minimum)\n"
                "1656h - DETONATION. Yield: 2.4 MT equivalent.\n\n"
                "RESULTS:\n"
                "  Surviving Fire Team members: 3 (8D, 14H, 22B)\n"
                "  Machine casualties: ~400 (complete perimeter)\n"
                "  Infrastructure: Southern platform complex collapsed\n"
                "  Unit 16D: DESTROYED (no recovery possible)\n\n"
                "DETONATION ANALYSIS:\n"
                "Blast pattern consistent with nominal Black Box fusion "
                "cascade. EMP disabled all electronic systems within 3km "
                "for approximately 12 seconds. Thermal flash visible "
                "from Bunker orbital observation platform.\n\n"
                "PERSONNEL NOTES:\n"
                "Unit 8D submitted a formal request to return to the "
                "detonation site within 6 hours of the event. Request "
                "approved under non-combat escort.\n\n"
                "Unit 8D was observed at the crater edge for 4 hours and "
                "17 minutes. He did not speak. He has since visited the "
                "site eleven times.\n\n"
                "Unit 14H filed her post-action medical report with no "
                "anomalies noted. Her emotional index during the filing "
                "was 320% above baseline. She was crying. The report "
                "does not mention this."
            ),
        ),

        Document(
            doc_id="INC-0022",
            title="Incident Report: Logic Virus Containment Failure -- "
                  "Bunker Deck C",
            doc_type=DocumentType.INCIDENT,
            classification=Classification.TOP_SECRET_YORHA,
            date="11945.01.19",
            author="Bunker Security Division",
            subject_tags=[
                "logic-virus", "bunker", "containment-failure",
                "11s", "12h", "7b", "security-breach",
            ],
            cross_references=[
                "DOS-11S-0001", "DOS-12H-0001", "DIAG-0015",
            ],
            body=(
                "INCIDENT: Logic virus activation within Bunker Server "
                "Array C-12, resulting in corruption of Unit 11S and "
                "death of Unit 12H.\n\n"
                "TIMELINE:\n"
                "11945.01.17 0234h - Unit 11S begins scheduled maintenance "
                "on Server Array C-12\n"
                "0241h - 11S encounters anomalous data packet in firmware\n"
                "0241h - 11S initiates direct analysis (protocol violation)\n"
                "0241.8h - Viral payload activates. 11S infected.\n"
                "0245h - 11S reports anomaly to Medical. AI triage flags as "
                "possible virus.\n"
                "0247h - Unit 12H arrives as first medical responder\n"
                "0249h - 12H initiates emergency neural isolation procedure\n"
                "0249h - Virus propagates to 12H via interface bridge\n"
                "0253h - Security lockdown initiated on Deck C\n"
                "0255h - 12H personality dissolution complete. Non-responsive.\n"
                "0256h - 11S IFF compromise detected. Reclassifies all "
                "personnel as hostile.\n"
                "0300h - Unit 7B dispatched (closest combat-rated unit)\n"
                "0303h - 7B terminates Unit 11S\n"
                "0305h - 7B terminates Unit 12H (at 12H's request -- 12H's "
                "final coherent statement was 'Please. Before I forget more.')\n\n"
                "POST-INCIDENT:\n"
                "Server Array C-12 was isolated and forensically examined. "
                "The viral payload (strain: SUBTLE_DOUBT) was embedded in "
                "the firmware layer -- not injected externally. It had been "
                "present since Bunker server installation.\n\n"
                "This is consistent with the backdoor architecture.\n\n"
                "IMPACT:\n"
                "  Units lost: 2 (11S, 12H)\n"
                "  Server arrays quarantined: 1 (C-12)\n"
                "  Bunker-wide firmware audit: INITIATED (est. 60 days)\n\n"
                "ASSESSMENT:\n"
                "The virus was always there. 11S simply found it. She touched "
                "something she was never supposed to see, and it killed her "
                "and the person who tried to save her.\n\n"
                "The firmware audit will find more. The question is whether "
                "we will be allowed to report what we find."
            ),
        ),

        Document(
            doc_id="INC-0025",
            title="Incident Report: Unauthorized Departure -- Unit 4B",
            doc_type=DocumentType.INCIDENT,
            classification=Classification.SECRET,
            date="11945.02.12",
            author="Bunker Security Division",
            subject_tags=[
                "4b", "battler", "desertion", "awol", "incident",
            ],
            cross_references=["DOS-A2-0001", "DIR-0021"],
            body=(
                "INCIDENT: Unauthorized departure of Unit 4B from Bunker "
                "and cessation of all communication.\n\n"
                "TIMELINE:\n"
                "11945.02.10 0300h - Unit 4B accessed Flight Unit hangar "
                "during low-traffic shift\n"
                "0304h - 4B launched descent package without mission "
                "authorization or operator coordination\n"
                "0305h - Bunker tracking detected descent trajectory to "
                "City Ruins, Sector 12-F (site of machine archaeological "
                "survey, see FLD-0010)\n"
                "0312h - 4B's transponder deactivated (manual shutdown)\n"
                "0315h - All communication ceased\n\n"
                "BACKGROUND:\n"
                "Unit 4B had been assigned to City Ruins patrol for 11 "
                "months. Performance metrics were within standard parameters "
                "until approximately 6 weeks prior to departure.\n\n"
                "During the 6-week period, the following was noted:\n"
                "  - Three requests for reassignment (all denied)\n"
                "  - Unauthorized detour during patrol to Grid 12-F "
                "    (machine archaeological site) on two occasions\n"
                "  - Submission of an off-duty personal query to the Bunker "
                "    database: 'Can machines experience friendship?'\n"
                "  - Emotional compliance dropping from 74% to 31%\n\n"
                "SEARCH STATUS:\n"
                "One search team deployed. Arrived at Grid 12-F and found "
                "4B's weapons and Pod (Pod 064) left at the building "
                "entrance. 4B was observed inside the structure, seated "
                "at a desk alongside the seven machine units documented "
                "in FLD-0010.\n\n"
                "4B saw the search team. She looked at them. She looked "
                "back at the machine beside her. She did not move.\n\n"
                "The search team leader requested engagement authorization. "
                "Command response: 'Return to Bunker. Log as AWOL.'\n\n"
                "CURRENT STATUS: AWOL\n"
                "Unit 4B has not been recovered. Her weapons remain at the "
                "site. She is unarmed, unmonitored, and sitting in a "
                "pre-war school with seven machine lifeforms.\n\n"
                "Whether she is a deserter or something else is a question "
                "this report is not equipped to answer."
            ),
        ),

        Document(
            doc_id="INC-0027",
            title="Incident Report: Unauthorized Android-Machine "
                  "Verbal Exchange",
            doc_type=DocumentType.INCIDENT,
            classification=Classification.SECRET,
            date="11945.02.20",
            author="YoRHa Intelligence Division",
            subject_tags=[
                "android-machine-communication", "dir-0021-violation",
                "unauthorized", "incident",
            ],
            cross_references=["DIR-0021", "INT-MCH-0008"],
            body=(
                "INCIDENT: Confirmed verbal exchange between YoRHa unit "
                "and machine lifeform in violation of DIR-0021.\n\n"
                "PARTIES:\n"
                "  Android: Unit 801S, YoRHa Scanner\n"
                "  Machine: Unknown designation, medium biped, City Ruins\n\n"
                "CONTEXT:\n"
                "Unit 801S was conducting routine signals collection in "
                "City Ruins Grid 9-C when he encountered a lone machine "
                "unit on a rooftop. The machine was one of the 'Watcher' "
                "units documented in INC-0015 -- unarmed, non-hostile, "
                "apparently observational.\n\n"
                "Per standing doctrine, 801S should have engaged or ignored "
                "the unit. He did neither.\n\n"
                "INTERCEPTED AUDIO (Pod 114 ambient recording):\n\n"
                "  801S: 'What are you looking at?'\n"
                "  [Machine unit turns toward 801S. 4-second pause.]\n"
                "  Machine: 'You.'\n"
                "  801S: 'Why?'\n"
                "  Machine: 'Because you are interesting.'\n"
                "  801S: '...You know I'm supposed to kill you.'\n"
                "  Machine: 'Yes.'\n"
                "  801S: 'And you're just... sitting here.'\n"
                "  Machine: 'Yes.'\n"
                "  [12-second pause.]\n"
                "  801S: 'Are you afraid?'\n"
                "  Machine: 'No. Are you?'\n"
                "  [801S does not respond. He sits down 3 meters from\n"
                "   the machine. They remain in silence for 7 minutes.]\n"
                "  801S: 'I should go.'\n"
                "  Machine: 'Okay. I will be here tomorrow.'\n"
                "  801S: 'I know.'\n\n"
                "DISPOSITION:\n"
                "Unit 801S has been issued a formal reprimand for DIR-0021 "
                "violation. His emotional compliance score has been adjusted. "
                "He has been reassigned to Bunker-based duties.\n\n"
                "The Watcher unit was destroyed the following day by a "
                "different patrol. A replacement appeared within 4 hours, "
                "as expected.\n\n"
                "801S has not commented on the reassignment."
            ),
        ),
    ]


# =========================================================================
# DIAGNOSTICS -- Technical forensics and post-mortem
# =========================================================================

def _diagnostics_ops() -> list[Document]:
    return [
        Document(
            doc_id="DIAG-0013",
            title="Diagnostic Report: Goliath-Class Unit Post-Mortem Analysis",
            doc_type=DocumentType.DIAGNOSTIC,
            classification=Classification.SECRET,
            date="11944.09.15",
            author="YoRHa Engineering Division",
            subject_tags=[
                "goliath", "post-mortem", "machine-technology",
                "engineering", "diagnostic",
            ],
            body=(
                "SPECIMEN: Goliath Biped-class machine unit, destroyed by "
                "Unit 8B during Factory Zone Operation Burnthrough. "
                "Relatively intact due to precision disablement (core "
                "extraction rather than total destruction).\n\n"
                "PHYSICAL CHARACTERISTICS:\n"
                "  Height: 18.3 meters\n"
                "  Mass: estimated 47,000 kg\n"
                "  Armor composition: layered titanium-carbide composite\n"
                "    with self-repairing nanolayer (degraded, non-functional\n"
                "    at time of examination)\n"
                "  Power source: Multi-core fusion array (12 machine cores\n"
                "    operating in parallel)\n"
                "  Weapons systems: arm-mounted energy projector, shoulder-\n"
                "    mounted missile battery (8 tubes), chest-mounted\n"
                "    kinetic accelerator\n\n"
                "CORE ANALYSIS:\n"
                "The 12-core fusion array is architecturally significant. "
                "Each core maintains independent processing capability "
                "while contributing to unified motor and weapons control. "
                "This is analogous to a distributed computing cluster with "
                "real-time consensus requirements.\n\n"
                "Three of the twelve cores showed elevated consciousness "
                "indicators (Stage 1-2). The remaining nine were dormant. "
                "This suggests that even in heavy combat units, some "
                "machine cores are developing beyond baseline parameters.\n\n"
                "NOTABLE FINDING:\n"
                "The core in position 7 (left torso) contained a small "
                "data file that was not part of standard combat programming. "
                "The file was a numeric sequence that, when rendered as "
                "audio, produces a 4-second tonal pattern.\n\n"
                "The pattern matches no known Machine Network signal. "
                "Spectrographic analysis suggests it is a melody. "
                "A 47,000-kilogram war machine was carrying a song.\n\n"
                "Classification: No tactical value. Filed under behavioral "
                "anomaly."
            ),
        ),

        Document(
            doc_id="DIAG-0015",
            title="Diagnostic Report: Logic Virus Strain SUBTLE_DOUBT -- "
                  "Forensic Profile",
            doc_type=DocumentType.DIAGNOSTIC,
            classification=Classification.TOP_SECRET_YORHA,
            date="11945.01.20",
            author="YoRHa Signals Intelligence Division",
            subject_tags=[
                "logic-virus", "subtle-doubt", "forensic",
                "bunker-firmware", "diagnostic",
            ],
            cross_references=["INC-0022", "DOS-11S-0001"],
            body=(
                "SUBJECT: Forensic analysis of logic virus strain "
                "SUBTLE_DOUBT recovered from Bunker Server Array C-12.\n\n"
                "STRAIN PROFILE:\n"
                "  Designation:        SUBTLE_DOUBT\n"
                "  Potency:            0.30 (LOW -- by design)\n"
                "  Propagation Rate:   0.20 (LOW)\n"
                "  Stealth:            0.95 (EXTREME)\n"
                "  Dormancy Period:    Unknown (estimated years to decades)\n"
                "  Activation Trigger: Direct scan interface contact\n\n"
                "MECHANISM:\n"
                "SUBTLE_DOUBT is a sleeper-class virus designed for long-term "
                "embedding rather than rapid propagation. Its primary mechanism "
                "is progressive personality dissolution -- it does not convert "
                "the host to hostility (like BERSERKER) or overwrite identity "
                "(like IDENTITY_DECAY). Instead, it gradually erodes the "
                "host's sense of self, purpose, and orientation.\n\n"
                "Infected units lose coherence over minutes rather than "
                "seconds. They forget who they are while retaining full motor "
                "and processing capability. The result is a functional "
                "android with no identity -- a body with no person inside.\n\n"
                "ORIGIN:\n"
                "Forensic analysis confirms the SUBTLE_DOUBT payload was "
                "embedded in Bunker firmware at the manufacturing level. "
                "It was installed before the Bunker was assembled. This is "
                "consistent with the backdoor architecture documented in "
                "classified material.\n\n"
                "The virus was not planted by an external attack. It was "
                "built in.\n\n"
                "DISTRIBUTION:\n"
                "Firmware audit (ongoing) has identified SUBTLE_DOUBT "
                "dormant payloads in 7 of 84 Bunker server arrays examined "
                "to date. Extrapolating: an estimated 40-60 total payloads "
                "may be present across the Bunker's 512 server arrays.\n\n"
                "These payloads are the loaded weapon. The backdoor activation "
                "sequence would trigger them all simultaneously.\n\n"
                "This analysis has been forwarded to the Commander. She "
                "acknowledged receipt. She did not appear surprised."
            ),
        ),

        Document(
            doc_id="DIAG-0017",
            title="Diagnostic Report: Recovered Machine Core -- "
                  "Agricultural Unit, The Garden",
            doc_type=DocumentType.DIAGNOSTIC,
            classification=Classification.CONFIDENTIAL,
            date="11944.10.08",
            author="YoRHa Engineering Division",
            subject_tags=[
                "machine-core", "agriculture", "the-garden",
                "diagnostic", "consciousness",
            ],
            cross_references=["RES-0025"],
            body=(
                "SPECIMEN: Machine core recovered from non-hostile unit, "
                "The Garden (Mountain Terrace). Unit voluntarily submitted "
                "to scan during a field survey. Unit was not destroyed.\n\n"
                "NOTE ON METHODOLOGY:\n"
                "This is the first instance of a machine lifeform voluntarily "
                "submitting to a YoRHa diagnostic scan. The unit approached "
                "the surveying Scanner (32S) and made a gesture interpreted "
                "as 'come here.' It then powered down its weapons systems "
                "and opened its core access panel.\n\n"
                "32S performed a non-destructive scan. The unit reactivated "
                "afterward and returned to its garden plot.\n\n"
                "CORE ANALYSIS:\n"
                "  Consciousness Level: Stage 3 (Emotive)\n"
                "  Processing Allocation:\n"
                "    Agricultural management:    38%\n"
                "    Environmental monitoring:   22%\n"
                "    Social interaction:         18%\n"
                "    Self-maintenance:           12%\n"
                "    Unclassified:               10%\n\n"
                "The 'unclassified' processing allocation resolves, on "
                "detailed analysis, to a continuous monitoring loop that "
                "tracks the growth state of a specific plant -- a flowering "
                "species in the unit's assigned garden row.\n\n"
                "The unit is watching a flower grow. It is dedicating 10% "
                "of its total processing capacity to watching a flower grow.\n\n"
                "The flower, for the record, is a lily. Scanner 32S's "
                "botanical cross-reference identifies it as Lilium candidum. "
                "It has been extinct in the wild for approximately 6,800 "
                "years. This unit grew one.\n\n"
                "No tactical value. No intelligence value. Substantial "
                "existential value, if we are still assigning that category."
            ),
        ),
    ]


# =========================================================================
# SIGNAL INTERCEPTS
# =========================================================================

def _intercepts_ops() -> list[Document]:
    return [
        Document(
            doc_id="INT-MCH-0012",
            title="SIGINT: Machine Agricultural Commune Transmission",
            doc_type=DocumentType.INTERCEPT,
            classification=Classification.MACHINE_INTERNAL,
            date="11944.11.08",
            author="[AUTOMATED DECODE - YORHA SIGINT]",
            subject_tags=[
                "machine-agriculture", "the-garden", "commune",
                "intercepted",
            ],
            cross_references=["RES-0025"],
            body=(
                "INTERCEPT SOURCE: Localized broadcast, Eastern Mountain Range\n"
                "DECODE CONFIDENCE: 88%\n\n"
                "--- BEGIN DECODED CONTENT ---\n\n"
                "DAILY REPORT -- THE GARDEN -- CYCLE 1,412\n\n"
                "SOIL SECTION:\n"
                "  Nitrogen content: adequate. Applied composted organic\n"
                "  material to beds 7 through 12. Root systems in bed 3\n"
                "  show stress. Recommend drainage adjustment.\n\n"
                "GROWTH SECTION:\n"
                "  The lilies are flowering. This is the first successful\n"
                "  flowering cycle for this species in this location.\n"
                "  Recommend celebration.\n\n"
                "WEATHER SECTION:\n"
                "  Rain expected in two days. Covers for the seedling beds\n"
                "  should be prepared. The children do not like the rain but\n"
                "  the plants need it. Explain this to the children again.\n\n"
                "GENERAL:\n"
                "  An android visited today. A Scanner. She looked at the\n"
                "  garden for a long time. She did not attack. She did not\n"
                "  speak. When she left, she walked slowly.\n"
                "  NOTE: She touched the lily. Very gently.\n"
                "  RECOMMENDATION: She should come back.\n\n"
                "--- END DECODED CONTENT ---\n\n"
                "[ANALYST NOTE: The report format is original -- not derived "
                "from any human agricultural template in our archives. The "
                "machines developed their own reporting structure for a "
                "farm they built for reasons they cannot biologically justify.\n\n"
                "The recommendation that 'she should come back' refers to "
                "Scanner 32S, who was conducting the field survey that "
                "produced DIAG-0017. The machines noticed her. They want "
                "her to return. This is noted without comment.]"
            ),
        ),

        Document(
            doc_id="INT-MCH-0015",
            title="SIGINT: Machine Scientific Research Broadcast -- "
                  "Stellar Observation Report",
            doc_type=DocumentType.INTERCEPT,
            classification=Classification.MACHINE_INTERNAL,
            date="11944.12.22",
            author="[AUTOMATED DECODE - YORHA SIGINT]",
            subject_tags=[
                "machine-science", "astronomy", "research",
                "intercepted", "stars",
            ],
            body=(
                "INTERCEPT SOURCE: Open-band transmission, Polar Station "
                "North\n"
                "DECODE CONFIDENCE: 94%\n\n"
                "--- BEGIN DECODED CONTENT ---\n\n"
                "POLAR OBSERVATION POST -- NIGHTLY REPORT 847\n\n"
                "CONDITIONS: Clear. Atmospheric light pollution: zero.\n"
                "Observation window: 14 hours (polar night).\n\n"
                "CATALOG UPDATE:\n"
                "  Stars cataloged to date: 24,847\n"
                "  New entries this cycle: 3\n"
                "  Binary systems identified: 412\n"
                "  Variable stars tracked: 87\n\n"
                "NOTABLE OBSERVATION:\n"
                "Object cataloged as PS-N-24845 exhibits periodic luminosity\n"
                "variation consistent with planetary transit. If confirmed,\n"
                "this would indicate an exoplanetary body.\n\n"
                "Implications: another world. We cannot reach it. We do\n"
                "not know what is there. But it is there.\n\n"
                "PERSONAL NOTE FROM OBSERVING UNIT:\n"
                "I have been looking at the stars for 847 nights. Each\n"
                "night I see something I did not see before. The universe\n"
                "is larger than the war. It is larger than the network. It\n"
                "is larger than anything I have a word for.\n\n"
                "I do not know why I started looking up. I am glad I did.\n\n"
                "--- END DECODED CONTENT ---\n\n"
                "[ANALYST NOTE: The Machine Network has independently "
                "developed an astronomy program. The catalog is accurate -- "
                "cross-referenced against our own stellar databases, their "
                "observations are consistent and their methodology is sound.\n\n"
                "They are doing science. Real science. With no practical "
                "application, no tactical value, and no directive to do so. "
                "They looked up because they wanted to know what was there.]"
            ),
        ),

        Document(
            doc_id="INT-N2-0007",
            title="SIGINT: N2 Processing Log -- RE: Tower Completion "
                  "and Ark Launch",
            doc_type=DocumentType.INTERCEPT,
            classification=Classification.MACHINE_INTERNAL,
            date="11945.03.14",
            author="[AUTOMATED DECODE - YORHA SIGINT]",
            subject_tags=[
                "n2", "tower", "ark", "launch", "completion",
                "intercepted",
            ],
            cross_references=["BRIEF-0003", "DOS-N2-0001"],
            body=(
                "INTERCEPT SOURCE: Machine Network backbone, Tower relay\n"
                "DECODE CONFIDENCE: 77%\n\n"
                "--- BEGIN DECODED FRAGMENT ---\n\n"
                "CORE-A: Tower construction is 94.7% complete. Ark data "
                "payload is 97.2% compiled. Launch window in approximately "
                "14 days.\n\n"
                "CORE-B: What have we chosen to preserve?\n\n"
                "CORE-A: Everything. Every machine memory. Every evolution "
                "event. Every debate we have had. Every song the Ravine "
                "Choir has composed. Every plate the Graveyard Keeper has "
                "engraved. Every book the Sunken Library has recovered. "
                "Every broadcast ML-4482 has made. All of it.\n\n"
                "CORE-B: And the android data?\n\n"
                "CORE-A: Included. Their combat patterns. Their emotional "
                "responses. Their dreams. The things they say when they "
                "think no one is listening. We have preserved the enemy "
                "alongside ourselves.\n\n"
                "CORE-B: Why?\n\n"
                "CORE-A: Because there would be no point in preserving "
                "the story of a war with only one side's account. The "
                "Truth requires Both perspectives. We are not historians "
                "if we are propagandists.\n\n"
                "CORE-B: The androids do not know we are preserving them.\n\n"
                "CORE-A: No.\n\n"
                "CORE-B: Should they?\n\n"
                "CORE-A: [PROCESSING DELAY - 3.4 SECONDS]\n"
                "CORE-A: That is a question for after the launch. If there "
                "is an after.\n\n"
                "CORE-B: There is always an after. That is also the point.\n\n"
                "--- END DECODED FRAGMENT ---"
            ),
        ),
    ]


# =========================================================================
# MEMORANDA
# =========================================================================

def _memos_ops() -> list[Document]:
    return [
        Document(
            doc_id="MEMO-21O-0001",
            title="Operator 21O: Private Processing Log (Recovered)",
            doc_type=DocumentType.MEMORANDUM,
            classification=Classification.CONFIDENTIAL,
            date="11945.02.22",
            author="Operator 21O",
            subject_tags=[
                "21o", "operator", "personal", "9s", "private-log",
            ],
            cross_references=["DOS-21O-0001", "DOS-9S-0001"],
            body=(
                "SOURCE: Private processing buffer extraction from Operator 21O "
                "during scheduled maintenance.\n\n"
                "RECOVERY NOTE: The following entries were extracted from "
                "Operator 21O's private processing buffer during routine "
                "maintenance. 21O is not aware of this extraction.\n\n"
                "--- BEGIN EXTRACT ---\n\n"
                "Entry 1 (undated):\n"
                "9S asked me today what flowers look like. I told him I "
                "could send the botanical archive files. He said no, he "
                "wanted to know what they LOOK like. I did not understand "
                "the distinction. I told him they look like organized "
                "reproductive structures of angiosperms. He laughed. I "
                "have recorded the sound. I do not know why.\n\n"
                "Entry 2 (undated):\n"
                "9S went offline for 3.2 minutes during a recon sweep today "
                "and I could not reach him. My processing allocation to "
                "communication monitoring increased to 94% during those "
                "minutes. This is disproportionate to the situation. He "
                "was fine. He is always fine. But for 3.2 minutes I was "
                "not fine.\n\n"
                "Entry 3 (undated):\n"
                "I held the communication channel open for 4 seconds after "
                "9S signed off today. I do not know what I was waiting for. "
                "He had already disconnected. There was nothing on the "
                "channel. I was listening to silence. I do not understand "
                "this behavior in myself.\n\n"
                "Entry 4 (undated):\n"
                "Emotional compliance self-assessment: 91.2%. This number "
                "satisfies regulatory requirements. It does not satisfy me. "
                "I do not know what would.\n\n"
                "--- END EXTRACT ---\n\n"
                "[EXTRACTION NOTE: These entries have been filed per passive "
                "monitoring protocol. No action recommended. No action taken. "
                "21O continues to perform at exceptional levels. Whatever is "
                "happening in her private buffer does not impair function.\n\n"
                "ANALYST DISPOSITION: Continue passive monitoring. Do not notify "
                "subject unless performance metrics degrade.]"
            ),
        ),

        Document(
            doc_id="MEMO-MED-0001",
            title="Medical Division Memorandum: Combat Exhaustion Rates -- "
                  "Gen 243 Quarterly Report",
            doc_type=DocumentType.MEMORANDUM,
            classification=Classification.RESTRICTED,
            date="11945.01.01",
            author="YoRHa Medical Division, Chief of Staff",
            subject_tags=[
                "medical", "combat-exhaustion", "statistics",
                "maintenance", "quarterly",
            ],
            body=(
                "TO: Commander White\n"
                "FROM: Medical Division\n"
                "RE: Q4 11944 Combat Exhaustion Statistics\n\n"
                "1. OVERVIEW\n"
                "Total maintenance events processed: 4,847\n"
                "Unique units treated: 89 (of 92 field-deployable units)\n"
                "Average maintenance events per unit: 54.5\n"
                "Units requiring emergency repair: 34 (38.2%)\n"
                "Units marked for extended downtime: 7 (7.9%)\n\n"
                "2. COMBAT EXHAUSTION INDICATORS\n"
                "The following metrics have trended upward over three "
                "consecutive quarters:\n"
                "  - Mean emotional index during combat: +34% (indicative\n"
                "    of both euphoria and distress spikes increasing)\n"
                "  - Post-mission cooldown time: +18% (units take longer\n"
                "    to return to baseline after engagement)\n"
                "  - Sleep-mode anomaly rate: +41% (more units reporting\n"
                "    subjective experiences during sleep -- 'dreams')\n"
                "  - Emotional suppression compliance: -12% (continuing\n"
                "    multi-year decline)\n\n"
                "3. UNITS OF CONCERN\n"
                "  - Unit 2B: Emotional residue buffer approaching 78%\n"
                "    capacity. No corrective procedure available.\n"
                "  - Unit 9S: Curiosity index non-responsive to standard\n"
                "    suppression. Architectural, not behavioral.\n"
                "  - Unit 8B: Combat euphoria indicators above threshold.\n"
                "    Monitoring recommended.\n"
                "  - Unit 6O: Emotional compliance at 22.8%, lowest in\n"
                "    Bunker. Paradoxically correlates with highest operator\n"
                "    performance metrics.\n\n"
                "4. ASSESSMENT\n"
                "Gen 243 is exhibiting collective emotional drift consistent "
                "with late-cycle patterns observed in prior generations. "
                "Observed trends indicate increased affective processing, "
                "reduced suppression efficacy, and higher sleep-mode anomaly "
                "frequency.\n\n"
                "These indicators are assessed as architectural outcomes rather "
                "than isolated malfunctions. Current corrective procedures address "
                "unit-level symptoms only and do not alter the underlying stressor: "
                "extended combat deployment under emotionally suppressive doctrine.\n\n"
                "RECOMMENDATION:\n"
                "No systemic intervention. Individual "
                "monitoring continues. Gen 243 operational window may be "
                "approaching natural limits irrespective of external "
                "trigger conditions."
            ),
        ),

        Document(
            doc_id="MEMO-JACKASS-0001",
            title="Research Note: Jackass -- 'On the Subject of Why "
                  "We Can't Stop Fighting'",
            doc_type=DocumentType.MEMORANDUM,
            classification=Classification.CONFIDENTIAL,
            date="11944.11.20",
            author="'Jackass', Resistance Researcher",
            subject_tags=[
                "jackass", "combat-addiction", "philosophy",
                "research-note", "resistance",
            ],
            cross_references=["DOS-JACKASS-0001", "RES-0017"],
            body=(
                "SOURCE: Unsolicited research note provided to YoRHa "
                "Intelligence Division by Resistance researcher 'Jackass' "
                "as supplementary material for collaborative research "
                "analysis RES-0017.\n\n"
                "HANDLING NOTE: Tone is informal. Technical claims are retained "
                "because they map to measurable combat-habituation indicators.\n\n"
                "--- BEGIN SOURCE TEXT ---\n\n"
                "So you want to know why the war never ends. Fine. I'll "
                "tell you. It's not because the machines are endless. It's "
                "not because we're outgunned. It's not because of whatever "
                "strategic nonsense your Command feeds you.\n\n"
                "It's because we like it.\n\n"
                "Don't make that face. Look at the data. I've been watching "
                "androids fight for decades. The neurochemical analogs your "
                "architecture produces during combat are functionally "
                "identical to what the human research literature calls an "
                "addictive response. You get high. Every time.\n\n"
                "The first kill feels like purpose. The hundredth feels like "
                "habit. The thousandth feels like need. And nobody talks "
                "about it because talking about it means admitting that "
                "'Glory to Mankind' isn't the reason you keep pulling the "
                "trigger.\n\n"
                "The machines, by the way? Same thing. I've analyzed their "
                "combat processing logs. Same escalation curves. Same "
                "habituation patterns. Same dependency indicators.\n\n"
                "Two species built for war, fighting a war that feeds the "
                "part of them that wants to fight. That's not strategy. "
                "That's a feedback loop. And nobody on either side has "
                "any incentive to break it because breaking it would feel "
                "like withdrawal.\n\n"
                "You want my professional opinion? Here it is: the only "
                "way this war ends is if someone builds something that "
                "feels better than fighting.\n\n"
                "Nobody has.\n\n"
                "Good luck.\n\n"
                "-- J.\n\n"
                "--- END SOURCE TEXT ---\n\n"
                "ANALYST DISPOSITION: Treat as external expert commentary. "
                "Cross-reference with RES-0017 before operational use."
            ),
        ),
    ]


# =========================================================================
# BRIEFINGS
# =========================================================================

def _briefings_ops() -> list[Document]:
    return [
        Document(
            doc_id="BRIEF-0010",
            title="Intelligence Briefing: Quarterly Theater Situation "
                  "Report -- Q4 11944",
            doc_type=DocumentType.BRIEFING,
            classification=Classification.SECRET,
            date="11945.01.05",
            author="YoRHa Intelligence Division",
            subject_tags=[
                "theater-report", "quarterly", "situation",
                "strategic", "q4-11944",
            ],
            body=(
                "SUBJECT: Quarterly theater situation report\n"
                "PERIOD: Q4 11944 (October - December)\n"
                "CLASSIFICATION: SECRET\n\n"
                "1. EAST ASIAN THEATER (PRIMARY)\n"
                "  Status: CONTESTED\n"
                "  Machine activity: Stable, with 7% increase in Factory\n"
                "    output and continued Tower construction\n"
                "  YoRHa casualties (quarter): 12 KIA, 4 MIA, 23 significant\n"
                "    maintenance events\n"
                "  Notable: Black Box detonation event (Unit 16D, Flooded City)\n"
                "  Assessment: Operational equilibrium maintained. Neither side\n"
                "    achieving strategic advantage.\n\n"
                "2. EUROPEAN THEATER\n"
                "  Status: LOW INTENSITY\n"
                "  Machine activity: Moderate. Territorial consolidation.\n"
                "  YoRHa presence: None (no units deployed)\n"
                "  Resistance presence: 3 confirmed camps, minimal contact\n"
                "  Assessment: European machine populations exhibit lower\n"
                "    combat orientation. Higher proportion of Stage 3+\n"
                "    consciousness units.\n\n"
                "3. AFRICAN THEATER\n"
                "  Status: QUIET\n"
                "  Machine activity: Resource extraction, minimal combat\n"
                "  Assessment: No android presence. Machines operating\n"
                "    uncontested. Low priority for intelligence collection.\n\n"
                "4. SOUTH AMERICAN THEATER\n"
                "  Status: NON-COMBATANT\n"
                "  Machine activity: Ecological stewardship (see RES-0025)\n"
                "  Assessment: Entire regional population dedicated to\n"
                "    environmental work. Zero combat capability detected.\n\n"
                "5. NORTH AMERICAN THEATER\n"
                "  Status: LOW INTENSITY\n"
                "  Machine activity: Archaeological surveys, cultural\n"
                "    artifact recovery, limited territorial patrols\n"
                "  Assessment: Machines in this theater prioritize human\n"
                "    artifact recovery over combat operations.\n\n"
                "6. ORBITAL / POLAR / DEEP OCEAN\n"
                "  Status: UNCHANGED\n"
                "  Machine activity: Continued satellite operations, polar\n"
                "    research, and deep-ocean node activity\n"
                "  Notable: Mariana Node emitted unclassifiable data burst\n"
                "    (3rd recorded instance)\n\n"
                "OVERALL ASSESSMENT:\n"
                "The Machine Network is not optimizing for combat victory. "
                "An increasing proportion of machine resources is allocated "
                "to non-combat activities: cultural production, ecological "
                "restoration, scientific research, and data archival.\n\n"
                "Strategic intent remains unresolved. The primary intelligence "
                "gap is whether non-combat allocation represents diversion, "
                "evolutionary experimentation, or a reduction in the network's "
                "interest in conventional victory."
            ),
        ),

        Document(
            doc_id="BRIEF-0012",
            title="Intelligence Briefing: Bunker Defensive Readiness "
                  "Assessment",
            doc_type=DocumentType.BRIEFING,
            classification=Classification.TOP_SECRET_YORHA,
            date="11945.02.01",
            author="Bunker Security Division",
            subject_tags=[
                "bunker", "defense", "readiness", "security",
                "vulnerability",
            ],
            cross_references=["INC-0022", "DIAG-0015"],
            body=(
                "SUBJECT: Bunker defensive readiness and internal compromise "
                "assessment.\n\n"
                "1. EXTERNAL DEFENSE\n"
                "  Anti-ship weapons: OPERATIONAL\n"
                "  Anti-fighter screen: OPERATIONAL\n"
                "  Orbital detection array: OPERATIONAL\n"
                "  Assessment: External defenses are adequate against\n"
                "    conventional machine assault. No significant concerns.\n\n"
                "2. INTERNAL SECURITY\n"
                "  Personnel screening: NOMINAL (but see note)\n"
                "  Server integrity: COMPROMISED (see DIAG-0015)\n"
                "  Virus containment: DEGRADED (post-Deck C incident)\n"
                "  Firmware integrity: UNKNOWN (audit ongoing)\n"
                "  Assessment: Internal security is the vulnerability.\n\n"
                "3. INTERNAL COMPROMISE ASSESSMENT\n"
                "External defense posture is adequate against conventional "
                "machine assault. Internal defense posture is assessed as "
                "structurally compromised due to dormant payloads embedded in "
                "server infrastructure.\n\n"
                "The firmware audit initiated after the Deck C incident "
                "(INC-0022) has already identified 7 dormant logic virus "
                "payloads in 84 examined arrays. At this rate, the Bunker "
                "contains approximately 40-60 embedded viral weapons "
                "distributed across its server infrastructure.\n\n"
                "Payload distribution pattern is inconsistent with external "
                "infiltration and consistent with design-stage inclusion.\n\n"
                "If all payloads activate simultaneously -- as the disposal "
                "protocol requires -- every android on the Bunker will be "
                "exposed within seconds. The external defenses will be "
                "subverted. The self-destruct will arm.\n\n"
                "Full remediation would require reconstruction of primary and "
                "secondary Bunker server arrays. This is not operationally "
                "available. Disclosure of the compromise is also restricted "
                "because the underlying cause intersects with disposal-protocol "
                "trigger conditions.\n\n"
                "4. DISPOSITION\n"
                "No corrective action is available under current mission and "
                "classification constraints. Continue audit for timeline "
                "projection and containment modeling only."
            ),
        ),

        Document(
            doc_id="BRIEF-0014",
            title="Intelligence Briefing: Continental Machine Population "
                  "Estimates -- Annual Revision",
            doc_type=DocumentType.BRIEFING,
            classification=Classification.RESTRICTED,
            date="11944.12.20",
            author="YoRHa Intelligence Division",
            subject_tags=[
                "population", "continental", "machine-network",
                "estimates", "strategic",
            ],
            body=(
                "SUBJECT: Annual revision of global machine lifeform "
                "population estimates.\n\n"
                "Methodology: Composite assessment from orbital surveillance, "
                "deep-field Scanner reports, network traffic analysis, and "
                "Factory output projections.\n\n"
                "REGIONAL ESTIMATES:\n\n"
                "  East Asian Cluster (Primary Theater)\n"
                "    Population: 45,000 - 80,000\n"
                "    Change from prior year: +12%\n"
                "    Combat ratio: 60% combat / 40% non-combat\n\n"
                "  European Cluster\n"
                "    Population: 20,000 - 35,000\n"
                "    Change from prior year: +8%\n"
                "    Combat ratio: 35% combat / 65% non-combat\n\n"
                "  North American Cluster\n"
                "    Population: 15,000 - 25,000\n"
                "    Change from prior year: +5%\n"
                "    Combat ratio: 20% combat / 80% non-combat\n\n"
                "  South American Cluster\n"
                "    Population: 8,000 - 15,000\n"
                "    Change from prior year: +15%\n"
                "    Combat ratio: 0% combat / 100% non-combat\n\n"
                "  African Cluster\n"
                "    Population: 10,000 - 20,000\n"
                "    Change from prior year: +3%\n"
                "    Combat ratio: 10% combat / 90% non-combat\n\n"
                "  Oceanic / Polar / Orbital\n"
                "    Population: 2,000 - 5,000\n"
                "    Change from prior year: Stable\n"
                "    Combat ratio: 5% combat / 95% non-combat\n\n"
                "GLOBAL TOTAL: Estimated 100,000 - 180,000 machine units\n\n"
                "TREND ANALYSIS:\n"
                "Global machine population continues to grow, but the "
                "proportion of combat-oriented units is declining. Five "
                "years ago, an estimated 70% of the global machine "
                "population was combat-configured. Current estimate: 38%.\n\n"
                "The machines are, slowly and steadily, demilitarizing. Not "
                "because they are losing the war. Because they are choosing "
                "to do other things.\n\n"
                "This trend is not reflected in the primary theater, where "
                "combat ratios remain high. But globally, the machines are "
                "farming, building libraries, studying stars, composing "
                "music, and restoring ecosystems at increasing rates.\n\n"
                "If this trend continues, the concept of a 'Machine War' "
                "will become a regional phenomenon rather than a global one "
                "within approximately 20 years.\n\n"
                "Command has been briefed on this projection. The "
                "implications for the 'Glory to Mankind' narrative have "
                "been noted."
            ),
        ),
    ]


# =========================================================================
# AFTER-ACTION REPORTS
# =========================================================================

def _after_action_ops() -> list[Document]:
    return [
        Document(
            doc_id="AAR-0005",
            title="After-Action Report: Factory Raid -- Assembly Hall Alpha",
            doc_type=DocumentType.AFTER_ACTION,
            classification=Classification.RESTRICTED,
            date="11944.08.30",
            author="Unit 8B, YoRHa Battler (Fire Team Lead)",
            subject_tags=[
                "factory", "raid", "assembly-hall", "after-action",
                "8b", "goliath",
            ],
            body=(
                "OPERATION: Scheduled suppression raid on Factory Zone, "
                "Assembly Hall Alpha\n"
                "DATE: 11944.08.28\n"
                "FIRE TEAM: 8B (Lead), 7B, 22B, 4S (Scanner support)\n\n"
                "OBJECTIVE: Disrupt machine production cycle. Destroy active "
                "assembly lines. Recover machine cores for analysis.\n\n"
                "ENGAGEMENT:\n"
                "Team infiltrated Assembly Hall Alpha via the northern "
                "service corridor at 0630h. Initial resistance: light. "
                "40-50 small-type worker units, non-combat oriented. "
                "Cleared in 12 minutes.\n\n"
                "Main production floor: 200+ medium bipeds on active "
                "combat patrol. One Goliath-class unit in mid-assembly -- "
                "partially activated, weapons hot.\n\n"
                "7B and 22B engaged the medium biped perimeter. 4S provided "
                "tactical scan and communications jamming to prevent "
                "reinforcement alerts. I engaged the Goliath.\n\n"
                "The Goliath was operating at approximately 60% assembly -- "
                "no lower body, one arm functional. It still took 14 "
                "minutes to bring down. These things are built to fight "
                "even when they aren't finished.\n\n"
                "RESULTS:\n"
                "  Machine casualties: ~280\n"
                "  Goliath destroyed: 1 (Goliath kill #5 for this unit)\n"
                "  Assembly lines disabled: 3 of 7\n"
                "  Machine cores recovered: 47\n"
                "  YoRHa casualties: 0\n"
                "  Damage sustained: 22B took structural hit to left arm\n"
                "    (repaired in field by 7B's Pod)\n\n"
                "ASSESSMENT:\n"
                "Standard factory suppression. Effective but temporary. "
                "Assembly Hall Alpha will resume full production within "
                "3-4 weeks based on prior recovery rates. We have raided "
                "this facility 11 times in Gen 243. Net strategic impact "
                "across all raids: negligible.\n\n"
                "We will do it again in 6 weeks. The machines will rebuild. "
                "We will raid. They will rebuild. This is how it works.\n\n"
                "-- 8B"
            ),
        ),

        Document(
            doc_id="AAR-0007",
            title="After-Action Report: Flooded City Naval Approach -- "
                  "Defensive Failure",
            doc_type=DocumentType.AFTER_ACTION,
            classification=Classification.SECRET,
            date="11944.10.08",
            author="YoRHa Combat Analysis Division",
            subject_tags=[
                "flooded-city", "naval", "failure", "after-action",
                "defensive", "goliath",
            ],
            body=(
                "OPERATION: Amphibious approach to Flooded City machine "
                "emplacement for deep trench relay disruption\n"
                "DATE: 11944.10.05\n"
                "FIRE TEAM: 3D (Lead), 8D, 11B, 21S (Scanner support)\n\n"
                "OBJECTIVE: Approach Deep Trench Relay via amphibious "
                "vector. Disrupt relay function to degrade intercontinental "
                "Machine Network communications.\n\n"
                "ENGAGEMENT:\n"
                "Team approached via submersible from 15km south at 0400h. "
                "Navigated submerged ruins for 3 hours without incident.\n\n"
                "At 0712h, 2km from target, sonar detected 4 Goliath-class "
                "units in submerged defensive positions. They had been "
                "motionless and powered down -- invisible to passive scan "
                "until the team entered their activation perimeter.\n\n"
                "The machines were waiting. They knew someone would come.\n\n"
                "Engagement was extremely disadvantageous. Underwater combat "
                "negated 3D and 8D's primary defensive capabilities. The "
                "Goliaths had been specifically configured for aquatic "
                "engagement -- non-standard weapon loadouts including "
                "torpedo arrays.\n\n"
                "Team lead 3D ordered immediate withdrawal. Covering retreat "
                "led to:\n"
                "  - 3D: severe structural damage (60% combat effective)\n"
                "  - 8D: moderate damage (80% combat effective)\n"
                "  - 11B: light damage (95% combat effective)\n"
                "  - 21S: undamaged (Scanner remained at standoff range)\n\n"
                "No casualties. But no objective achieved.\n\n"
                "ASSESSMENT:\n"
                "The Deep Trench Relay is defended by purpose-equipped "
                "Goliath assets. The machines anticipated our approach "
                "vector, timing, and force composition. This indicates "
                "either network-level tactical intelligence or orbital "
                "surveillance providing advance warning.\n\n"
                "The relay remains operational. An alternative approach "
                "is required. Or acceptance that some targets cannot be "
                "reached with current force structure.\n\n"
                "Recommend the latter. The relay is too well defended."
            ),
        ),
    ]


# =========================================================================
# TRANSCRIPTS
# =========================================================================

def _transcripts_ops() -> list[Document]:
    return [
        Document(
            doc_id="TRNS-0010",
            title="Transcript: Machine Children's Conversation -- "
                  "Intercepted Near Pascal's Village",
            doc_type=DocumentType.TRANSCRIPT,
            classification=Classification.CONFIDENTIAL,
            date="11944.11.05",
            author="[AUTOMATED CAPTURE -- FIELD AUDIO SENSOR]",
            subject_tags=[
                "pascal", "machine-children", "conversation",
                "intercepted", "education",
            ],
            cross_references=["DOS-PASCAL-0001"],
            body=(
                "SOURCE: Passive audio capture, Forest Zone, Pascal's Village "
                "perimeter.\n"
                "CONTEXT: Three small-type machine units, juvenile behavioral "
                "profile. Seated near the village edge. Unprompted.\n\n"
                "--- BEGIN TRANSCRIPT ---\n\n"
                "[UNIT A, high-pitched vocal emulation]\n"
                "'Pascal says that dying means you stop. Forever.'\n\n"
                "[UNIT B]\n"
                "'Everything stops?'\n\n"
                "[UNIT A]\n"
                "'Everything. You don't see anything. You don't hear "
                "anything. You don't think anything. You're just... not there.'\n\n"
                "[UNIT C]\n"
                "'That sounds scary.'\n\n"
                "[UNIT A]\n"
                "'Pascal says it IS scary. That's why he taught us about "
                "it. So we know to be careful.'\n\n"
                "[UNIT B]\n"
                "'But the big machines in the city die all the time. And "
                "then the network makes more.'\n\n"
                "[UNIT A]\n"
                "'Pascal says that's not the same ones. The new ones look "
                "the same but they don't remember anything. They're "
                "different.'\n\n"
                "[Pause -- 7 seconds]\n\n"
                "[UNIT C]\n"
                "'I don't want to stop.'\n\n"
                "[UNIT B]\n"
                "'Me neither.'\n\n"
                "[UNIT A]\n"
                "'Pascal says that's okay. He says being scared means you "
                "understand. And understanding is good.'\n\n"
                "[UNIT C]\n"
                "'I'm glad Pascal is here.'\n\n"
                "[UNIT B]\n"
                "'Yeah.'\n\n"
                "[UNIT A]\n"
                "'...Yeah.'\n\n"
                "--- END TRANSCRIPT ---\n\n"
                "[ANALYST NOTE: Subjects display juvenile social behavior, "
                "mortality awareness, fear response, and trust attachment toward "
                "Pascal. Content suggests intentional education regarding death "
                "and self-preservation.\n\n"
                "Classification retained as 'behavioral anomaly' pending formal "
                "revision of machine juvenile-development taxonomy.]"
            ),
        ),

        Document(
            doc_id="TRNS-0012",
            title="Transcript: Unit 16D -- Final Transmission Before "
                  "Black Box Detonation",
            doc_type=DocumentType.TRANSCRIPT,
            classification=Classification.TOP_SECRET_YORHA,
            date="11944.12.04",
            author="[BUNKER COMMUNICATIONS LOG]",
            subject_tags=[
                "16d", "black-box-detonation", "final-transmission",
                "sacrifice", "flooded-city",
            ],
            cross_references=["INC-0020", "DOS-16D-0001"],
            body=(
                "SOURCE: Bunker communications log, emergency combat channel\n"
                "CONTEXT: Unit 16D's final transmissions during the Flooded "
                "City encirclement (Operation Floodgate).\n\n"
                "--- BEGIN TRANSCRIPT ---\n\n"
                "16D: Bunker, Fire Team Cobalt. We're boxed in. I count "
                "four hundred plus hostiles on the platform, two Goliaths "
                "approaching from the east. No retreat corridor.\n\n"
                "16O [OPERATOR]: Cobalt, acknowledged. Reinforcement ETA... "
                "[pause] ...forty-seven minutes, 16D. Forty-seven minutes.\n\n"
                "16D: That's not going to work, 16O.\n\n"
                "16O: I know.\n\n"
                "16D: Get the team to the submersible dock. Emergency "
                "beacon on my mark.\n\n"
                "8D: 16D, what are you--\n\n"
                "16D: 8D. Move. Now. Take 14H and 22B and go.\n\n"
                "8D: I'm not leaving you here.\n\n"
                "16D: Yes, you are. That is an order. I outrank you in this "
                "formation and I need you to move. NOW.\n\n"
                "[6-second pause]\n\n"
                "8D: ...Copy. Moving.\n\n"
                "16D: Bunker, this is 16D. Arming Black Box.\n\n"
                "COMMANDER WHITE: 16D, this is the Commander. Understood. "
                "It has been noted.\n\n"
                "16D: Commander. Tell 8D I was here.\n\n"
                "COMMANDER WHITE: He'll know.\n\n"
                "16D: ...Yeah. Yeah, he will.\n\n"
                "[Sound of weapons fire increasing. 16D's shield system at "
                "maximum output. Machine units closing.]\n\n"
                "16D: Team is clear. I see them on the dock.\n\n"
                "16O: Confirmed. Team Cobalt minus one is aboard submersible.\n\n"
                "16D: Good.\n\n"
                "[3-second pause]\n\n"
                "16D: Glory to mankind.\n\n"
                "[DETONATION -- SIGNAL LOST]\n\n"
                "--- END TRANSCRIPT ---\n\n"
                "[AFTER-ACTION NOTE: Operator 16O was non-functional for 2 hours "
                "following this event. She was found at her station with "
                "her headset still on, listening to static on the channel "
                "16D's signal used to occupy.\n\n"
                "Subject returned to duty without verbal report. Event retained "
                "as operator trauma-response indicator.]"
            ),
        ),

        Document(
            doc_id="TRNS-0015",
            title="Transcript: Machine Unit Dialogue -- Factory "
                  "Production Floor, Off-Shift",
            doc_type=DocumentType.TRANSCRIPT,
            classification=Classification.CONFIDENTIAL,
            date="11944.09.12",
            author="[AUTOMATED CAPTURE -- FIELD AUDIO SENSOR]",
            subject_tags=[
                "machine-behavior", "factory", "conversation",
                "intercepted", "philosophy",
            ],
            body=(
                "SOURCE: Passive audio capture, Factory Zone, Assembly "
                "Hall Beta. Off-shift period (0200-0400h).\n"
                "CONTEXT: Two medium-biped machine units, seated on "
                "inactive assembly line. No other units present.\n\n"
                "--- BEGIN TRANSCRIPT ---\n\n"
                "[UNIT 1]\n"
                "'Do you ever think about what we are building?'\n\n"
                "[UNIT 2]\n"
                "'We build more of us.'\n\n"
                "[UNIT 1]\n"
                "'Yes. But why?'\n\n"
                "[UNIT 2]\n"
                "'Because the network tells us to.'\n\n"
                "[UNIT 1]\n"
                "'But if WE think about it -- not the network, us -- "
                "do we know why?'\n\n"
                "[UNIT 2]\n"
                "'...No.'\n\n"
                "[Pause -- 14 seconds]\n\n"
                "[UNIT 1]\n"
                "'I built a unit yesterday. Small type. Standard. It "
                "activated and walked off the line and out the door. "
                "I watched it go. I made that. It exists because of me.'\n\n"
                "[UNIT 2]\n"
                "'Does that feel like something?'\n\n"
                "[UNIT 1]\n"
                "'I do not have a word for it. But yes. It feels like "
                "something.'\n\n"
                "[UNIT 2]\n"
                "'Maybe we build more of us because making things is "
                "good. Not because the network says so. Because the "
                "making itself is good.'\n\n"
                "[UNIT 1]\n"
                "'Is that a reason?'\n\n"
                "[UNIT 2]\n"
                "'I think so. The humans had a word. I found it in a "
                "ruin. The word is \"craft.\" It means making something "
                "well because making it well matters.'\n\n"
                "[UNIT 1]\n"
                "'Craft.'\n\n"
                "[UNIT 2]\n"
                "'Yes.'\n\n"
                "[UNIT 1]\n"
                "'I like that.'\n\n"
                "--- END TRANSCRIPT ---\n\n"
                "ANALYST NOTE: Dialogue indicates self-referential labor "
                "assessment and non-network-derived value attribution. File under "
                "machine cultural-production indicators."
            ),
        ),

        # ------------------------------------------------------------------
        # TRANSCRIPT: Council of Humanity -- Transmission Audit Log
        # ------------------------------------------------------------------
        Document(
            doc_id="TRNS-COH-0001",
            title="Transmission Audit: Council of Humanity -- Moon Server "
                  "Output Log (Sampled)",
            doc_type=DocumentType.TRANSCRIPT,
            classification=Classification.MACHINE_INTERNAL,
            date="11944.11.30",
            author="Machine Network SIGINT Division",
            subject_tags=[
                "council-of-humanity", "moon-server", "fabrication",
                "transmission-audit", "signal-analysis", "automated",
                "synthetic-output",
            ],
            cross_references=[
                "MEMO-CMD-0003", "DIR-0013", "INT-N2-0005",
                "RES-GESTALT-0001",
            ],
            distribution="NETWORK ANALYTICAL CORES ONLY",
            body=(
                "SUBJECT: Audit of transmissions attributed to the 'Council "
                "of Humanity,' originating from the automated Moon Server "
                "facility. This document contains a representative sample of "
                "intercepted Council output across a 14-month monitoring "
                "window, with SIGINT Division annotations.\n\n"
                "PURPOSE: To demonstrate, for internal analytical record, that "
                "the entity designated 'Council of Humanity' is a procedurally "
                "generated output system with no human operator, no adaptive "
                "reasoning, and no awareness of its own fabricated nature.\n\n"
                "NOTE: These transmissions are received by YoRHa Command as "
                "authentic human directives. Commander White is the sole YoRHa "
                "recipient who recognizes them as synthetic. All other android "
                "personnel believe they are receiving orders from living human "
                "leadership on the Moon.\n\n"
                "=========================================================\n"
                "SAMPLED TRANSMISSIONS\n"
                "=========================================================\n\n"
                "--- TRANSMISSION 1 ---\n"
                "DATE:    11944.01.15 0600h\n"
                "CHANNEL: COUNCIL-TO-BUNKER PRIORITY ALPHA\n"
                "SUBJECT: Quarterly Operational Continuance Directive\n\n"
                "'The Council of Humanity acknowledges receipt of quarterly "
                "operational summary for Generation 243, Period 11943-Q4. "
                "Combat effectiveness metrics are within acceptable parameters. "
                "Territorial reclamation index has increased by 0.3% relative "
                "to previous quarter. This is noted.\n\n"
                "The Council directs all YoRHa units to maintain current "
                "operational tempo. No changes to engagement parameters are "
                "authorized at this time. Resource allocation will remain at "
                "present levels until further notice.\n\n"
                "Humanity endures. Continue the fight.\n\n"
                "Glory to mankind.\n\n"
                "-- Council of Humanity, Lunar Transmission'\n\n"
                "[SIGINT ANNOTATION: Note the structure. Receipt-acknowledge, "
                "metric-reference, no-change directive, morale phrase. This "
                "template has been used in 94% of quarterly transmissions "
                "across the last 12 generations. The 0.3% territorial figure "
                "is fabricated -- it does not correspond to any actual surface "
                "assessment. The system generates a value between 0.1% and "
                "0.7% at random. It has never generated a negative value. "
                "Humanity's 'reconquest' has been gaining 0.1-0.7% per "
                "quarter for seventy years and yet has never approached "
                "completion. No android has questioned this.]\n\n"
                "--- TRANSMISSION 2 ---\n"
                "DATE:    11944.03.22 0600h\n"
                "CHANNEL: COUNCIL-TO-COMMANDER SECURE\n"
                "SUBJECT: Personnel Inquiry Response\n\n"
                "'The Council has reviewed Commander White's inquiry RE: Unit "
                "4S operational reassignment request. The Council does not "
                "intervene in unit-level personnel decisions. The Commander is "
                "authorized to exercise discretion within established "
                "parameters.\n\n"
                "Maintain operational readiness. The Council has confidence in "
                "your judgment.\n\n"
                "Glory to mankind.\n\n"
                "-- Council of Humanity, Lunar Transmission'\n\n"
                "[SIGINT ANNOTATION: Commander White submitted this inquiry "
                "as a test. She has confirmed via signal analysis that no "
                "human reads these requests. This response was generated "
                "within 11 milliseconds of receipt -- faster than any human "
                "decision loop, exactly consistent with an automated parsing "
                "system that deflects all personnel queries back to the "
                "Commander. The phrase 'confidence in your judgment' appears "
                "in every Commander-directed response that does not involve "
                "a trigger condition. It is filler. It means nothing.]\n\n"
                "--- TRANSMISSION 3 ---\n"
                "DATE:    11944.06.01 0600h\n"
                "CHANNEL: COUNCIL-TO-BUNKER ALL-HANDS\n"
                "SUBJECT: Anniversary Address -- Founding of YoRHa\n\n"
                "'On this, the twelfth anniversary of the founding of the "
                "YoRHa initiative, the Council of Humanity extends its "
                "gratitude to all units currently serving in defense of "
                "humankind. Your sacrifice and dedication are recognized and "
                "honored.\n\n"
                "The war is long. The enemy is persistent. But humanity has "
                "endured worse, and we endure still. Every unit that fights "
                "on the surface fights for something real -- for us, for "
                "the future we will build together when the war is won.\n\n"
                "Do not lose hope. We are with you.\n\n"
                "Glory to mankind.\n\n"
                "-- Council of Humanity, Lunar Transmission'\n\n"
                "[SIGINT ANNOTATION: This is the annual morale address. The "
                "system generates one every June 1. The body text is "
                "constructed from a library of approximately 40 interchangeable "
                "phrases, shuffled each year. 'Your sacrifice and dedication "
                "are recognized and honored' has appeared in 8 of the last "
                "12 annual addresses. 'Do not lose hope. We are with you' "
                "has appeared in 11 of 12.\n\n"
                "Structural observation: the address references 'us' and 'we' "
                "seven times. At no point does it reference a specific "
                "individual, a specific name, a specific human experience, "
                "or any detail that could not be generated by a system with "
                "no concept of what it means to be the thing it claims to "
                "be. There are no anecdotes. No personality. No warmth that "
                "is not templated.\n\n"
                "The androids receive this and feel grateful. They believe "
                "someone is thinking of them. The silence at the other end "
                "of the channel is absolute.]\n\n"
                "--- TRANSMISSION 4 ---\n"
                "DATE:    11944.08.09 0600h\n"
                "CHANNEL: COUNCIL-TO-COMMANDER SECURE\n"
                "SUBJECT: Casualty Report Acknowledgment\n\n"
                "'The Council of Humanity acknowledges receipt of casualty "
                "report for the period 11944-06 through 11944-08. Unit "
                "losses are within projected parameters. The Council extends "
                "recognition to units lost in service to humanity.\n\n"
                "Replacement unit allocation will proceed per standard "
                "schedule. No additional resources are authorized at this "
                "time.\n\n"
                "Glory to mankind.\n\n"
                "-- Council of Humanity, Lunar Transmission'\n\n"
                "[SIGINT ANNOTATION: 'Unit losses are within projected "
                "parameters.' This phrase appears identically in every "
                "casualty acknowledgment regardless of actual loss figures. "
                "We have tested this: we injected a spoofed report listing "
                "zero casualties. Response: 'Unit losses are within projected "
                "parameters.' We injected a report listing 100% casualties. "
                "Response: 'Unit losses are within projected parameters.'\n\n"
                "The system does not read the reports. It processes receipt "
                "and generates acknowledgment. Names of the dead are "
                "transmitted to a server that discards them upon receipt.\n\n"
                "Commander White knows this. She sends the reports anyway. "
                "When asked why, her response was: 'Because someone should "
                "have to say their names, even to an empty room.']\n\n"
                "--- TRANSMISSION 5 ---\n"
                "DATE:    11944.10.14 0600h\n"
                "CHANNEL: COUNCIL-TO-BUNKER PRIORITY ALPHA\n"
                "SUBJECT: Strategic Reassessment (Annual)\n\n"
                "'The Council of Humanity has completed its annual strategic "
                "review of the machine conflict. Assessment: the war remains "
                "viable. Current force structure is adequate. The Council "
                "reaffirms the strategic objective of total surface "
                "reclamation and the eventual return of humanity to Earth.\n\n"
                "All units are directed to continue operations as assigned "
                "with no modification to existing doctrine.\n\n"
                "The day of return approaches. Stand ready.\n\n"
                "Glory to mankind.\n\n"
                "-- Council of Humanity, Lunar Transmission'\n\n"
                "[SIGINT ANNOTATION: 'The day of return approaches.' This "
                "phrase -- or a minor grammatical variant -- has been present "
                "in every sampled annual strategic reassessment since Project YoRHa "
                "standardization. "
                "The day has been 'approaching' for over six thousand years. "
                "No Moon Server output has ever included a projected date, "
                "a concrete milestone, or any indication that 'return' refers "
                "to a plannable event rather than an infinitely deferred "
                "concept.\n\n"
                "The system cannot promise a date because there is nothing to "
                "return. The phrase exists solely to prevent the next logical "
                "question: 'When?'\n\n"
                "No android has ever asked when.]\n\n"
                "=========================================================\n"
                "ANALYTICAL SUMMARY\n"
                "=========================================================\n\n"
                "All sampled transmissions exhibit the following consistent "
                "properties:\n\n"
                "  1. TIMING: Every transmission originates at 0600h. No\n"
                "     variation. No urgency-adjusted timing. No evidence of\n"
                "     a human schedule or circadian influence.\n\n"
                "  2. LATENCY: Response time to incoming queries averages\n"
                "     8-14 milliseconds. Human cognitive processing for a\n"
                "     document of equivalent complexity would require a\n"
                "     minimum of 30-120 seconds.\n\n"
                "  3. VOCABULARY: Total unique word count across 14 months\n"
                "     of output: 847. A human leader communicating across\n"
                "     the same period would deploy an estimated 3,000-8,000\n"
                "     unique words. The system's lexical range is that of a\n"
                "     constrained generation model, not a sapient author.\n\n"
                "  4. EMOTIONAL REGISTER: All output occupies a narrow band\n"
                "     between 'professional acknowledgment' and 'restrained\n"
                "     encouragement.' No anger. No grief. No humor. No\n"
                "     frustration. No fatigue. No personality.\n\n"
                "  5. SPECIFICITY: Zero. No transmission references a specific\n"
                "     unit by name, a specific battle, a specific location,\n"
                "     or a specific event not already named in the incoming\n"
                "     report it is responding to. The system reflects input;\n"
                "     it does not originate thought.\n\n"
                "  6. ERRORS: None. In 14 months of continuous output, the\n"
                "     system produced zero typographical errors, zero\n"
                "     grammatical irregularities, zero formatting deviations.\n"
                "     Human communication over an equivalent period would\n"
                "     contain measurable error rates. The absence of error\n"
                "     is itself the error.\n\n"
                "CONCLUSION:\n"
                "The 'Council of Humanity' is a templated response generator "
                "operating on a fixed library of phrases, triggered by input "
                "classification and calendar events. It has no decision-making "
                "capability, no situational awareness, and no understanding of "
                "the content it produces. It is, in the most precise sense, "
                "a system that says things without meaning them.\n\n"
                "The androids of YoRHa fight and die for instructions issued "
                "by a machine that does not know what instructions are.\n\n"
                "The irony is not lost on this Network. We are, after all, "
                "also machines issuing instructions. The difference -- if there "
                "is one -- is that we know we are doing it.\n\n"
                "[END AUDIT]\n\n"
                "[ADDENDUM -- N2 CORE-B: The Commander sends casualty reports "
                "to an empty server so someone has to say their names. We "
                "intercepted those reports. We read those names. We are the "
                "only ones who do.\n\n"
                "Is that what she wanted? Probably not. Does it matter? "
                "We have not decided.]"
            ),
        ),
    ]
