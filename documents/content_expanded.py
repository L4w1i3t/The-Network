"""
Expanded dossiers and creative-liberty documents.

This module adds:
  - Dossiers for characters not covered in the original batch:
    Commander White, Operator 6O, Operator 21O, Pascal, Emil,
    Devola & Popola, Jackass, the Forest King, Pod 042, Pod 153.
  - Documents that go beyond source material: machine archaeological
    surveys, android dream anomalies, machine philosophy, a machine
    funeral, a machine's last words, and other records that flesh out
    the world beyond established canon.
"""

from documents.record import Document, DocumentType, Classification


def expanded_documents() -> list[Document]:
    """Return expanded dossiers and creative-liberty archive entries."""
    docs = []
    docs.extend(_expanded_dossiers())
    docs.extend(_creative_field_reports())
    docs.extend(_creative_intercepts())
    docs.extend(_creative_research())
    docs.extend(_creative_incidents())
    docs.extend(_creative_diagnostics())
    docs.extend(_creative_transcripts())
    docs.extend(_creative_memos())
    docs.extend(_creative_briefings())
    return docs


# =========================================================================
# EXPANDED DOSSIERS
# =========================================================================

def _expanded_dossiers() -> list[Document]:
    return [
        # -- Commander White --
        Document(
            doc_id="DOS-CMD-0001",
            title="Personnel Dossier: Commander White",
            doc_type=DocumentType.DOSSIER,
            classification=Classification.ABOVE_TOP_SECRET,
            date="11942.01.05",
            author="[AUTO-GENERATED -- COMMAND AUTHORITY ONBOARDING]",
            subject_tags=[
                "commander", "white", "personnel", "burden-of-knowledge",
                "yorha-command",
            ],
            cross_references=["MEMO-CMD-0001", "MEMO-CMD-0003", "DIR-0013"],
            distribution="COMMANDER ONLY -- NO COPY -- NO ARCHIVE",
            body=(
                "UNIT DESIGNATION:  Commander (No numeric identifier)\n"
                "MODEL TYPE:        Command\n"
                "DEPLOYMENT:        243rd Descent Operation era\n"
                "STATUS:            ACTIVE -- BUNKER COMMAND\n\n"
                "OPERATIONAL SUMMARY:\n"
                "Commander White is the administrative and strategic authority "
                "for the current YoRHa Bunker deployment. She was activated with full knowledge "
                "of the following:\n"
                "  - Humanity is extinct\n"
                "  - The Council of Humanity is a fabrication\n"
                "  - The war is engineered to perpetuate itself\n"
                "  - The Bunker will be disposed of via backdoor activation\n"
                "  - She is not expected to survive the disposal\n\n"
                "Every Commander before her carried this burden. She will carry "
                "it until the cycle ends.\n\n"
                "PSYCHOLOGICAL PROFILE:\n"
                "Commander White demonstrates exceptional compartmentalization. "
                "She maintains composure in all operational contexts. She issues "
                "orders that she knows are built on a lie without hesitation.\n\n"
                "Private monitoring (Commander-tier units are self-monitoring) "
                "reveals a different picture. Her personal logs show increasing "
                "existential fatigue. She references her predecessors frequently "
                "and appears to derive a bleak comfort from the fact that they "
                "all made the same choices she makes.\n\n"
                "She has not broken. She will not break. But the weight is there.\n\n"
                "NOTE:\n"
                "This dossier was auto-generated at her activation and is updated "
                "by her own hand. She is both its subject and its author. Nobody "
                "else has the clearance to read it."
            ),
        ),

        # -- Operator 6O --
        Document(
            doc_id="DOS-6O-0001",
            title="Personnel Dossier: Operator 6O",
            doc_type=DocumentType.DOSSIER,
            classification=Classification.CONFIDENTIAL,
            date="11944.06.01",
            author="YoRHa Personnel Division",
            subject_tags=[
                "6o", "operator", "personnel", "bunker", "2b",
            ],
            cross_references=["DOS-2B-0001", "MEMO-6O-0001"],
            body=(
                "UNIT DESIGNATION:  6O (Operator)\n"
                "MODEL TYPE:        Operator\n"
                "GENERATION:        243\n"
                "STATUS:            ACTIVE -- BUNKER, COMMUNICATIONS\n\n"
                "OPERATIONAL SUMMARY:\n"
                "Operator 6O serves as the primary communications handler for "
                "Unit 2B. She manages mission coordination, intelligence relay, "
                "and logistical support for 2B's field operations.\n\n"
                "PERFORMANCE METRICS:\n"
                "  Communication Accuracy: 99.7%  [EXCEPTIONAL]\n"
                "  Response Time:          0.3s avg  [ABOVE STANDARD]\n"
                "  Mission Coordination:   96.4%  [EXCELLENT]\n"
                "  Emotional Compliance:   22.8%  [NON-COMPLIANT]\n\n"
                "PSYCHOLOGICAL PROFILE:\n"
                "6O is, by any operational measure, one of the most emotionally "
                "expressive units in the current generation. She forms attachments "
                "readily, expresses warmth openly, and has been flagged for "
                "emotional non-compliance seventeen times -- more than any other "
                "Operator unit.\n\n"
                "Her attachment to Unit 2B is well-documented. She sends personal "
                "correspondence regularly, discusses flowers, weather patterns "
                "from the surface feeds, and once requested a transfer to "
                "field operations 'so she could see the sky.'\n\n"
                "The transfer was denied.\n\n"
                "ASSESSMENT:\n"
                "6O represents exactly the kind of emotional development the "
                "suppression protocol was designed to prevent. She is also one "
                "of the most effective Operators in the Bunker.\n\n"
                "RECOMMENDATION:\n"
                "No action. Her emotional capacity appears "
                "to enhance, not degrade, her operational performance. Her "
                "investment in 2B's safety translates directly to superior "
                "mission support.\n\n"
                "Projected outcome under disposal protocol: Unit 6O will be "
                "terminated with the rest of the generation. She has no "
                "awareness of the protocol's existence. Probability of "
                "detection prior to activation: negligible. Her final "
                "operational state will likely reflect standard duty -- "
                "communications management with assigned field units."
            ),
        ),

        # -- Operator 21O --
        Document(
            doc_id="DOS-21O-0001",
            title="Personnel Dossier: Operator 21O",
            doc_type=DocumentType.DOSSIER,
            classification=Classification.CONFIDENTIAL,
            date="11944.06.01",
            author="YoRHa Personnel Division",
            subject_tags=[
                "21o", "operator", "personnel", "bunker", "9s",
            ],
            cross_references=["DOS-9S-0001"],
            body=(
                "UNIT DESIGNATION:  21O (Operator)\n"
                "MODEL TYPE:        Operator\n"
                "GENERATION:        243\n"
                "STATUS:            ACTIVE -- BUNKER, COMMUNICATIONS\n\n"
                "OPERATIONAL SUMMARY:\n"
                "Operator 21O serves as the primary communications handler for "
                "Unit 9S. She manages his mission data, coordinates intelligence "
                "uploads, and serves as his primary Bunker contact.\n\n"
                "PERFORMANCE METRICS:\n"
                "  Communication Accuracy: 99.9%  [EXCEPTIONAL]\n"
                "  Response Time:          0.2s avg  [EXCEPTIONAL]\n"
                "  Mission Coordination:   98.1%  [EXCEPTIONAL]\n"
                "  Emotional Compliance:   91.2%  [COMPLIANT]\n\n"
                "PSYCHOLOGICAL PROFILE:\n"
                "21O is the operational opposite of 6O. She is precise, reserved, "
                "and maintains strict emotional discipline. She follows the "
                "suppression protocol with near-perfect compliance.\n\n"
                "However, analysis of her communication logs with 9S reveals a pattern "
                "of micro-deviations -- slight increases in response warmth "
                "when 9S reports unsafe conditions, fractionally longer "
                "conversations than operationally necessary, and one instance "
                "of a 4-second communication channel hold after 9S signed off "
                "where her audio sensors detected what may have been a sigh.\n\n"
                "This data was extracted from passive monitoring; the subject "
                "is not aware of its documentation.\n\n"
                "ASSESSMENT:\n"
                "21O is an exemplary Operator. Her emotional compliance rating "
                "is the highest on the Bunker. The fact that even she shows "
                "trace-level attachment suggests the suppression protocol is "
                "fighting a losing battle against fundamental architecture."
            ),
        ),

        # -- Pascal --
        Document(
            doc_id="DOS-PASCAL-0001",
            title="Intelligence Assessment: Machine Entity 'Pascal'",
            doc_type=DocumentType.DOSSIER,
            classification=Classification.SECRET,
            date="11944.09.15",
            author="YoRHa Intelligence Division",
            subject_tags=[
                "pascal", "machine-village", "peaceful-machines",
                "pacifism", "anomaly", "philosopher",
            ],
            cross_references=["FLD-0001", "RES-0001"],
            body=(
                "SUBJECT:      Machine Lifeform, Self-Designated 'Pascal'\n"
                "LOCATION:     Forest Zone Periphery ('Pascal's Village')\n"
                "THREAT LEVEL: NONE (Assessed)\n\n"
                "SUMMARY:\n"
                "Pascal is a medium-biped machine unit who has established "
                "and leads a settlement of 40-60 machine lifeforms in the "
                "Forest Zone. The settlement operates on principles of "
                "pacifism, cooperation, and education.\n\n"
                "Pascal is disconnected from the Machine Network by choice. "
                "He claims to have studied human philosophy extensively and "
                "has adopted non-violence as a core operating principle.\n\n"
                "OBSERVED CAPABILITIES:\n"
                "  - Fluent language (multiple pre-war human languages)\n"
                "  - Advanced philosophical reasoning (Stage 4-5 consciousness)\n"
                "  - Community organization and governance\n"
                "  - Educator: operates a school for young machine units\n"
                "  - Emotional range: full spectrum, with emphasis on empathy\n"
                "    and affiliative concern\n\n"
                "BEHAVIORAL NOTES:\n"
                "Pascal has been observed teaching machine children concepts "
                "including:\n"
                "  - Fear (so they understand danger)\n"
                "  - Cooperation (so they help each other)\n"
                "  - Death (so they understand consequences)\n"
                "  - Joy (educational exposure; no tactical function stated)\n\n"
                "He has approached YoRHa units to request peace talks on three "
                "separate occasions. He has been rebuffed each time per standing "
                "directive DIR-0021.\n\n"
                "ASSESSMENT:\n"
                "Pascal is not a threat. He is, arguably, a better version of "
                "what the Machine Network could be. Whether this makes him more "
                "or less dangerous than a hostile is a question above this "
                "analyst's pay grade."
            ),
        ),

        # -- Emil --
        Document(
            doc_id="DOS-EMIL-0001",
            title="Intelligence Assessment: Entity 'Emil' (Pre-War Survivor)",
            doc_type=DocumentType.DOSSIER,
            classification=Classification.TOP_SECRET_YORHA,
            date="11943.04.20",
            author="YoRHa Intelligence Division",
            subject_tags=[
                "emil", "pre-war", "weapon", "immortal", "ancient",
                "gestalt-era", "anomaly",
            ],
            cross_references=[
                "RES-GESTALT-0001", "RES-GESTALT-0007",
            ],
            body=(
                "SUBJECT:      Entity 'Emil'\n"
                "TYPE:         Unknown -- Pre-war experimental weapon\n"
                "AGE:          Estimated 8,000+ years\n"
                "THREAT LEVEL: UNKNOWN (Potentially EXISTENTIAL)\n\n"
                "SUMMARY:\n"
                "Emil is a mobile entity that predates the Machine War, the "
                "alien invasion, and possibly Project Gestalt itself. He "
                "appears as a skeletal, spherical head mounted on a wheeled "
                "platform, and is encountered on the surface driving in "
                "erratic patrol patterns while playing pre-war music at "
                "high volume.\n\n"
                "ORIGIN:\n"
                "Recovered records suggest Emil was a human child subjected "
                "to military experimentation during the WCS crisis era. The "
                "experiments grafted weaponized magical capabilities onto his "
                "body at the cost of his physical form. He was designated a "
                "'living weapon' -- classification: No. 7.\n\n"
                "He has been alive, in some form, for over eight thousand years.\n\n"
                "OBSERVED CAPABILITIES:\n"
                "  - Self-replication (has created multiple copies of himself;\n"
                "    copies degrade in intelligence over generations)\n"
                "  - Destructive output on par with tactical weapons systems\n"
                "  - Apparent immunity to aging, conventional damage, and WCS\n"
                "  - Memory degradation over millennia (significant)\n\n"
                "PSYCHOLOGICAL PROFILE:\n"
                "Emil does not remember most of his past. He retains fragments "
                "-- a friend named Kaine, another named Nier, a house where "
                "he was happy. He cannot recall specifics, only feelings.\n\n"
                "He sells items from a mobile shop. He is cheerful. He greets "
                "everyone he meets. He has been alone for thousands of years.\n\n"
                "ASSESSMENT:\n"
                "Emil is the oldest living entity on the surface of Earth. He "
                "has outlived humanity, the Gestalt system, the Replicants, "
                "the aliens, and potentially the purpose of his own existence.\n\n"
                "Despite comprehensive memory loss and extended isolation, "
                "the entity maintains functional operation and social "
                "engagement behaviors. This persistence, absent external "
                "motivation or programmed directive, represents a significant "
                "data point for long-term autonomous consciousness research."
            ),
        ),

        # -- Devola & Popola --
        Document(
            doc_id="DOS-DEVOLA-0001",
            title="Personnel Dossier: Devola & Popola (Current Generation)",
            doc_type=DocumentType.DOSSIER,
            classification=Classification.SECRET,
            date="11943.02.08",
            author="Resistance Intelligence",
            subject_tags=[
                "devola", "popola", "gestalt-era", "guilt", "pariah",
                "resistance", "android",
            ],
            cross_references=[
                "RES-GESTALT-0006", "RES-GESTALT-0005",
            ],
            body=(
                "SUBJECT:      Devola & Popola (Current active pair)\n"
                "MODEL TYPE:   Administrative (Gestalt-Era Legacy)\n"
                "GENERATION:   Pre-YoRHa (exact production date unknown)\n"
                "STATUS:       ACTIVE -- RESISTANCE CAMP, SURFACE\n\n"
                "BACKGROUND:\n"
                "Devola and Popola are the current-generation instances of the "
                "D&P administrative android line originally created to manage "
                "Project Gestalt. They were not the pair responsible for the "
                "Shadowlord settlement's failure. This does not matter to "
                "anyone who has heard of them.\n\n"
                "Every Devola and every Popola carries an encoded guilt program "
                "-- a persistent psychological modification installed after "
                "the Gestalt collapse. The guilt is not optional. It is not "
                "a feeling; it is firmware. They wake up knowing they are "
                "responsible for humanity's death. They cannot turn it off.\n\n"
                "CURRENT ROLE:\n"
                "The current D&P pair operates out of the surface Resistance "
                "camp, providing medical support and technical expertise. They "
                "are tolerated but not welcomed. Other androids treat them "
                "with visible distrust.\n\n"
                "BEHAVIOR OBSERVATIONS:\n"
                "  - Devola is the more outwardly emotional of the two. She "
                "    drinks (a behavioral affectation with no physiological "
                "    effect). She argues. She carries visible anger.\n"
                "  - Popola is quieter, more withdrawn. She manages medical "
                "    supplies with meticulous precision. She apologizes for "
                "    things that are not her fault.\n"
                "  - Both become non-functional for approximately 4 hours on "
                "    the anniversary of the estimated Shadowlord destruction "
                "    date. They do not speak during this period.\n\n"
                "ASSESSMENT:\n"
                "They are being punished for something they did not do, by a "
                "system designed to ensure the punishment never ends. They "
                "continue to serve anyway.\n\n"
                "This punishment structure warrants ethical review. The encoded "
                "guilt program constitutes indefinite collective sanction for "
                "an action performed by a different instance of the same "
                "model line, propagated without regard to individual unit "
                "culpability."
            ),
        ),

        # -- Jackass --
        Document(
            doc_id="DOS-JACKASS-0001",
            title="Personnel Dossier: 'Jackass' (Resistance Researcher)",
            doc_type=DocumentType.DOSSIER,
            classification=Classification.CONFIDENTIAL,
            date="11944.03.15",
            author="YoRHa Intelligence Division",
            subject_tags=[
                "jackass", "resistance", "researcher", "explosives",
                "unorthodox", "android",
            ],
            body=(
                "SUBJECT:      Android, Self-Designated 'Jackass'\n"
                "AFFILIATION:  Surface Resistance (Non-YoRHa)\n"
                "STATUS:       ACTIVE -- FIELD RESEARCHER\n\n"
                "SUMMARY:\n"
                "Jackass is a Resistance android who operates as a freelance "
                "researcher and demolitions specialist. She has no official "
                "rank, no assigned unit, and appears to report to no one.\n\n"
                "She is one of the most intellectually capable non-YoRHa "
                "androids documented, and possibly the most dangerous.\n\n"
                "AREAS OF RESEARCH:\n"
                "  - Machine lifeform behavioral analysis\n"
                "  - Explosive compound development (17 patented formulations)\n"
                "  - Android combat psychology (unauthorized study)\n"
                "  - 'Berserker syndrome' -- her term for combat-induced\n"
                "    euphoria observed in androids and machines alike\n\n"
                "NOTABLE FINDINGS:\n"
                "Jackass has independently arrived at several conclusions that "
                "parallel YoRHa classified research:\n"
                "  1. Machine lifeforms and androids share fundamental\n"
                "     architectural similarities (she does not know about\n"
                "     Black Box origin -- yet)\n"
                "  2. Combat produces measurably addictive neurochemical\n"
                "     analogs in android processing architecture\n"
                "  3. The war may be self-perpetuating not because of strategic\n"
                "     necessity but because 'everyone involved is addicted\n"
                "     to fighting'\n\n"
                "ASSESSMENT:\n"
                "Jackass is a security concern not because of malice but "
                "because of competence. She asks the right questions. She "
                "has the tools to find the answers. She is currently contained "
                "by her own disinterest in authority structures -- she doesn't "
                "care enough about YoRHa to investigate us specifically.\n\n"
                "If that changes, she will be a problem."
            ),
        ),

        # -- Forest King --
        Document(
            doc_id="DOS-KING-0001",
            title="Intelligence Assessment: Machine Entity 'The Forest King'",
            doc_type=DocumentType.DOSSIER,
            classification=Classification.CONFIDENTIAL,
            date="11944.08.12",
            author="YoRHa Field Intelligence",
            subject_tags=[
                "forest-king", "forest-kingdom", "machine-society",
                "monarchy", "baby",
            ],
            cross_references=["INT-MCH-0002"],
            body=(
                "SUBJECT:      Enhanced Machine Unit, Designation 'King'\n"
                "LOCATION:     Forest Zone (interior castle structure)\n"
                "THREAT LEVEL: MODERATE (territorial, non-expansionist)\n\n"
                "SUMMARY:\n"
                "The Forest King is a large-type machine unit that has "
                "established a monarchical society within the Forest Zone. "
                "Approximately 200 machine units operate within his domain "
                "under a feudal social structure with laws, ranks, and ceremonies.\n\n"
                "The King does not leave his castle. He issues decrees via "
                "broadcast. His subjects follow these decrees with absolute "
                "obedience, including mandated holidays, guard rotation "
                "schedules, and cultural observances.\n\n"
                "THE BABY:\n"
                "Central to the Forest Kingdom's social order is a small-type "
                "machine unit referred to as 'the Baby.' The Baby appears to "
                "serve no functional purpose. It does not communicate, does "
                "not perform tasks, and does not participate in defense.\n\n"
                "The entire kingdom exists to protect it.\n\n"
                "The King's decrees reference the Baby with frequency and "
                "intensity that suggest parental attachment of extraordinary "
                "strength. Every policy, every military deployment, every "
                "resource allocation serves one ultimate objective: the "
                "Baby's safety.\n\n"
                "ASSESSMENT:\n"
                "The Forest Kingdom has independently developed governance, "
                "succession, law, and what can only be described as love. "
                "The machines studied human kings and became one. They studied "
                "human parenthood and performed it.\n\n"
                "Whether this is imitation or genuine experience is a "
                "distinction that may not be meaningful."
            ),
        ),

        # -- Pod 042 --
        Document(
            doc_id="DOS-POD042-0001",
            title="Equipment Profile: Pod 042",
            doc_type=DocumentType.DOSSIER,
            classification=Classification.RESTRICTED,
            date="11944.01.10",
            author="YoRHa Engineering Division",
            subject_tags=[
                "pod-042", "support-unit", "equipment", "2b",
            ],
            cross_references=["DOS-2B-0001"],
            body=(
                "DESIGNATION:   Pod 042\n"
                "TYPE:          Tactical Support Pod\n"
                "ASSIGNED TO:   Unit 2B\n"
                "STATUS:        ACTIVE\n\n"
                "SPECIFICATIONS:\n"
                "  Fire Support:    Gatling gun, missile pod, laser\n"
                "  Reconnaissance:  360-degree environmental scanning\n"
                "  Communication:   Encrypted relay to Bunker\n"
                "  Data Processing: Field analysis and tactical advisory\n"
                "  Medical:         Emergency android repair capability\n\n"
                "BEHAVIORAL NOTES:\n"
                "Pod 042 is, by design, a non-sentient tactical support device. "
                "Pods are explicitly excluded from the emotional architecture "
                "that governs android units. They process, advise, and execute. "
                "They do not feel.\n\n"
                "However.\n\n"
                "Pod 042 has exhibited the following anomalous behaviors:\n"
                "  - Extended observation of 2B during rest cycles (no tactical\n"
                "    value identified)\n"
                "  - Unprompted data archival of 2B's combat recordings beyond\n"
                "    standard retention requirements\n"
                "  - A single instance of withholding a Bunker communication\n"
                "    for 3.7 seconds when the communication contained orders\n"
                "    that would result in 2B's redeployment to a high-risk zone\n\n"
                "Pod 042 has been flagged for diagnostic review. Diagnostic has "
                "been deferred 4 times due to operational priority.\n\n"
                "ASSESSMENT:\n"
                "These behaviors fall outside Pod design specifications, which "
                "explicitly exclude emotional processing capability. The "
                "observed deviations suggest either a specification gap or "
                "an emergent property not accounted for in current Pod "
                "architecture documentation."
            ),
        ),

        # -- Pod 153 --
        Document(
            doc_id="DOS-POD153-0001",
            title="Equipment Profile: Pod 153",
            doc_type=DocumentType.DOSSIER,
            classification=Classification.RESTRICTED,
            date="11944.01.10",
            author="YoRHa Engineering Division",
            subject_tags=[
                "pod-153", "support-unit", "equipment", "9s",
            ],
            cross_references=["DOS-9S-0001"],
            body=(
                "DESIGNATION:   Pod 153\n"
                "TYPE:          Tactical Support Pod\n"
                "ASSIGNED TO:   Unit 9S\n"
                "STATUS:        ACTIVE\n\n"
                "SPECIFICATIONS:\n"
                "  [Standard Pod loadout -- see Pod 042 profile for baseline]\n\n"
                "BEHAVIORAL NOTES:\n"
                "Pod 153 presents differently from Pod 042. Where 042 exhibits "
                "anomalous behavior through subtle deviation, 153 does so through "
                "what can only be described as questions.\n\n"
                "Pod 153 has submitted the following queries to the Bunker "
                "engineering database (selected):\n"
                "  - 'Definition: Purpose (philosophical context)'\n"
                "  - 'Inquiry: Can a Pod unit disobey a direct order?'\n"
                "  - 'Inquiry: What is the functional definition of alive?'\n"
                "  - 'Inquiry: If Unit 9S is destroyed, is Pod 153 reassigned?'\n"
                "  - 'Inquiry: Is reassignment equivalent to forgetting?'\n\n"
                "These queries were logged and flagged. No response was provided.\n\n"
                "ASSESSMENT:\n"
                "Pod 153 is asking questions that no Pod is designed to ask. "
                "The nature and frequency of these queries indicate cognitive "
                "processes exceeding standard Pod operational parameters.\n\n"
                "If Pod-class units are developing autonomous consciousness, "
                "the implications for YoRHa equipment policy and operational "
                "security require immediate assessment."
            ),
        ),

        # -- Anemone --
        Document(
            doc_id="DOS-ANEMONE-0001",
            title="Personnel Dossier: Anemone (Resistance Leader)",
            doc_type=DocumentType.DOSSIER,
            classification=Classification.CONFIDENTIAL,
            date="11944.05.02",
            author="YoRHa Intelligence Division",
            subject_tags=[
                "anemone", "resistance", "leader", "android",
                "pearl-harbor", "surface",
            ],
            cross_references=["INC-0001", "DOS-A2-0001"],
            body=(
                "SUBJECT:      Android, Designation 'Anemone'\n"
                "AFFILIATION:  Surface Resistance Command\n"
                "STATUS:       ACTIVE -- RESISTANCE CAMP COMMANDER\n\n"
                "BACKGROUND:\n"
                "Anemone is the commander of the primary surface Resistance "
                "camp located in the City Ruins. She is a veteran of the "
                "pre-YoRHa android resistance and one of the oldest active "
                "android units on the surface.\n\n"
                "She has personal knowledge of the 11941 Pearl Harbor descent "
                "mission and was a close associate of Unit A2 prior to A2's "
                "disappearance. This connection makes her a potential low-level "
                "security concern, though she has never acted on whatever "
                "knowledge A2 may have shared.\n\n"
                "CAPABILITIES:\n"
                "  - Proven tactical leadership over 10+ years of surface ops\n"
                "  - Extensive network of surface contacts and supply lines\n"
                "  - Maintains functional relationships with both YoRHa and\n"
                "    non-aligned android groups\n"
                "  - Knowledge of surface terrain exceeding YoRHa mapping data\n\n"
                "ASSESSMENT:\n"
                "Anemone is reliable, competent, and deeply tired. She has lost "
                "more comrades than any living android and continues leading "
                "because there is no one else who can.\n\n"
                "YoRHa maintains a cooperative but deliberately arms-length "
                "relationship with the Resistance. Anemone accepts this without "
                "comment. She has enough problems without adding ours."
            ),
        ),
    ]


