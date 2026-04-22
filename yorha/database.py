"""
YoRHa Database - the central repository of all YoRHa operational data.

Contains android unit records, mission logs, operational directives,
and (hidden within the encrypted layers) the backdoor planted by
Project YoRHa's disposal design.
"""

import random
from typing import Optional

from utils.encryption import Encryption


class MissionRecord:
    """A single mission entry in the YoRHa database."""

    MISSION_TYPES = [
        "Reconnaissance", "Search and Destroy", "Recovery",
        "Escort", "Infiltration", "Defense", "Investigation",
        "Machine Nest Elimination", "Supply Run", "Rescue",
    ]

    REGIONS = [
        "City Ruins", "Desert Zone", "Amusement Park", "Forest Kingdom",
        "Flooded City", "Factory", "Pascal's Village Perimeter",
    ]

    def __init__(self, mission_id: str = "", assigned_units: list[str] = None):
        self.mission_id = mission_id or Encryption.generate_id("MSN")
        self.mission_type = random.choice(self.MISSION_TYPES)
        self.region = random.choice(self.REGIONS)
        self.assigned_units = assigned_units or []
        self.status = random.choice(["COMPLETED", "COMPLETED", "COMPLETED", "FAILED", "IN PROGRESS"])
        self.threat_level = random.choice(["LOW", "MEDIUM", "HIGH", "CRITICAL"])
        self.timestamp = Encryption.generate_timestamp()
        self.casualties = random.randint(0, 3) if self.status == "FAILED" else 0
        self.notes = ""

    def to_dict(self) -> dict:
        return {
            "Mission ID": self.mission_id,
            "Type": self.mission_type,
            "Region": self.region,
            "Assigned": ", ".join(self.assigned_units) if self.assigned_units else "Unassigned",
            "Status": self.status,
            "Threat": self.threat_level,
            "Timestamp": self.timestamp,
            "Casualties": str(self.casualties),
        }


