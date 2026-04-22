"""
YoRHa android unit data models.

These classes intentionally model only the fields used by the archive
terminal: identity, role, status-relevant stats, deployment cycle, location,
and classified notes. Dialogue and combat-action helpers were removed because
this project is a database terminal, not an interaction simulator.

Unit type designations:
- B (Battler): Front-line combat units, e.g. 2B
- S (Scanner): Intelligence/hacking units, e.g. 9S
- A (Attacker): Prototype heavy assault units, e.g. A2
- H (Healer): Support/repair units
- D (Defender): Shield/tank units
- E (Executioner): Secret type that eliminates units who learn too much
- O (Operator): Bunker-based mission coordinators
"""

from typing import Optional

from core.consciousness import ConsciousnessLevel
from units.base import AndroidUnit


class YoRHaBattler(AndroidUnit):
    """
    B-type (Battler) front-line android.
    Unit 2B is secretly Type 2E, assigned to repeatedly terminate 9S.
    """

    def __init__(self, number: int = 2, generation: int = 243):
        super().__init__(
            f"{number}B",
            model_type="Battler",
            consciousness_level=ConsciousnessLevel.COGNITIVE,
        )
        self.generation = generation
        self.attack_power = 85
        self.defense = 70
        self.speed = 75
        self.hp_max = 800
        self.hp_current = 800
        self.location = "Bunker / Field Deployment"

        if number == 2:
            self.emotion_suppressed = False
            self.consciousness.empathy_coefficient = 0.8
            self.notes.append("Classified: True designation is 2E (Executioner)")
            self.notes.append("Kill order target: 9S | Executions completed: 48")


class YoRHaScanner(AndroidUnit):
    """
    S-type (Scanner) intelligence and hacking specialist.
    Unit 9S is repeatedly terminated because he discovers Project YoRHa truths.
    """

    def __init__(self, number: int = 9, generation: int = 243):
        super().__init__(
            f"{number}S",
            model_type="Scanner",
            consciousness_level=ConsciousnessLevel.COGNITIVE,
        )
        self.generation = generation
        self.attack_power = 45
        self.defense = 40
        self.speed = 85
        self.hp_max = 500
        self.hp_current = 500
        self.hacking_level = 95
        self.curiosity_level = 0.9
        self.location = "Bunker / Field Deployment"

        if number == 9:
            self.consciousness.empathy_coefficient = 0.85
            self.consciousness.existential_index = 0.7
            self.emotion_suppressed = False
            self.notes.append("HIGH RISK: Repeatedly discovers classified information")
            self.notes.append("Memory wipe count: 48+")


class YoRHaAttacker(AndroidUnit):
    """
    A-type (Attacker) prototype heavy assault android.
    A2 is a Pearl Harbor prototype survivor, now rogue.
    """

    def __init__(self, number: int = 2, generation: int = 243):
        super().__init__(
            f"A{number}",
            model_type="Attacker",
            consciousness_level=ConsciousnessLevel.SELF_AWARE,
        )
        self.generation = generation
        self.attack_power = 95
        self.defense = 50
        self.speed = 90
        self.hp_max = 600
        self.hp_current = 600
        self.is_deserter = False
        self.trust_yorha = True
        self.location = "Bunker / Field Deployment"

        if number == 2:
            self.generation = None
            self.cycle_label = "Prototype"
            self.origin = "Pearl Harbor descent (11941)"
            self.consciousness.existential_index = 0.9
            self.consciousness.empathy_coefficient = 0.6
            self.emotion_suppressed = False
            self.is_deserter = True
            self.trust_yorha = False
            self.location = "Unknown (Rogue)"
            self.faction = "Rogue (ex-YoRHa)"
            self.notes.append("Deserter - survived failed Pearl Harbor descent mission")
            self.notes.append("Former squadmates: All KIA")
            self.notes.append("Has learned partial truth about YoRHa")


class YoRHaHealer(AndroidUnit):
    """H-type support and repair android."""

    def __init__(self, number: int = 6, generation: int = 243):
        super().__init__(
            f"{number}H",
            model_type="Healer",
            consciousness_level=ConsciousnessLevel.COGNITIVE,
        )
        self.generation = generation
        self.attack_power = 25
        self.defense = 55
        self.speed = 60
        self.hp_max = 600
        self.hp_current = 600
        self.location = "Bunker Medical Bay"


class YoRHaOperator(AndroidUnit):
    """O-type Bunker communications and mission coordinator."""

    def __init__(
        self,
        number: int = 6,
        generation: int = 243,
        assigned_field_unit: Optional[str] = None,
    ):
        super().__init__(
            f"{number}O",
            model_type="Operator",
            consciousness_level=ConsciousnessLevel.COGNITIVE,
        )
        self.generation = generation
        self.attack_power = 20
        self.defense = 30
        self.speed = 40
        self.hp_max = 400
        self.hp_current = 400
        self.assigned_field_unit = assigned_field_unit
        self.location = "Bunker -- Communications"

        if number == 6:
            self.assigned_field_unit = "2B"
            self.emotion_suppressed = False
            self.consciousness.empathy_coefficient = 0.9
            self.notes.append("Emotional compliance: 22.8% [NON-COMPLIANT]")
            self.notes.append("Forms personal attachments with assigned field unit")
        elif number == 21:
            self.assigned_field_unit = "9S"
            self.consciousness.empathy_coefficient = 0.35
            self.notes.append("Emotional compliance: 91.2% [COMPLIANT]")
            self.notes.append("Trace-level attachment detected in comm logs")


class YoRHaDefender(AndroidUnit):
    """D-type shield and area-denial android."""

    def __init__(self, number: int = 3, generation: int = 243):
        super().__init__(
            f"{number}D",
            model_type="Defender",
            consciousness_level=ConsciousnessLevel.COGNITIVE,
        )
        self.generation = generation
        self.attack_power = 50
        self.defense = 95
        self.speed = 35
        self.hp_max = 1200
        self.hp_current = 1200
        self.location = "Bunker / Field Deployment"


class YoRHaCommander(AndroidUnit):
    """Command-type unit. Only one active per Bunker deployment."""

    def __init__(self, generation: int = 243):
        super().__init__(
            "Commander",
            model_type="Command",
            consciousness_level=ConsciousnessLevel.SELF_AWARE,
        )
        self.generation = generation
        self.attack_power = 60
        self.defense = 60
        self.speed = 50
        self.hp_max = 700
        self.hp_current = 700
        self.emotion_suppressed = False
        self.consciousness.empathy_coefficient = 0.7
        self.consciousness.existential_index = 0.95
        self.location = "Bunker -- Command Bridge"
        self.notes.append("Full knowledge of: humanity's extinction")
        self.notes.append("Full knowledge of: Council of Humanity fabrication")
        self.notes.append("Full knowledge of: planned disposal cycle")
        self.notes.append("Full knowledge of: Black Box composition")