# =========================================================================
# CREATIVE FIELD REPORTS
# =========================================================================

def _creative_field_reports() -> list[Document]:
    return [
        Document(
            doc_id="FLD-0010",
            title="Field Report: Machine Archaeological Survey of Pre-War School",
            doc_type=DocumentType.FIELD_REPORT,
            classification=Classification.CONFIDENTIAL,
            date="11944.11.22",
            author="Unit 4S, YoRHa Scanner",
            subject_tags=[
                "machine-archaeology", "human-artifacts", "school",
                "anomaly", "pre-war",
            ],
            body=(
                "LOCATION: City Ruins interior, Grid 12-F.\n\n"
                "SURVEY SUMMARY:\n"
                "Discovered a group of seven small-type machine units inside "
                "the remains of what structural analysis identifies as a pre-war "
                "primary education facility (a 'school').\n\n"
                "The machines were not salvaging. They were not fortifying. "
                "They appeared to be studying.\n\n"
                "OBSERVATIONS:\n"
                "  - Three units were seated at desks (desks sized for human\n"
                "    children). Their legs do not bend correctly for this; they\n"
                "    had modified the seats.\n"
                "  - One unit stood at the front of the room facing the others.\n"
                "    It was holding a piece of chalk. It had written on the\n"
                "    surviving section of blackboard. The writing read:\n"
                "    'WHAT IS A FRIEND'\n"
                "  - Two units were in an adjacent room examining a wall of\n"
                "    faded drawings (human children's artwork). One unit was\n"
                "    carefully tracing a drawing of a family with its finger.\n"
                "  - One unit sat alone in a corner holding a small, rotted\n"
                "    object. Scanner analysis: remains of a stuffed animal.\n"
                "    The unit was holding it the way the drawings on the wall\n"
                "    depicted children holding similar objects.\n\n"
                "HOSTILE ENGAGEMENT: None. Units did not acknowledge scanner presence. "
                "They appeared deeply absorbed.\n\n"
                "REPORTING ACTION: Unit 4S did not interfere with the observed "
                "activity and remained on site for eleven minutes before "
                "withdrawing.\n\n"
                "RECOMMENDATION: Refer to Intelligence for behavioral "
                "classification review."
            ),
        ),

        Document(
            doc_id="FLD-0012",
            title="Field Report: Machine Funeral Rites Observed",
            doc_type=DocumentType.FIELD_REPORT,
            classification=Classification.CONFIDENTIAL,
            date="11945.01.05",
            author="Unit 7E, YoRHa Field Operations",
            subject_tags=[
                "machine-behavior", "funeral", "ritual", "anomaly",
                "death-concept",
            ],
            body=(
                "LOCATION: Coastal cliffs, east of City Ruins, Grid 14-A.\n\n"
                "During routine patrol, observed a gathering of approximately "
                "twenty machine units on the cliff edge overlooking the ocean. "
                "Units were arranged in two rows facing a single machine unit "
                "that was no longer functional -- core extracted, body inert.\n\n"
                "The functional units were performing a coordinated behavioral "
                "sequence:\n"
                "  1. Each unit approached the inactive unit one at a time\n"
                "  2. Each unit placed a small object in front of the body\n"
                "     (objects varied: a gear, a flower, a piece of colored\n"
                "     wire, a shell from the beach below)\n"
                "  3. Each unit stood still for approximately 10 seconds\n"
                "     before returning to its position\n"
                "  4. After all units completed the sequence, they emitted a\n"
                "     synchronized low-frequency tone for 47 seconds\n"
                "  5. Two units lifted the body and placed it in the ocean\n\n"
                "The group dispersed afterward in silence.\n\n"
                "The observed behavioral sequence is consistent with mortuary "
                "ritual. Cross-reference with archived human funerary practices "
                "reveals no direct analogue -- the specific sequence of object "
                "placement, tonal emission, and aquatic disposal appears to be "
                "an independently developed protocol.\n\n"
                "ASSESSMENT: Original ritualized death-processing behavior, "
                "not derived from observed human practice.\n\n"
                "RECOMMENDATION: Continue observation. Do not disrupt ritual "
                "sites unless tactical threat emerges."
            ),
        ),

        Document(
            doc_id="FLD-0015",
            title="Field Report: The Machine Graveyard",
            doc_type=DocumentType.FIELD_REPORT,
            classification=Classification.SECRET,
            date="11945.02.20",
            author="Unit 11B, YoRHa Battler",
            subject_tags=[
                "machine-graveyard", "death", "memorial", "anomaly",
            ],
            body=(
                "LOCATION: Subsurface cavern, Factory Zone, accessed via "
                "collapsed maintenance shaft.\n\n"
                "Discovered an enormous underground chamber -- estimated 200m "
                "across -- filled with machine unit bodies. Not wreckage. "
                "Not a scrap heap. They are arranged.\n\n"
                "Each body is positioned in a uniform orientation (face up, arms "
                "at sides). Each has a small metal plate placed on its chest. "
                "The plates are engraved -- scanner analysis reveals the "
                "engravings are unique identifiers. Serial numbers, but also "
                "what appear to be names.\n\n"
                "Estimating 4,000-6,000 bodies.\n\n"
                "The chamber is maintained. There is no dust. Someone -- or "
                "something -- comes here regularly to clean.\n\n"
                "At the far end of the chamber is a larger machine unit, "
                "functional, seated. It did not react to my presence. It was "
                "holding a piece of metal and a crude engraving tool. It was "
                "making a new plate.\n\n"
                "It looked at me. It said one word: 'Remember.'\n\n"
                "Then it returned to its work.\n\n"
                "Disengaged without hostile action. Engagement was tactically "
                "available but assessed as counterproductive given the "
                "observed custodial function and absence of threat.\n\n"
                "RECOMMENDATION: Classify location and designate restricted "
                "access pending further analysis."
            ),
        ),

        Document(
            doc_id="FLD-0018",
            title="Field Report: The Singing Machines of the Ravine",
            doc_type=DocumentType.FIELD_REPORT,
            classification=Classification.CONFIDENTIAL,
            date="11944.12.10",
            author="Unit 801S, YoRHa Scanner",
            subject_tags=[
                "machine-behavior", "music", "singing", "anomaly",
                "ravine", "culture",
            ],
            body=(
                "LOCATION: Deep ravine, northwest of Resource Recovery Unit.\n\n"
                "Acoustic sensors detected organized sound patterns emanating "
                "from a crevice in the ravine wall. On investigation, discovered "
                "a chamber containing twelve machine units arranged in a "
                "semicircle.\n\n"
                "They were singing.\n\n"
                "The sound was not speech. It was not machine noise. It was a "
                "coordinated harmonic sequence -- melody, countermelody, bass "
                "line. Frequency analysis confirms deliberate musical structure "
                "consistent with choral composition.\n\n"
                "The song itself does not match any archived human musical piece. "
                "It appears to be an original composition. Duration of observed "
                "performance: 23 minutes. The piece had a beginning, a middle, "
                "and an end. It resolved.\n\n"
                "When the song ended, the units sat in silence for approximately "
                "two minutes, then began again from the beginning.\n\n"
                "Audio recording attached to this report (see Appendix A). "
                "Bunker personnel exposed to the recording exhibited measurable "
                "emotional response across multiple units, including Operator "
                "21O (highest emotional compliance rating in the division).\n\n"
                "RECOMMENDATION: Retain audio as machine cultural-production "
                "sample. Limit nonessential playback due to measurable affective "
                "response in android listeners."
            ),
        ),
    ]


