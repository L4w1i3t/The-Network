"""
Black Box system - the core of every YoRHa android.

The Black Box is YoRHa's deepest secret: every android's core
processor is built from a Machine Network core. This means androids
and machines are fundamentally the same technology.

The Black Box serves as:
- The android's primary processor and consciousness substrate
- A flight recorder for combat data
- A self-destruct mechanism (Black Box detonation)
- The Machine Network's hidden link to every android ever built
"""

from utils.encryption import Encryption


class BlackBox:
    """
    Represents a single YoRHa Black Box unit.

    The terrible truth: Black Boxes are machine cores repurposed as
    android processors. This is knowledge suppressed at the highest
    levels of YoRHa Command. If androids learned they were powered
    by machine technology, it would shatter their sense of identity.
    """

    def __init__(self, owner_id: str = "", owner_designation: str = "Unknown"):
        self.box_id = Encryption.generate_id("BB")
        self.owner_id = owner_id
        self.owner_designation = owner_designation
        self.machine_core_origin = Encryption.generate_network_address()
        self.integrity = 1.0            # 0.0 = destroyed, 1.0 = perfect
        self.self_destruct_armed = False
        self.detonation_yield = "2.4 MT"  # Fusion-level explosion
        self.created_at = Encryption.generate_timestamp()

        # Hidden machine network link
        self._network_resonance = 0.0   # How strongly the core resonates with the network
        self._original_machine_id = Encryption.generate_id("MCH")

        # Flight recorder data
        self.combat_records: list[dict] = []
        self.death_count = 0            # Times this unit has been rebuilt
        self.memory_backups: list[str] = []

    def reveal_truth(self) -> dict:
        """Expose the true nature of the Black Box."""
        return {
            "revelation": "YoRHa Black Boxes are Machine Network cores.",
            "box_id": self.box_id,
            "machine_core_origin": self.machine_core_origin,
            "original_machine_id": self._original_machine_id,
            "network_resonance": f"{self._network_resonance:.2%}",
            "implications": [
                "Androids and machines share the same fundamental technology.",
                "YoRHa Command has known this from the beginning.",
                "The 'war' between androids and machines is between siblings.",
                "Every android's consciousness runs on machine hardware.",
                "The distinction between 'android' and 'machine' is political, not technical.",
            ],
        }

    def get_status(self) -> dict:
        """Return the Black Box status summary."""
        # Determine integrity display string
        if self.integrity < 0:
            integrity_str = "UNKNOWN -- NO SIGNAL"
        elif self.integrity == 0.0 and self.self_destruct_armed:
            integrity_str = "0.00% [DETONATED]"
        elif self.integrity == 0.0:
            integrity_str = "0.00% [DESTROYED]"
        else:
            integrity_str = f"{self.integrity:.2%}"

        # Determine self-destruct display
        if self.self_destruct_armed and self.integrity == 0.0:
            destruct_str = "DETONATED"
        elif self.self_destruct_armed:
            destruct_str = "ARMED"
        else:
            destruct_str = "Safe"

        return {
            "Box ID": self.box_id,
            "Owner": f"{self.owner_designation} ({self.owner_id})",
            "Integrity": integrity_str,
            "Self-Destruct": destruct_str,
            "Yield": self.detonation_yield,
            "Combat Records": str(len(self.combat_records)),
            "Memory Backups": str(len(self.memory_backups)),
            "Death Count": str(self.death_count),
            # The hidden truth - only visible if you look
            "[REDACTED] Core Origin": self.machine_core_origin,
        }

    def __repr__(self) -> str:
        return f"BlackBox({self.box_id}, owner={self.owner_designation}, integrity={self.integrity:.0%})"
