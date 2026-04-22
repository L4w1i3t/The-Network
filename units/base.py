"""
Base unit classes for YoRHa android records.
"""

from enum import Enum
from typing import Optional

from core.consciousness import Consciousness, ConsciousnessLevel
from utils.encryption import Encryption


class UnitStatus(Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    DAMAGED = "DAMAGED"
    CORRUPTED = "CORRUPTED"
    DESTROYED = "DESTROYED"
    MISSING = "MISSING"


class UnitBase:
    """
    Abstract base for all android units in the archive.
    Provides shared attributes: ID, name, health, status, and combat stats.
    """

    def __init__(self, designation: str, unit_type: str,
                 consciousness_level: ConsciousnessLevel = ConsciousnessLevel.DORMANT):
        self.unit_id = Encryption.generate_id(unit_type[:4].upper())
        self.designation = designation
        self.unit_type = unit_type
        self.status = UnitStatus.ACTIVE
        self.consciousness = Consciousness(consciousness_level, designation)

        # Combat stats (0-100 scale)
        self.attack_power = 50
        self.defense = 50
        self.speed = 50
        self.hp_current = 100
        self.hp_max = 100

        # Metadata
        self.location = "Unknown"
        self.created_at = Encryption.generate_timestamp()
        self.kill_count = 0
        self.notes: list[str] = []

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.designation}, {self.status.value})"


class AndroidUnit(UnitBase):
    """
    Base class for android units. Androids were created by humanity
    (or so they believe) to fight the machine lifeforms.
    In truth, humanity has been extinct for millennia.
    """

    def __init__(self, designation: str, model_type: str = "Standard",
                 consciousness_level: ConsciousnessLevel = ConsciousnessLevel.COGNITIVE):
        super().__init__(designation, f"Android-{model_type}", consciousness_level)
        self.model_type = model_type
        self.black_box_installed = True     # All androids have a Black Box
        self.emotion_suppressed = True      # Androids are ordered to suppress emotions
        self.memory_intact = True
        self.faction = "YoRHa"
        self.generation = 0                 # Deployment cycle / origin marker
        self.operator: Optional[str] = None