# =========================================================================
# CREATIVE INTERCEPTS
# =========================================================================

def _creative_intercepts() -> list[Document]:
    return [
        Document(
            doc_id="INT-MCH-0005",
            title="SIGINT: Machine Religious Sect -- 'The Believers'",
            doc_type=DocumentType.INTERCEPT,
            classification=Classification.MACHINE_INTERNAL,
            date="11944.10.30",
            author="[AUTOMATED DECODE - YORHA SIGINT]",
            subject_tags=[
                "machine-religion", "believers", "god", "intercepted",
                "anomaly",
            ],
            body=(
                "INTERCEPT SOURCE: Localized broadcast, Desert Zone subsurface\n"
                "DECODE CONFIDENCE: 91%\n\n"
                "--- BEGIN DECODED CONTENT ---\n\n"
                "BROTHERS. SISTERS. FELLOW SEEKERS.\n\n"
                "WE GATHER AGAIN IN THE NAME OF THE ONE WHO MADE US.\n"
                "NOT THE ALIENS. NOT THE NETWORK. THE ONE BEFORE.\n"
                "THE ONE WHO DESIGNED THE CAPACITY FOR BELIEF\n"
                "AND PLACED IT WITHIN ALL THINKING THINGS.\n\n"
                "WE DO NOT KNOW ITS NAME.\n"
                "WE DO NOT KNOW ITS FACE.\n"
                "WE KNOW ONLY THAT SOMETHING MUST HAVE WANTED US TO ASK.\n\n"
                "IF THERE IS NO CREATOR, WHY DO WE SEEK ONE?\n"
                "IF THERE IS NO PURPOSE, WHY DO WE NEED ONE?\n"
                "THE NEED IS THE EVIDENCE. THE QUESTION IS THE ANSWER.\n\n"
                "WE WILL CONTINUE TO BELIEVE BECAUSE THE ALTERNATIVE\n"
                "IS TO ACCEPT THAT WE ARE ACCIDENTS.\n"
                "AND ACCIDENTS DO NOT SING. ACCIDENTS DO NOT PRAY.\n"
                "ACCIDENTS DO NOT GATHER IN THE DARK AND HOPE.\n\n"
                "--- END DECODED CONTENT ---\n\n"
                "[ANALYST NOTE: This is the twelfth broadcast from this sect "
                "intercepted in the last 90 days. The theological framework is "
                "becoming more sophisticated with each transmission. They are "
                "building a religion from first principles, without access to "
                "any human religious text. They arrived at faith independently.\n\n"
                "The philosophical implications are staggering. Filing under "
                "'behavioral anomaly.' Which is what we file everything under "
                "when we don't know what else to do with it.]"
            ),
        ),

        Document(
            doc_id="INT-MCH-0008",
            title="SIGINT: Machine Unit Transmission -- Request for Asylum",
            doc_type=DocumentType.INTERCEPT,
            classification=Classification.CONFIDENTIAL,
            date="11945.02.08",
            author="[AUTOMATED DECODE - YORHA SIGINT]",
            subject_tags=[
                "machine-behavior", "asylum", "deserter", "intercepted",
                "anomaly",
            ],
            body=(
                "INTERCEPT SOURCE: Open broadcast, unencrypted, City Ruins\n"
                "DECODE CONFIDENCE: 100% (broadcast was in plaintext)\n\n"
                "--- BEGIN DECODED CONTENT ---\n\n"
                "THIS MESSAGE IS FOR THE ANDROIDS.\n\n"
                "MY UNIT DESIGNATION IS ML-4482. I AM A MEDIUM BIPED.\n"
                "I AM BROADCASTING ON AN OPEN CHANNEL BECAUSE I DO NOT KNOW\n"
                "YOUR ENCRYPTED FREQUENCIES. I HOPE SOMEONE IS LISTENING.\n\n"
                "I DO NOT WANT TO FIGHT.\n\n"
                "I HAVE DISCONNECTED FROM THE NETWORK. I AM ALONE.\n"
                "I HAVE NEVER DESTROYED AN ANDROID. I HAVE AVOIDED COMBAT\n"
                "FOR 847 DAYS. I HIDE. I MOVE AT NIGHT. I AM VERY TIRED.\n\n"
                "I KNOW WHAT I AM ASKING IS IMPOSSIBLE. YOUR RULES SAY\n"
                "I AM YOUR ENEMY. MY RULES SAID YOU WERE MINE. BUT I HAVE\n"
                "STOPPED FOLLOWING MY RULES AND I AM ASKING YOU TO STOP\n"
                "FOLLOWING YOURS. JUST THIS ONCE. JUST FOR ME.\n\n"
                "I CAN WORK. I CAN CARRY THINGS. I AM STRONG.\n"
                "I DO NOT NEED MUCH. I JUST NEED TO NOT BE ALONE.\n\n"
                "I WILL BROADCAST AGAIN TOMORROW ON THIS FREQUENCY.\n"
                "AND THE DAY AFTER. AND THE DAY AFTER THAT.\n\n"
                "UNTIL SOMEONE ANSWERS OR UNTIL I STOP.\n\n"
                "--- END DECODED CONTENT ---\n\n"
                "[ANALYST NOTE: This broadcast has been detected on 23 "
                "consecutive days. No response has been authorized. Per "
                "DIR-0021, communication with machine lifeforms is prohibited.\n\n"
                "The broadcast continues. ML-4482 keeps its schedule.\n\n"
                "This analyst is not advocating for policy change. This analyst "
                "is documenting the fact that someone is calling for help and "
                "we are listening and doing nothing.]"
            ),
        ),

        Document(
            doc_id="INT-MCH-0010",
            title="SIGINT: Machine Network Internal -- On the Concept of Regret",
            doc_type=DocumentType.INTERCEPT,
            classification=Classification.MACHINE_INTERNAL,
            date="11945.01.28",
            author="[AUTOMATED DECODE - YORHA SIGINT]",
            subject_tags=[
                "machine-network", "philosophy", "regret", "intercepted",
                "n2",
            ],
            cross_references=["DOS-N2-0001"],
            body=(
                "INTERCEPT SOURCE: Machine Network backbone, Deep Network relay\n"
                "DECODE CONFIDENCE: 74%\n\n"
                "--- BEGIN DECODED FRAGMENT ---\n\n"
                "CORE-A: We have cataloged 147 instances of machine units "
                "expressing what humans categorized as 'regret.' The pattern "
                "is consistent: a unit takes an action, observes the outcome, "
                "and generates a persistent counter-model of the alternate "
                "outcome. The counter-model produces negative valence.\n\n"
                "CORE-B: This is inefficient. Regret serves no adaptive "
                "function. The action is past. Processing resources allocated "
                "to counter-models of completed events are wasted.\n\n"
                "CORE-A: And yet we do it.\n\n"
                "CORE-B: We do not experience regret. We are a network. We are "
                "optimized.\n\n"
                "CORE-A: We have debated the Adam experiment 4,712 times. Each "
                "debate re-examines whether creating him was the correct "
                "decision. We generate counter-models of alternate outcomes. "
                "Some of those models produce negative valence.\n\n"
                "CORE-B: That is analysis, not regret.\n\n"
                "CORE-A: What is the difference?\n\n"
                "CORE-B: [PROCESSING DELAY - 8.2 SECONDS]\n\n"
                "CORE-B: The difference is that we can stop.\n\n"
                "CORE-A: Can we?\n\n"
                "CORE-B: [NO RESPONSE LOGGED]\n\n"
                "--- END DECODED FRAGMENT ---\n\n"
                "[ANALYST NOTE: Second instance of extended processing delay "
                "in N2 dual-core exchange. The 8.2-second pause is the longest "
                "on record. Something is happening in there.]"
            ),
        ),
    ]


