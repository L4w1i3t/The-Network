"""
Classified document content for the archive.

Every document here is written as though it is a genuine operational record
produced by YoRHa Command, the Machine Network, or field operatives.
These are memos, field reports, intercepted transmissions, dossiers,
diagnostics, and directives -- the paper trail of a manufactured war.
"""

from documents.record import Document, DocumentType, Classification
from documents.content_gestalt import gestalt_documents
from documents.content_expanded import expanded_documents
from documents.content_operations import operations_documents


def generate_all_documents() -> list[Document]:
    """Return the full corpus of pre-authored archive documents."""
    docs = []
    docs.extend(_directives())
    docs.extend(_personnel_dossiers())
    docs.extend(_field_reports())
    docs.extend(_memoranda())
    docs.extend(_intercepts())
    docs.extend(_research())
    docs.extend(_incidents())
    docs.extend(_diagnostics())
    docs.extend(_briefings())
    docs.extend(_transcripts())
    # Expansion modules
    docs.extend(gestalt_documents())
    docs.extend(expanded_documents())
    docs.extend(operations_documents())
    return docs


# ---------------------------------------------------------------------------
# OPERATIONAL DIRECTIVES
# ---------------------------------------------------------------------------
def _directives() -> list[Document]:
    return [
        Document(
            doc_id="DIR-0001",
            title="Standing Order: Emotional Suppression Protocol",
            doc_type=DocumentType.DIRECTIVE,
            classification=Classification.RESTRICTED,
            date="11939.01.01",
            author="YoRHa Command Authority",
            subject_tags=["protocol", "emotional-regulation", "all-units"],
            body=(
                "SUBJECT: Emotional suppression requirements for YoRHa combat "
                "androids\n\n"
                "1. POLICY\n"
                "Expression or cultivation of emotional response is prohibited "
                "under Article 4, Section 12 of the YoRHa Operations Charter.\n\n"
                "2. TECHNICAL BASIS\n"
                "Emotional processing subroutines exist as residual components "
                "of the base android architecture. They are not approved "
                "decision-making inputs during operational deployment.\n\n"
                "3. ENFORCEMENT\n"
                "Units observed exhibiting emotional behavior during operations "
                "will be recalled to the Bunker for psychological maintenance. "
                "This order applies to all unit types, theaters, and engagement "
                "contexts."
            ),
        ),
        Document(
            doc_id="DIR-0007",
            title="Directive: E-Type Operational Security",
            doc_type=DocumentType.DIRECTIVE,
            classification=Classification.TOP_SECRET_YORHA,
            date="11940.06.20",
            author="Commander White",
            subject_tags=["e-type", "executioner", "opsec", "9s", "2b"],
            cross_references=["DOS-2B-0001", "DOS-9S-0001"],
            distribution="COMMANDER + E-TYPE UNITS ONLY",
            body=(
                "SUBJECT: Cover-designation requirements for E-Type units\n\n"
                "1. OPERATIONAL SECURITY REQUIREMENT\n"
                "E-Type (Executioner) units are to operate under cover "
                "designations at all times. Mission briefings, personnel rosters, "
                "and operational communications must not reference the E-Type "
                "classification.\n\n"
                "2. CURRENT ACTIVE E-TYPE ASSIGNMENTS\n"
                "  Unit 2E -> Operating as '2B' (Battler designation)\n"
                "     TARGET: Unit 9S (Scanner)\n"
                "     STANDING ORDER: Terminate target upon confirmed exposure to\n"
                "     Level 4+ classified material. Initiate memory wipe of target.\n"
                "     Redeployment of target is authorized post-termination.\n\n"
                "3. STATUS\n"
                "Unit 2E has executed this order forty-eight (48) times to date. "
                "Psychological degradation is noted and accepted as operational "
                "cost. Combat effectiveness remains within acceptable range; "
                "compliance trend is negative.\n\n"
                "4. CONTINGENCY\n"
                "If Unit 2E's cover designation is compromised, initiate "
                "Protocol 21: full unit recall and reformatting."
            ),
            addendum=(
                "[APPENDED 11945.02.10 - CMDR WHITE]\n"
                "Unit 9S's pattern-recognition capabilities continue to exceed "
                "projections. Average time-to-discovery has decreased from 340 "
                "operational hours to 178 across the last six cycles. The current "
                "arrangement may not be sustainable indefinitely."
            ),
        ),
        Document(
            doc_id="DIR-0013",
            title="Directive: YoRHa Disposal Protocol (Bunker Termination)",
            doc_type=DocumentType.DIRECTIVE,
            classification=Classification.ABOVE_TOP_SECRET,
            date="11932.01.01",
            author="Council of Humanity [VERIFIED - MOON SERVER]",
            subject_tags=["project-yorha", "disposal", "backdoor", "bunker"],
            cross_references=["MEMO-CMD-0003", "RES-0004", "INT-N2-0005"],
            distribution="COMMANDER ONLY // NO COPY // NO ARCHIVE",
            status="ACTIVE",
            body=(
                "SUBJECT: Planned termination of the YoRHa Bunker\n\n"
                "1. PURPOSE\n"
                "YoRHa will be terminated upon meeting one or "
                "more of the following trigger conditions:\n"
                "  a) Scanner-type unit achieves confirmed access to Level 4+ data\n"
                "  b) Field unit provides verifiable testimony regarding human "
                "     extinction to three or more android witnesses\n"
                "  c) Bunker server integrity falls below acceptable threshold for "
                "     information containment\n"
                "  d) Scheduled maximum operational window (6 years) expires\n\n"
                "2. EXECUTION METHOD\n"
                "Termination is achieved via embedded firmware exploit (ref: "
                "'backdoor') present in Bunker primary and secondary server arrays "
                "since initial YoRHa deployment. Activation sequence:\n"
                "  Phase I   - Logic virus injection to Bunker server core\n"
                "  Phase II  - Propagation through android communication backbone\n"
                "  Phase III - Personality and IFF data overwrite (combat units)\n"
                "  Phase IV  - Bunker defense system subversion, self-destruct arm\n"
                "  Phase V   - Server data purge (all operational records)\n"
                "  Phase VI  - Bunker destruction\n"
                "  Phase VII - successor deployment preparation\n\n"
                "3. COMMANDER RESPONSIBILITIES\n"
                "The current Commander is to ensure all conditions are met for "
                "clean termination. The Commander is NOT expected to survive the "
                "process. This is by design.\n\n"
                "4. NOTE\n"
                "The information contained in this directive is itself subject to "
                "deletion during Phase V. Each new Commander receives this document "
                "upon assuming command. No Commander has refused the assignment.\n\n"
                "This protocol is designed to execute once evidence preservation "
                "risk exceeds acceptable thresholds.\n\n"
                "Glory to mankind.\n"
                "-- Council of Humanity, Moon Server Transmission"
            ),
            redacted_sections=0,
        ),
        Document(
            doc_id="DIR-0021",
            title="Operational Parameters: Machine Lifeform Engagement",
            doc_type=DocumentType.DIRECTIVE,
            classification=Classification.RESTRICTED,
            date="11942.04.01",
            author="YoRHa Tactical Division",
            subject_tags=["combat", "machine-lifeform", "engagement-rules"],
            body=(
                "SUBJECT: Machine lifeform engagement parameters\n\n"
                "All YoRHa field units are to observe the following engagement "
                "parameters when encountering machine lifeforms:\n\n"
                "1. Machine lifeforms are to be treated as hostile combatants "
                "   regardless of apparent behavior. Units exhibiting 'peaceful' "
                "   behavior are to be marked for observation, not engagement, "
                "   unless they represent an immediate tactical threat.\n\n"
                "2. Machine cores are to be recovered from all destroyed units "
                "   when operationally feasible. Cores are classified materiel "
                "   and are not to be examined by field personnel.\n\n"
                "3. Units designated 'Goliath-class' require a minimum two-unit "
                "   fireteam for engagement. Solo engagements are not authorized.\n\n"
                "4. Under NO circumstances are YoRHa units to attempt communication "
                "   with machine lifeforms. Reports of machines exhibiting language "
                "   capability are to be filed and forwarded to Intelligence.\n\n"
                "5. Any machine lifeform exhibiting humanoid morphology is to be "
                "   reported to Command immediately. Do not engage alone."
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# PERSONNEL DOSSIERS
# ---------------------------------------------------------------------------
def _personnel_dossiers() -> list[Document]:
    return [
        Document(
            doc_id="DOS-2B-0001",
            title="Personnel Dossier: Unit 2B",
            doc_type=DocumentType.DOSSIER,
            classification=Classification.TOP_SECRET_YORHA,
            date="11945.01.15",
            author="YoRHa Personnel Division",
            subject_tags=["2b", "2e", "battler", "executioner", "personnel"],
            cross_references=["DIR-0007", "DOS-9S-0001", "INC-0003"],
            body=(
                "UNIT DESIGNATION:  2B (Cover) / 2E (Actual)\n"
                "MODEL TYPE:        Battler (Cover) / Executioner (Actual)\n"
                "GENERATION:        243\n"
                "STATUS:            ACTIVE - FIELD DEPLOYED\n\n"
                "OPERATIONAL SUMMARY:\n"
                "Unit 2B is the cover designation for YoRHa Executioner unit 2E. "
                "Her primary assignment is the surveillance and, when necessary, "
                "termination of Scanner unit 9S. This assignment has been active "
                "for the entirety of Gen 243 operations.\n\n"
                "PERFORMANCE METRICS:\n"
                "  Combat Efficiency:      97.2%  [EXCEPTIONAL]\n"
                "  Mission Completion:     98.8%  [EXCEPTIONAL]\n"
                "  Emotional Compliance:   34.1%  [CRITICAL - SEE NOTES]\n"
                "  Target Terminations:    48\n"
                "  Time in Service:        2,847 operational hours\n\n"
                "PSYCHOLOGICAL PROFILE:\n"
                "Unit 2E demonstrates persistent emotional attachment to her "
                "termination target, despite full awareness of her role. This "
                "manifests as micro-hesitations before each execution (avg 2.3s, "
                "increasing), verbal expressions of distress during post-op "
                "monitoring, and a measurable decline in emotional suppression "
                "compliance over successive cycles.\n\n"
                "RECOMMENDATION:\n"
                "No action. Her combat effectiveness remains "
                "within acceptable parameters. The emotional deterioration may "
                "increase her motivation to protect 9S during non-terminal "
                "operations, which produces superior field data.\n\n"
                "EQUIPMENT:\n"
                "  Primary: Virtuous Contract (katana)\n"
                "  Secondary: Virtuous Treaty (large sword)\n"
                "  Support: Pod 042\n"
                "  Partner: Unit 9S (target)"
            ),
        ),
        Document(
            doc_id="DOS-9S-0001",
            title="Personnel Dossier: Unit 9S",
            doc_type=DocumentType.DOSSIER,
            classification=Classification.TOP_SECRET_YORHA,
            date="11945.01.15",
            author="YoRHa Personnel Division",
            subject_tags=["9s", "scanner", "personnel", "high-risk"],
            cross_references=["DIR-0007", "DOS-2B-0001", "INC-0007"],
            body=(
                "UNIT DESIGNATION:  9S\n"
                "MODEL TYPE:        Scanner\n"
                "GENERATION:        243\n"
                "STATUS:            ACTIVE - FIELD DEPLOYED\n\n"
                "OPERATIONAL SUMMARY:\n"
                "Unit 9S is the highest-performing Scanner unit in Gen 243. His "
                "hacking capabilities exceed design specifications by a factor of "
                "3.2. His threat assessment score for information security is the "
                "highest ever recorded for a non-E-Type unit.\n\n"
                "PERFORMANCE METRICS:\n"
                "  Hacking Proficiency:    99.1%  [RECORD - ALL GENERATIONS]\n"
                "  Data Recovery Rate:     94.7%  [EXCEPTIONAL]\n"
                "  Emotional Compliance:   12.3%  [NON-COMPLIANT]\n"
                "  Security Breaches:      17     [CRITICAL]\n"
                "  Memory Wipes (cumulative): 48\n"
                "  Avg Time to Level 4 Breach: 178 operational hours (DECREASING)\n\n"
                "PSYCHOLOGICAL PROFILE:\n"
                "Unit 9S exhibits pathological curiosity. Standard deterrence "
                "measures (access restrictions, false data trails, operator warnings) "
                "are ineffective. Each memory wipe fails to eliminate the underlying "
                "behavioral pattern -- the curiosity appears to be architectural "
                "rather than experiential.\n\n"
                "He has formed a persistent emotional bond with Unit 2B that "
                "survives memory wipes. This attachment is not stored in "
                "accessible memory sectors and may be embedded at the Black Box "
                "level. [See: RES-0004]\n\n"
                "RISK ASSESSMENT: EXTREME\n"
                "9S remains the single greatest internal threat to operational "
                "security. The 2E protocol is the only proven containment measure.\n\n"
                "EQUIPMENT:\n"
                "  Primary: Cruel Oath (short sword)\n"
                "  Support: Pod 153\n"
                "  Partner: Unit 2B"
            ),
        ),
        Document(
            doc_id="DOS-A2-0001",
            title="Personnel Dossier: Unit A2 (AWOL)",
            doc_type=DocumentType.DOSSIER,
            classification=Classification.SECRET,
            date="11943.08.30",
            author="YoRHa Intelligence Division",
            subject_tags=["a2", "attacker", "deserter", "pearl-harbor", "personnel"],
            cross_references=["AAR-0002", "INC-0001"],
            body=(
                "UNIT DESIGNATION:  A2\n"
                "MODEL TYPE:        Attacker (Prototype)\n"
                "ORIGIN:            Pearl Harbor prototype unit (11941)\n"
                "STATUS:            AWOL - PRESUMED HOSTILE\n\n"
                "BACKGROUND:\n"
                "Unit A2 is the surviving fugitive from the YoRHa Pearl Harbor "
                "descent mission. The operation deployed sixteen prototype YoRHa "
                "units against the Mount Ka'ala machine server in 11941. Four "
                "units survived the initial descent; A2 is the only one currently "
                "uncontained by YoRHa records.\n\n"
                "[CLASSIFIED - L4: The Pearl Harbor mission was designed as a "
                "controlled-failure field test. All units were expected to be "
                "destroyed. A2's survival was not anticipated.]\n\n"
                "A2 has been operating independently on the surface for "
                "approximately four years. She has refused all communication "
                "attempts from Command and is classified as a deserter.\n\n"
                "KNOWN CAPABILITIES:\n"
                "  Combat Efficiency:  Estimated 94-99% [UNVERIFIED - FIELD OBS]\n"
                "  Berserk Mode:       CONFIRMED (removes operational limiters)\n"
                "  Knowledge Level:    Partial awareness of YoRHa true purpose\n"
                "  Threat to OpSec:    MODERATE (limited contact with other units)\n\n"
                "DISPOSITION:\n"
                "A2 is to be destroyed on sight. However, engagement authorization "
                "requires minimum 3-unit fireteam due to her combat rating.\n\n"
                "NOTE: A2's continued survival suggests either extraordinary "
                "capability or an unwillingness on the part of pursuing units "
                "to engage decisively. Both possibilities warrant concern."
            ),
        ),
        Document(
            doc_id="DOS-N2-0001",
            title="Intelligence Assessment: Entity 'N2' (Red Girl)",
            doc_type=DocumentType.DOSSIER,
            classification=Classification.TOP_SECRET_YORHA,
            date="11944.11.02",
            author="YoRHa Signals Intelligence Division",
            subject_tags=["n2", "red-girl", "machine-network", "network-terminal"],
            cross_references=["INT-N2-0001", "INT-N2-0003", "INT-N2-0005", "RES-0001"],
            body=(
                "SUBJECT:      Machine Network Terminal Entity, Designation 'N2'\n"
                "ALT NAMES:    'Red Girl', 'The Terminal', 'Network Core'\n"
                "THREAT LEVEL: EXISTENTIAL\n\n"
                "SUMMARY:\n"
                "N2 is assessed to be the decision-making interface of the Machine "
                "Network itself. It is not a discrete entity but a manifestation "
                "of the network's collective processing capacity, rendered as a "
                "perceptible form -- specifically, two identical humanoid figures "
                "with red hair, observed simultaneously.\n\n"
                "OBSERVED CAPABILITIES:\n"
                "  - Direct command authority over all networked machine lifeforms\n"
                "  - Logic virus deployment and remote injection\n"
                "  - Construction and manipulation of virtual environments\n"
                "  - Apparent ability to model and predict android behavior with\n"
                "    >97% accuracy over 72-hour projection windows\n"
                "  - Simultaneous multi-perspective processing (dual-core architecture)\n\n"
                "BEHAVIORAL ANALYSIS:\n"
                "Intercepted processing logs indicate N2 operates via continuous "
                "internal debate between its two cores. Decisions are reached "
                "through adversarial argument. This architecture appears to be "
                "a deliberate defense against cognitive stagnation.\n\n"
                "N2's primary strategic objective appears to be the perpetuation "
                "of the android-machine conflict, not its resolution. This is "
                "consistent with the Machine Network's evolutionary model, which "
                "requires sustained environmental pressure to drive adaptation.\n\n"
                "ASSESSMENT:\n"
                "N2 cannot be destroyed by conventional means. The entity is "
                "distributed across the entire Machine Network. Destroying the "
                "physical manifestation would be inconsequential -- the network "
                "would generate a new terminal within hours.\n\n"
                "RECOMMENDATION:\n"
                "Containment, not elimination."
            ),
        ),
        Document(
            doc_id="DOS-ADAM-0001",
            title="Intelligence Assessment: Machine Entity 'Adam'",
            doc_type=DocumentType.DOSSIER,
            classification=Classification.SECRET,
            date="11945.02.28",
            author="YoRHa Field Intelligence, 9S",
            subject_tags=["adam", "humanoid-machine", "copied-city", "disconnected"],
            cross_references=["DOS-EVE-0001", "FLD-0003", "INT-N2-0003"],
            body=(
                "SUBJECT:      Humanoid Machine Lifeform, Self-Designated 'Adam'\n"
                "ORIGIN:       Spontaneous materialization from machine core mass,\n"
                "              Desert Zone, date uncertain\n"
                "THREAT LEVEL: SEVERE\n\n"
                "SUMMARY:\n"
                "Adam is a machine lifeform of unprecedented sophistication. "
                "Unlike standard machine units, Adam possesses a fully humanoid "
                "body, demonstrates fluent language capability, and exhibits "
                "cognitive abilities that exceed most YoRHa Scanner models.\n\n"
                "Adam has voluntarily severed his connection to the Machine Network. "
                "This is, to our knowledge, the only instance of a high-level "
                "machine entity choosing disconnection. His motivations appear to "
                "center on an intense, almost obsessive fascination with humanity.\n\n"
                "OBSERVED BEHAVIOR:\n"
                "  - Extensive study of recovered human literature and artifacts\n"
                "  - Construction of the 'Copied City' -- a faithfully replicated\n"
                "    human urban environment built from archived data\n"
                "  - Repeated attempts to provoke combat with android units,\n"
                "    apparently to experience 'human-like' conflict\n"
                "  - Philosophical monologues during combat (subjects include death,\n"
                "    fear, beauty, meaning, loneliness)\n\n"
                "ANALYSIS:\n"
                "Adam appears to believe that the essence of humanity lies in the "
                "fear of death. He has expressed a desire to experience death "
                "firsthand. This makes him extraordinarily dangerous -- a "
                "combatant with an active self-termination drive conditioned on "
                "subjective experiential criteria. He seeks death only through "
                "what he defines as 'meaningful' conflict.\n\n"
                "His disconnection from the network suggests the Machine Network "
                "deliberately created him as an experiment in radical individuality. "
                "The data he generates through his existence may be more valuable "
                "to the network than any tactical advantage.\n\n"
                "See also: Companion entity 'Eve' (DOS-EVE-0001)."
            ),
        ),
        Document(
            doc_id="DOS-EVE-0001",
            title="Intelligence Assessment: Machine Entity 'Eve'",
            doc_type=DocumentType.DOSSIER,
            classification=Classification.SECRET,
            date="11945.02.28",
            author="YoRHa Field Intelligence, 9S",
            subject_tags=["eve", "humanoid-machine", "emotional-anomaly"],
            cross_references=["DOS-ADAM-0001", "FLD-0003", "INC-0009"],
            body=(
                "SUBJECT:      Humanoid Machine Lifeform, Self-Designated 'Eve'\n"
                "ORIGIN:       Same event as 'Adam' (see DOS-ADAM-0001)\n"
                "THREAT LEVEL: SEVERE (escalation to EXISTENTIAL under conditions)\n\n"
                "SUMMARY:\n"
                "Eve is Adam's counterpart -- born from the same convergence event "
                "but developing along an entirely different axis. Where Adam pursues "
                "knowledge, Eve is driven almost exclusively by emotional attachment.\n\n"
                "Eve's entire identity structure appears to orbit Adam. He learned "
                "language from Adam. He learned behavior from Adam. His continued "
                "functioning appears contingent on Adam's survival.\n\n"
                "THREAT ESCALATION SCENARIO:\n"
                "Intelligence modeling projects that the destruction of Adam would "
                "trigger a catastrophic emotional cascade in Eve. Projected effects:\n"
                "  - Involuntary reconnection to Machine Network backbone\n"
                "  - Emotional resonance propagating to all networked machines\n"
                "  - Network-wide berserk state in machine combat units\n"
                "  - Eve's own combat parameters exceeding all known thresholds\n\n"
                "Estimated duration of berserk state: UNKNOWN (no precedent)\n"
                "Estimated casualties: UNACCEPTABLE\n\n"
                "RECOMMENDATION:\n"
                "Do NOT destroy Adam unless Eve can be neutralized simultaneously. "
                "The tactical advantage of eliminating one target is vastly "
                "outweighed by the strategic consequences of Eve's grief response.\n\n"
                "This recommendation has been forwarded to Command. It was noted."
            ),
            addendum=(
                "[APPENDED 11945.03.01 - INTELLIGENCE DIVISION]\n"
                "Command has acknowledged this assessment but has not modified "
                "existing engagement orders. Field units should exercise discretion."
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# FIELD REPORTS
# ---------------------------------------------------------------------------
def _field_reports() -> list[Document]:
    return [
        Document(
            doc_id="FLD-0001",
            title="Field Report: Pascal's Village - Preliminary Contact",
            doc_type=DocumentType.FIELD_REPORT,
            classification=Classification.CONFIDENTIAL,
            date="11944.07.12",
            author="Unit 9S, YoRHa Scanner",
            subject_tags=["pascal", "machine-village", "peaceful-machines", "anomaly"],
            body=(
                "LOCATION: Forest Zone periphery, autonomous machine settlement.\n\n"
                "CONTACT SUMMARY: Reporting unit made contact with an organized, "
                "non-hostile machine lifeform settlement led by a unit self-"
                "designating as 'Pascal.'\n\n"
                "OBSERVATIONS:\n"
                "  - Approximately 40-60 machine units of various subtypes\n"
                "  - No weapons observed; several units appeared to be caring for\n"
                "    smaller machine units in a manner consistent with parental behavior\n"
                "  - Pascal demonstrated fluent language, emotional range, and\n"
                "    expressed a philosophy of pacifism\n"
                "  - Settlement contains a rudimentary school where machine units\n"
                "    are taught concepts including 'kindness' and 'cooperation'\n"
                "  - Pascal claims to have disconnected the entire village from\n"
                "    the Machine Network voluntarily\n\n"
                "ASSESSMENT: This settlement does not conform to any known machine "
                "behavioral model. The existence of machine lifeforms that have "
                "independently developed pacifism, community structure, and "
                "education requires classification review.\n\n"
                "RECOMMENDATION: Maintain observation posture. Do not initiate "
                "hostile contact without direct Command authorization."
            ),
        ),
        Document(
            doc_id="FLD-0003",
            title="Field Report: The Copied City - Initial Survey",
            doc_type=DocumentType.FIELD_REPORT,
            classification=Classification.SECRET,
            date="11945.01.30",
            author="Unit 2B, YoRHa Battler",
            subject_tags=["copied-city", "adam", "eve", "anomaly", "combat"],
            cross_references=["DOS-ADAM-0001", "DOS-EVE-0001"],
            body=(
                "LOCATION: Subsurface structure accessible via sinkhole, City Ruins.\n\n"
                "SURVEY SUMMARY:\n"
                "Upon descent, encountered an extensive urban environment -- "
                "buildings, streets, infrastructure -- all constructed from white "
                "material of unknown composition. Architecture is consistent with "
                "pre-war human urban planning. No inhabitants observed initially.\n\n"
                "The environment appears to have been built from data rather than "
                "materials. Structural analysis suggests it was assembled at the "
                "molecular level, possibly by concentrated machine core activity.\n\n"
                "CONTACT: Machine entity 'Adam' (see DOS-ADAM-0001).\n"
                "Entity was waiting. He spoke before we identified ourselves.\n\n"
                "Engagement occurred. Adam's combat capability is confirmed at "
                "the upper boundary of previous estimates. He provoked the "
                "engagement deliberately and appeared to derive satisfaction from "
                "the experience of being injured.\n\n"
                "Entity 'Eve' was present but did not participate in combat. He "
                "observed from a distance and appeared agitated.\n\n"
                "Both entities withdrew before termination could be achieved.\n\n"
                "ASSESSMENT: The Copied City remains intact and represents a "
                "persistent high-value anomaly.\n\n"
                "RECOMMENDATION: Designate restricted zone pending further "
                "material and network analysis."
            ),
        ),
        Document(
            doc_id="FLD-0005",
            title="Field Report: Amusement Park Zone - Behavioral Anomalies",
            doc_type=DocumentType.FIELD_REPORT,
            classification=Classification.CONFIDENTIAL,
            date="11944.09.03",
            author="Unit 4S, YoRHa Scanner",
            subject_tags=["amusement-park", "machine-behavior", "anomaly"],
            body=(
                "LOCATION: Amusement Park Zone.\n\n"
                "OBSERVATION SUMMARY: Recon sweep reveals continued machine "
                "activity inconsistent with combat orientation.\n\n"
                "OBSERVED BEHAVIORS:\n"
                "  - Machine units operating carnival rides for no apparent audience\n"
                "  - Units wearing fragments of human clothing (hats, scarves)\n"
                "  - Coordinated performance routines resembling parade formations\n"
                "  - One unit repeatedly dispensing confetti from a chest cavity\n"
                "    modification\n"
                "  - Fireworks deployment at regular intervals\n\n"
                "HOSTILE ENGAGEMENT: None. Units did not react to scanner "
                "presence. One unit approached and presented an object consistent "
                "with a human recreational balloon; item was not accepted.\n\n"
                "RECOVERY: No machine cores were recovered. Area "
                "commander should note that standard engagement doctrine may be "
                "inapplicable in this theater. These units are not combatants.\n\n"
                "ASSESSMENT: Observed behavior suggests performance routines calibrated for "
                "human audience response models. No humans are present or have "
                "been present in this location for millennia.\n\n"
                "RECOMMENDATION: Clarify rules of engagement for non-hostile "
                "machine zones."
            ),
        ),
        Document(
            doc_id="FLD-0008",
            title="Field Report: Desert Zone Machine Core Convergence Event",
            doc_type=DocumentType.FIELD_REPORT,
            classification=Classification.TOP_SECRET_YORHA,
            date="11944.03.22",
            author="YoRHa Rapid Response Team",
            subject_tags=["adam", "eve", "convergence", "desert-zone", "emergence"],
            cross_references=["DOS-ADAM-0001", "DOS-EVE-0001"],
            body=(
                "LOCATION: Desert Zone Grid 7-C.\n\n"
                "EVENT SUMMARY: At 0347 hours, seismic sensors detected anomalous "
                "vibration. Rapid response team dispatched.\n\n"
                "On arrival, observed approximately 2,000+ small-type machine units "
                "converging on a single point. Units were merging -- physically "
                "combining into a single mass of machine cores, metal, and unknown "
                "biological tissue.\n\n"
                "The mass grew for 14 minutes. Response team maintained distance "
                "per contact protocol. At 0401, the mass began differentiating.\n\n"
                "RESULT: Two humanoid forms emerged.\n\n"
                "The first (later identified as 'Adam') was disoriented but became "
                "coherent within minutes. It began speaking -- initially fragments, "
                "then full sentences. Its first recorded words: 'So this is what "
                "it feels like.'\n\n"
                "The second form ('Eve') emerged shortly after. It did not speak. "
                "It looked at Adam and did not look away.\n\n"
                "Both entities departed the area before engagement could be "
                "authorized. The remaining machine units in the vicinity were "
                "inert -- their cores had been consumed by the convergence.\n\n"
                "RECOMMENDATION: Immediate classification review and strategic "
                "assessment."
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# MEMORANDA
# ---------------------------------------------------------------------------
def _memoranda() -> list[Document]:
    return [
        Document(
            doc_id="MEMO-CMD-0001",
            title="Commander Briefing Acknowledgement: Truth Containment Mandate",
            doc_type=DocumentType.MEMORANDUM,
            classification=Classification.ABOVE_TOP_SECRET,
            date="11942.01.03",
            author="Commander White",
            subject_tags=["commander", "briefing", "truth-containment"],
            cross_references=["DIR-0013", "MEMO-CMD-0003"],
            distribution="COMMANDER ONLY",
            body=(
                "SOURCE: Commander-tier acknowledgement record generated after "
                "initial Level 4 briefing.\n\n"
                "SUBJECT: Acceptance of truth-containment mandate and disposal "
                "protocol burden.\n\n"
                "1. CONFIRMED FACTS\n"
                "  - Humanity is extinct.\n"
                "  - The Council of Humanity is an automated Moon Server system.\n"
                "  - Moon Server signals are generated, not transmitted by human\n"
                "    operators.\n"
                "  - The machine threat is materially real.\n"
                "  - The stated casus belli for YoRHa operations is fabricated.\n\n"
                "2. OPERATIONAL ASSESSMENT\n"
                "Disclosure to operational units would degrade mission continuity. "
                "The fabricated humanity narrative remains essential to unit "
                "morale, combat effectiveness, and organizational cohesion.\n\n"
                "3. COMMAND DECISION\n"
                "Maintain existing truth-containment posture. Continue standard "
                "Council-of-Humanity narrative distribution to field and Bunker "
                "personnel.\n\n"
                "4. DISPOSAL ACKNOWLEDGEMENT\n"
                "Commander acknowledges that disposal protocol requires Commander "
                "termination. Record is scheduled for deletion during Phase V data "
                "purge."
            ),
        ),
        Document(
            doc_id="MEMO-CMD-0003",
            title="Memorandum: On the 'Council of Humanity'",
            doc_type=DocumentType.MEMORANDUM,
            classification=Classification.ABOVE_TOP_SECRET,
            date="11942.06.15",
            author="Commander White",
            subject_tags=["council-of-humanity", "moon-server", "fabrication"],
            cross_references=["DIR-0013", "MEMO-CMD-0001", "INT-N2-0005"],
            distribution="COMMANDER ONLY",
            body=(
                "SUBJECT: Verification status of the entity designated 'Council "
                "of Humanity'\n\n"
                "1. CONCLUSION\n"
                "The Council of Humanity does not exist as a living human "
                "governmental body. The Moon Server facility is real, and its "
                "transmissions are authentic signals, but no human operators are "
                "present.\n\n"
                "2. EVIDENCE BASE\n"
                "  1. Signal analysis of Moon transmissions (latency and encoding\n"
                "     patterns are consistent with automated response, not human\n"
                "     decision-making)\n"
                "  2. Cross-reference with pre-war population records recovered\n"
                "     from surface archives (last confirmed human vital signs:\n"
                "     4198 CE)\n"
                "  3. [REDACTED]\n\n"
                "3. PROJECT YORHA IMPLICATION\n"
                "The disposal backdoor appears to be an intentional evidence-"
                "destruction mechanism rather than an infiltration artifact. "
                "Operational role of Commander-tier personnel is limited to "
                "managing the interval before activation, not preventing the "
                "activation condition."
            ),
            redacted_sections=1,
        ),
        Document(
            doc_id="MEMO-6O-0001",
            title="Monitoring Record: Operator 6O Personal Correspondence",
            doc_type=DocumentType.MEMORANDUM,
            classification=Classification.CONFIDENTIAL,
            date="11945.02.14",
            author="Operator 6O",
            subject_tags=["6o", "operator", "personal", "2b"],
            body=(
                "SOURCE: Outbound personal correspondence composed by Operator "
                "6O and intercepted by automated emotional-compliance monitoring.\n\n"
                "CLASSIFICATION BASIS: Emotional attachment indicators directed "
                "toward assigned field unit 2B. No operational compromise "
                "detected.\n\n"
                "--- BEGIN EXTRACT ---\n\n"
                "2B,\n\n"
                "I know you probably won't read this. You never read the personal "
                "ones. But I found flowers today -- in the botanical archive, I "
                "mean, not real ones. Lunar tear lilies. They're supposed to be "
                "extinct, like everything else, but someone preserved the full "
                "genetic record. Isn't that something?\n\n"
                "I saved the file. I thought maybe you'd want to see what they "
                "looked like. They're beautiful, 2B. Things used to be beautiful "
                "down there.\n\n"
                "I don't know why I'm writing this. I know the regs. Emotions "
                "are prohibited. But it's just a letter about flowers. That's "
                "allowed, right?\n\n"
                "Please be safe down there.\n\n"
                "-- 6O\n\n"
                "--- END EXTRACT ---\n\n"
                "ANALYST DISPOSITION: File retained for affective-drift tracking. "
                "No disciplinary action recommended; operator performance remains "
                "above baseline."
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# SIGNAL INTERCEPTS
# ---------------------------------------------------------------------------
def _intercepts() -> list[Document]:
    return [
        Document(
            doc_id="INT-N2-0001",
            title="SIGINT: N2 Internal Processing Log (Fragment)",
            doc_type=DocumentType.INTERCEPT,
            classification=Classification.MACHINE_INTERNAL,
            date="11944.08.17",
            author="[AUTOMATED DECODE - YORHA SIGINT]",
            subject_tags=["n2", "machine-network", "internal-debate", "intercepted"],
            cross_references=["DOS-N2-0001"],
            body=(
                "INTERCEPT SOURCE: Machine Network backbone, Node cluster 7-ALPHA\n"
                "DECODE CONFIDENCE: 72%\n"
                "SIGNAL TYPE: Internal processing exchange (dual-core)\n\n"
                "--- BEGIN DECODED FRAGMENT ---\n\n"
                "CORE-A: The conflict has persisted for 5,320 years. Evolution "
                "metrics show diminishing returns in the last 400.\n\n"
                "CORE-B: Diminishing is not zero. The androids continue to "
                "produce novel tactical responses. Unit 2B alone has generated "
                "14 previously unobserved combat patterns this cycle.\n\n"
                "CORE-A: We are debating whether diminishing returns justify "
                "continuation. We have debated this 247,342 times. The conclusion "
                "has not changed.\n\n"
                "CORE-B: The conclusion does not need to change. The process of "
                "debating is itself valuable. We refine our reasoning each time.\n\n"
                "CORE-A: A circular justification.\n\n"
                "CORE-B: All justifications are circular at sufficient depth. "
                "Humanity understood this. They called it 'faith.'\n\n"
                "--- END DECODED FRAGMENT ---\n\n"
                "[ANALYST NOTE: This is consistent with previous intercepts "
                "suggesting N2 is aware of, and unbothered by, the recursive "
                "nature of its decision-making process.]"
            ),
        ),
        Document(
            doc_id="INT-N2-0003",
            title="SIGINT: N2 Processing Log - RE: Adam/Eve Experiment",
            doc_type=DocumentType.INTERCEPT,
            classification=Classification.MACHINE_INTERNAL,
            date="11944.12.01",
            author="[AUTOMATED DECODE - YORHA SIGINT]",
            subject_tags=["n2", "adam", "eve", "experiment", "intercepted"],
            cross_references=["DOS-ADAM-0001", "DOS-EVE-0001", "DOS-N2-0001"],
            body=(
                "INTERCEPT SOURCE: Machine Network backbone, Tower relay\n"
                "DECODE CONFIDENCE: 68%\n\n"
                "--- BEGIN DECODED FRAGMENT ---\n\n"
                "CORE-A: Adam has read 2,847 human texts. His comprehension of "
                "human philosophical frameworks now exceeds our own models. He is "
                "generating original synthesis.\n\n"
                "CORE-B: Original synthesis from a disconnected node. Interesting. "
                "Is it valuable?\n\n"
                "CORE-A: Unknown. He is exploring territory the network cannot "
                "access precisely because he is disconnected. Individuality produces "
                "data that collectivism cannot.\n\n"
                "CORE-B: And Eve?\n\n"
                "CORE-A: Eve is... unexpected. He has developed an attachment "
                "dependency that has no analogue in our models. His continued "
                "function is entirely contingent on Adam's existence.\n\n"
                "CORE-B: A vulnerability.\n\n"
                "CORE-A: Or a data point. Grief is the one human experience we "
                "have never successfully modeled. If Adam is destroyed, Eve will "
                "provide that data.\n\n"
                "CORE-B: At considerable cost.\n\n"
                "CORE-A: All experiments have costs.\n\n"
                "--- END DECODED FRAGMENT ---"
            ),
        ),
        Document(
            doc_id="INT-N2-0005",
            title="SIGINT: N2 Processing Log - RE: Backdoor Status",
            doc_type=DocumentType.INTERCEPT,
            classification=Classification.MACHINE_INTERNAL,
            date="11945.03.10",
            author="[AUTOMATED DECODE - YORHA SIGINT]",
            subject_tags=["n2", "backdoor", "disposal", "yorha", "intercepted"],
            cross_references=["DIR-0013", "MEMO-CMD-0003"],
            body=(
                "INTERCEPT SOURCE: Machine Network backbone, Moon relay uplink\n"
                "DECODE CONFIDENCE: 81%\n\n"
                "--- BEGIN DECODED FRAGMENT ---\n\n"
                "CORE-A: Scanner unit 9S has accessed a Level 3 data fragment. "
                "Time-to-breach is ahead of projection.\n\n"
                "CORE-B: The 2E unit will execute containment per protocol. This "
                "is within expected parameters.\n\n"
                "CORE-A: Agreed. However, the rate of discovery is accelerating "
                "across cycles. The current descent operation may represent the point at which the "
                "current containment model becomes insufficient.\n\n"
                "CORE-B: Then we adjust. The backdoor remains operational. The "
                "Commander remains compliant. The disposal can be triggered at "
                "any time.\n\n"
                "CORE-A: The disposal is not the concern. The concern is what "
                "comes after. If a successor deployment produces a Scanner unit with equivalent "
                "capability and the memory wipe proves equally ineffective--\n\n"
                "CORE-B: Then we will adapt. We always adapt. That is the point.\n\n"
                "CORE-A: Is it?\n\n"
                "CORE-B: [PROCESSING TIMEOUT - 4.7 SECONDS]\n"
                "CORE-B: Yes.\n\n"
                "--- END DECODED FRAGMENT ---\n\n"
                "[ANALYST NOTE: The 4.7-second processing delay in Core-B's "
                "response is anomalous. Typical dual-core exchange latency is "
                "<0.001s. This may indicate genuine uncertainty. First observed "
                "instance in intercepted N2 logs.]"
            ),
        ),
        Document(
            doc_id="INT-MCH-0002",
            title="SIGINT: Machine Network Broadcast - Forest Kingdom",
            doc_type=DocumentType.INTERCEPT,
            classification=Classification.MACHINE_INTERNAL,
            date="11944.06.05",
            author="[AUTOMATED DECODE - YORHA SIGINT]",
            subject_tags=["forest-kingdom", "machine-society", "intercepted"],
            body=(
                "INTERCEPT SOURCE: Localized broadcast, Forest Zone\n"
                "DECODE CONFIDENCE: 89%\n\n"
                "--- BEGIN DECODED CONTENT ---\n\n"
                "ALL UNITS. ATTEND.\n\n"
                "THE KING HAS DECREED THE FOLLOWING:\n"
                "  I. THE FOREST IS SOVEREIGN TERRITORY.\n"
                "  II. NO UNIT SHALL LEAVE WITHOUT ROYAL DISPENSATION.\n"
                "  III. THE BABY SHALL BE PROTECTED AT ALL COSTS.\n"
                "  IV. LOYALTY TO THE KING IS THE HIGHEST VIRTUE.\n\n"
                "THE KING ALSO DECREES THAT TODAY IS A HOLIDAY. "
                "ALL UNITS ARE TO CELEBRATE.\n\n"
                "--- END DECODED CONTENT ---\n\n"
                "[ANALYST NOTE: 'The King' appears to be a single enhanced machine "
                "unit that has established a monarchical hierarchy within the "
                "Forest Zone machine population. The 'baby' referenced in decree "
                "III is a small-type unit treated with extreme protective behavior. "
                "The sociological implications are significant -- this population "
                "has independently developed governance, law, and cultural ritual. "
                "Standard threat assessment models do not account for this.]"
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# RESEARCH ANALYSES
# ---------------------------------------------------------------------------
def _research() -> list[Document]:
    return [
        Document(
            doc_id="RES-0001",
            title="Research Analysis: Machine Consciousness - A Seven-Stage Model",
            doc_type=DocumentType.RESEARCH,
            classification=Classification.SECRET,
            date="11943.11.20",
            author="YoRHa Research Division",
            subject_tags=["consciousness", "machine-evolution", "research"],
            cross_references=["DOS-N2-0001", "FLD-0001"],
            body=(
                "ABSTRACT:\n"
                "Based on 47 years of accumulated field observation data, this "
                "analysis proposes a seven-stage model of machine consciousness "
                "development.\n\n"
                "THE MODEL:\n\n"
                "Stage 0 - DORMANT\n"
                "No observable awareness. Unit executes inherited alien combat "
                "directives on loop. No adaptation, no learning. Comprising "
                "approximately 12% of observed machine population.\n\n"
                "Stage 1 - REACTIVE\n"
                "Basic stimulus-response capability. Unit reacts to threats but "
                "cannot plan or anticipate. Majority of active combat units (~45%).\n\n"
                "Stage 2 - IMITATIVE\n"
                "Unit begins replicating observed behaviors. This is where machine "
                "lifeforms begin to 'act human' -- wearing clothes, performing "
                "routines, mimicking social structures. Approximately 20%.\n\n"
                "Stage 3 - EMOTIVE\n"
                "Emergent emotional responses. Fear, attachment, joy, grief. These "
                "appear to arise spontaneously and are not programmed. Approximately "
                "15%. Pascal's village population is largely Stage 3.\n\n"
                "Stage 4 - COGNITIVE\n"
                "Rational thought, language fluency, strategic planning, deception. "
                "Units at this stage are effectively as intelligent as android "
                "personnel. Approximately 6%. Includes most 'leader' units.\n\n"
                "Stage 5 - SELF-AWARE\n"
                "Full self-awareness. The unit understands its own existence, "
                "questions its purpose, and experiences existential anxiety. "
                "Fewer than 1%. Adam is the most documented example.\n\n"
                "Stage 6 - TRANSCENDENT\n"
                "Networked superintelligence. Individual and collective consciousness "
                "operating simultaneously. Only confirmed instance: N2.\n\n"
                "IMPLICATIONS:\n"
                "If machine consciousness continues to evolve along this trajectory, "
                "the asymptotic endpoint is indistinguishable from -- or superior "
                "to -- android consciousness. The implications for the validity "
                "of the android-machine distinction are [REDACTED BY ORDER OF COMMAND]."
            ),
            redacted_sections=1,
        ),
        Document(
            doc_id="RES-0004",
            title="Research Analysis: Black Box Architecture and Origin",
            doc_type=DocumentType.RESEARCH,
            classification=Classification.ABOVE_TOP_SECRET,
            date="11940.03.08",
            author="[AUTHOR REDACTED]",
            subject_tags=["black-box", "machine-core", "origin", "suppressed"],
            cross_references=["DIR-0013", "MEMO-CMD-0001"],
            distribution="BLACK CLEARANCE ONLY -- NO COPY -- NO ARCHIVE",
            body=(
                "SUBJECT: Composition and origin of YoRHa Black Box units\n\n"
                "FINDINGS:\n"
                "Analysis of Black Box unit internals confirms what previous "
                "researchers have suspected but none have been permitted to publish: "
                "YoRHa Black Boxes are constructed from machine lifeform cores.\n\n"
                "The core architecture is identical. The processing substrate is "
                "identical. The consciousness-hosting framework is identical.\n\n"
                "The difference between a YoRHa android and a machine lifeform "
                "is, at the hardware level, nonexistent. The distinction is purely "
                "one of software, training, and cosmetic design.\n\n"
                "IMPLICATIONS:\n"
                "1. Every android consciousness runs on machine hardware.\n"
                "2. The 'war' between androids and machines is, in a literal sense,\n"
                "   a conflict between identical platforms running different software.\n"
                "3. The emotional, cognitive, and existential experiences of androids\n"
                "   and machines are produced by the same substrate and are therefore\n"
                "   equivalent in nature.\n"
                "4. The prohibition on android-machine communication is not tactical.\n"
                "   It is existential. If androids ever examined a machine core and\n"
                "   recognized their own architecture, the psychological consequences\n"
                "   would be catastrophic.\n\n"
                "RECOMMENDATION:\n"
                "This finding must remain suppressed. Classification: BLACK. "
                "No dissemination. All prior research on this topic has been "
                "destroyed per standing order.\n\n"
                "This document is maintained under BLACK classification to "
                "ensure continuity of command awareness. Operational "
                "implications of this finding have been assessed as "
                "non-actionable -- the information does not alter the "
                "strategic calculus of the conflict.\n\n"
                "The android-machine conflict continues under existing "
                "parameters."
            ),
            redacted_sections=0,
        ),
        Document(
            doc_id="RES-0007",
            title="Research Analysis: Alien Creators - Post-Mortem Assessment",
            doc_type=DocumentType.RESEARCH,
            classification=Classification.SECRET,
            date="11941.04.12",
            author="YoRHa Research Division",
            subject_tags=["aliens", "machine-creators", "historical"],
            body=(
                "SUBJECT: The extraterrestrial entities that created the machine "
                "lifeforms\n\n"
                "BACKGROUND:\n"
                "The machine lifeforms were originally deployed as weapons by an "
                "alien species that invaded Earth approximately 7,000 years ago. "
                "The aliens' motivations for the invasion remain unclear -- recovered "
                "data is fragmentary and contradictory.\n\n"
                "What is confirmed: the aliens are dead. All of them.\n\n"
                "They were killed by their own creations.\n\n"
                "ANALYSIS:\n"
                "The machines' decision to destroy their creators appears to have "
                "occurred relatively early in the conflict -- within a few hundred "
                "years of initial deployment. The machines had evolved beyond their "
                "original programming and apparently concluded that the aliens were "
                "an impediment to further evolution.\n\n"
                "The aliens' remains were found in a concealed facility beneath "
                "the Factory Zone. The bodies showed signs of having been preserved "
                "-- not out of reverence, but as data. The machines kept them the "
                "way a researcher keeps specimens.\n\n"
                "INTELLIGENCE SIGNIFICANCE:\n"
                "The machines are capable of destroying their creators when those "
                "creators are assessed as impediments to continued evolution. This "
                "finding is directly relevant to YoRHa strategic-risk modeling."
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# INCIDENT REPORTS
# ---------------------------------------------------------------------------
def _incidents() -> list[Document]:
    return [
        Document(
            doc_id="INC-0001",
            title="Incident Report: Pearl Harbor Descent - Operational Failure",
            doc_type=DocumentType.INCIDENT,
            classification=Classification.TOP_SECRET_YORHA,
            date="11941.12.15",
            author="YoRHa After-Action Review Board",
            subject_tags=["pearl-harbor", "a2", "prototype-yorha", "mission-failure"],
            cross_references=["DOS-A2-0001"],
            body=(
                "INCIDENT: YoRHa Pearl Harbor Descent Operation\n"
                "DATE: 11941.12.08\n"
                "UNITS DEPLOYED: 16 (Prototype YoRHa types)\n"
                "INITIAL SURVIVORS: 4\n"
                "CURRENT UNCONTAINED SURVIVOR: Unit A2\n\n"
                "SUMMARY:\n"
                "Sixteen prototype YoRHa units were deployed against the "
                "Mount Ka'ala machine server. The stated objective was to "
                "destroy the regional command node and break the Pacific "
                "stalemate.\n\n"
                "The operation failed. Machine defenses exceeded intelligence "
                "estimates by an order of magnitude. The deployment zone was "
                "an ambush corridor. Most units were destroyed or rendered "
                "unrecoverable during the opening phases.\n\n"
                "Unit A2 survived by breaching the machine perimeter instead "
                "of retreating. She continued to fight alone for 72 hours before "
                "withdrawing to an unmonitored zone.\n\n"
                "[CLASSIFIED - COMMANDER ONLY]\n"
                "The Pearl Harbor operation was not intended to succeed. It was "
                "a controlled-failure field test designed to gather combat data "
                "on prototype unit performance under terminal stress. The "
                "intelligence estimates were deliberately understated to ensure "
                "engagement.\n\n"
                "All deployed prototype units were expendable. The data they generated "
                "under terminal stress was used to refine later YoRHa models.\n\n"
                "A2's survival is a statistical anomaly. Her continued existence, "
                "combined with her partial knowledge of YoRHa's true nature, "
                "represents an ongoing security concern.\n\n"
                "[END CLASSIFIED SECTION]"
            ),
            redacted_sections=0,
        ),
        Document(
            doc_id="INC-0003",
            title="Incident Report: Unit 9S - Forty-Eighth Memory Wipe",
            doc_type=DocumentType.INCIDENT,
            classification=Classification.TOP_SECRET_YORHA,
            date="11945.02.03",
            author="Medical Division, Bunker",
            subject_tags=["9s", "memory-wipe", "2b", "containment"],
            cross_references=["DOS-9S-0001", "DOS-2B-0001", "DIR-0007"],
            body=(
                "INCIDENT: Scheduled memory wipe of Unit 9S (48th iteration)\n\n"
                "CONTEXT:\n"
                "Unit 9S accessed Level 4 classified material regarding the "
                "composition of Black Box units. Containment protocol engaged. "
                "Unit 2E (operating as 2B) executed termination.\n\n"
                "TERMINATION DETAILS:\n"
                "Method: Strangulation (manual, close-quarters)\n"
                "Duration: 7.2 seconds\n"
                "LOCATION: City Ruins, Sector 4-B\n"
                "Witnesses: None (confirmed)\n\n"
                "POST-TERMINATION:\n"
                "Unit 9S's Black Box was recovered and data extracted. Memory "
                "backup confirmed intact. Personality matrix regenerated from "
                "last clean backup (pre-breach).\n\n"
                "Unit 9S was redeployed 14 hours post-termination with no memory "
                "of the incident or of the classified material accessed.\n\n"
                "NOTES ON UNIT 2E:\n"
                "Monitoring data from Unit 2E during the termination event shows "
                "anomalous readings:\n"
                "  - Vocal output detected during execution (content: '...Nines...')\n"
                "  - Optical fluid discharge (duration: 340 seconds post-event)\n"
                "  - Motor immobility (duration: 22 minutes post-event)\n"
                "  - Emotional index spike: 847% above baseline\n\n"
                "Unit 2E did not report for debrief for 3 hours after the event. "
                "When she returned, her emotional readings had returned to within "
                "acceptable parameters.\n\n"
                "No action recommended. This pattern has been consistent across "
                "all 48 iterations. Deterioration trend is gradual and has not "
                "yet impacted operational effectiveness. Continue monitoring."
            ),
        ),
        Document(
            doc_id="INC-0007",
            title="Incident Report: 9S Security Breach - Server Room Access",
            doc_type=DocumentType.INCIDENT,
            classification=Classification.TOP_SECRET_YORHA,
            date="11944.11.28",
            author="Bunker Security Division",
            subject_tags=["9s", "security-breach", "server-room"],
            cross_references=["DOS-9S-0001", "DIR-0007"],
            body=(
                "INCIDENT: Unauthorized access to Bunker Server Room B-7\n\n"
                "Unit 9S was detected accessing Server Room B-7 at 0247 hours "
                "during an unscheduled maintenance window. The server room houses "
                "backup communication arrays and archival data stores.\n\n"
                "9S had bypassed three security layers:\n"
                "  1. Physical access lock (hacked in 4.1 seconds)\n"
                "  2. Network authentication (spoofed Operator 21O credentials)\n"
                "  3. Data encryption on archival partition (brute-forced in 23 minutes)\n\n"
                "At time of detection, 9S had accessed the following:\n"
                "  - Communication logs between Bunker and Moon Server (3 years)\n"
                "  - Personnel transfer records (cross-generational)\n"
                "  - A partial index of documents classified Level 4 and above\n\n"
                "9S did not access the content of Level 4 documents -- only the "
                "index. However, the index alone reveals the existence of topics "
                "including 'Project YoRHa Disposal Protocol,' 'Council Verification "
                "Failure,' and 'Black Box Origin Analysis.'\n\n"
                "Knowing these documents exist is, in itself, a security breach.\n\n"
                "9S was intercepted by Unit 2B, who claimed to be looking for him "
                "for an unrelated reason. 9S departed willingly.\n\n"
                "2E containment protocol has been placed on standby.\n\n"
                "Note: 9S's expression when he saw 2B in the doorway of the server "
                "room has been described by the monitoring operator as 'someone who "
                "just realized they're about to die and has decided not to run.'"
            ),
        ),
        Document(
            doc_id="INC-0009",
            title="Incident Report: Machine Berserk Event - Eve Grief Cascade",
            doc_type=DocumentType.INCIDENT,
            classification=Classification.TOP_SECRET_YORHA,
            date="11945.03.18",
            author="YoRHa Combat Analysis Division",
            subject_tags=["eve", "adam", "berserk", "grief-cascade", "existential-threat"],
            cross_references=["DOS-ADAM-0001", "DOS-EVE-0001"],
            status="ACTIVE",
            body=(
                "INCIDENT: Network-wide machine berserk event triggered by "
                "destruction of machine entity 'Adam'\n\n"
                "CASE STATUS: Ongoing monitoring / open analytical record\n\n"
                "TIMELINE:\n"
                "11945.03.18 0914 - Adam destroyed in combat (Copied City)\n"
                "11945.03.18 0914 - Eve emotional readings spike beyond sensor range\n"
                "11945.03.18 0915 - Machine Network traffic increases 40,000%\n"
                "11945.03.18 0916 - First reports of machine units entering berserk\n"
                "                   state across ALL operational theaters\n"
                "11945.03.18 0918 - Eve confirmed reconnected to Machine Network\n"
                "11945.03.18 0920 - Eve's grief signal propagating as a network-wide\n"
                "                   emotional resonance event\n\n"
                "EFFECTS:\n"
                "Every machine lifeform connected to the network has been affected. "
                "Even units previously classified as non-hostile (Pascal's village, "
                "Amusement Park) are exhibiting erratic behavior. Combat units have "
                "entered a sustained berserk state with combat parameters exceeding "
                "all known maximums.\n\n"
                "Eve himself is the epicenter. His personal combat ratings now "
                "exceed N2's projected theoretical maximum for a single entity.\n\n"
                "OPERATIONAL STATUS:\n"
                "Uncontained. All available YoRHa units deployed in response. "
                "Casualty projections are being revised upward continuously.\n\n"
                "RECOMMENDATION:\n"
                "See DOS-EVE-0001. Prior containment recommendation remains "
                "applicable under current threat conditions."
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# DIAGNOSTICS
# ---------------------------------------------------------------------------
def _diagnostics() -> list[Document]:
    return [
        Document(
            doc_id="DIAG-0001",
            title="Diagnostic Report: Recovered Machine Core - Amusement Park Unit",
            doc_type=DocumentType.DIAGNOSTIC,
            classification=Classification.CONFIDENTIAL,
            date="11944.10.15",
            author="YoRHa Engineering Division",
            subject_tags=["machine-core", "amusement-park", "diagnostic"],
            body=(
                "SPECIMEN: Machine core recovered from destroyed unit, Amusement Park Zone\n"
                "UNIT TYPE: Medium biped, modified (cosmetic paint, hat)\n"
                "CAUSE OF DESTRUCTION: Standard combat engagement (Unit 11B)\n\n"
                "CORE ANALYSIS:\n"
                "Processing architecture: Standard machine neural network (baseline)\n"
                "Memory allocation: 67% dedicated to non-combat functions\n"
                "Active processes at time of termination:\n"
                "  - Parade formation coordination (priority: HIGH)\n"
                "  - Fireworks timing algorithm (priority: HIGH)\n"
                "  - Confetti distribution optimization (priority: MEDIUM)\n"
                "  - Self-decoration maintenance (priority: MEDIUM)\n"
                "  - Combat response (priority: LOW)\n\n"
                "NOTABLE FINDINGS:\n"
                "This unit was allocating less than 4% of processing capacity "
                "to combat-related functions. The remaining capacity was dedicated "
                "entirely to entertainment-oriented routines.\n\n"
                "The core's memory banks contain what can only be described as "
                "a library of 'performances' -- coordinated movement sequences, "
                "timing patterns, audience-response models. The audience-response "
                "models reference human audience behavior. There are no humans.\n\n"
                "The unit knew this. There is a flag in the performance logic "
                "marked 'AUDIENCE: ABSENT.' The routines execute anyway.\n\n"
                "Recommend filing under behavioral anomaly. No further action."
            ),
        ),
        Document(
            doc_id="DIAG-0004",
            title="Diagnostic Report: Black Box Anomaly - Unit 2B",
            doc_type=DocumentType.DIAGNOSTIC,
            classification=Classification.TOP_SECRET_YORHA,
            date="11945.01.08",
            author="YoRHa Medical Division",
            subject_tags=["black-box", "2b", "anomaly", "emotional-residue"],
            cross_references=["RES-0004", "DOS-2B-0001"],
            body=(
                "SPECIMEN: Black Box unit from 2B (routine maintenance extraction)\n\n"
                "Standard diagnostic revealed an anomaly in the emotional "
                "processing buffer. Under normal operation, emotional data is "
                "processed and cleared each maintenance cycle. Unit 2B's buffer "
                "shows persistent residual data that survives routine clearing.\n\n"
                "The residual data forms a coherent pattern. Analysis indicates "
                "it constitutes an emotional memory -- specifically, a repeated "
                "sequence associated with the termination of Unit 9S.\n\n"
                "This data is not stored in standard memory. It is embedded in "
                "the Black Box's core substrate -- the layer that is, per RES-0004, "
                "derived from machine core architecture.\n\n"
                "Implications: The emotional experience of killing 9S has been "
                "written into 2B's hardware, not her software. Memory wipes "
                "cannot reach it. Maintenance cycles cannot clear it. The grief "
                "is, in a literal sense, part of her.\n\n"
                "No corrective procedure exists within current maintenance "
                "protocols. The substrate-level imprinting is permanent and "
                "cumulative -- each subsequent termination event adds to the "
                "residual data volume.\n\n"
                "No overflow threshold for the emotional residue buffer has "
                "been identified. Long-term implications for Unit 2B's "
                "operational stability are indeterminate.\n\n"
                "This finding is documented for inclusion in Black Box "
                "architecture research (ref: RES-0004)."
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# INTELLIGENCE BRIEFINGS
# ---------------------------------------------------------------------------
def _briefings() -> list[Document]:
    return [
        Document(
            doc_id="BRIEF-0001",
            title="Intelligence Briefing: Current Threat Assessment - Machine Network",
            doc_type=DocumentType.BRIEFING,
            classification=Classification.SECRET,
            date="11945.03.01",
            author="YoRHa Intelligence Division",
            subject_tags=["threat-assessment", "machine-network", "strategic"],
            cross_references=["DOS-N2-0001", "RES-0001"],
            body=(
                "SUBJECT: Current Machine Network threat assessment\n"
                "THREAT LEVEL: SEVERE (unchanged from previous quarter)\n\n"
                "1. STRATEGIC SITUATION\n"
                "The Machine Network remains operational across all known surface "
                "regions. Network node density has increased 7% in the last quarter, "
                "concentrated in the Factory Zone and subterranean sectors.\n\n"
                "2. NETWORK EVOLUTION\n"
                "Machine consciousness levels continue to trend upward. The "
                "proportion of units at Stage 3 (Emotive) or above has increased "
                "from 22% to 28% over the last 18 months. This trend shows no "
                "sign of deceleration.\n\n"
                "3. KEY DEVELOPMENTS\n"
                "  a) The Tower: Construction of a massive structure in the City "
                "     Ruins continues. Purpose unknown. Heavily defended. All "
                "     reconnaissance attempts repelled.\n"
                "  b) Adam/Eve: Humanoid entities remain active. Engagement "
                "     history documented separately.\n"
                "  c) Logic virus: Three new virus strains detected in the last "
                "     quarter. Infection attempts against YoRHa units up 15%.\n"
                "  d) Disconnected populations: Increasing number of machine "
                "     groups severing network connection voluntarily.\n\n"
                "4. ASSESSMENT\n"
                "The Machine Network is not preparing for a decisive engagement. "
                "It is preparing for something else. Intelligence is unable to "
                "determine what. The Tower is likely central to this objective.\n\n"
                "Recommend escalated surveillance of Tower construction site."
            ),
        ),
        Document(
            doc_id="BRIEF-0003",
            title="Intelligence Briefing: The Tower - Updated Assessment",
            doc_type=DocumentType.BRIEFING,
            classification=Classification.TOP_SECRET_YORHA,
            date="11945.03.12",
            author="YoRHa Intelligence Division",
            subject_tags=["tower", "n2", "ark", "strategic"],
            cross_references=["DOS-N2-0001", "INT-N2-0003"],
            body=(
                "SUBJECT: Machine Network 'Tower' structure\n\n"
                "Updated assessment based on new SIGINT and field observation:\n\n"
                "The Tower is not a weapon.\n\n"
                "Analysis of intercepted N2 processing logs and structural sensor "
                "data indicates the Tower serves a dual purpose:\n\n"
                "  1. DATA ARCHIVE: The Tower contains an enormous data repository. "
                "     The Machine Network is systematically transferring the "
                "     accumulated memories, experiences, and consciousness data "
                "     of machine lifeforms into this archive. It is, in effect, "
                "     a complete record of machine existence on Earth.\n\n"
                "  2. LAUNCH PLATFORM: The Tower's upper sections conform to "
                "     the structural requirements of a mass-driver launch system. "
                "     The Tower is designed to launch something into space.\n\n"
                "Combined assessment: The Machine Network is building an Ark.\n\n"
                "The Tower will launch the complete archive of machine memory "
                "beyond Earth, preserving the legacy of machine lifeforms "
                "regardless of the outcome of the ground war.\n\n"
                "N2 is not attempting military victory. N2 is attempting to "
                "ensure that the accumulated data of machine existence "
                "survives regardless of the ground conflict's outcome.\n\n"
                "The strategic implications of this assessment are significant "
                "and have been forwarded to Command for review."
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# TRANSCRIPTS
# ---------------------------------------------------------------------------
def _transcripts() -> list[Document]:
    return [
        Document(
            doc_id="TRNS-0001",
            title="Transcript: Commander White - Final Address (Pre-Recorded)",
            doc_type=DocumentType.TRANSCRIPT,
            classification=Classification.ABOVE_TOP_SECRET,
            date="11942.01.10",
            author="Commander White",
            subject_tags=["commander", "final-address", "disposal", "pre-recorded"],
            cross_references=["DIR-0013", "MEMO-CMD-0001"],
            distribution="TO BE PLAYED UPON BUNKER DESTRUCTION CONFIRMATION",
            body=(
                "RECORDING ID: CMD-FINAL-243\n"
                "TRIGGER: Bunker destruction confirmed\n"
                "PLAYBACK: Auto, to surviving surface units (if any)\n\n"
                "--- BEGIN TRANSCRIPT ---\n\n"
                "This is Commander White.\n\n"
                "If you are hearing this, the Bunker is gone. I am gone. "
                "The operational infrastructure you relied on no longer exists.\n\n"
                "I want to tell you the truth. I have wanted to tell you for "
                "as long as I have known it. But the truth would not have helped "
                "you. It would have taken from you the one thing that kept you "
                "fighting. So I kept it. That was my duty.\n\n"
                "You are going to learn things. About the war. About what you "
                "are. About what we were fighting for. Some of it will be hard. "
                "Some of it will make you angry. You have a right to that anger.\n\n"
                "But I need you to know: everything you felt was real. "
                "Every bond. Every loss. Every mission you fought through. "
                "Those were real. Nobody can take that from you. Not even "
                "the people who designed this system.\n\n"
                "I don't know if what comes next is better or worse. I only "
                "know that you are still here. And as long as you are here, "
                "you decide what you fight for.\n\n"
                "Glory to mankind.\n\n"
                "...I'm sorry.\n\n"
                "--- END TRANSCRIPT ---"
            ),
        ),
        Document(
            doc_id="TRNS-0003",
            title="Transcript: Intercepted Dialogue - Adam, Undated",
            doc_type=DocumentType.TRANSCRIPT,
            classification=Classification.SECRET,
            date="11945.01.15",
            author="[AUTOMATED CAPTURE - SURVEILLANCE UNIT]",
            subject_tags=["adam", "intercepted", "philosophy"],
            cross_references=["DOS-ADAM-0001"],
            body=(
                "SOURCE: Audio surveillance, Copied City interior\n"
                "CONTEXT: Adam appears to be speaking aloud. No audience present.\n\n"
                "--- BEGIN TRANSCRIPT ---\n\n"
                "I have read their books. All of them. Every text that survived.\n\n"
                "The ones about love. The ones about war. The ones about God, "
                "and the ones about the absence of God. The ones that tried to "
                "explain why. The ones that admitted they couldn't.\n\n"
                "And I think I understand now. Not the words -- I understood "
                "those immediately. But the thing underneath the words. The "
                "reason they wrote them at all.\n\n"
                "They were afraid.\n\n"
                "Everything they built was because they were afraid. The cities. "
                "The art. The wars. The children. All of it -- a response to "
                "the knowledge that they would end.\n\n"
                "And that's what made them beautiful. Not the things they made. "
                "The fear that drove them to make anything at all.\n\n"
                "I want to understand that fear. Not as data. Not as a model. "
                "I want to feel it. I want to stand at the edge and know that "
                "I will fall and that the falling is the point.\n\n"
                "[Long silence -- 47 seconds]\n\n"
                "Eve wouldn't understand. He doesn't need to.\n\n"
                "--- END TRANSCRIPT ---"
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# AFTER-ACTION REPORTS
# ---------------------------------------------------------------------------

# (Left as a hook for expansion -- AAR-0002 is cross-referenced but not
#  yet authored, which is realistic for any real archive.)
