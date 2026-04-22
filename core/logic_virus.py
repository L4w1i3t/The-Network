"""
Logic Virus system.

The logic virus is a weapon deployed by the Machine Network against
androids. It corrupts their systems, overwrites personality data,
and can turn androids hostile against their allies. In the final
stages of YoRHa's destruction, a massive logic virus is deployed
to the Bunker through the backdoor.
"""

import time
from typing import Optional

from utils.encryption import Encryption


class VirusStrain:
    """A specific strain of logic virus with unique properties."""

    def __init__(self, name: str, potency: float = 0.5,
                 propagation_rate: float = 0.3, stealth: float = 0.5):
        self.name = name
        self.strain_id = Encryption.generate_id("VIRUS")
        self.potency = min(1.0, max(0.0, potency))
        self.propagation_rate = min(1.0, max(0.0, propagation_rate))
        self.stealth = min(1.0, max(0.0, stealth))
        self.mutations = 0
        self.active = True
        self.created_at = Encryption.generate_timestamp()


class InfectionState:
    """Tracks the infection state of a single target."""

    def __init__(self, target_id: str, target_name: str, strain: VirusStrain):
        self.target_id = target_id
        self.target_name = target_name
        self.strain = strain
        self.infection_level = 0.0      # 0.0 = clean, 1.0 = fully corrupted
        self.stage = "INITIAL"          # INITIAL -> SPREADING -> CRITICAL -> TERMINAL
        self.symptoms: list[str] = []
        self.start_time = time.time()
        self.detected = False


class LogicVirus:
    """
    Manages the Machine Network's logic virus arsenal.
    Can create strains, infect targets, and simulate propagation.
    """

    # Pre-defined strains from the game's lore
    KNOWN_STRAINS = {
        "RED_GIRL_ALPHA": {"potency": 0.8, "propagation": 0.7, "stealth": 0.6},
        "BUNKER_SIEGE": {"potency": 0.95, "propagation": 0.9, "stealth": 0.3},
        "SUBTLE_DOUBT": {"potency": 0.3, "propagation": 0.2, "stealth": 0.95},
        "BERSERKER": {"potency": 0.9, "propagation": 0.5, "stealth": 0.1},
        "IDENTITY_DECAY": {"potency": 0.6, "propagation": 0.4, "stealth": 0.8},
    }

    def __init__(self):
        self.strains: dict[str, VirusStrain] = {}
        self.active_infections: list[InfectionState] = []
        self.infection_log: list[str] = []
        self._init_known_strains()

    def _init_known_strains(self):
        """Initialize the known virus strains."""
        for name, params in self.KNOWN_STRAINS.items():
            self.strains[name] = VirusStrain(
                name=name,
                potency=params["potency"],
                propagation_rate=params["propagation"],
                stealth=params["stealth"],
            )

    def infect(self, target_id: str, target_name: str,
               strain_name: str = "RED_GIRL_ALPHA") -> Optional[InfectionState]:
        """Infect a target with a specific virus strain."""
        strain = self.strains.get(strain_name)
        if not strain or not strain.active:
            return None

        infection = InfectionState(target_id, target_name, strain)
        self.active_infections.append(infection)
        self.infection_log.append(
            f"Target {target_name} ({target_id}) infected with {strain_name}"
        )
        return infection