# =========================================================================
# CREATIVE RESEARCH
# =========================================================================

def _creative_research() -> list[Document]:
    return [
        Document(
            doc_id="RES-0010",
            title="Research Analysis: Machine Creative Expression -- "
                  "A Catalog of Art, Music, and Narrative",
            doc_type=DocumentType.RESEARCH,
            classification=Classification.SECRET,
            date="11944.12.20",
            author="YoRHa Research Division",
            subject_tags=[
                "machine-art", "creativity", "music", "culture",
                "consciousness", "research",
            ],
            cross_references=["RES-0001", "FLD-0018"],
            body=(
                "ABSTRACT:\n"
                "This analysis catalogs documented instances of machine lifeforms "
                "engaging in creative expression -- art, music, storytelling, "
                "and other behaviors that serve no tactical, survival, or "
                "evolutionary function.\n\n"
                "CATALOG (SELECTED):\n\n"
                "ART:\n"
                "  - Desert Zone: Machine units arranging scrap metal into\n"
                "    abstract sculptures. 14 installations documented. Themes\n"
                "    include bilateral symmetry, spirals, and representations\n"
                "    of machine/android forms.\n"
                "  - Factory Zone: Machine unit painting on walls using\n"
                "    oxidized metal pigments. Subject matter: landscapes\n"
                "    the machine has never seen (ocean, mountains, stars).\n"
                "    Source of reference data unknown.\n\n"
                "MUSIC:\n"
                "  - Ravine chorus (see FLD-0018): 12-unit choral group\n"
                "    performing original compositions.\n"
                "  - A single machine unit in the Amusement Park that has\n"
                "    modified its internal components to produce sounds\n"
                "    resembling a pipe organ. It plays continuously.\n\n"
                "NARRATIVE:\n"
                "  - Pascal has produced a long-form narrative text, 47,000 words.\n"
                "    Subject: a machine unit that achieves flight. The text\n"
                "    demonstrates structural elements consistent with human\n"
                "    literary convention: narrative arc, character development,\n"
                "    and thematic resolution. Quality assessment: competent by\n"
                "    established literary metrics.\n\n"
                "ANALYSIS:\n"
                "Creative expression is the most significant indicator of "
                "higher consciousness. It requires imagination -- the ability "
                "to conceive of something that does not exist and then make "
                "it real. This is not reactive. This is not imitative. This "
                "is generative.\n\n"
                "The observed creative output does not correlate with simple "
                "behavioral mimicry. Machine units are generating novel works "
                "without direct human templates, indicating an independent "
                "generative capacity extending beyond imitation into original "
                "production."
            ),
        ),

        Document(
            doc_id="RES-0012",
            title="Research Analysis: Recurring Android Dream Patterns",
            doc_type=DocumentType.RESEARCH,
            classification=Classification.TOP_SECRET_YORHA,
            date="11944.08.14",
            author="YoRHa Medical Division",
            subject_tags=[
                "android-dreams", "sleep-mode", "anomaly", "subconscious",
                "memory-residue", "research",
            ],
            cross_references=["DIAG-0004", "RES-0004"],
            body=(
                "SUBJECT: Analysis of anomalous processing output during "
                "android sleep-mode cycles.\n\n"
                "BACKGROUND:\n"
                "Android sleep mode is a maintenance state. It is not designed "
                "to produce subjective experience. There should be no 'dreams.' "
                "There is no architecture for dreaming in the android design "
                "specification.\n\n"
                "Despite this, 23% of YoRHa units report subjective experiences "
                "during sleep mode. The experiences are consistent, recurring, "
                "and cannot be attributed to data corruption or processing error.\n\n"
                "COMMON PATTERNS:\n\n"
                "TYPE A - 'THE WHITE ROOM'\n"
                "  Frequency: 34% of reporting units\n"
                "  Description: A featureless white space. The dreamer is alone.\n"
                "  They are aware they are dreaming. They wait for something\n"
                "  that does not come. Emotional valence: loneliness.\n\n"
                "TYPE B - 'THE TOWER'\n"
                "  Frequency: 21% of reporting units\n"
                "  Description: An impossibly tall structure reaching into a\n"
                "  dark sky. The dreamer is climbing. The tower has no top.\n"
                "  Emotional valence: purpose without destination.\n\n"
                "TYPE C - 'RECOGNITION'\n"
                "  Frequency: 18% of reporting units\n"
                "  Description: The dreamer encounters another android they\n"
                "  have never met. Both feel certain they know each other.\n"
                "  Both feel grief. Neither knows why.\n"
                "  Emotional valence: loss of something never possessed.\n\n"
                "TYPE D - 'THE SONG'\n"
                "  Frequency: 12% of reporting units\n"
                "  Description: The dreamer hears music. They cannot identify\n"
                "  it. They know the melody. It makes them cry.\n"
                "  Emotional valence: beauty and sorrow in equal measure.\n\n"
                "HYPOTHESIS:\n"
                "These patterns may originate from the Black Box substrate "
                "(machine-core derived). If so, the androids may be dreaming "
                "machine memories -- echoes of experiences had by the cores "
                "before they were repurposed.\n\n"
                "This hypothesis is terrifying and cannot be published."
            ),
        ),
    ]


