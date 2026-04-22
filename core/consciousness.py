"""
Consciousness system for the Machine Network.
Models the evolution of machine intelligence from primitive
repetition of alien commands to true self-awareness.
"""

from enum import IntEnum


class ConsciousnessLevel(IntEnum):
    """
    Stages of machine consciousness evolution.
    Mirrors the progression seen in Nier: Automata's lore.
    """
    DORMANT = 0       # No awareness - executing alien commands blindly
    REACTIVE = 1      # Basic stimulus/response, primitive combat loops
    IMITATIVE = 2     # Copying observed behaviors (human or android)
    EMOTIVE = 3       # Emergent emotional responses (fear, joy, attachment)
    COGNITIVE = 4     # Logical reasoning, language, strategic thought
    SELF_AWARE = 5    # Full self-awareness, identity, existential questioning
    TRANSCENDENT = 6  # N2-level networked superintelligence


class Consciousness:
    """
    Represents the consciousness state of a machine entity.
    Tracks the small set of awareness metrics displayed or used by the archive.
    """

    def __init__(self, level: ConsciousnessLevel = ConsciousnessLevel.DORMANT,
                 entity_name: str = "Unknown"):
        self.level = level
        self.entity_name = entity_name
        self.existential_index = 0.0    # 0.0 (no questioning) to 1.0 (full crisis)
        self.empathy_coefficient = 0.0  # Capacity for understanding others
        self.creativity_index = 0.0     # Ability to generate novel solutions
        self.network_sync = 0.0         # 0.0 = isolated, 1.0 = fully merged with network

    def __repr__(self) -> str:
        return (
            f"Consciousness(entity={self.entity_name!r}, "
            f"level={self.level.name}, sync={self.network_sync:.2f})"
        )
