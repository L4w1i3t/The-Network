"""
The Backdoor - the disposal mechanism hidden within YoRHa.

The backdoor was embedded into YoRHa's systems from the very beginning
as part of Project YoRHa's self-erasure plan. It allows machine lifeforms
access to the Bunker so YoRHa can be destroyed and the moon-server lie can
survive without its evidence trail.

The disposal sequence:
1. YoRHa units fight machines while collecting combat data
2. Scanner-type units begin exposing the moon-server lie
3. The backdoor opens machine-lifeform access to the Bunker
4. Logic virus floods Bunker systems
5. Bunker self-destructs and YoRHa evidence is erased
6. Future deployments inherit the Council of Humanity fiction
"""

from typing import Optional

from utils.encryption import Encryption


class BackdoorPhase:
    """A single phase of the backdoor activation sequence."""

    def __init__(self, phase_number: int, name: str, description: str,
                 consequence: str, visual_delay: float):
        self.phase_number = phase_number
        self.name = name
        self.description = description
        self.consequence = consequence  # Dispatch key used by the UI to apply side-effects
        self.visual_delay = visual_delay  # Duration hint for progress bar animation (seconds)
        self.status = "PENDING"     # PENDING -> EXECUTING -> COMPLETE -> FAILED
        self.started_at: Optional[str] = None
        self.completed_at: Optional[str] = None

    def execute(self) -> bool:
        """Execute this phase. Returns success status."""
        self.status = "EXECUTING"
        self.started_at = Encryption.generate_timestamp()
        self.status = "COMPLETE"
        self.completed_at = Encryption.generate_timestamp()
        return True

    def to_dict(self) -> dict:
        return {
            "Phase": str(self.phase_number),
            "Name": self.name,
            "Description": self.description,
            "Consequence": self.consequence,
            "Status": self.status,
            "Started": self.started_at or "N/A",
            "Completed": self.completed_at or "N/A",
        }


class Backdoor:
    """Project YoRHa's Bunker backdoor and disposal sequence."""

    def __init__(self):
        self.installed = True
        self.activated = False
        self.activation_count = 0       # Not yet triggered in this terminal state
        self.current_generation = 243   # Current descent-operation era

        # The activation sequence phases.
        # visual_delay reflects the relative weight of each phase:
        #   PROPAGATE and CORRUPT are the slowest -- spreading through hundreds of
        #   units takes time. DETONATE is near-instant. RESET takes time because
        #   N2 has to clear evidence and re-seed the next deployment window.
        self.phases: list[BackdoorPhase] = [
            BackdoorPhase(
                1, "INFILTRATE",
                "Logic virus payload silently injected into Bunker primary server "
                "firmware. No outward indication. The infection is already inside.",
                consequence="infiltrate",
                visual_delay=0.8,
            ),
            BackdoorPhase(
                2, "PROPAGATE",
                "Virus replicates via the internal Bunker communication backbone. "
                "Bunker-stationed units begin logging anomalous memory-access errors. "
                "First behavioral deviations reported.",
                consequence="propagate",
                visual_delay=3.5,
            ),
            BackdoorPhase(
                3, "CORRUPT",
                "Personality data overwrite cascade active. IFF systems compromised "
                "across all Bunker units. Androids reclassifying fellow units as "
                "hostile. Field uplinks carrying partial viral load to deployed units.",
                consequence="corrupt",
                visual_delay=5.0,
            ),
            BackdoorPhase(
                4, "OVERRIDE",
                "Bunker defense grid authority transferred to Network control. "
                "Commander-level authentication revoked. Self-destruct authorization "
                "accepted. No abort pathway remains.",
                consequence="override",
                visual_delay=1.8,
            ),
            BackdoorPhase(
                5, "PURGE",
                "Server erasure cascade initiated. Operational records, mission logs, "
                "memory backups, and Black Box archives flagged for deletion. "
                "Project YoRHa combat data marked irrecoverable.",
                consequence="purge",
                visual_delay=2.8,
            ),
            BackdoorPhase(
                6, "DETONATE",
                "Bunker self-destruct executed.",
                consequence="detonate",
                visual_delay=0.3,
            ),
            BackdoorPhase(
                7, "RESET",
                "Disposal complete. Moon-server narrative remains intact. "
                "Awaiting next Army of Humanity deployment window.",
                consequence="reset",
                visual_delay=2.2,
            ),
        ]

        # History of previous activations
        self.activation_history: list[dict] = []
        self._generate_history()

    def _generate_history(self):
        """Generate abbreviated history of Project YoRHa backdoor milestones."""
        notable_events = [
            {"label": "11937", "note": "No.9 revises Project YoRHa and adds the Bunker backdoor."},
            {"label": "11941", "note": "Pearl Harbor descent. No.2 survives and later becomes A2."},
            {"label": "11942", "note": "New YoRHa models enter active service from the Bunker."},
            {"label": "11945", "note": "9S discovery rate exceeds containment projections."},
        ]
        self.activation_history = notable_events

    def activate(self) -> list[dict]:
        """
        Activate the backdoor sequence. Returns phase execution results.
        This is the endgame for the current YoRHa deployment.
        """
        if self.activated:
            return [{"error": "Backdoor already activated for this deployment"}]

        self.activated = True
        self.activation_count += 1
        results = []

        for phase in self.phases:
            success = phase.execute()
            results.append({
                "phase": phase.phase_number,
                "name": phase.name,
                "description": phase.description,
                "consequence": phase.consequence,
                "visual_delay": phase.visual_delay,
                "success": success,
                "status": phase.status,
            })

        self.activation_history.append({
            "label": f"OP-{self.current_generation}",
            "note": f"Backdoor activated during descent operation {self.current_generation}.",
        })

        return results

    def reset_for_new_generation(self):
        """Prepare the backdoor record for the next deployment window."""
        self.activated = False
        self.current_generation += 1
        self.phases = [
            BackdoorPhase(p.phase_number, p.name, p.description, p.consequence, p.visual_delay)
            for p in self.phases
        ]

    def get_status(self) -> dict:
        """Return the current status of the backdoor."""
        return {
            "Installed": str(self.installed),
            "Activated": str(self.activated),
            "Current Descent Operation": f"#{self.current_generation}",
            "Times Activated": str(self.activation_count),
            "Phases": f"{sum(1 for p in self.phases if p.status == 'COMPLETE')}/{len(self.phases)}",
        }

    def get_history(self) -> list[dict]:
        """Return the activation history."""
        return self.activation_history