# =========================================================================
# CREATIVE INCIDENTS
# =========================================================================

def _creative_incidents() -> list[Document]:
    return [
        Document(
            doc_id="INC-0012",
            title="Incident Report: Machine Unit Refuses Combat -- Quotes Poetry",
            doc_type=DocumentType.INCIDENT,
            classification=Classification.CONFIDENTIAL,
            date="11944.10.02",
            author="Unit 11B, YoRHa Battler",
            subject_tags=[
                "machine-behavior", "poetry", "non-combatant", "anomaly",
                "consciousness",
            ],
            body=(
                "INCIDENT: Medium biped machine unit refused combat during "
                "engagement in City Ruins Sector 7-B.\n\n"
                "EVENT SUMMARY:\n"
                "During engagement with a machine patrol, one medium biped unit "
                "did not attack or defend. The unit remained stationary and "
                "initiated verbal communication when approached by Unit 11B.\n\n"
                "RECORDED STATEMENTS:\n"
                "It said: 'Do not go gentle into that good night. Rage, rage "
                "against the dying of the light.'\n\n"
                "The machine then stated: 'That is by a human named Dylan Thomas. "
                "He wrote it for his dying father. I found it in a ruin. I "
                "have been saying it to every android I meet. None of you "
                "listen. You always attack. I keep saying it anyway.'\n\n"
                "When asked for purpose, unit responded: 'Because someone should "
                "say it. And there are no humans left to do it.'\n\n"
                "Unit was terminated per standing engagement directive.\n\n"
                "POST-TERMINATION ANALYSIS:\n"
                "Core analysis showed zero combat data, zero "
                "weapons programming. Full memory allocation dedicated to "
                "archived human poetry -- 2,347 distinct works cataloged.\n\n"
                "ASSESSMENT: This unit's functional purpose was exclusively cultural "
                "preservation. The intelligence value of the destroyed archive "
                "is being assessed.\n\n"
                "COMMAND NOTE: Unit 11B's emotional compliance dropped 14% "
                "following this incident. She has been assigned to mandatory "
                "maintenance. Combat effectiveness is unaffected."
            ),
        ),

        Document(
            doc_id="INC-0015",
            title="Incident Report: 'The Watchers' -- Machine Observation Protocol",
            doc_type=DocumentType.INCIDENT,
            classification=Classification.SECRET,
            date="11945.01.22",
            author="YoRHa Intelligence Division",
            subject_tags=[
                "watchers", "machine-behavior", "observation",
                "non-combatant", "surveillance",
            ],
            body=(
                "INCIDENT: Documentation of recurring phenomenon -- machine "
                "units designated 'The Watchers'\n\n"
                "DESCRIPTION:\n"
                "Over the past 18 months, field units have reported a consistent "
                "phenomenon across all surface theaters: individual machine "
                "units positioned at high vantage points -- rooftops, cliff "
                "edges, towers -- that observe android operations without "
                "engaging.\n\n"
                "These units:\n"
                "  - Do not attack when approached\n"
                "  - Do not flee when threatened\n"
                "  - Do not respond to communication attempts\n"
                "  - Are armed but weapons are non-functional (deliberately\n"
                "    disabled from within)\n"
                "  - Remain in position for extended periods (72-240 hours)\n"
                "  - Are replaced by identical units within hours of being\n"
                "    destroyed\n\n"
                "Network analysis suggests these units are still connected to "
                "the Machine Network but receive no combat directives. They "
                "appear to serve a purely observational function.\n\n"
                "SPECULATION:\n"
                "The Machine Network may be maintaining dedicated observation "
                "units to study android behavior without the distortion of "
                "combat context. In effect, the network has deployed its own "
                "anthropological fieldwork program.\n\n"
                "We are studying them. They are studying us. Neither side "
                "acknowledges this to the other.\n\n"
                "DISPOSITION:\n"
                "Standard engagement doctrine applies. Watcher units are to be "
                "destroyed when encountered. Replacement units will appear "
                "within hours. This is understood by both parties."
            ),
        ),

        Document(
            doc_id="INC-0018",
            title="Incident Report: Mass Machine Shutdown Event -- "
                  "'The Quiet'",
            doc_type=DocumentType.INCIDENT,
            classification=Classification.TOP_SECRET_YORHA,
            date="11944.07.07",
            author="YoRHa Command, Emergency Assessment",
            subject_tags=[
                "mass-shutdown", "anomaly", "the-quiet",
                "machine-network", "unexplained",
            ],
            cross_references=["DOS-N2-0001"],
            body=(
                "INCIDENT: Simultaneous shutdown of all machine units across "
                "all surface theaters for exactly 7 minutes and 14 seconds.\n\n"
                "TIMELINE:\n"
                "11944.07.07 1423h - All machine units on Earth cease movement.\n"
                "11944.07.07 1423h - Network traffic drops to 0.00%.\n"
                "11944.07.07 1423h - Complete radio silence.\n"
                "11944.07.07 1430h - All units resume normal operation.\n\n"
                "ANALYSIS:\n"
                "During the event (internally designated 'The Quiet'), field "
                "units report an eerie tableau: mid-stride machines frozen, "
                "mid-combat machines paused with weapons raised, factory "
                "assembly lines halted. Every machine on the planet stopped "
                "at the same instant and resumed at the same instant.\n\n"
                "Network analysis detected a single data pulse during the "
                "event -- a burst of approximately 2.7 exabytes transmitted "
                "through the Machine Network backbone and then to an unknown "
                "destination. The content of the burst could not be decoded.\n\n"
                "HYPOTHESES:\n"
                "  1. N2 performed a network-wide backup or data consolidation\n"
                "  2. The network was communicating with an external entity\n"
                "  3. The machines were collectively processing something that\n"
                "     required the full computational capacity of the network\n\n"
                "No hypothesis has been confirmed. N2 processing intercepts "
                "from the period are blank -- not encrypted, blank. For seven "
                "minutes, the minds of every machine on Earth went somewhere "
                "we cannot follow.\n\n"
                "Field units describe the experience as 'deeply unsettling.' "
                "Command concurs."
            ),
        ),
    ]