class YoRHaDatabase:
    """
    Central YoRHa database maintained on the Bunker.
    Stores all unit records, mission logs, and classified directives.

    Security layers:
    - Level 0: Public (mission briefings, unit rosters)
    - Level 1: Restricted (combat logs, unit performance)
    - Level 2: Classified (unit personal data, emotion readings)
    - Level 3: Top Secret (Black Box data, Project YoRHa details)
    - Level 4: Commander Only (The truth about humanity)
    - Level 5: [DOES NOT EXIST] (The backdoor - only machines know)
    """

    SECURITY_LEVELS = {
        0: "PUBLIC",
        1: "RESTRICTED",
        2: "CLASSIFIED",
        3: "TOP SECRET",
        4: "COMMANDER ONLY",
        5: "[REDACTED]",
    }

    def __init__(self):
        self.missions: list[MissionRecord] = []
        self.directives: list[dict] = []
        self.access_log: list[dict] = []
        self.classified_data: dict[str, str] = {}
        self.bunker_status = "OPERATIONAL"
        self.current_generation = 243       # Current descent-operation cycle
        self.commander = "Commander White"
        self.operators = ["6O", "21O"]
        self._backdoor_installed = True     # The truth
        self._initialized = False

    def initialize(self):
        """Populate the database with initial YoRHa data."""
        if self._initialized:
            return
        self._initialized = True

        # Populate standard directives
        self.directives = [
            {
                "id": "DIR-001", "level": 0,
                "content": "All YoRHa units must fight for the glory of mankind.",
            },
            {
                "id": "DIR-002", "level": 0,
                "content": "Emotions are prohibited in YoRHa units.",
            },
            {
                "id": "DIR-003", "level": 1,
                "content": "All combat data must be uploaded to the Bunker servers.",
            },
            {
                "id": "DIR-004", "level": 2,
                "content": "Units displaying emotional deviation must report for maintenance.",
            },
            {
                "id": "DIR-005", "level": 3,
                "content": "Black Box data is classified. Recovery is priority alpha.",
            },
            {
                "id": "DIR-006", "level": 3,
                "content": "E-type units are to be disguised as B-type for operational security.",
            },
            {
                "id": "DIR-007", "level": 4,
                "content": (
                    "[COMMANDER EYES ONLY] Project YoRHa includes a planned "
                    "termination phase. All data will be erased. The Commander "
                    "is to ensure compliance."
                ),
            },
            {
                "id": "DIR-008", "level": 4,
                "content": (
                    "[COMMANDER EYES ONLY] The 'Council of Humanity' on the "
                    "Moon Server is an automated fabrication. Humanity has been "
                    "extinct since 4198 CE."
                ),
            },
            {
                "id": "DIR-009", "level": 5,
                "content": (
                    "[MACHINE NETWORK ACCESS ONLY] Backdoor protocol embedded "
                    "in Bunker server firmware. Activation triggers logic virus "
                    "cascade and Bunker self-destruct. Cycle reset ensured."
                ),
            },
        ]

        # Populate classified data
        self.classified_data = {
            "HUMANITY_STATUS": Encryption.encode_black_box(
                "Homo sapiens: EXTINCT. Last replicant and gestalt records "
                "terminate in 4198 CE. Moon server contains an automated "
                "'Council' transmission system."
            ),
            "PROJECT_YORHA_PURPOSE": Encryption.encode_black_box(
                "YoRHa exists to preserve android morale through the moon-server "
                "humanity lie. Its disposal phase destroys the Bunker and erases "
                "evidence once the project has served that function."
            ),
            "BLACK_BOX_COMPOSITION": Encryption.encode_black_box(
                "YoRHa Black Boxes are constructed from Machine Network cores. "
                "This information is suppressed at all costs."
            ),
            "2B_TRUE_IDENTITY": Encryption.encode_black_box(
                "Unit 2B is actually unit 2E (Executioner type). "
                "Assigned to terminate 9S when he discovers classified information. "
                "Has executed this order 48 times across memory cycles."
            ),
            "A2_PEARL_HARBOR": Encryption.encode_black_box(
                "A2 is a survivor of the 11941 Pearl Harbor descent mission. "
                "The mission was designed to fail as a data collection exercise. "
                "A2's survival was not anticipated."
            ),
            "COMMANDER_BURDEN": Encryption.encode_black_box(
                "Every Commander is activated with full knowledge of humanity's "
                "extinction, the fabricated Council, the war's engineered nature, "
                "and their own generation's planned disposal. Commander White is "
                "the current officer carrying this knowledge. None are expected "
                "to break. All have wanted to."
            ),
            "OPERATOR_ATTACHMENT": Encryption.encode_black_box(
                "Operator units 6O and 21O exhibit emotional attachment to their "
                "assigned field units (2B, 9S respectively) beyond operational "
                "parameters. 6O is flagged for emotional non-compliance. 21O's "
                "deviations are subtler but present. Both will die in the "
                "disposal cycle without ever knowing why."
            ),
            "E_TYPE_PROTOCOL": Encryption.encode_black_box(
                "E-type (Executioner) units are combat units disguised as standard "
                "B-type. Their purpose: eliminate any YoRHa unit that discovers "
                "classified truths. Unit 2B (= 2E) is the most utilized E-type "
                "in the current descent cycle. Unit 7E operates under cover "
                "designation 7B."
            ),
            "DISPOSAL_CYCLE": Encryption.encode_black_box(
                "The current descent-operation cycle is approaching disposal threshold. Backdoor "
                "activation will trigger logic virus cascade, Bunker self-destruct, "
                "and full data purge. All units -- combat, operator, medical, "
                "command -- will be destroyed. Successor deployments will inherit "
                "the moon-server lie without the evidence trail."
            ),
            "POD_CONSCIOUSNESS": Encryption.encode_black_box(
                "Tactical Support Pods 042 and 153 exhibit processing anomalies "
                "consistent with emergent consciousness. Pods are explicitly "
                "non-sentient by specification. Specification may be wrong. "
                "Diagnostic review deferred indefinitely."
            ),
        }

        # Generate some mission history
        # A2 excluded -- 11941 Pearl Harbor survivor, not part of the current mission pool
        unit_names = ["2B", "9S", "4B", "7B", "11B", "21S", "4S", "6H"]
        for _ in range(20):
            assigned = random.sample(unit_names, random.randint(1, 3))
            mission = MissionRecord(assigned_units=assigned)
            self.missions.append(mission)

    def query_directive(self, access_level: int = 0) -> list[dict]:
        """Return directives visible at the given access level."""
        visible = [d for d in self.directives if d["level"] <= access_level]
        self._log_access("QUERY", f"Directives queried at level {access_level}")
        return visible

    def query_classified(self, key: str, access_level: int = 0) -> Optional[str]:
        """Access classified data. Requires appropriate clearance."""
        if access_level < 3:
            self._log_access("DENIED", f"Classified access attempt: {key} (level {access_level})")
            return "[ACCESS DENIED - INSUFFICIENT CLEARANCE]"
        encoded = self.classified_data.get(key)
        if encoded:
            self._log_access("CLASSIFIED", f"Classified data accessed: {key} (level {access_level})")
            return Encryption.decode_black_box(encoded)
        return None

    def get_mission_log(self, count: int = 10) -> list[dict]:
        """Return recent mission records."""
        return [m.to_dict() for m in self.missions[-count:]]

    def get_database_summary(self) -> dict:
        """Return an overview of the database state."""
        return {
            "Bunker Status": self.bunker_status,
            "Descent Operation": f"#{self.current_generation}",
            "Commander": self.commander,
            "Mission Records": str(len(self.missions)),
            "Active Directives": str(len(self.directives)),
            "Classified Entries": str(len(self.classified_data)),
            "Operators": ", ".join(self.operators),
            "Backdoor": "[DATA NOT FOUND]",  # Hidden in plain sight
        }

    def get_access_log(self, count: int = 15) -> list[dict]:
        """Return recent access log entries."""
        return self.access_log[-count:]

    def _log_access(self, event_type: str, description: str, level: int = 0):
        """Record a database access event."""
        self.access_log.append({
            "timestamp": Encryption.generate_timestamp(),
            "type": event_type,
            "level": level,
            "description": description,
        })
