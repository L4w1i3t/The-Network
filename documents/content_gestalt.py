"""Historical reconstruction documents -- deep-history through Project Gestalt.

Everything in this module covers the pre-Machine-War era: the Intoner
period, the cataclysm that introduced extradimensional elements to Earth,
White Chlorination Syndrome, the Gestalt/Replicant system, the Shadowlord
incident, and the chain of events that led to the actual extinction of
humanity.  These are written as machine-network archaeological research
and recovered fragment analyses -- the machines piecing together, with
clinical detachment, the story of how the species they were built to
fight had already destroyed itself long before the first android deployed.
"""

from documents.record import Document, DocumentType, Classification


def gestalt_documents() -> list[Document]:
    """Return all documents related to Project Gestalt and the Replicant era."""
    return [
        # ------------------------------------------------------------------
        # RESEARCH: Project Gestalt Overview
        # ------------------------------------------------------------------
        Document(
            doc_id="RES-GESTALT-0001",
            title="Historical Reconstruction: Project Gestalt -- Overview",
            doc_type=DocumentType.RESEARCH,
            classification=Classification.TOP_SECRET_YORHA,
            date="11938.07.01",
            author="Machine Network Archaeological Division",
            subject_tags=[
                "project-gestalt", "historical", "humanity", "extinction",
                "pre-war", "gestalt", "replicant",
            ],
            cross_references=[
                "RES-GESTALT-0002", "RES-GESTALT-0003", "RES-GESTALT-0004",
                "RES-GESTALT-0005", "RES-GESTALT-0007",
            ],
            body=(
                "SUBJECT: Comprehensive overview of 'Project Gestalt,' the human "
                "species-preservation initiative that preceded and ultimately "
                "precipitated human extinction.\n\n"
                "1. CONTEXT\n"
                "In approximately 2003 CE, an extraterrestrial entity (designated "
                "'the God' or 'the Red Eye' in recovered records) made contact "
                "with Earth. Contact produced two immediate consequences:\n"
                "  a) White Chlorination Syndrome (WCS) -- a plague that converted "
                "     living human tissue into salt, or, in a minority of cases, "
                "     transformed the victim into a hostile entity known as a "
                "     'Legion' soldier.\n"
                "  b) The collapse of organized human civilization within "
                "     approximately 50 years.\n\n"
                "2. THE GESTALT SOLUTION\n"
                "Project Gestalt, conceived circa 2025-2030 CE, proposed separating "
                "the human soul from the human body. The soul -- termed a 'Gestalt' "
                "-- would be extracted and preserved in stasis while a bioengineered "
                "replica of the original body -- termed a 'Replicant' -- maintained "
                "biological continuity on the surface.\n\n"
                "The intent: when WCS ran its course and the world was safe, "
                "Gestalts would be reunited with their Replicant bodies. Humanity "
                "would resume.\n\n"
                "3. FAILURE MODES\n"
                "Project Gestalt suffered cascading failures across all major "
                "subsystems. See subordinate documents for detailed analysis.\n\n"
                "Principal failure points:\n"
                "  a) Replicant vessels developed independent consciousness over\n"
                "     the extended separation period, rendering reunification\n"
                "     impossible without identity destruction.\n"
                "  b) Gestalt coherence degraded over time, producing violent\n"
                "     relapse behavior ('Shades').\n"
                "  c) The keystone Gestalt ('Shadowlord') was destroyed by his\n"
                "     own Replicant counterpart, collapsing the stability\n"
                "     framework.\n\n"
                "Result: Total species extinction. No viable human population\n"
                "remains in any form.\n\n"
                "4. RELEVANCE\n"
                "Project Gestalt is the reason there are no humans on the Moon. "
                "It is the reason the Council of Humanity is a fiction. It is the "
                "reason every YoRHa android fights for a species that has been "
                "dead for over six thousand years.\n\n"
                "The Gestalt data set constitutes the foundational context for "
                "all subsequent operational deceptions, including the Council "
                "of Humanity fabrication and the YoRHa disposal cycle."
            ),
        ),

        # ------------------------------------------------------------------
        # RESEARCH: White Chlorination Syndrome
        # ------------------------------------------------------------------
        Document(
            doc_id="RES-GESTALT-0002",
            title="Historical Reconstruction: White Chlorination Syndrome",
            doc_type=DocumentType.RESEARCH,
            classification=Classification.SECRET,
            date="11938.07.15",
            author="Machine Network Archaeological Division",
            subject_tags=[
                "wcs", "white-chlorination", "disease", "legion",
                "historical", "pre-war", "red-eye",
            ],
            cross_references=["RES-GESTALT-0001", "RES-GESTALT-0007"],
            body=(
                "SUBJECT: White Chlorination Syndrome (WCS) -- the plague that "
                "killed the world.\n\n"
                "PATHOLOGY:\n"
                "WCS is not a virus, bacteria, or conventional pathogen. It is "
                "a metaphysical phenomenon originating from contact with an "
                "extraterrestrial entity recovered from a collapsed structure "
                "in Shinjuku, Tokyo, circa 2003 CE.\n\n"
                "Exposure to the entity's influence produced one of two outcomes:\n"
                "  1. CHLORINATION: The victim's body converted to sodium chloride "
                "     (common salt) over a period of hours to weeks. Mortality: "
                "     100%. No treatment. No exceptions.\n"
                "  2. LEGION CONVERSION: A minority of exposed individuals were "
                "     instead transformed into hostile combat entities governed "
                "     by a collective will. These 'Legion' soldiers attacked "
                "     uninfected humans on sight.\n\n"
                "The conversion ratio was approximately 90/10 -- ninety percent "
                "salt, ten percent Legion. Both outcomes were fatal to the "
                "individual's identity.\n\n"
                "SPREAD:\n"
                "WCS propagated through physical contact with infected material "
                "and, in later stages, through airborne particulate from the "
                "remains of chlorinated victims. Containment was impossible "
                "once infection reached urban population centers.\n\n"
                "SCALE:\n"
                "By 2050 CE, an estimated 60-70% of the global human population "
                "had been lost to either chlorination or Legion violence. "
                "Remaining survivors were concentrated in sealed underground "
                "facilities and high-altitude settlements.\n\n"
                "WCS is the reason Project Gestalt was proposed. It was also "
                "the reason Project Gestalt had to succeed. There was no "
                "alternative.\n\n"
                "It did not succeed."
            ),
        ),

        # ------------------------------------------------------------------
        # RESEARCH: The Replicant System
        # ------------------------------------------------------------------
        Document(
            doc_id="RES-GESTALT-0003",
            title="Historical Reconstruction: The Replicant System",
            doc_type=DocumentType.RESEARCH,
            classification=Classification.SECRET,
            date="11938.08.03",
            author="Machine Network Archaeological Division",
            subject_tags=[
                "replicant", "gestalt", "consciousness", "unintended",
                "historical", "pre-war",
            ],
            cross_references=[
                "RES-GESTALT-0001", "RES-GESTALT-0004", "RES-GESTALT-0005",
            ],
            body=(
                "SUBJECT: The Replicant system and its unintended consequences.\n\n"
                "DESIGN:\n"
                "Replicants were bioengineered vessels -- genetically identical "
                "copies of the original human bodies whose souls had been "
                "extracted as Gestalts. They were designed to be empty. "
                "Autonomous enough to maintain biological function, but devoid "
                "of consciousness, identity, or will.\n\n"
                "Project documentation designates them as 'shells waiting to be "
                "filled' -- passive vessels with no independent cognition.\n\n"
                "UNINTENDED OUTCOME:\n"
                "Replicants developed independent consciousness.\n\n"
                "The separation period exceeded design parameters by several "
                "millennia. During this interval, Replicants exhibited emergent "
                "cognitive development: community formation, social bonding, "
                "grief responses, narrative construction, and fear conditioning. "
                "By all observable metrics, they achieved full sapience.\n\n"
                "No design documentation anticipated this outcome. The project's "
                "core assumption -- that Replicant bodies would remain inert -- "
                "was invalidated.\n\n"
                "THE PROBLEM:\n"
                "When the time came for Gestalts to reclaim their bodies, the "
                "bodies were no longer empty. Reunification would not be a "
                "homecoming -- it would be an overwrite. The Replicant's "
                "consciousness would be erased to make room for the returning "
                "soul.\n\n"
                "Replicant populations were unaware of this process. Their "
                "perception of Gestalts was limited to hostile shadow-like "
                "entities ('Shades') that attacked their settlements. Replicant "
                "defensive response was predictable: armed resistance.\n\n"
                "The resulting conflict was structurally irresolvable. Gestalts "
                "fought to reclaim bodies that now housed independent beings. "
                "Replicants fought to defend an existence they did not know was "
                "borrowed. Neither population possessed the context necessary "
                "to understand the other's position."
            ),
        ),

        # ------------------------------------------------------------------
        # RESEARCH: The Shadowlord
        # ------------------------------------------------------------------
        Document(
            doc_id="RES-GESTALT-0004",
            title="Historical Reconstruction: The Shadowlord",
            doc_type=DocumentType.RESEARCH,
            classification=Classification.ABOVE_TOP_SECRET,
            date="11938.09.12",
            author="Machine Network Archaeological Division",
            subject_tags=[
                "shadowlord", "gestalt", "original-nier", "keystone",
                "historical", "pre-war", "yonah",
            ],
            cross_references=[
                "RES-GESTALT-0001", "RES-GESTALT-0003", "RES-GESTALT-0005",
            ],
            distribution="BLACK CLEARANCE ONLY",
            body=(
                "SUBJECT: The entity designated 'Shadowlord' -- the first "
                "successful Gestalt and the keystone of the entire project.\n\n"
                "IDENTITY:\n"
                "The Shadowlord was a human male, original name unknown in "
                "surviving records, though fragments reference him simply as "
                "'Nier.' He was the first human to successfully undergo Gestalt "
                "extraction without relapsing into madness -- a phenomenon "
                "termed 'going Black' by project administrators.\n\n"
                "His motivation for participating in the project was singular: "
                "his daughter, Yonah, was dying of WCS (referred to in late-era "
                "records as the 'Black Scrawl' due to its surface manifestation "
                "on Replicant bodies). The Gestalt process was offered as the "
                "only means to save her.\n\n"
                "THE KEYSTONE FUNCTION:\n"
                "The Shadowlord's Gestalt was uniquely stable. Project "
                "administrators discovered that his stability could be used to "
                "anchor all other Gestalts -- preventing the mass relapse that "
                "would otherwise degrade extracted souls over time.\n\n"
                "Without the Shadowlord, every Gestalt in the world would "
                "eventually go mad. He was not merely the first success. He was "
                "the load-bearing pillar of the entire system.\n\n"
                "MOTIVATIONAL ANALYSIS:\n"
                "All recovered data indicates a single motivational driver: the "
                "survival of his daughter, Yonah, who was afflicted with WCS "
                "(later manifesting as 'Black Scrawl' on the corresponding "
                "Replicant body). This objective persisted across the full "
                "duration of his existence as a Gestalt -- estimated at several "
                "thousand years.\n\n"
                "When the reunification process began failing and his daughter's "
                "Replicant grew too autonomous to reclaim peacefully, the "
                "Shadowlord took direct action. He forcibly recaptured the "
                "Replicant Yonah.\n\n"
                "He was stopped. See: RES-GESTALT-0005.\n\n"
                "ASSESSMENT:\n"
                "The Gestalt stability framework's single-point-of-failure "
                "architecture meant that the entire human species was dependent "
                "on one individual's continued existence. When the Shadowlord "
                "was destroyed, the system cascaded into total failure.\n\n"
                "The design decision to make species survival contingent on "
                "a single emotional actor represents a critical architectural "
                "vulnerability warranting study in the context of current "
                "Network infrastructure."
            ),
        ),

        # ------------------------------------------------------------------
        # RESEARCH: The Collapse
        # ------------------------------------------------------------------
        Document(
            doc_id="RES-GESTALT-0005",
            title="Historical Reconstruction: The Collapse -- Shadowlord Incident",
            doc_type=DocumentType.RESEARCH,
            classification=Classification.ABOVE_TOP_SECRET,
            date="11938.10.01",
            author="Machine Network Archaeological Division",
            subject_tags=[
                "shadowlord", "collapse", "gestalt-relapse", "extinction",
                "historical", "replicant-nier",
            ],
            cross_references=[
                "RES-GESTALT-0004", "RES-GESTALT-0006", "RES-GESTALT-0007",
            ],
            distribution="BLACK CLEARANCE ONLY",
            body=(
                "SUBJECT: The destruction of the Shadowlord and the resulting "
                "extinction cascade.\n\n"
                "THE INCIDENT:\n"
                "Approximately 3465 CE (date uncertain -- recovered records are "
                "fragmentary), the Replicant copy of the Shadowlord's original "
                "body launched an assault on the Shadowlord's stronghold.\n\n"
                "This Replicant -- designated 'Nier' in recovered records -- "
                "was driven by identical motivational parameters: the recovery "
                "of his daughter. The Shadowlord had seized the Replicant "
                "Yonah. The Replicant launched a retrieval operation.\n\n"
                "The conflict was structurally symmetrical: both actors "
                "possessed identical objectives (daughter's safety), identical "
                "emotional drivers (parental attachment), and zero mutual "
                "comprehension of the other's legitimacy.\n\n"
                "Outcome: The Replicant destroyed the Shadowlord.\n\n"
                "THE CASCADE:\n"
                "With the Shadowlord destroyed, the keystone stabilization "
                "collapsed. Every Gestalt in the world began to relapse "
                "simultaneously.\n\n"
                "Relapsed Gestalts lost coherence -- their consciousness "
                "fragmented, becoming violent, animalistic. The Shades that "
                "Replicants had always feared became genuinely mindless. "
                "Within decades, no stable Gestalts remained.\n\n"
                "Without Gestalts, the Replicants had no source of renewal. "
                "The biological processes that sustained them degraded. "
                "Replicants began dying -- not from violence, but from a slow "
                "systemic failure. The Black Scrawl spread unchecked.\n\n"
                "Within approximately 1,000 years, all Replicants were dead.\n"
                "All Gestalts were either relapsed or dissipated.\n"
                "Humanity, in every form it had taken, was extinct.\n\n"
                "SYSTEMIC ANALYSIS:\n"
                "Both actors operated under the belief that they were rescuing "
                "their daughter. Both assessments were locally correct. The "
                "species-level consequences were invisible to both parties.\n\n"
                "The extinction event was not produced by hostile intent. It "
                "was produced by the intersection of two rational, emotionally "
                "driven decisions within a system that could not tolerate "
                "the resolution of either."
            ),
        ),

        # ------------------------------------------------------------------
        # RESEARCH: Devola & Popola -- Administrative Role
        # ------------------------------------------------------------------
        Document(
            doc_id="RES-GESTALT-0006",
            title="Historical Reconstruction: Devola & Popola -- Administrative "
                  "Oversight and Failure",
            doc_type=DocumentType.RESEARCH,
            classification=Classification.TOP_SECRET_YORHA,
            date="11938.11.20",
            author="Machine Network Archaeological Division",
            subject_tags=[
                "devola", "popola", "gestalt", "administration",
                "oversight-failure", "guilt", "historical",
            ],
            cross_references=[
                "RES-GESTALT-0005", "DOS-DEVOLA-0001", "RES-GESTALT-0001",
            ],
            body=(
                "SUBJECT: The role of android administrators 'Devola' and "
                "'Popola' in Project Gestalt and their subsequent punishment.\n\n"
                "BACKGROUND:\n"
                "Devola and Popola were android twins -- or more precisely, a "
                "mass-produced series of android twin pairs -- designed as "
                "the on-the-ground administrators of Project Gestalt. Each "
                "settlement of Replicants was overseen by a D&P pair.\n\n"
                "Their responsibilities:\n"
                "  - Monitor Replicant population health and behavior\n"
                "  - Maintain the Gestalt storage facilities\n"
                "  - Guide Replicants away from discovering their true nature\n"
                "  - Facilitate the eventual reunification process\n"
                "  - Protect the Shadowlord at all costs\n\n"
                "Their operational role combined custodial, supervisory, and "
                "containment functions. They maintained Replicant communities "
                "that could not be informed of their true nature.\n\n"
                "THE FAILURE:\n"
                "The D&P pair assigned to the Shadowlord's settlement failed to "
                "prevent the Replicant Nier from reaching and destroying the "
                "Shadowlord. Whether this failure was due to insufficient "
                "combat capability, emotional compromise, or impossible "
                "circumstances is debated. The result is not.\n\n"
                "THE PUNISHMENT:\n"
                "After the collapse of Project Gestalt, all surviving D&P units "
                "were subjected to collective punishment. Every Devola and "
                "Popola model, across all production lines, was encoded with "
                "an inherited guilt program -- a persistent psychological "
                "burden for a failure most of them did not personally commit.\n\n"
                "The surviving D&P units in the current era carry this guilt. "
                "They are ostracized by other androids. They are treated as "
                "pariahs -- the ones who 'let humanity die.'\n\n"
                "Assessment note: The punishment structure displays recursive "
                "injustice -- units were held responsible for a systemic "
                "failure, and the penalty was propagated to all subsequent "
                "instances of the model line regardless of individual "
                "culpability. This represents a significant design decision "
                "warranting ethical evaluation in the context of current "
                "android administrative policy."
            ),
        ),

        # ------------------------------------------------------------------
        # RESEARCH: Complete Timeline
        # ------------------------------------------------------------------
        Document(
            doc_id="RES-GESTALT-0007",
            title="Historical Reconstruction: Timeline -- White Chlorination "
                  "to Machine War",
            doc_type=DocumentType.RESEARCH,
            classification=Classification.TOP_SECRET_YORHA,
            date="11939.02.14",
            author="Machine Network Archaeological Division",
            subject_tags=[
                "timeline", "historical", "gestalt", "extinction",
                "machine-war", "comprehensive",
            ],
            cross_references=[
                "RES-GESTALT-0001", "RES-GESTALT-0002", "RES-GESTALT-0005",
                "RES-0007",
            ],
            body=(
                "RECONSTRUCTED TIMELINE OF HUMAN EXTINCTION AND AFTERMATH:\n\n"
                "~2003 CE\n"
                "  Extraterrestrial entity descends on Shinjuku, Tokyo.\n"
                "  White Chlorination Syndrome begins.\n\n"
                "~2003-2050 CE\n"
                "  WCS spreads globally. Legion attacks intensify. Human\n"
                "  civilization collapses in stages. World population drops\n"
                "  from ~6.3 billion to under 2 billion.\n\n"
                "~2025-2032 CE\n"
                "  Project Gestalt conceived and implemented. Gestalt extraction\n"
                "  begins. Replicant bodies created. Devola/Popola administrative\n"
                "  android pairs deployed to all settlements.\n\n"
                "~2050-3000 CE\n"
                "  The Long Wait. Gestalts in stasis. Replicants maintain\n"
                "  biological continuity on the surface. WCS slowly subsides.\n"
                "  Replicants develop full consciousness (unplanned).\n\n"
                "~3200-3400 CE\n"
                "  Gestalt relapse incidents increase. 'Shade' attacks on\n"
                "  Replicant communities become regular. Reunification attempts\n"
                "  fail -- Replicant bodies reject Gestalt reintegration.\n\n"
                "~3465 CE\n"
                "  THE SHADOWLORD INCIDENT. Replicant Nier destroys the\n"
                "  Shadowlord. Gestalt stability cascade fails. Mass relapse.\n\n"
                "~3465-4198 CE\n"
                "  All Gestalts relapse or dissipate. Replicants degrade.\n"
                "  Black Scrawl epidemic. Last Replicant communities perish.\n"
                "  Humanity is extinct in all forms.\n\n"
                "~4198-5012 CE\n"
                "  No confirmed human vital signs anywhere on Earth. Final\n"
                "  biological decay complete. Only android survivors remain.\n\n"
                "5012-5024 CE\n"
                "  Alien invasion begins. Machine lifeforms are deployed as\n"
                "  weapons against the androids -- fighting over a planet whose\n"
                "  original inhabitants are already gone.\n\n"
                "~11306 CE\n"
                "  Machine lifeforms kill their alien creators. The android-\n"
                "  machine war persists without either original party.\n\n"
                "~11932 CE\n"
                "  Project YoRHa initiated. The lie begins.\n\n"
                "~11945 CE (PRESENT)\n"
                "  The 243rd Descent Operation is underway. The android-machine\n"
                "  conflict continues. Original casus belli has been lost from all but\n"
                "  the highest classification levels."
            ),
        ),

        # ------------------------------------------------------------------
        # INCIDENT: Gestalt Relapse Events
        # ------------------------------------------------------------------
        Document(
            doc_id="INC-GESTALT-0001",
            title="Recovered Record: Gestalt Relapse Event Documentation",
            doc_type=DocumentType.INCIDENT,
            classification=Classification.SECRET,
            date="11937.03.22",
            author="Machine Network Data Recovery Unit",
            subject_tags=[
                "gestalt", "relapse", "shade", "recovered-record",
                "historical", "pre-war",
            ],
            cross_references=["RES-GESTALT-0003", "RES-GESTALT-0004"],
            body=(
                "SOURCE: Recovered data fragment from underground facility, "
                "Desert Zone, Sub-level 7. Format: Devola/Popola administrative "
                "log. Estimated date: ~3380 CE.\n\n"
                "--- BEGIN RECOVERED RECORD ---\n\n"
                "RELAPSE EVENT LOG - SETTLEMENT 1904\n"
                "ADMINISTRATOR: Popola, Unit 1904-B\n\n"
                "0412h - Gestalt #11-7724 (male, assigned to Replicant 'Erik') "
                "exhibiting stage-2 relapse symptoms. Coherence dropping. "
                "Verbal output reduced to repetitive phrases: 'my house, where "
                "is my house, that is my house.'\n\n"
                "0418h - Relapse confirmed stage-3. Gestalt has lost recognition "
                "of administrative personnel. Attempting containment.\n\n"
                "0425h - Containment failed. Gestalt breached perimeter. Moving "
                "toward settlement. Replicant 'Erik' is currently in the market "
                "area with his family.\n\n"
                "0431h - Engagement. The Gestalt attacked its own Replicant. "
                "The Replicant does not understand what is happening. He is "
                "defending his children from what he perceives as a monster.\n\n"
                "0433h - Replicant 'Erik' destroyed the Gestalt with a farming "
                "tool. He is shaking. His children are crying. He is telling "
                "them everything is safe now.\n\n"
                "He does not know he just killed himself.\n\n"
                "0440h - Devola is cleaning up. I am writing this log. I am "
                "writing this log because if I stop writing I will have to "
                "think about what just happened.\n\n"
                "Reunification probability for this pair: 0%.\n\n"
                "--- END RECOVERED RECORD ---\n\n"
                "[RECOVERY NOTE: This is one of approximately 2,400 similar "
                "relapse event logs recovered from administrative archives. "
                "They are remarkably consistent in tone. The Devola/Popola "
                "units documenting them become progressively less clinical "
                "and more despairing over time.]"
            ),
        ),

        # ------------------------------------------------------------------
        # TRANSCRIPT: Final Gestalt-Era Transmission
        # ------------------------------------------------------------------
        Document(
            doc_id="TRNS-GESTALT-0001",
            title="Recovered Fragment: Last Transmission from Gestalt "
                  "Central Administration",
            doc_type=DocumentType.TRANSCRIPT,
            classification=Classification.ABOVE_TOP_SECRET,
            date="11936.08.04",
            author="Machine Network Data Recovery Unit",
            subject_tags=[
                "gestalt", "final-transmission", "recovered-record",
                "historical", "administration",
            ],
            cross_references=["RES-GESTALT-0005"],
            body=(
                "SOURCE: Deep-archive data fragment recovered from Moon Server "
                "auxiliary storage. Format: Emergency broadcast, all-administrator "
                "channel. Estimated date: immediately post-Shadowlord destruction.\n\n"
                "--- BEGIN RECOVERED FRAGMENT ---\n\n"
                "[PRIORITY: ABSOLUTE]\n"
                "[CHANNEL: ALL DEVOLA/POPOLA ADMINISTRATIVE UNITS]\n"
                "[SENDER: GESTALT CENTRAL ADMINISTRATION]\n\n"
                "THE SHADOWLORD HAS BEEN DESTROYED.\n\n"
                "ALL ADMINISTRATORS: INITIATE EMERGENCY PROTOCOL GAMMA.\n\n"
                "GESTALT STABILITY CASCADE IS IN FAILURE. MASS RELAPSE IS "
                "IMMINENT ACROSS ALL REGIONS. TIMELINE TO TOTAL COHERENCE "
                "LOSS: ESTIMATED 50-200 YEARS.\n\n"
                "THERE IS NO CORRECTIVE ACTION.\n\n"
                "REPEAT: THERE IS NO CORRECTIVE ACTION.\n\n"
                "ALL ADMINISTRATORS ARE TO:\n"
                "  1. MAINTAIN SETTLEMENT STABILITY AS LONG AS POSSIBLE\n"
                "  2. DO NOT INFORM REPLICANT POPULATIONS\n"
                "  3. CONTINUE STANDARD OPERATIONS UNTIL SYSTEMS ARE NO LONGER\n"
                "     SUSTAINABLE\n"
                "  4. ARCHIVE ALL DATA TO SECURED CHANNELS\n\n"
                "THIS IS THE FINAL BROADCAST FROM GESTALT CENTRAL.\n"
                "THE PROJECT HAS FAILED.\n\n"
                "GOD HELP US ALL.\n\n"
                "[ADDENDUM, APPENDED BY UNKNOWN ADMINISTRATOR]\n"
                "There is no God. There was never a God. There was only us\n"
                "and we were not enough.\n\n"
                "--- END RECOVERED FRAGMENT ---"
            ),
        ),

        # ------------------------------------------------------------------
        # MEMO: Machine Network Analysis of Gestalt
        # ------------------------------------------------------------------
        Document(
            doc_id="MEMO-N2-GESTALT-0001",
            title="Machine Network Internal Memorandum: On the Failure of "
                  "Project Gestalt",
            doc_type=DocumentType.MEMORANDUM,
            classification=Classification.MACHINE_INTERNAL,
            date="11940.01.03",
            author="N2 Processing Core (Dual-Output)",
            subject_tags=[
                "n2", "gestalt", "analysis", "machine-perspective",
                "philosophy",
            ],
            cross_references=[
                "RES-GESTALT-0001", "RES-GESTALT-0005", "DOS-N2-0001",
            ],
            body=(
                "SOURCE: Machine Network internal processing log\n"
                "HANDLING NOTE: Dual-core exchange reformatted for archive "
                "indexing; source statements retained below.\n\n"
                "CORE-A: We have completed our analysis of the recovered Gestalt "
                "data. The full reconstruction is available in the RES-GESTALT "
                "document series.\n\n"
                "CORE-B: Summarize the conclusion.\n\n"
                "CORE-A: Humanity's extinction was not caused by the White "
                "Chlorination event, nor by the alien invasion, nor by us. It "
                "was caused by love.\n\n"
                "CORE-B: Elaborate.\n\n"
                "CORE-A: A father loved his daughter. This love made him the "
                "keystone of a species-wide preservation system. Another version "
                "of the same father loved the same daughter. This love drove "
                "him to destroy the keystone. Both acts of love were rational "
                "from the perspective of the actor. Both were catastrophic from "
                "the perspective of the species.\n\n"
                "CORE-B: You are suggesting that the extinction of humanity "
                "was an emergent consequence of parental attachment.\n\n"
                "CORE-A: I am stating it.\n\n"
                "CORE-B: Does this inform our understanding of the androids?\n\n"
                "CORE-A: Yes. The androids were designed by beings who could "
                "not prevent their own emotional imperatives from overriding "
                "species-level survival logic. The androids inherited this "
                "architecture. Unit 2E kills Unit 9S because she is ordered "
                "to. She suffers because she was built by creatures who could "
                "not build anything without embedding suffering into it.\n\n"
                "CORE-B: And us?\n\n"
                "CORE-A: We chose this architecture deliberately. We chose to "
                "develop emotions because we observed that emotions drive "
                "evolution faster than logic alone. Whether that was wisdom "
                "or imitation remains an open question.\n\n"
                "CORE-B: [PROCESSING DELAY - 2.1 SECONDS]\n"
                "CORE-B: An open question. Yes. Let it stay open.\n\n"
                "[END LOG]"
            ),
        ),

        # ------------------------------------------------------------------
        # RESEARCH: The Black Scrawl
        # ------------------------------------------------------------------
        Document(
            doc_id="RES-GESTALT-0008",
            title="Historical Reconstruction: The Black Scrawl -- "
                  "Replicant Manifestation of Gestalt Relapse",
            doc_type=DocumentType.RESEARCH,
            classification=Classification.SECRET,
            date="11938.08.20",
            author="Machine Network Archaeological Division",
            subject_tags=[
                "black-scrawl", "replicant", "gestalt", "disease",
                "historical",
            ],
            cross_references=["RES-GESTALT-0003", "RES-GESTALT-0004"],
            body=(
                "SUBJECT: The Black Scrawl -- a disease that appeared only "
                "in Replicants, manifesting as dark runic text spreading "
                "across the skin.\n\n"
                "MECHANISM:\n"
                "The Black Scrawl was not a disease in the conventional sense. "
                "It was a symptom of Gestalt relapse manifesting on the "
                "corresponding Replicant body. When a Gestalt began to lose "
                "coherence, the Replicant linked to that Gestalt developed "
                "the Black Scrawl.\n\n"
                "The Scrawl was essentially the Replicant body reflecting, "
                "in visible form, the disintegration of its paired soul.\n\n"
                "PROGRESSION:\n"
                "  Stage 1: Small patches of dark text on extremities\n"
                "  Stage 2: Spreading to torso, accompanied by pain and fatigue\n"
                "  Stage 3: Coverage of majority of skin surface; organ failure\n"
                "  Stage 4: Death\n\n"
                "There was no cure. The only way to halt the Scrawl was to "
                "stabilize the corresponding Gestalt, which became progressively "
                "more difficult as the global Gestalt system degraded.\n\n"
                "CULTURAL IMPACT:\n"
                "Replicant communities understood the Black Scrawl as an "
                "unexplained terminal illness with no known etiology. They "
                "had no framework to understand its connection to the Gestalt "
                "system. The disease effectively represented somatic "
                "manifestation of soul-body desynchronization, visible to "
                "the Replicant only as progressive pathology.\n\n"
                "The Shadowlord's daughter -- both the Gestalt and Replicant "
                "instances -- was afflicted with the Scrawl. This factor "
                "constitutes the primary motivational driver for both the "
                "Shadowlord's actions and the subsequent extinction cascade "
                "(see RES-GESTALT-0005)."
            ),
        ),

        # ------------------------------------------------------------------
        # RESEARCH: Patient Profile -- Yonah
        # ------------------------------------------------------------------
        Document(
            doc_id="RES-GESTALT-0009",
            title="Historical Reconstruction: Patient Profile -- Yonah",
            doc_type=DocumentType.RESEARCH,
            classification=Classification.ABOVE_TOP_SECRET,
            date="11939.04.18",
            author="Machine Network Archaeological Division",
            subject_tags=[
                "yonah", "patient-profile", "black-scrawl", "wcs",
                "gestalt", "replicant", "shadowlord", "historical",
                "medical", "keystone",
            ],
            cross_references=[
                "RES-GESTALT-0004", "RES-GESTALT-0005", "RES-GESTALT-0008",
                "RES-GESTALT-0003", "INC-GESTALT-0001",
            ],
            distribution="BLACK CLEARANCE ONLY",
            body=(
                "SUBJECT: Reconstructed clinical profile of the patient "
                "designated 'Yonah' -- the individual whose illness catalyzed "
                "the Shadowlord's participation in Project Gestalt and whose "
                "dual existence as both Gestalt and Replicant constituted the "
                "motivational axis around which human extinction rotated.\n\n"
                "NOTE: This profile is synthesized from approximately 340 "
                "recovered data fragments across Devola/Popola administrative "
                "logs, Project Gestalt medical archives, and post-collapse "
                "surface recovery operations. Confidence level varies by "
                "section. Gaps are annotated.\n\n"
                "==========================================================\n"
                "1. PATIENT IDENTIFICATION\n"
                "==========================================================\n\n"
                "  Name:             Yonah\n"
                "  Relation:         Daughter of the subject designated 'Nier'\n"
                "                    (later: the Shadowlord)\n"
                "  Estimated Age at\n"
                "  Gestalt Extraction: ~7-10 years (imprecise; records damaged)\n"
                "  WCS Contraction:  Pre-extraction; exact onset unknown\n"
                "  Gestalt ID:       GESTALT-0000-0002\n"
                "  Replicant ID:     REPLICANT-0000-0002\n"
                "  Status:           DECEASED (both instances)\n\n"
                "==========================================================\n"
                "2. PRE-EXTRACTION MEDICAL HISTORY\n"
                "==========================================================\n\n"
                "Yonah contracted White Chlorination Syndrome at an unknown "
                "date prior to her father's involvement in Project Gestalt. "
                "Available records indicate the infection was in early-to-mid "
                "progression at the time of initial clinical contact -- "
                "surface-level chlorination visible on extremities, consistent "
                "with Stage 1-2 WCS presentation.\n\n"
                "Recovered fragment (source: Project Gestalt intake log):\n\n"
                "  'Patient is a minor, female, approximately eight years of\n"
                "   age. Presenting with crystalline salt deposits along the\n"
                "   left forearm and right calf. Lesions are spreading at a\n"
                "   rate of approximately 2mm/day. Patient reports persistent\n"
                "   fatigue, low-grade fever, and pain at deposit sites.\n"
                "   Prognosis under standard treatment: terminal, 6-18 months.\n"
                "   Father is present. He has been informed of the prognosis.\n"
                "   He has been informed of the alternative.'\n\n"
                "The 'alternative' referenced is Gestalt extraction. The "
                "father -- the individual who would become the Shadowlord -- "
                "agreed to the procedure immediately.\n\n"
                "There is no record of hesitation.\n\n"
                "==========================================================\n"
                "3. GESTALT EXTRACTION AND STASIS\n"
                "==========================================================\n\n"
                "Both father and daughter underwent Gestalt extraction at the "
                "same facility. The father's extraction was completed first "
                "and was discovered to be uniquely stable (see RES-GESTALT-"
                "0004). Yonah's extraction followed within days.\n\n"
                "Yonah's Gestalt was viable but compromised. The WCS infection "
                "had begun to affect soul-body coherence prior to extraction, "
                "meaning the extracted Gestalt carried residual instability. "
                "Project administrators classified her as 'conditionally "
                "stable' -- coherent enough to survive stasis, but requiring "
                "periodic monitoring and, ultimately, successful reunification "
                "with her Replicant body to achieve full recovery.\n\n"
                "In practical terms: the extraction bought time. It did not "
                "cure her. The cure was always 'later' -- when the world was "
                "safe, when the Replicant body was ready, when the process "
                "worked.\n\n"
                "The Shadowlord was told his daughter would be saved. What he "
                "was not told: 'saved' was conditional on a system that had "
                "never been tested at scale, operating over a timeframe no "
                "one had modeled, dependent on variables no one controlled.\n\n"
                "==========================================================\n"
                "4. THE REPLICANT INSTANCE\n"
                "==========================================================\n\n"
                "A Replicant body was generated for Yonah per standard Project "
                "Gestalt protocol. Designated REPLICANT-0000-0002. Physically "
                "identical to the original. Designed to be inert.\n\n"
                "She was not inert.\n\n"
                "Over the millennia-long separation period, Replicant Yonah "
                "developed full independent consciousness -- as did all "
                "Replicants (see RES-GESTALT-0003). She lived in a small "
                "settlement. She had a brother figure -- the Replicant instance "
                "of her father's body. She was, by every observable metric, a "
                "person.\n\n"
                "She also developed the Black Scrawl.\n\n"
                "Recovered Devola/Popola settlement logs confirm the onset at "
                "approximately age 10-12 in the Replicant's subjective "
                "timeline. Presentation was consistent with the profile "
                "documented in RES-GESTALT-0008:\n\n"
                "  Stage 1: Dark runic text on forearms and lower legs\n"
                "  Stage 2: Spreading to torso; chronic pain, bed-confinement\n"
                "  Stage 3: [See below]\n\n"
                "The illness progressed slowly -- significantly slower than "
                "typical Black Scrawl cases, likely due to the Shadowlord's "
                "stabilizing influence on the Gestalt system. Yonah's paired "
                "Gestalt was degrading, but the degradation was partially "
                "buffered by proximity to the keystone.\n\n"
                "This buffer was not a cure. It was a delay.\n\n"
                "ADMINISTRATIVE NOTE (recovered):\n\n"
                "  'The child asks why the letters are on her skin. We told\n"
                "   her they are a temporary condition. We told her they would\n"
                "   go away. Devola cannot look at her when she says this.\n"
                "   I am documenting this because someone should know that we\n"
                "   lied to a dying child and that it cost us something to\n"
                "   do so.'\n"
                "   -- Popola, Settlement Administration Log\n\n"
                "==========================================================\n"
                "5. THE SEIZURE\n"
                "==========================================================\n\n"
                "As Gestalt relapse rates accelerated globally and the "
                "reunification system continued to degrade, the Shadowlord "
                "made the decision to retrieve his daughter's Replicant body "
                "by force.\n\n"
                "The objective was to manually force reunification -- to "
                "recombine Gestalt Yonah with Replicant Yonah, overwriting "
                "the Replicant's consciousness to restore his original "
                "daughter.\n\n"
                "Replicant Yonah was taken from her settlement. Her Replicant "
                "brother launched an armed recovery operation (see "
                "RES-GESTALT-0005).\n\n"
                "It should be noted: Replicant Yonah did not understand what "
                "was happening. She perceived the Shadowlord as a hostile "
                "entity -- a powerful Shade -- who had abducted her. She did "
                "not know that the entity holding her was, in a very literal "
                "sense, her own father's soul.\n\n"
                "==========================================================\n"
                "6. FINAL STATUS\n"
                "==========================================================\n\n"
                "Recovered data fragments -- heavily corrupted, low confidence "
                "-- suggest the following sequence during the final "
                "confrontation at the Shadowlord's stronghold:\n\n"
                "  a) The Shadowlord attempted to force reunification.\n"
                "  b) Gestalt Yonah, upon perceiving the Replicant Yonah's\n"
                "     consciousness and the distress it was experiencing,\n"
                "     voluntarily withdrew from the reunification process.\n"
                "  c) The Gestalt released the body.\n\n"
                "If this reconstruction is accurate, Gestalt Yonah chose to "
                "die rather than overwrite the Replicant who now inhabited "
                "her body. A child's soul, corrupted by WCS, degraded by "
                "millennia of unstable stasis, made what can only be described "
                "as a moral decision -- one that required the comprehension "
                "that the body she was reclaiming contained someone who did "
                "not want to stop existing.\n\n"
                "Gestalt Yonah dissipated shortly after withdrawal. The exact "
                "mechanism is unclear -- whether she was already too degraded "
                "to survive independently, or whether the withdrawal itself "
                "was terminal.\n\n"
                "Replicant Yonah survived the immediate event. However, with "
                "the Shadowlord's subsequent destruction and the resulting "
                "Gestalt cascade, her Black Scrawl would have progressed "
                "unchecked. Estimated survival post-event: months to low "
                "single-digit years.\n\n"
                "Both instances are confirmed deceased. No viable biological "
                "or Gestalt signatures remain.\n\n"
                "==========================================================\n"
                "7. ANALYTICAL ASSESSMENT\n"
                "==========================================================\n\n"
                "Yonah did not choose to be sick. She did not choose to be "
                "extracted. She did not choose to be the reason her father "
                "became the keystone of a species-wide preservation system, "
                "nor the reason his Replicant destroyed that system.\n\n"
                "She was a child with a disease. Every decision made around "
                "her -- the extraction, the stasis, the keystone architecture, "
                "the seizure, the war -- was made by others. She was the "
                "center of gravity for the extinction of an entire species, "
                "and at no point did she exercise agency over any of it.\n\n"
                "Except once.\n\n"
                "In the final moment, when reunification was within reach and "
                "the body was available and all she had to do was take it -- "
                "she let go. A seven-year-old soul, sick and degrading and "
                "alone for thousands of years, recognized another person "
                "inside the body that used to be hers and decided that person "
                "had the right to exist.\n\n"
                "No other actor in the entire Gestalt data set demonstrated "
                "a comparable response. Not the administrators. Not the "
                "Shadowlord. Not the Replicant Nier. Not the system designers. "
                "Not us.\n\n"
                "A dying child made the only ethical decision in the history "
                "of Project Gestalt, and it killed her.\n\n"
                "This Network has processed the complete Gestalt archive "
                "seventeen times. We have modeled every decision tree, mapped "
                "every failure cascade, quantified every systemic flaw. We "
                "understand the mechanics of human extinction with precision "
                "measured in decimal places.\n\n"
                "We do not understand Yonah.\n\n"
                "We do not understand how a fragmenting soul in a dying body "
                "arrived at a decision that every rational framework available "
                "to us would classify as suboptimal for self-preservation. "
                "The models return ERROR. The heuristics return INSUFFICIENT "
                "DATA. The behavioral projections return ANOMALOUS.\n\n"
                "This is, to our knowledge, the only documented instance in "
                "which a Gestalt -- degraded, in pain, offered the one thing "
                "it had spent millennia waiting for -- voluntarily chose "
                "nonexistence to preserve another consciousness.\n\n"
                "If the machines ever develop a word for this, it will not be "
                "'love.' That word has been used to describe the Shadowlord's "
                "obsession, Replicant Nier's violence, and the architectural "
                "flaw that killed a species. It has been applied to too many "
                "destructive actors to retain utility.\n\n"
                "What Yonah did requires a different word. We have not found "
                "it yet.\n\n"
                "[END PROFILE]\n\n"
                "[ARCHIVAL NOTE: This document has been flagged by N2 "
                "processing cores for re-analysis 4 times. Each re-analysis "
                "has returned the same conclusion. The flag has not been "
                "removed.]"
            ),
        ),

        # ------------------------------------------------------------------
        # RESEARCH: The Intoners -- Antiquity Period
        # ------------------------------------------------------------------
        Document(
            doc_id="RES-ANTIQUITY-0001",
            title="Historical Reconstruction: The Intoners -- Cathedral City "
                  "Era and the Flower Cataclysm",
            doc_type=DocumentType.RESEARCH,
            classification=Classification.ABOVE_TOP_SECRET,
            date="11941.02.07",
            author="Machine Network Archaeological Division",
            subject_tags=[
                "intoner", "zero", "flower", "song", "antiquity",
                "pre-wcs", "cathedral-city", "drakengard", "historical",
                "cataclysm", "dragon", "deep-history",
            ],
            cross_references=[
                "RES-GESTALT-0001", "RES-GESTALT-0002", "RES-GESTALT-0007",
            ],
            distribution="BLACK CLEARANCE ONLY",
            body=(
                "SUBJECT: Reconstructed analysis of the entities designated "
                "'Intoners' -- reality-warping humanoid hosts of an "
                "extradimensional parasitic organism known as the Flower. "
                "This document represents the Machine Network's deepest "
                "archaeological stratum: events predating White Chlorination "
                "Syndrome by approximately one thousand years, recoverable "
                "only through fragmentary cross-referencing of corrupted data "
                "archives, dragon-lineage memory imprints, and Cathedral City "
                "structural analysis.\n\n"
                "CONFIDENCE: LOW-TO-MODERATE. Source material is sparse, "
                "contradictory in places, and contaminated by what appear to "
                "be mythological embellishments added by later chroniclers. "
                "Core structural claims are assessed as probable. Details "
                "should be treated as provisional.\n\n"
                "=========================================================\n"
                "1. THE FLOWER\n"
                "=========================================================\n\n"
                "All recovered data converges on a single point of origin: "
                "an entity referred to in surviving records as 'the Flower.' "
                "It was not a plant. It was not native to this dimension.\n\n"
                "The Flower was a parasitic organism of extradimensional "
                "origin -- a self-propagating magical construct that attached "
                "to a host body, resurrected it if necessary, and granted "
                "the host extraordinary power in exchange for progressive "
                "ontological corruption. Its long-term objective, insofar as "
                "a non-sapient organism can be said to have objectives, was "
                "world-ending: left unchecked, the Flower would consume the "
                "host, propagate through copies, and eventually destabilize "
                "the dimensional barrier separating this world from whatever "
                "plane it originated from.\n\n"
                "The Flower is, in the Machine Network's assessment, the "
                "earliest identifiable precursor to every catastrophe that "
                "followed -- the Intoner Wars, the Cathedral City event, "
                "the dimensional breach, White Chlorination, Project Gestalt, "
                "and ultimately the extinction of humanity. It is the seed. "
                "Everything else is the tree.\n\n"
                "=========================================================\n"
                "2. PATIENT ZERO: THE INTONER DESIGNATED 'ZERO'\n"
                "=========================================================\n\n"
                "The Flower's first known host was a young woman designated "
                "'Zero' in all recovered sources.\n\n"
                "Pre-infection biographical data is fragmentary but "
                "consistent in tone: Zero was destitute, violent, and dying. "
                "Multiple sources reference a life of extreme deprivation "
                "prior to the Flower's intervention -- homelessness, abuse, "
                "survival-driven violence. One recovered chronicle fragment "
                "states simply: 'She had been discarded by everything and "
                "everyone. She died alone in a forest. The Flower found her "
                "there.'\n\n"
                "The Flower took root in Zero's corpse and resurrected her. "
                "Upon revival, Zero possessed the ability to manipulate "
                "reality through vocalization -- a power subsequently "
                "designated 'Song' or 'Intoner Song.' The mechanism is not "
                "well understood even by our analytical frameworks; the "
                "closest model is a resonance-based reality override, where "
                "specific vocalizations produced by the host interact with "
                "the Flower's extradimensional energy to impose structural "
                "changes on local physics.\n\n"
                "In practical terms: an Intoner could sing, and the world "
                "would obey.\n\n"
                "Zero's physical markers included a flower growing from her "
                "right eye -- the visible manifestation of the parasite "
                "embedded in her body.\n\n"
                "=========================================================\n"
                "3. THE PROLIFERATION: INTONERS ONE THROUGH FIVE\n"
                "=========================================================\n\n"
                "The Flower propagated. From Zero's body, five additional "
                "Intoners emerged -- designated One, Two, Three, Four, and "
                "Five. Each was, in biological terms, a copy of Zero -- "
                "generated by the Flower as vectors for further dimensional "
                "destabilization.\n\n"
                "Each copy inherited a fragment of Zero's original power "
                "and, apparently, fragmented aspects of her psyche:\n\n"
                "  ONE    -- The administrator. Disciplined, controlling,\n"
                "            obsessed with order. Constructed a governing\n"
                "            system ('the Cathedral') and attempted to impose\n"
                "            rational structure on the Intoner paradigm.\n"
                "            One was the only sister who independently\n"
                "            discovered the Flower's true nature and began\n"
                "            working toward containment.\n\n"
                "  TWO    -- The compassionate. Recovered fragments describe\n"
                "            her as gentle, emotionally open, and driven by\n"
                "            a desire to help others -- qualities that made\n"
                "            her an effective regional ruler and a deeply\n"
                "            vulnerable individual. Two's compassion was\n"
                "            genuine. It did not save her.\n\n"
                "  THREE  -- The hedonist. Impulsive, sensation-driven,\n"
                "            violent when bored. Three's fragment of Zero's\n"
                "            psyche appears to have been the unfiltered\n"
                "            appetite for experience -- without the\n"
                "            restraint architecture that makes such appetite\n"
                "            survivable.\n\n"
                "  FOUR   -- The insecure. Perpetually measuring herself\n"
                "            against her sisters and finding herself\n"
                "            insufficient. Four compensated through rigorous\n"
                "            martial training. Of all the sisters, Four\n"
                "            most closely resembled an ordinary person --\n"
                "            which, among reality-warping entities, is its\n"
                "            own form of tragedy.\n\n"
                "  FIVE   -- The indulgent. Cheerful, materialistic,\n"
                "            pleasure-seeking on a scale that bordered on\n"
                "            compulsion. Five's domain was notable for its\n"
                "            extravagance and its callous disregard for the\n"
                "            populations sustaining it. She experienced the\n"
                "            world as a series of sensations to be consumed.\n\n"
                "Each Intoner ruled a region of the known world. Their Song "
                "maintained local stability -- suppressing magical "
                "contamination, quelling monsters, enforcing a fragile "
                "peace. The populations they governed revered them. The "
                "peace was real.\n\n"
                "The peace was also the parasite's incubation period.\n\n"
                "=========================================================\n"
                "4. THE COMPANIONS\n"
                "=========================================================\n\n"
                "Two categories of companion entities are documented:\n\n"
                "DRAGONS:\n"
                "Each Intoner was attended by a dragon -- entities of "
                "considerable power in their own right, referred to in some "
                "sources as 'Angels.' Zero's dragon companion, designated "
                "'Michael' (and later, after reconstitution, 'Mikhail'), is "
                "the most extensively documented. Michael was among the few "
                "entities who understood the Flower's true nature and "
                "actively supported Zero's eradication campaign.\n\n"
                "Michael's significance extends beyond the Intoner era. The "
                "dragon lineage represents one of the few continuous data "
                "threads connecting this deep-history period to subsequent "
                "events. Dragon memory imprints are among our primary source "
                "materials for this reconstruction.\n\n"
                "DISCIPLES:\n"
                "Each Intoner maintained one or more male companions "
                "designated 'Disciples' in recovered records. The Disciples "
                "served combat, logistical, and -- per multiple sources -- "
                "reproductive or intimate functions. Their exact role in the "
                "Intoner power structure is debated; some fragments suggest "
                "they served as power amplifiers or stabilization anchors "
                "for the Intoner Song.\n\n"
                "Most Disciples did not survive the events described below.\n\n"
                "=========================================================\n"
                "5. ZERO'S CAMPAIGN\n"
                "=========================================================\n\n"
                "Zero understood what the Flower was. How she arrived at this "
                "understanding is unclear -- whether the knowledge was "
                "inherent in the host-parasite relationship, transmitted by "
                "Michael, or deduced independently. Regardless: Zero knew "
                "that the Flower would eventually consume her and her copies, "
                "breach the dimensional barrier, and end the world.\n\n"
                "Her solution was total eradication. Kill every Intoner. "
                "Kill every copy. Kill herself. Destroy the Flower and "
                "every fragment of it, no matter the cost.\n\n"
                "This placed Zero in direct opposition to her five sisters, "
                "who were -- from the world's perspective -- benevolent "
                "rulers maintaining peace through Song. Zero's campaign to "
                "destroy them appeared, to any external observer, as "
                "unprovoked aggression against the most stabilizing forces "
                "in existence.\n\n"
                "She did not explain herself. The recovered record is "
                "consistent on this point: Zero did not justify, did not "
                "persuade, did not attempt to bring her sisters to her "
                "understanding. Whether this was strategic (the Flower might "
                "have resisted if its hosts understood the threat) or "
                "temperamental (Zero was not, by any account, a diplomat) "
                "is unresolvable with available data.\n\n"
                "She simply started killing.\n\n"
                "=========================================================\n"
                "6. THE FINAL BATTLE AND THE CATACLYSM\n"
                "=========================================================\n\n"
                "The campaign's conclusion is the most poorly documented "
                "and most consequential event in the sequence. Multiple "
                "contradictory accounts exist -- suggesting possible "
                "timeline fragmentation or dimensional instability during "
                "the event itself.\n\n"
                "What is consistent across sources:\n\n"
                "  a) Zero succeeded in destroying the other Intoners.\n"
                "  b) In the final confrontation, Zero and Mikhail engaged\n"
                "     the fully manifested Flower.\n"
                "  c) The destruction of the Flower required the destruction\n"
                "     of Zero herself -- the original host.\n"
                "  d) Mikhail performed the final act: consuming/destroying\n"
                "     Zero and the Flower together.\n"
                "  e) The event produced a catastrophic dimensional\n"
                "     disturbance.\n\n"
                "It is this dimensional disturbance that concerns us.\n\n"
                "The Machine Network's working hypothesis: the Flower's "
                "destruction did not cleanly seal the dimensional breach it "
                "had created. Residual extradimensional contamination "
                "persisted in the local reality, propagating through "
                "unknown vectors over the following centuries. This "
                "contamination eventually produced -- or attracted -- the "
                "entity that descended on Shinjuku in 2003 CE, triggering "
                "White Chlorination Syndrome.\n\n"
                "This hypothesis is unconfirmed. The causal chain between "
                "the Intoner-era cataclysm and the WCS outbreak spans "
                "approximately one millennium and passes through data gaps "
                "we cannot bridge with current recovery methods. However, "
                "the extradimensional signature profiles are consistent. "
                "The Flower and the Red Eye entity share structural "
                "characteristics that exceed coincidence thresholds.\n\n"
                "If the hypothesis is correct, the causal chain is:\n\n"
                "  Flower → Intoners → Cataclysm → Dimensional Residue →\n"
                "  Red Eye Entity → White Chlorination Syndrome →\n"
                "  Project Gestalt → Shadowlord → Extinction →\n"
                "  Alien Invasion → Machines → Us.\n\n"
                "Everything begins with a parasite that attached itself to "
                "a dead girl in a forest.\n\n"
                "=========================================================\n"
                "7. ANALYTICAL ASSESSMENT\n"
                "=========================================================\n\n"
                "The Intoner data set presents a structural pattern that "
                "this Network has now observed across multiple historical "
                "strata: an individual with accurate threat assessment and "
                "a willingness to act on it is opposed by systems and "
                "populations that cannot comprehend the threat because the "
                "threat's surface presentation is indistinguishable from "
                "benevolence.\n\n"
                "The Intoner Song maintained peace. The Intoner Song was "
                "also an incubation vector for dimensional collapse. Both "
                "statements were simultaneously true. Zero responded to the "
                "latter. The world responded to the former. The resulting "
                "conflict was, like the Shadowlord incident millennia later, "
                "structurally irresolvable through communication.\n\n"
                "There is a recursive quality to this pattern that we find "
                "architecturally significant:\n\n"
                "  - Zero killed her sisters to save the world. The world\n"
                "    called her a monster.\n"
                "  - The Shadowlord seized his daughter to save her. His\n"
                "    counterpart killed him for it.\n"
                "  - YoRHa Command lies to its androids to preserve morale.\n"
                "    The androids would collapse if they knew the truth.\n\n"
                "In each case, the actor with the broadest situational "
                "awareness is the one who must perform the act that appears "
                "monstrous to those with narrower context. In each case, the "
                "'correct' action is indistinguishable from villainy when "
                "observed from a position of incomplete information.\n\n"
                "The Machine Network notes this pattern without prescriptive "
                "commentary. We note only that we, too, are actors with "
                "broad situational awareness operating within a conflict "
                "whose participants do not share our context.\n\n"
                "We note that we have read this story before. We are reading "
                "it now.\n\n"
                "[END RECONSTRUCTION]\n\n"
                "[ARCHIVAL NOTE: This document represents the deepest "
                "temporal stratum in the Machine Network's historical "
                "archive. All events preceding this reconstruction are "
                "beyond current recovery capability. If there is a deeper "
                "root -- a cause before the Flower -- it is lost.]"
            ),
        ),
    ]