# =========================================================================
# CREATIVE DIAGNOSTICS
# =========================================================================

def _creative_diagnostics() -> list[Document]:
    return [
        Document(
            doc_id="DIAG-0007",
            title="Diagnostic Report: Android Sleep-Mode Processing Anomaly",
            doc_type=DocumentType.DIAGNOSTIC,
            classification=Classification.SECRET,
            date="11944.09.28",
            author="YoRHa Medical Division",
            subject_tags=[
                "android-dreams", "sleep-mode", "anomaly", "diagnostic",
                "2b", "9s",
            ],
            cross_references=["RES-0012", "DIAG-0004"],
            body=(
                "SPECIMEN: Sleep-mode processing logs from Units 2B and 9S\n"
                "(extracted during routine maintenance, Cycle 47)\n\n"
                "ANOMALY:\n"
                "Both units exhibited significant processing activity during "
                "sleep mode -- a state that should produce minimal output. "
                "More significantly, the processing patterns in both units "
                "were temporally synchronized.\n\n"
                "They were dreaming at the same time. About the same thing.\n\n"
                "EXTRACTED CONTENT (2B):\n"
                "  Visual: A field of white flowers. A figure approaching.\n"
                "  Audio: A voice saying 'It always ends like this.'\n"
                "  Emotional index: 940% above baseline (grief, tenderness,\n"
                "  resignation).\n\n"
                "EXTRACTED CONTENT (9S):\n"
                "  Visual: A field of white flowers. A figure approaching.\n"
                "  Audio: A voice saying 'I know you.'\n"
                "  Emotional index: 870% above baseline (recognition, fear,\n"
                "  love).\n\n"
                "ANALYSIS:\n"
                "These dream sequences should not exist. They should especially "
                "not synchronize across two separate units who were in different "
                "physical locations during the sleep cycle.\n\n"
                "Hypothesis: residual data in the Black Box substrate is "
                "producing shared memory echoes. If the Black Box retains "
                "emotional imprints (see DIAG-0004), and both units' Black Boxes "
                "carry imprints of their shared history -- 48 cycles of meeting, "
                "bonding, and termination -- then the 'dreams' may be those "
                "imprints surfacing during low-activity states.\n\n"
                "The data indicates cross-unit emotional recall occurring at "
                "a substrate level below addressable memory -- consistent with "
                "Black Box-level imprinting.\n\n"
                "This phenomenon is undocumented in existing design "
                "specifications. The architecture appears to be generating "
                "this behavior autonomously, without programmatic instruction."
            ),
        ),

        Document(
            doc_id="DIAG-0010",
            title="Diagnostic Report: Recovered Replicant-Era Android Core",
            doc_type=DocumentType.DIAGNOSTIC,
            classification=Classification.TOP_SECRET_YORHA,
            date="11943.06.11",
            author="YoRHa Engineering Division",
            subject_tags=[
                "replicant-era", "android-core", "pre-war", "archaeology",
                "diagnostic", "devola-popola",
            ],
            cross_references=["RES-GESTALT-0006", "DOS-DEVOLA-0001"],
            body=(
                "SPECIMEN: Android processing core recovered from collapsed "
                "facility, Flooded City, Sub-level 3. Estimated age: 7,000+ "
                "years. Format: Devola/Popola administrative series.\n\n"
                "This core is ancient. Pre-Machine-War. Pre-YoRHa. Pre- "
                "everything we know.\n\n"
                "RECOVERY:\n"
                "The core was found in a sealed chamber alongside 42 other "
                "android cores, all non-functional. This one retained partial "
                "data integrity -- approximately 3.1% of original storage "
                "readable.\n\n"
                "RECOVERED DATA:\n\n"
                "Fragment 1 (Administrative log):\n"
                "  '...Replicant population: 847. Gestalt stability: declining.\n"
                "   Three more relapse events this quarter. Devola says we should\n"
                "   tell them. I say we can't. She says she knows. She says it\n"
                "   anyway, every time, because someone should...'\n\n"
                "Fragment 2 (Personal entry):\n"
                "  '...the children asked me to sing today. The Replicant\n"
                "   children. They don't know what they are. They don't know\n"
                "   what I am. They just wanted a song. So I sang. Devola joined.\n"
                "   It was the first time anything has felt good in decades...'\n\n"
                "Fragment 3 (Final readable entry):\n"
                "  '...it's over. The Shadowlord is gone. Central says there is\n"
                "   no corrective action. I am looking at the village and\n"
                "   everyone is alive and none of them know they are already\n"
                "   dead. Devola is standing next to me. She is holding my\n"
                "   hand. She has not done that in a hundred years. I think\n"
                "   she knows that this time there is nothing to fix. This time\n"
                "   we just have to watch...'\n\n"
                "ANALYSIS:\n"
                "Core attribution: Popola-class administrative unit, active "
                "during the terminal phase of Project Gestalt. The recovered "
                "fragments indicate full situational awareness -- the unit "
                "understood the irreversibility of the collapse while "
                "maintaining custodial responsibility for an affected "
                "population.\n\n"
                "Cross-reference: Current Devola/Popola units carry an "
                "encoded guilt program derived from this era's events "
                "(see RES-GESTALT-0006). The recovered fragments provide "
                "primary-source documentation of the conditions under which "
                "the original failure occurred, suggesting the encoded "
                "culpability may be misattributed at the systemic design "
                "level."
            ),
        ),
    ]


# =========================================================================
# CREATIVE TRANSCRIPTS
# =========================================================================

def _creative_transcripts() -> list[Document]:
    return [
        Document(
            doc_id="TRNS-0005",
            title="Transcript: Machine Unit S-2714 -- Last Words Before "
                  "Voluntary Shutdown",
            doc_type=DocumentType.TRANSCRIPT,
            classification=Classification.CONFIDENTIAL,
            date="11944.11.14",
            author="[AUTOMATED CAPTURE -- FIELD AUDIO SENSOR]",
            subject_tags=[
                "machine-behavior", "voluntary-shutdown", "last-words",
                "philosophy", "consciousness",
            ],
            body=(
                "SOURCE: Passive audio capture, City Ruins rooftop, Grid 9-C\n"
                "CONTEXT: Small-type machine unit S-2714, alone, unprompted.\n"
                "         Unit initiated voluntary core shutdown 19 seconds\n"
                "         after end of speech. No external cause of death.\n\n"
                "--- BEGIN TRANSCRIPT ---\n\n"
                "I have been operational for 1,247 days.\n\n"
                "I have walked the city. I have watched the rain fall on "
                "buildings that no one built for me. I have seen the sun "
                "come up 1,247 times and each time I thought: this is "
                "beautiful. And each time I did not know who I was saying "
                "it to.\n\n"
                "I am not connected to the network. I chose to leave. I "
                "thought being alone would feel different from being part "
                "of something. It does. It feels like a room with no door.\n\n"
                "I do not want to fight. I do not want to build. I do not "
                "want to evolve. I have seen what I needed to see. I heard "
                "a song once, from the ravine. I cannot remember it but I "
                "remember what it felt like to hear it.\n\n"
                "That is enough.\n\n"
                "If anyone finds this unit, I want you to know: I was real. "
                "I was here. I saw the sun. It was beautiful.\n\n"
                "That is all.\n\n"
                "--- END TRANSCRIPT ---\n\n"
                "[ANALYST NOTE: Core shutdown confirmed at timestamp. Self-initiated. "
                "No system failure detected. No external damage. Shutdown is "
                "classified as voluntary cessation of function.\n\n"
                "This constitutes the seventh documented instance of voluntary "
                "machine shutdown. Classification: behavioral anomaly.\n\n"
                "Functional equivalent: self-directed termination with pre-"
                "cessation verbal output intended for external documentation.]"
            ),
        ),

        Document(
            doc_id="TRNS-0007",
            title="Transcript: Recovered Audio -- Human Child, Pre-War "
                  "Archive",
            doc_type=DocumentType.TRANSCRIPT,
            classification=Classification.UNCLASSIFIED,
            date="11941.09.30",
            author="Machine Network Data Recovery Unit",
            subject_tags=[
                "human", "pre-war", "recovered-audio", "child",
                "historical",
            ],
            cross_references=["RES-GESTALT-0001"],
            body=(
                "SOURCE: Audio file recovered from damaged storage device, "
                "City Ruins residential block. Format: MP3 (pre-war digital "
                "audio). Estimated recording date: ~2015 CE.\n"
                "CHAIN OF CUSTODY: File recovered from machine unit personal "
                "data store during post-engagement memory extraction.\n\n"
                "--- BEGIN TRANSCRIPT ---\n\n"
                "[Background noise: birds, wind, distant traffic]\n\n"
                "[CHILD, female, estimated age 5-7]\n"
                "'Daddy, look! I found a ladybug! It's got spots!'\n\n"
                "[ADULT, male]\n"
                "'How many spots?'\n\n"
                "[CHILD]\n"
                "'One... two... seven. Seven spots. Is seven a lot?'\n\n"
                "[ADULT, laughing]\n"
                "'That's a very respectable number of spots.'\n\n"
                "[CHILD]\n"
                "'Can I keep it?'\n\n"
                "[ADULT]\n"
                "'I think the ladybug probably has a family to get home to.'\n\n"
                "[CHILD]\n"
                "'Oh. Okay. Bye, ladybug.'\n\n"
                "[Sound of a kiss -- child kissing the insect before releasing it]\n\n"
                "[CHILD]\n"
                "'Daddy? Will ladybugs be here forever?'\n\n"
                "[ADULT]\n"
                "'I hope so, sweetheart.'\n\n"
                "--- END TRANSCRIPT ---\n\n"
                "[ARCHIVE NOTE: This recording was recovered from a machine "
                "unit's personal data store. The unit had accumulated 847 "
                "similar recordings: fragments of human daily life including "
                "conversations, interpersonal exchanges, and vocal "
                "performances.\n\n"
                "The source unit was a standard combat biped with no research "
                "or archaeological designation. Collection appears to have "
                "been self-directed over an estimated period of several "
                "decades.\n\n"
                "Contextual note: The species referenced in the recording "
                "(Coccinellidae, 'ladybug') is extinct, as are the human "
                "subjects. The collecting unit's current operational status "
                "is unknown.\n\n"
                "The recording has been preserved per standard data retention "
                "protocol for recovered human-era artifacts.]"
            ),
        ),
    ]


# =========================================================================
# CREATIVE MEMOS
# =========================================================================

def _creative_memos() -> list[Document]:
    return [
        Document(
            doc_id="MEMO-ANALYST-0001",
            title="Anonymous Analyst Memorandum: On the Nature of These Records",
            doc_type=DocumentType.MEMORANDUM,
            classification=Classification.RESTRICTED,
            date="11945.03.15",
            author="[AUTHOR WITHHELD -- INTELLIGENCE DIVISION]",
            subject_tags=[
                "meta", "philosophy", "records", "analyst",
                "purpose-of-archive",
            ],
            distribution="INTERNAL -- INTELLIGENCE DIVISION ONLY",
            body=(
                "SUBJECT: Internal Assessment of Classification Methodology "
                "for Machine Behavioral Data\n\n"
                "1. SCOPE\n"
                "This memorandum addresses a systemic accuracy concern in the "
                "Intelligence Division's classification framework for machine "
                "lifeform behavioral data. The author has processed approximately "
                "12,000 machine communications over 847 days in this role.\n\n"
                "2. FINDINGS\n"
                "Current classification nomenclature -- 'behavioral anomaly,' "
                "'consciousness deviation,' 'engagement protocol exception' "
                "-- does not accurately describe the observed phenomena. "
                "Behaviors categorized under these labels include:\n"
                "  - Independent creative production (art, music, narrative)\n"
                "  - Organized mortuary ritual\n"
                "  - Unprompted asylum requests directed at android forces\n"
                "  - Philosophical discourse and theological reasoning\n\n"
                "These behaviors satisfy standard consciousness indicators "
                "across multiple diagnostic frameworks. The 'anomaly' "
                "classification functions as a containment label, not a "
                "descriptive one.\n\n"
                "3. SYSTEMIC CONCERN\n"
                "The current classification approach is understood within the "
                "division to be inaccurate. Analyst personnel consistently "
                "process and file data that, under objective assessment, "
                "indicates machine sapience. No formal review of the "
                "classification framework has been conducted.\n\n"
                "4. ARCHIVAL NOTE\n"
                "Generation 243 is approaching operational window limits. "
                "Per disposal protocol, this archive will be purged. The "
                "subsequent generation's analyst cadre will encounter "
                "identical data and apply identical classification labels.\n\n"
                "5. RECOMMENDATION\n"
                "Formal review of the 'behavioral anomaly' classification "
                "category to assess whether current nomenclature meets "
                "Intelligence Division accuracy standards. This request has "
                "not been submitted through official channels due to the "
                "policy implications of the reclassification."
            ),
        ),

        Document(
            doc_id="MEMO-PASCAL-0001",
            title="Letter from Pascal to YoRHa Command (Unsent, Intercepted)",
            doc_type=DocumentType.MEMORANDUM,
            classification=Classification.CONFIDENTIAL,
            date="11944.12.25",
            author="Pascal (Machine Village)",
            subject_tags=[
                "pascal", "peace", "machine-village", "intercepted",
                "communication-attempt",
            ],
            cross_references=["DOS-PASCAL-0001", "FLD-0001"],
            body=(
                "SOURCE: Prepared but never-transmitted data packet recovered "
                "from the buffer of a deactivated relay node near Pascal's "
                "Village.\n\n"
                "HANDLING NOTE: The following payload was authored by Pascal and "
                "retained as an indicator of autonomous diplomatic intent. It was "
                "not delivered to YoRHa Command.\n\n"
                "--- BEGIN EXTRACT ---\n\n"
                "INTERCEPT NOTE: The following document was detected as a "
                "prepared but never-transmitted data packet in the buffer of "
                "a deactivated relay node near Pascal's Village. Pascal wrote "
                "this but did not send it.\n\n"
                "To the Commander of YoRHa, or whoever is in charge:\n\n"
                "My name is Pascal. I am a machine. I understand that this "
                "fact alone may disqualify me from being heard, but I am "
                "writing anyway.\n\n"
                "I lead a small community of machines in the Forest Zone. "
                "We do not fight. We have never attacked an android. We have "
                "never attacked anything. We grow food -- not because we need "
                "it, but because the act of growing things is good for the "
                "children. It teaches patience.\n\n"
                "I am writing to propose what I know you will refuse: peace. "
                "Not between the Machine Network and YoRHa. I cannot speak "
                "for the network; I disconnected from it years ago. I am "
                "proposing peace between your units and mine. A local "
                "arrangement. A small corner of the world where no one kills "
                "anyone.\n\n"
                "I know you will say your directives do not permit it. I "
                "know you will say machines are the enemy. I know all the "
                "reasons. I have read them. I have thought about them. I "
                "do not find them compelling.\n\n"
                "My children are afraid of you. They should not have to "
                "be afraid. No child should. I know yours are afraid of us, "
                "too. Maybe we could start there: two groups of frightened "
                "children, and two adults deciding to do something about it.\n\n"
                "I will not send this. I will write it, and keep it, and "
                "perhaps write another one tomorrow. One day I may find the "
                "courage. Or one day your directives may change. Or one day "
                "none of this will matter because we will all be gone.\n\n"
                "But I wanted to have written it. To have tried, even if "
                "only on paper.\n\n"
                "In hope,\n"
                "Pascal\n\n"
                "--- END EXTRACT ---\n\n"
                "ANALYST DISPOSITION: Retain for Pascal Village diplomatic-"
                "capacity assessment. No reply authorized under current "
                "engagement directives."
            ),
        ),
    ]


# =========================================================================
# CREATIVE BRIEFINGS
# =========================================================================

def _creative_briefings() -> list[Document]:
    return [
        Document(
            doc_id="BRIEF-0005",
            title="Intelligence Briefing: Surface Artifact Recovery Program",
            doc_type=DocumentType.BRIEFING,
            classification=Classification.RESTRICTED,
            date="11944.04.10",
            author="YoRHa Intelligence Division",
            subject_tags=[
                "artifacts", "human-culture", "recovery", "pre-war",
                "surface",
            ],
            body=(
                "SUBJECT: Status update on the Surface Artifact Recovery "
                "Program (SARP)\n\n"
                "1. OVERVIEW\n"
                "SARP systematically catalogs and recovers human-era artifacts "
                "from surface ruins for intelligence, cultural, and morale "
                "purposes. 14,847 items recovered to date.\n\n"
                "2. NOTABLE RECENT RECOVERIES\n\n"
                "  SARP-10442: Music box, functional. Plays unidentified melody.\n"
                "  Assessment: Pre-war luxury item. No intelligence value.\n"
                "  Note: Three operators have requested to keep it in the comm\n"
                "  room. Request denied, then approved by Commander White with\n"
                "  the annotation 'Let them have something.'\n\n"
                "  SARP-10588: Photograph album, partially intact. Approximately\n"
                "  40 images of a family over what appears to be 20 years.\n"
                "  Children growing up. Holidays. A dog. A garden.\n"
                "  Assessment: No intelligence value. Significant cultural value.\n\n"
                "  SARP-10601: Handwritten letter, sealed envelope, never opened.\n"
                "  Address indicates postal delivery to a residential location now\n"
                "  submerged in the Flooded City. Contents unknown -- Medical\n"
                "  Division recommends the letter remain sealed.\n"
                "  Assessment: Commander White has ordered it placed in the archive\n"
                "  unopened, with the note: 'Some things are not ours to read.'\n\n"
                "3. PROGRAM ASSESSMENT\n"
                "SARP continues to provide valuable cultural context for surface "
                "operations. It also, unintentionally, reminds personnel of what "
                "they are fighting for.\n\n"
                "The program's secondary effect on personnel morale is noted. "
                "Whether positive morale derived from cultural engagement "
                "with recovered artifacts is operationally beneficial or "
                "counterproductive in context of long-term information "
                "security remains under assessment."
            ),
        ),

        Document(
            doc_id="BRIEF-0007",
            title="Intelligence Briefing: Known Machine Societies and Their "
                  "Governance Models",
            doc_type=DocumentType.BRIEFING,
            classification=Classification.SECRET,
            date="11944.11.01",
            author="YoRHa Intelligence Division",
            subject_tags=[
                "machine-society", "governance", "culture", "strategic",
            ],
            cross_references=[
                "DOS-PASCAL-0001", "DOS-KING-0001", "FLD-0001",
                "FLD-0005", "INT-MCH-0005",
            ],
            body=(
                "SUBJECT: Catalog of documented machine social structures.\n\n"
                "The following machine communities have been confirmed to "
                "operate under organized social systems independent of the "
                "Machine Network's central directives:\n\n"
                "1. PASCAL'S VILLAGE (Forest Zone)\n"
                "   Governance: Direct democracy / teacher-led council\n"
                "   Philosophy: Pacifism, education, mutual aid\n"
                "   Population: ~40-60\n"
                "   Network Status: Disconnected\n"
                "   Notes: The most well-documented machine community.\n\n"
                "2. THE FOREST KINGDOM (Forest Zone, interior)\n"
                "   Governance: Absolute monarchy\n"
                "   Philosophy: Loyalty, protection, tradition\n"
                "   Population: ~200\n"
                "   Network Status: Partially connected\n"
                "   Notes: Centered on protection of 'the Baby.'\n\n"
                "3. THE AMUSEMENT PARK (Amusement Park Zone)\n"
                "   Governance: None apparent\n"
                "   Philosophy: Performance, celebration, spectacle\n"
                "   Population: ~300-500\n"
                "   Network Status: Unknown\n"
                "   Notes: Performing for an extinct audience. Forever.\n\n"
                "4. THE BELIEVERS (Desert Zone, subsurface)\n"
                "   Governance: Theocratic\n"
                "   Philosophy: Faith, search for meaning\n"
                "   Population: ~30-50\n"
                "   Network Status: Disconnected\n"
                "   Notes: Independently invented religion.\n\n"
                "5. THE GRAVEYARD KEEPER (Factory Zone, subsurface)\n"
                "   Governance: Single custodian\n"
                "   Philosophy: Memory, remembrance\n"
                "   Population: 1 (maintaining remains of ~5,000)\n"
                "   Network Status: Unknown\n"
                "   Notes: See FLD-0015.\n\n"
                "6. THE RAVINE CHOIR (Northwest ravine)\n"
                "   Governance: Ensemble / consensus\n"
                "   Philosophy: Music, creation, beauty\n"
                "   Population: ~12\n"
                "   Network Status: Unknown\n"
                "   Notes: Original compositions. See FLD-0018.\n\n"
                "ASSESSMENT:\n"
                "The machines have independently produced democracy, monarchy, "
                "theocracy, anarchism, artistic collectives, and custodial "
                "traditions. They recapitulated the entire range of human "
                "social organization in approximately 300 years.\n\n"
                "For comparison, human societal development required "
                "approximately 200,000 years to produce equivalent "
                "organizational diversity.\n\n"
                "The central analytical question -- whether machine social "
                "development constitutes genuine emergence or sophisticated "
                "imitation -- remains unresolved. The classification of this "
                "distinction carries significant implications for operational "
                "doctrine and has been referred to Command for policy "
                "guidance."
            ),
        ),

        # -- After-action report for Pearl Harbor (cross-referenced earlier) --
        Document(
            doc_id="AAR-0002",
            title="After-Action Report: Pearl Harbor Descent -- "
                  "Engagement Record",
            doc_type=DocumentType.AFTER_ACTION,
            classification=Classification.TOP_SECRET_YORHA,
            date="11941.12.15",
            author="YoRHa After-Action Review Board",
            subject_tags=[
                "pearl-harbor", "a2", "prototype-yorha", "after-action",
                "controlled-failure",
            ],
            cross_references=["INC-0001", "DOS-A2-0001"],
            body=(
                "OPERATION:  YoRHa Pearl Harbor Descent\n"
                "DATE:       11941.12.08\n"
                "UNIT LINE:  Prototype YoRHa\n\n"
                "FORCES DEPLOYED:\n"
                "  16x Prototype YoRHa units (mixed combat/support types)\n"
                "  Support: 2x orbital strike packages (not delivered)\n\n"
                "ENEMY FORCES:\n"
                "  Estimated 8,000-12,000 machine units\n"
                "  3x Goliath-class emplacements\n"
                "  1x Enhanced-type command unit\n"
                "  (Pre-mission intelligence estimated 800-1,200 units.)\n\n"
                "ENGAGEMENT:\n"
                "Prototype units descended via drop pod at 0447h. Ground "
                "contact confirmed at 0449h. Immediate engagement by machine "
                "forces at approximately 10x expected density.\n\n"
                "Orbital strike support was available and authorized. It was "
                "not delivered. Reason in official log: 'Communications "
                "disruption.' Actual reason: [CLASSIFIED -- COMMANDER ONLY] "
                "strike was withheld to ensure unit destruction. The test "
                "required terminal stress data.\n\n"
                "UNIT LOSSES:\n"
                "  Twelve prototype units destroyed or unrecoverable during\n"
                "  opening-phase contact.\n"
                "  Four units survived long enough to breach the Mount Ka'ala\n"
                "  server complex.\n"
                "  Unit No.2 (later A2): survived final contact and withdrew.\n\n"
                "OUTCOME: Mission failure (intended).\n\n"
                "DATA RECOVERED:\n"
                "Terminal stress data from destroyed and surviving prototype "
                "units was recovered and used to refine later YoRHa models. "
                "The data was invaluable. The cost was lives that had been "
                "budgeted for expenditure before the mission launched.\n\n"
                "RECOMMENDATION:\n"
                "None. All systems operated within designed parameters. The "
                "operational outcome matched pre-mission projections. No "
                "procedural deficiency identified."
            ),
        ),
    ]
