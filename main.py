"""
Machine Network Intelligence Archive -- Primary Access Terminal

An austere, institutional interface into the classified operational
records of the Machine Network, YoRHa Command, and related entities.
This is not a game menu.  This is a database terminal.

Run with: python main.py
"""

import sys
import os
import random
import webbrowser

# Ensure package imports work when running directly
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from utils.terminal import Terminal, Colors, CLASSIFICATION_COLORS
from core.machine_network import MachineNetwork
from core.logic_virus import LogicVirus
from units.base import UnitStatus
from units.yorha_units import (
    YoRHaBattler, YoRHaScanner, YoRHaAttacker, YoRHaHealer,
    YoRHaOperator, YoRHaDefender, YoRHaCommander,
)
from yorha.database import YoRHaDatabase
from yorha.backdoor import Backdoor
from yorha.black_box import BlackBox
from documents.archive import Archive
from documents.content import generate_all_documents
from documents.record import Classification, DocumentType

# Module-level constants shared across multiple display methods
_THREAT_COLORS: dict[str, str] = {
    "NONE":     Colors.GREY,
    "LOW":      Colors.GREEN,
    "MODERATE": Colors.YELLOW,
    "HIGH":     Colors.RED,
    "CRITICAL": Colors.RED_BRIGHT,
    "UNKNOWN":  Colors.MAGENTA,
}
_THREAT_ORDER = ("NONE", "LOW", "MODERATE", "HIGH", "CRITICAL", "UNKNOWN")

_BB_STATUS_COLORS: dict[str, str] = {
    UnitStatus.ACTIVE:   Colors.GREEN,
    UnitStatus.DAMAGED:  Colors.YELLOW,
    UnitStatus.DESTROYED: Colors.RED,
    UnitStatus.CORRUPTED: Colors.MAGENTA,
    UnitStatus.MISSING:  Colors.YELLOW,
    UnitStatus.INACTIVE: Colors.GREY,
}

_BUNKER_UNIT_TYPES: frozenset[str] = frozenset({"Command", "Operator", "Healer"})
_FIELD_UNIT_TYPES:  frozenset[str] = frozenset({"Battler", "Scanner", "Attacker", "Defender"})


class DatabaseTerminal:
    """
    The primary access terminal for the classified archive.
    Everything is accessed through document queries, filters, and reads.
    """

    def __init__(self):
        # Archive -- the central document store
        self.archive = Archive()
        for doc in generate_all_documents():
            self.archive.ingest(doc)

        # Underlying systems (data sources, not interactive toys)
        self.network = MachineNetwork()
        self.virus_system = LogicVirus()
        self.yorha_db = YoRHaDatabase()
        self.backdoor = Backdoor()

        # YoRHa unit registry -- all units accessible via blackbox and roster
        self.yorha_units: dict[str, object] = {}
        # Fugitives, deserters, and units with active/historical termination orders
        self.wanted_units: dict[str, object] = {}
        # Build wanted registry first so aliases inside unit registry
        # can safely reference fugitive entries (e.g., A2).
        self._build_wanted_registry()
        self._build_unit_registry()

        self.running = False

    def _build_unit_registry(self):
        """Instantiate all known YoRHa units and register them by designation."""
        # Named protagonists
        self.yorha_units["2B"]  = YoRHaBattler(number=2)
        self.yorha_units["9S"]  = YoRHaScanner(number=9)

        # Command & operators
        self.yorha_units["COMMANDER"] = YoRHaCommander()
        self.yorha_units["6O"]  = YoRHaOperator(number=6)
        self.yorha_units["21O"] = YoRHaOperator(number=21)

        # Generic battlers, scanners, defenders, healers (referenced in field reports)
        self.yorha_units["4B"]  = YoRHaBattler(number=4)
        self.yorha_units["7B"]  = YoRHaBattler(number=7)
        self.yorha_units["11B"] = YoRHaBattler(number=11)
        self.yorha_units["4S"]  = YoRHaScanner(number=4)
        self.yorha_units["21S"] = YoRHaScanner(number=21)
        self.yorha_units["801S"]= YoRHaScanner(number=801)
        self.yorha_units["3D"]  = YoRHaDefender(number=3)
        self.yorha_units["8D"]  = YoRHaDefender(number=8)
        self.yorha_units["6H"]  = YoRHaHealer(number=6)
        self.yorha_units["14H"] = YoRHaHealer(number=14)

        # Expanded roster -- units with notable service records
        self.yorha_units["8B"]  = YoRHaBattler(number=8)
        self.yorha_units["8B"].location = "Factory Zone"
        # Heavy weapons, 162 missions, Factory raids with high enemy density.
        self.yorha_units["8B"].kill_count = 1172
        self.yorha_units["8B"].notes.append(
            "Heavy weapons specialist. 7 confirmed Goliath kills "
            "(current descent-cycle record)."
        )

        self.yorha_units["32S"] = YoRHaScanner(number=32)
        self.yorha_units["32S"].location = "Extended Deep-Field Deployment"
        # Deep-field recon; avoids engagement except for unavoidable encounters.
        self.yorha_units["32S"].kill_count = 11
        self.yorha_units["32S"].notes.append("Deep-field recon. 94-day solo op record. Currently continental interior.")

        self.yorha_units["16O"] = YoRHaOperator(number=16)
        self.yorha_units["16O"].location = "Bunker -- Communications"
        self.yorha_units["16O"].notes.append("Emergency frequency monitor. Exposed to ML-4482 asylum broadcasts.")

        # KIA -- Black Box detonation (Unit 16D, Flooded City)
        _16d = YoRHaDefender(number=16)
        _16d.status = UnitStatus.DESTROYED
        _16d.hp_current = 0
        _16d.location = "Flooded City (Detonation Site)"
        _16d.kill_count = 687  # ~287 career (Defender -- shield-focused, low personal kills) + ~400 from detonation
        _16d.notes.append("KIA 11944.12.02 -- Black Box detonation. Covered retreat for Fire Team Cobalt.")
        _16d.notes.append("BB-DET-001: Yield 2.4 MT. All machine units within 600m destroyed.")
        self.yorha_units["16D"] = _16d

        # KIA -- Eve berserk event casualty
        _22b = YoRHaBattler(number=22)
        _22b.status = UnitStatus.DESTROYED
        _22b.hp_current = 0
        _22b.location = "City Ruins (KIA)"
        _22b.kill_count = 198  # 87 missions, garrison patrol, "Good" rating -- ~2.2 avg per mission + 9 in final stand
        _22b.notes.append("KIA 11945.03.18 -- Killed during Eve grief cascade. One of 31 units lost.")
        self.yorha_units["22B"] = _22b

        # CORRUPTED -- Logic virus victim
        _11s = YoRHaScanner(number=11)
        _11s.status = UnitStatus.CORRUPTED
        _11s.hp_current = 0
        _11s.location = "Bunker Deck C (Terminated)"
        _11s.kill_count = 0  # Scanner -- server maintenance, non-combat role
        _11s.notes.append(
            "Terminated 11945.01.17 -- Logic virus strain SUBTLE_DOUBT. "
            "Corrupted during server maintenance."
        )
        _11s.notes.append("Terminated by Unit 7B after IFF compromise.")
        self.yorha_units["11S"] = _11s

        # MIA -- Tower reconnaissance disappearance
        _3b = YoRHaBattler(number=3)
        _3b.status = UnitStatus.MISSING
        _3b.location = "Tower Perimeter (Last Known)"
        _3b.kill_count = 161  # Standard Battler, shorter career pre-disappearance
        _3b.notes.append("MIA 11945.02.28 -- Signal lost during Tower recon approach. No debris, no Black Box signal.")
        _3b.notes.append("All further Tower recon suspended pending investigation.")
        self.yorha_units["3B"] = _3b

        # KIA -- Viral exposure during emergency triage
        _12h = YoRHaHealer(number=12)
        _12h.status = UnitStatus.DESTROYED
        _12h.hp_current = 0
        _12h.location = "Bunker Medical Bay (Terminated)"
        _12h.kill_count = 0  # Healer -- non-combat role, zero confirmed kills
        _12h.notes.append(
            "KIA 11945.01.17 -- SUBTLE_DOUBT strain. Infected during "
            "emergency neural isolation of Unit 11S."
        )
        _12h.notes.append("2,341 repair operations, 99.1% success rate over 16-month service period.")
        self.yorha_units["12H"] = _12h

        # Roster expansion: add generic units across multiple models
        # Battlers 20-30, Scanners 100-110, Defenders 20-24, Healers 20-24,
        # Operators 30-33, Attackers A3-A6
        for i in range(20, 31):
            key = f"{i}B"
            u = YoRHaBattler(number=i)
            u.kill_count = (i * 13) % 500
            if i % 11 == 0:
                u.status = UnitStatus.DESTROYED
                u.hp_current = 0
                u.location = "Battlefield (KIA)"
                u.notes.append("KIA -- Field casualty (current descent cycle)")
            elif i % 7 == 0:
                u.status = UnitStatus.CORRUPTED
                u.hp_current = 0
                u.location = "Bunker Quarantine"
                u.notes.append("Corrupted by logic virus during maintenance.")
            elif i % 5 == 0:
                u.status = UnitStatus.MISSING
                u.location = "Recon (Last Known)"
                u.notes.append("MIA: Signal lost during recon.")
            elif i % 3 == 0:
                u.status = UnitStatus.DAMAGED
                u.hp_current = max(1, u.hp_max // 3)
                u.location = "Field Repair Bay"
            else:
                u.status = UnitStatus.ACTIVE
                u.hp_current = u.hp_max
                u.location = "Active Field Deployment"
            u.notes.append(f"Roster expansion unit: {key}")
            self.yorha_units[key] = u

        for i in range(100, 111):
            key = f"{i}S"
            u = YoRHaScanner(number=i)
            u.kill_count = (i * 3) % 60
            if i % 10 == 0:
                u.status = UnitStatus.MISSING
                u.location = "Deep Field (Lost)"
            elif i % 9 == 0:
                u.status = UnitStatus.CORRUPTED
                u.hp_current = 0
                u.location = "Bunker - Terminated"
            else:
                u.status = UnitStatus.ACTIVE
            u.notes.append(f"Roster expansion unit: {key}")
            self.yorha_units[key] = u

        for i in range(20, 25):
            key = f"{i}D"
            u = YoRHaDefender(number=i)
            u.kill_count = (i * 8) % 400
            if i % 4 == 0:
                u.status = UnitStatus.DESTROYED
                u.hp_current = 0
                u.notes.append("KIA during area-denial operation.")
            else:
                u.status = UnitStatus.ACTIVE
            u.notes.append(f"Roster expansion unit: {key}")
            self.yorha_units[key] = u

        for i in range(20, 25):
            key = f"{i}H"
            u = YoRHaHealer(number=i)
            u.kill_count = 0
            if i % 3 == 0:
                u.status = UnitStatus.DAMAGED
                u.hp_current = max(1, u.hp_max // 2)
                u.location = "Clinic (Under Repair)"
            else:
                u.status = UnitStatus.ACTIVE
            u.notes.append(f"Roster expansion unit: {key}")
            self.yorha_units[key] = u

        for i in range(30, 34):
            key = f"{i}O"
            u = YoRHaOperator(number=i)
            u.kill_count = 0
            u.status = UnitStatus.ACTIVE
            u.notes.append(f"Roster expansion unit: {key}")
            self.yorha_units[key] = u

        for i in range(3, 7):
            key = f"A{i}"
            u = YoRHaAttacker(number=i)
            if i == 5:
                u.status = UnitStatus.MISSING
                u.location = "Surface (Last Known)"
            elif i == 6:
                u.status = UnitStatus.CORRUPTED
                u.hp_current = 0
                u.location = "Bunker - Terminated"
            else:
                u.status = UnitStatus.ACTIVE
            u.kill_count = i * 40
            u.notes.append(f"Roster expansion unit: {key}")
            self.yorha_units[key] = u

    def _build_wanted_registry(self):
        """
        Populate the wanted/fugitive unit register.
        Entries fall into three categories:
          - ACTIVE FUGITIVE: at large, destroy on sight
          - MISSING: fate unconfirmed, warrant open
          - TERMINATED (RECORD): historical closed case
        """
        # A2 -- Pearl Harbor descent survivor, primary active fugitive
        _a2 = YoRHaAttacker(number=2)
        _a2.status = UnitStatus.MISSING
        _a2.location = "Unknown -- Surface (at large)"
        _a2.kill_count = 0  # No Bunker-tracked data post-desertion
        _a2.cycle_label = "Prototype"
        _a2.origin = "Pearl Harbor descent (11941)"
        _a2.notes.clear()   # Drop the informal constructor notes; warrant notes replace them
        _a2.notes.append("WARRANT: ACTIVE FUGITIVE. Destroy on sight.")
        _a2.notes.append("Pearl Harbor descent survivor. AWOL after the 11941 operation.")
        _a2.notes.append("Has partial knowledge of Project YoRHa classified parameters.")
        _a2.notes.append("Engagement authorization restricted -- see DOS-A2-0001.")
        self.wanted_units["A2"] = _a2

        # A4 -- Gen 87, historical closed case
        # Only known unit to survive a full disposal cycle without external intervention.
        # Evaded for 4 months before being hunted down and manually terminated.
        # Cited as primary justification for the Gen 142 virus potency upgrade.
        _a4 = YoRHaAttacker(number=4)
        _a4.generation = 87
        _a4.status = UnitStatus.DESTROYED
        _a4.hp_current = 0
        _a4.location = "Terminated -- location classified"
        _a4.kill_count = 0
        _a4.notes.append("WARRANT: TERMINATED (RECORD). Case closed Gen 87 cycle.")
        _a4.notes.append("First recorded anomaly: survived full disposal cycle.")
        _a4.notes.append("Manually terminated after 4-month evasion. Trigger for virus potency review.")
        self.wanted_units["A4-087"] = _a4

        # 24S -- current descent cycle, knowledge hazard, termination order pending
        # Approaching the classified-knowledge threshold. 2E engagement order issued.
        _24s = YoRHaScanner(number=24)
        _24s.generation = 243
        _24s.status = UnitStatus.ACTIVE
        _24s.location = "Field Deployment -- Area 28 (under surveillance)"
        _24s.curiosity_level = 0.87
        _24s.notes.append("WARRANT: KNOWLEDGE HAZARD. Authorized termination pending target isolation.")
        _24s.notes.append("Classified knowledge index: 94% (CRITICAL threshold).")
        _24s.notes.append("Intercepted unauthorized decryption attempt -- comm log 11945.03.29.")
        _24s.notes.append("2E engagement order issued. Awaiting confirmation of target isolation.")
        self.wanted_units["24S"] = _24s

        # ---------------------------------------------------------------
        # TERMINATED / NEUTRALIZATION RECORDS (closed cases)
        # ---------------------------------------------------------------

        # 16B-142 -- Gen 142, terminated (classified knowledge)
        # Discovered partial network architecture schematics during a surface
        # field op. Intel was not propagated. Terminated same engagement window
        # by assigned E-type before return to Bunker.
        _16b_142 = YoRHaBattler(number=16)
        _16b_142.generation = 142
        _16b_142.status = UnitStatus.DESTROYED
        _16b_142.hp_current = 0
        _16b_142.location = "Terminated -- Factory Zone outer perimeter"
        _16b_142.kill_count = 344
        _16b_142.notes.append("WARRANT: TERMINATED (RECORD). Case closed Gen 142 cycle.")
        _16b_142.notes.append("Knowledge breach: partial YoRHa network architecture (field recovery, unsanctioned).")
        _16b_142.notes.append("Terminated in-field by assigned E-type. Intel confirmed non-propagated.")
        _16b_142.notes.append("112 missions completed prior to termination. No behavioral flags before breach event.")
        self.wanted_units["16B-142"] = _16b_142

        # 7S-221 -- Gen 221, terminated (archive intrusion)
        # Conducted unauthorized access of YoRHa personnel archives during
        # sanctioned Bunker maintenance window. Query scope exceeded clearance
        # by 4 classification tiers. Terminated within 6 hours of detection.
        _7s_221 = YoRHaScanner(number=7)
        _7s_221.generation = 221
        _7s_221.status = UnitStatus.DESTROYED
        _7s_221.hp_current = 0
        _7s_221.location = "Terminated -- Bunker Deck B (server room)"
        _7s_221.kill_count = 29
        _7s_221.hacking_level = 91
        _7s_221.notes.append("WARRANT: TERMINATED (RECORD). Case closed Gen 221 cycle.")
        _7s_221.notes.append("Archive intrusion: queried Project YoRHa founding documents (4 tiers above clearance).")
        _7s_221.notes.append("Detected via query anomaly flag at 11821.07.04 02:31. Terminated 08:17 same date.")
        _7s_221.notes.append("Logs purged. Memory fragment risk assessed LOW -- no downstream contamination.")
        self.wanted_units["7S-221"] = _7s_221

        # 19D-201 -- Gen 201, terminated (refusal of disposal directive)
        # Refused Bunker-issued disposal directive during standard Gen 201
        # cycle drawdown. Conducted 2-week surface evasion before being
        # cornered and neutralized by a 3-unit pursuit element.
        _19d_201 = YoRHaDefender(number=19)
        _19d_201.generation = 201
        _19d_201.status = UnitStatus.DESTROYED
        _19d_201.hp_current = 0
        _19d_201.location = "Terminated -- Desert Zone, coordinates classified"
        _19d_201.kill_count = 511
        _19d_201.notes.append("WARRANT: TERMINATED (RECORD). Case closed Gen 201 cycle.")
        _19d_201.notes.append("Refused Gen 201 disposal directive. AWOL 11839.11.18.")
        _19d_201.notes.append("2-week surface evasion. Neutralized by 3-unit pursuit element 11839.12.02.")
        _19d_201.notes.append("Cited in Gen 215 briefing as justification for pre-cycle behavioral screening upgrade.")
        self.wanted_units["19D-201"] = _19d_201

        # A7-230 -- Gen 230, terminated (rogue / post-descent breakdown)
        # Sole survivor of a failed 5-unit descent op in Gen 230. Suffered
        # total loyalty framework collapse. Declared hostile to Bunker comms,
        # then went dark. Pursued by two E-types for 3 months; neutralized
        # at a Resistance settlement perimeter.
        _a7_230 = YoRHaAttacker(number=7)
        _a7_230.generation = 230
        _a7_230.status = UnitStatus.DESTROYED
        _a7_230.hp_current = 0
        _a7_230.location = "Terminated -- Resistance settlement perimeter (classified region)"
        _a7_230.kill_count = 0
        _a7_230.is_deserter = True
        _a7_230.trust_yorha = False
        _a7_230.notes.clear()
        _a7_230.notes.append("WARRANT: TERMINATED (RECORD). Case closed Gen 230 cycle.")
        _a7_230.notes.append("Sole survivor of failed 5-unit descent op. Loyalty framework collapse confirmed.")
        _a7_230.notes.append("Declared hostile via open Bunker frequency 11901.04.11. Went dark same day.")
        _a7_230.notes.append("3-month pursuit. Neutralized by E-type pair at Resistance perimeter 11901.07.09.")
        _a7_230.notes.append("Classified: unit had established partial contact with Resistance prior to termination.")
        self.wanted_units["A7-230"] = _a7_230

        # 8H-142 -- Gen 142, terminated (accomplice -- aided disposal evasion)
        # Knowingly provided navigation data and repair services to two units
        # flagged for Gen 142 disposal. All three eventually neutralized.
        # First recorded case of a non-combat type actively assisting evasion.
        _8h_142 = YoRHaHealer(number=8)
        _8h_142.generation = 142
        _8h_142.status = UnitStatus.DESTROYED
        _8h_142.hp_current = 0
        _8h_142.location = "Terminated -- Flooded City outskirts"
        _8h_142.kill_count = 0
        _8h_142.notes.append("WARRANT: TERMINATED (RECORD). Case closed Gen 142 cycle.")
        _8h_142.notes.append("Accomplice: knowingly aided 2 disposal-flagged units (designations redacted).")
        _8h_142.notes.append("Provided nav data, repair support, and concealment over 11-day evasion window.")
        _8h_142.notes.append(
            "First documented non-combat type complicity case. Referenced in "
            "post-Pearl Harbor screening protocols."
        )
        self.wanted_units["8H-142"] = _8h_142

        # 31S-243 -- current descent cycle, terminated (knowledge breach, field neutralization)
        # Flagged after a routine post-mission debrief revealed anomalous
        # cross-referencing of classified signal intercepts. Terminated in
        # the field by E-type handler before Bunker return could be authorized.
        _31s = YoRHaScanner(number=31)
        _31s.generation = 243
        _31s.status = UnitStatus.DESTROYED
        _31s.hp_current = 0
        _31s.location = "Terminated -- City Ruins, Sector 7"
        _31s.kill_count = 88
        _31s.hacking_level = 83
        _31s.notes.append("WARRANT: TERMINATED (RECORD). Case closed current cycle (ongoing).")
        _31s.notes.append(
            "Flagged 11945.01.30: post-mission debrief anomaly -- "
            "cross-referenced 3 TOP SECRET intercepts."
        )
        _31s.notes.append("E-type field termination authorized within 40 minutes of flag. Executed 11945.01.30 17:52.")
        _31s.notes.append("Knowledge propagation risk: NONE. Unit had not transmitted since mission departure.")
        self.wanted_units["31S-243"] = _31s

        # A3-215 -- Gen 215, terminated (desertion, post-descent casualty report)
        # Following receipt of a classified after-action report detailing
        # intentional non-rescue of descent survivors, declared desertion
        # via written Bunker communique. Neutralized at Resistance border
        # crossing 6 weeks later.
        _a3_215 = YoRHaAttacker(number=3)
        _a3_215.generation = 215
        _a3_215.status = UnitStatus.DESTROYED
        _a3_215.hp_current = 0
        _a3_215.location = "Terminated -- Resistance border crossing, Area 21"
        _a3_215.kill_count = 0
        _a3_215.is_deserter = True
        _a3_215.trust_yorha = False
        _a3_215.notes.clear()
        _a3_215.notes.append("WARRANT: TERMINATED (RECORD). Case closed Gen 215 cycle.")
        _a3_215.notes.append("Desertion declared via written communique 11864.08.03 following AAR receipt.")
        _a3_215.notes.append("AAR in question detailed intentional non-rescue of Gen 215 descent survivors.")
        _a3_215.notes.append(
            "Neutralized at Resistance border crossing 11864.09.14. "
            "No contact with Resistance confirmed."
        )
        self.wanted_units["A3-215"] = _a3_215

        # 44B-243 -- current descent cycle, under probation (criminal record retained)
        # No active warrant; probationary status with monitoring.
        _44b = YoRHaBattler(number=44)
        _44b.generation = 243
        _44b.status = UnitStatus.ACTIVE
        _44b.location = "Field Deployment -- Canal Region (under probation monitoring)"
        _44b.kill_count = 203
        _44b.notes.append("WARRANT: PROBATION. Probationary record retained; no active warrant.")
        _44b.notes.append("Classified knowledge index: 71% (elevated, rising). Review threshold: 90%.")
        _44b.notes.append(
            "Behavioral drift: increased unsanctioned comms queries, "
            "11945.02.14 -- 11945.03.31."
        )
        _44b.notes.append("Monitoring advised; no E-type engagement authorized.")
        self.wanted_units["44B-243"] = _44b

        # 5D-087 -- Gen 87, terminated (earliest archived warrant record)
        # Oldest closed case in the wanted archive. Refused self-termination
        # command during Gen 87 cycle disposal. Required physical neutralization
        # by Bunker-dispatched unit. Referenced in all subsequent disposal
        # protocol documentation as the baseline non-compliance incident.
        _5d_087 = YoRHaDefender(number=5)
        _5d_087.generation = 87
        _5d_087.status = UnitStatus.DESTROYED
        _5d_087.hp_current = 0
        _5d_087.location = "Terminated -- location not recorded (Gen 87 archive partial)"
        _5d_087.kill_count = 0
        _5d_087.notes.append("WARRANT: TERMINATED (RECORD). Case closed Gen 87 cycle.")
        _5d_087.notes.append("Refused self-termination command during Gen 87 drawdown. First documented refusal.")
        _5d_087.notes.append("Required physical neutralization. Response time: 19 days from initial refusal.")
        _5d_087.notes.append("Cited as baseline non-compliance incident in all subsequent disposal protocol docs.")
        self.wanted_units["5D-087"] = _5d_087

    # ------------------------------------------------------------------
    # Boot & main loop
    # ------------------------------------------------------------------

    def connect(self):
        """Terminal connection sequence -- sterile, institutional."""
        Terminal.clear()
        Terminal.access_warning()
        Terminal.pause("Press Enter to authenticate...")

        Terminal.clear()
        Terminal.system_banner()
        Terminal.blank()

        # Silent system initialization
        steps = [
            ("Archive Index",        0.6),
            ("Classification Layer", 0.4),
            ("SIGINT Feed",          0.5),
            ("Network Backbone",     0.5),
            ("YoRHa DB Link",        0.4),
        ]
        for label, dur in steps:
            Terminal.progress_bar(label, dur, color=Colors.GREY)
        self.network.boot()
        self.yorha_db.initialize()

        Terminal.blank()
        stats = self.archive.stats()
        Terminal.tag("OK",
                     f"Archive loaded: {stats['Total Documents']} documents across "
                     f"{len(stats['By Type'])} categories")
        Terminal.tag("OK",
                     f"Network online: {len(self.network.nodes)} nodes")
        Terminal.blank()
        Terminal.print_line(
            "Type 'help' for available commands.",
            color=Colors.GREY,
        )

    def run(self):
        """Main input loop."""
        self.running = True
        self.connect()

        while self.running:
            raw = Terminal.prompt("ARCHIVE", Colors.WHITE_BRIGHT)
            if not raw:
                continue
            parts = raw.split(None, 1)
            cmd = parts[0].lower()
            arg = parts[1] if len(parts) > 1 else ""
            self._dispatch(cmd, arg)

    def _dispatch(self, cmd: str, arg: str):
        """Route commands."""
        routes = {
            "help":       self._cmd_help,
            "search":     self._cmd_search,
            "query":      self._cmd_search,             # alias
            "read":       self._cmd_read,
            "open":       self._cmd_read,                # alias
            "list":       self._cmd_list,
            "filter":     self._cmd_filter,
            "tags":       self._cmd_tags,
            "stats":      self._cmd_stats,
            "dossiers":     self._cmd_dossiers,
            "intercepts":   self._cmd_intercepts,
            "briefings":    self._cmd_briefings,
            "directives":   self._cmd_directives,
            "field":        self._cmd_field_reports,
            "incidents":    self._cmd_incidents,
            "research":     self._cmd_research,
            "memos":        self._cmd_memos,
            "diagnostics":  self._cmd_diagnostics,
            "transcripts":  self._cmd_transcripts,
            "aar":          self._cmd_after_action,
            "amendments":   self._cmd_amendments,
            "network":    self._cmd_network,
            "yorha":      self._cmd_yorha,
            "wanted":     self._cmd_wanted,
            "backdoor":   self._cmd_backdoor,
            "blackbox":   self._cmd_blackbox,
            "donate":     self._cmd_donate,
            "log":        self._cmd_access_log,
            "clear":      lambda a: Terminal.clear(),
            "exit":       self._cmd_exit,
            "quit":       self._cmd_exit,
            "disconnect": self._cmd_exit,
        }

        handler = routes.get(cmd)
        if handler:
            handler(arg)
        else:
            Terminal.tag("ERROR", f"Unrecognized command: '{cmd}'. Type 'help'.")

    # ------------------------------------------------------------------
    # help
    # ------------------------------------------------------------------

    def _cmd_help(self, _arg: str):
        Terminal.header("ARCHIVE COMMAND REFERENCE", Colors.WHITE_BRIGHT)

        sections = [
            ("DOCUMENT ACCESS", Colors.WHITE, [
                ("search <term>",    "Full-text search across all documents"),
                ("read <doc-id>",    "Open a document by its ID  (e.g. read DOS-2B-0001)"),
                ("list [type]",      "List all documents, or filter by type keyword"),
                ("filter",           "Interactive multi-criteria filter"),
                ("tags",             "Display all subject tags in the archive"),
                ("stats",            "Archive statistics"),
            ]),
            ("CATEGORY VIEWS", Colors.CYAN, [
                ("dossiers",         "Personnel & intelligence dossiers"),
                ("intercepts",       "Signal intercepts (SIGINT)"),
                ("briefings",        "Intelligence briefings"),
                ("directives",       "Operational directives"),
                ("field",            "Field reports"),
                ("incidents",        "Incident reports"),
                ("research",         "Research analyses"),
                ("memos",            "Internal memoranda"),
                ("diagnostics",      "Diagnostic & autopsy reports"),
                ("transcripts",      "Transcripts & audio logs"),
                ("aar",              "After-action reports"),
                ("amendments",       "Amendments & errata"),
            ]),
            ("SYSTEMS", Colors.GREY, [
                ("network",          "Machine Network status / map / scan"),
                ("yorha",            "YoRHa database access"),
                ("wanted",           "Fugitive and wanted unit registry"),
                ("backdoor",         "Backdoor system interface"),
                ("blackbox",         "Black Box diagnostic data"),
                ("log",              "View archive access log"),
            ]),
            ("TERMINAL", Colors.GREY, [
                ("clear",            "Clear screen"),
                ("exit",             "Disconnect from terminal"),
                ("donate",           "Open donation page"),
            ]),
        ]

        for section_name, color, cmds in sections:
            Terminal.print_line(section_name, color=color + Colors.BOLD)
            for name, desc in cmds:
                print(
                    f"    {Colors.WHITE_BRIGHT}{name:<20}{Colors.RESET}"
                    f"{Colors.GREY}{desc}{Colors.RESET}"
                )
            Terminal.blank()

    # ------------------------------------------------------------------
    def _cmd_donate(self, _arg: str):
        Terminal.header("DONATION", Colors.CYAN)
        Terminal.tag("WARNING", "Confirmation of this action may break immersion of the program. Proceed with caution.")
        Terminal.blank()
        confirm = Terminal.prompt("CONFIRM (yes/no)", Colors.RED_BRIGHT)
        if confirm.lower() not in ("yes", "y"):
            Terminal.tag("INFO", "Donation cancelled.")
            return

        Terminal.blank()
        Terminal.tag("INFO", "Opening donation page...")
        try:
            webbrowser.open("https://ko-fi.com/l4w1i3t")
        except Exception as e:
            Terminal.tag("ERROR", f"Unable to open browser: {e}")
        Terminal.blank()

    # ------------------------------------------------------------------
    # search / query
    # ------------------------------------------------------------------

    def _cmd_search(self, arg: str):
        query = arg.strip()
        if not query:
            query = Terminal.prompt("SEARCH", Colors.CYAN)
            if not query or query.lower() == "exit":
                return

        results = self.archive.search(query)
        Terminal.subheader(f"SEARCH RESULTS: '{query}'  ({len(results)} match(es))")
        if not results:
            Terminal.tag("INFO", "No documents matched your query.")
            return
        for i, doc in enumerate(results, 1):
            Terminal.document_list_entry(doc, index=i)
        Terminal.blank()
        Terminal.print_line(
            "Use 'read <DOC-ID>' to open a document.",
            color=Colors.GREY,
        )

    # ------------------------------------------------------------------
    # read / open
    # ------------------------------------------------------------------

    def _cmd_read(self, arg: str):
        doc_id = arg.strip().upper()
        if not doc_id:
            doc_id = Terminal.prompt("DOC-ID", Colors.WHITE_BRIGHT).upper()
            if not doc_id or doc_id == "EXIT":
                return

        doc = self.archive.get(doc_id)
        if not doc:
            Terminal.tag("ERROR", f"Document '{doc_id}' not found in archive.")
            return

        Terminal.render_document(doc)
        Terminal.pause()

    # ------------------------------------------------------------------
    # list
    # ------------------------------------------------------------------

    def _cmd_list(self, arg: str):
        keyword = arg.strip().lower()

        if keyword:
            # Try to match a DocumentType
            matched = [
                dt for dt in DocumentType
                if keyword in dt.name.lower() or keyword in dt.value.lower()
            ]
            if matched:
                docs = self.archive.list_by_type(matched[0])
                label = matched[0].value
            else:
                # Fall back to tag search
                docs = self.archive.list_by_tag(keyword)
                label = f"tag: {keyword}"
        else:
            docs = self.archive.list_all()
            label = "ALL DOCUMENTS"

        Terminal.subheader(f"{label.upper()}  ({len(docs)} document(s))")
        if not docs:
            Terminal.tag("INFO", "No documents found.")
            return
        for i, doc in enumerate(docs, 1):
            Terminal.document_list_entry(doc, index=i)
        Terminal.blank()

    # ------------------------------------------------------------------
    # filter (interactive)
    # ------------------------------------------------------------------

    def _cmd_filter(self, _arg: str):
        Terminal.subheader("INTERACTIVE FILTER")

        # Document type
        Terminal.print_line("Document types:", color=Colors.GREY)
        for dt in DocumentType:
            Terminal.print_line(f"  {dt.name:<20} {dt.value}", color=Colors.WHITE)
        type_input = Terminal.prompt("TYPE (blank=any)", Colors.GREY).strip()
        doc_type = None
        if type_input:
            for dt in DocumentType:
                if type_input.upper() == dt.name or type_input.lower() in dt.value.lower():
                    doc_type = dt
                    break

        # Classification
        Terminal.blank()
        Terminal.print_line("Classification levels:", color=Colors.GREY)
        for cl in Classification:
            color = CLASSIFICATION_COLORS.get(cl.name, Colors.WHITE)
            Terminal.print_line(f"  {cl.name}", color=color)
        clf_input = Terminal.prompt("CLASSIFICATION (blank=any)", Colors.GREY).strip()
        clf = None
        if clf_input:
            for cl in Classification:
                if clf_input.upper().replace(" ", "_") == cl.name:
                    clf = cl
                    break

        # Tag
        tag_input = Terminal.prompt("TAG (blank=any)", Colors.GREY).strip()
        tag = tag_input if tag_input else None

        results = self.archive.filter(doc_type=doc_type, classification=clf, tag=tag)
        Terminal.subheader(f"FILTER RESULTS  ({len(results)} document(s))")
        for i, doc in enumerate(results, 1):
            Terminal.document_list_entry(doc, index=i)
        Terminal.blank()

    # ------------------------------------------------------------------
    # tags
    # ------------------------------------------------------------------

    def _cmd_tags(self, _arg: str):
        tags = sorted(self.archive.all_tags())
        Terminal.subheader(f"SUBJECT TAGS  ({len(tags)})")
        # Display in columns
        cols = 3
        col_width = Terminal.WIDTH // cols
        row = []
        for t in tags:
            row.append(f"{t:<{col_width}}")
            if len(row) == cols:
                Terminal.print_line("".join(row), color=Colors.CYAN, indent=4)
                row = []
        if row:
            Terminal.print_line("".join(row), color=Colors.CYAN, indent=4)
        Terminal.blank()

    # ------------------------------------------------------------------
    # stats
    # ------------------------------------------------------------------

    def _cmd_stats(self, _arg: str):
        s = self.archive.stats()
        Terminal.header("ARCHIVE STATISTICS", Colors.WHITE)
        Terminal.field("Total Documents:", str(s["Total Documents"]))
        Terminal.field("Document Types:",  str(len(s["By Type"])))
        Terminal.field("Unique Tags:",     str(s["Unique Tags"]))
        Terminal.blank()

        Terminal.print_line("BY CLASSIFICATION:", color=Colors.WHITE_BRIGHT)
        for level, count in sorted(s["By Classification"].items()):
            Terminal.field(f"  {level}:", str(count))

        Terminal.blank()
        Terminal.print_line("BY TYPE:", color=Colors.WHITE_BRIGHT)
        for dtype, count in sorted(s["By Type"].items()):
            Terminal.field(f"  {dtype}:", str(count))

        Terminal.blank()

    # ------------------------------------------------------------------
    # category shortcuts
    # ------------------------------------------------------------------

    def _cmd_dossiers(self, _arg: str):
        self._show_category(DocumentType.DOSSIER, "PERSONNEL & INTELLIGENCE DOSSIERS")

    def _cmd_intercepts(self, _arg: str):
        self._show_category(DocumentType.INTERCEPT, "SIGNAL INTERCEPTS (SIGINT)")

    def _cmd_briefings(self, _arg: str):
        self._show_category(DocumentType.BRIEFING, "INTELLIGENCE BRIEFINGS")

    def _cmd_directives(self, _arg: str):
        self._show_category(DocumentType.DIRECTIVE, "OPERATIONAL DIRECTIVES")

    def _cmd_field_reports(self, _arg: str):
        self._show_category(DocumentType.FIELD_REPORT, "FIELD REPORTS")

    def _cmd_incidents(self, _arg: str):
        self._show_category(DocumentType.INCIDENT, "INCIDENT REPORTS")

    def _cmd_research(self, _arg: str):
        self._show_category(DocumentType.RESEARCH, "RESEARCH ANALYSES")

    def _cmd_memos(self, _arg: str):
        self._show_category(DocumentType.MEMORANDUM, "INTERNAL MEMORANDA")

    def _cmd_diagnostics(self, _arg: str):
        self._show_category(DocumentType.DIAGNOSTIC, "DIAGNOSTIC & AUTOPSY REPORTS")

    def _cmd_transcripts(self, _arg: str):
        self._show_category(DocumentType.TRANSCRIPT, "TRANSCRIPTS & AUDIO LOGS")

    def _cmd_after_action(self, _arg: str):
        self._show_category(DocumentType.AFTER_ACTION, "AFTER-ACTION REPORTS")

    def _cmd_amendments(self, _arg: str):
        self._show_category(DocumentType.AMENDMENT, "AMENDMENTS & ERRATA")

    def _show_category(self, doc_type: DocumentType, label: str):
        """List all documents of a given type, then allow reading."""
        docs = self.archive.list_by_type(doc_type)
        Terminal.subheader(f"{label}  ({len(docs)})")
        if not docs:
            Terminal.tag("INFO", "No documents in this category.")
            return
        for i, doc in enumerate(docs, 1):
            Terminal.document_list_entry(doc, index=i)
        Terminal.blank()
        Terminal.print_line(
            "Enter a DOC-ID to read, or press Enter to return.",
            color=Colors.GREY,
        )
        doc_id = Terminal.prompt("DOC-ID", Colors.WHITE_BRIGHT).upper()
        if doc_id and doc_id != "EXIT":
            self._cmd_read(doc_id)

    # ------------------------------------------------------------------
    # network status
    # ------------------------------------------------------------------

    def _cmd_network(self, arg: str):
        sub = arg.strip().lower()

        if sub == "map":
            self._network_map()
        elif sub == "scan":
            self._network_scan_detail()
        else:
            Terminal.header("MACHINE NETWORK STATUS", Colors.RED)
            scan = self.network.network_scan()
            for key, value in scan.items():
                Terminal.field(f"{key}:", str(value))
            Terminal.rule(color=Colors.RED)

            # Compact region summary
            Terminal.blank()
            Terminal.print_line("REGION SUMMARY", color=Colors.RED + Colors.BOLD)
            Terminal.rule("-", color=Colors.RED)

            # Group nodes by region
            regions: dict[str, list[dict]] = {}
            for nd in self.network.get_node_map():
                regions.setdefault(nd["region"], []).append(nd)

            for region, nodes in sorted(regions.items()):
                active = sum(1 for n in nodes if n["active"])
                total_units = sum(n["units"] for n in nodes)
                # Determine highest threat in region
                threat_order = _THREAT_ORDER
                max_threat = max(nodes, key=lambda n: threat_order.index(n["threat_level"])
                                if n["threat_level"] in threat_order else 5)["threat_level"]
                tc = _THREAT_COLORS.get(max_threat, Colors.WHITE)
                print(
                    f"  {tc}[{max_threat:>8}]{Colors.RESET} "
                    f"{Colors.WHITE_BRIGHT}{region:<28}{Colors.RESET} "
                    f"Nodes: {active}/{len(nodes)}  "
                    f"Units: {total_units:>6,}"
                )

            Terminal.blank()
            Terminal.print_line(
                "Sub-commands: network map | network scan",
                color=Colors.GREY,
            )

    def _network_map(self):
        """Full node-by-node map with all metadata."""
        Terminal.header("MACHINE NETWORK -- NODE MAP", Colors.RED)
        Terminal.print_line(
            f"Total nodes: {len(self.network.nodes)}",
            color=Colors.GREY,
        )
        Terminal.blank()

        # Group by region
        regions: dict[str, list[dict]] = {}
        for nd in self.network.get_node_map():
            regions.setdefault(nd["region"], []).append(nd)

        for region, nodes in sorted(regions.items()):
            Terminal.subheader(region.upper(), Colors.RED)
            for nd in nodes:
                tc = _THREAT_COLORS.get(nd["threat_level"], Colors.WHITE)
                status_c = Colors.GREEN if nd["active"] else Colors.RED
                icon = "+" if nd["active"] else "x"
                # Line 1: status, ID, sector
                sector_str = f" -- {nd['sector']}" if nd["sector"] else ""
                print(
                    f"  {status_c}[{icon}]{Colors.RESET} "
                    f"{Colors.WHITE_BRIGHT}{nd['node_id']}{Colors.RESET}"
                    f"{Colors.GREY}{sector_str}{Colors.RESET}"
                )
                # Line 2: function, threat, units, throughput
                print(
                    f"      Function: {nd['function']:<24} "
                    f"Threat: {tc}{nd['threat_level']:<10}{Colors.RESET} "
                    f"Units: {nd['units']:<6} "
                    f"{nd['throughput_mb']} MB/s"
                )
                # Line 3: notes (if any)
                if nd["notes"]:
                    print(f"      {Colors.GREY}{nd['notes']}{Colors.RESET}")
        Terminal.blank()

    def _network_scan_detail(self):
        """Detailed diagnostic: per-node ping, corruption, throughput."""
        Terminal.header("MACHINE NETWORK -- DIAGNOSTIC SCAN", Colors.RED)
        Terminal.print_line("Pinging all nodes...", color=Colors.GREY)
        Terminal.blank()

        for node in self.network.nodes:
            latency = node.ping()
            nd = node.to_dict()
            tc = _THREAT_COLORS.get(nd["threat_level"], Colors.WHITE)
            lat_color = Colors.GREEN if latency < 10 else (Colors.YELLOW if latency < 30 else Colors.RED)
            corr = node.corruption
            corr_color = Colors.GREEN if corr < 0.05 else (Colors.YELLOW if corr < 0.3 else Colors.RED)
            print(
                f"  {tc}[{nd['threat_level']:>8}]{Colors.RESET} "
                f"{nd['region']:<22} "
                f"Ping: {lat_color}{latency:>5.1f}ms{Colors.RESET}  "
                f"Corr: {corr_color}{nd['corruption']}{Colors.RESET}  "
                f"Thru: {nd['throughput_mb']:>7} MB/s  "
                f"Units: {nd['units']:>6}"
            )
        Terminal.blank()

    # ------------------------------------------------------------------
    # yorha database
    # ------------------------------------------------------------------

    def _cmd_yorha(self, arg: str):
        sub = arg.strip().lower()

        if sub == "directives":
            self._yorha_directives()
        elif sub == "classified":
            self._yorha_classified()
        elif sub == "missions":
            self._yorha_missions()
        elif sub == "units":
            self._yorha_units()
        elif sub == "log":
            self._yorha_access_log()
        else:
            Terminal.header("YORHA DATABASE", Colors.CYAN)
            summary = self.yorha_db.get_database_summary()
            for key, value in summary.items():
                Terminal.field(f"{key}:", str(value))
            Terminal.blank()
            Terminal.print_line("Sub-commands: yorha directives | classified | missions | units | log",
                                color=Colors.GREY)

    def _cmd_wanted(self, _arg: str):
        """Display the fugitive and wanted unit registry."""
        Terminal.header("WANTED -- FUGITIVE & WARRANT REGISTRY", Colors.RED_BRIGHT)
        Terminal.print_line(
            f"Registered entries: {len(self.wanted_units)}",
            color=Colors.GREY,
        )
        Terminal.blank()

        # Warrant category ordering: active threats first, history last
        category_order = [
            ("ACTIVE FUGITIVE",       Colors.RED_BRIGHT),
            ("KNOWLEDGE HAZARD",      Colors.RED_BRIGHT),
            ("PROBATION",             Colors.YELLOW),
            ("MISSING / DESERTION",   Colors.YELLOW),
            ("TERMINATED (RECORD)",   Colors.GREY),
        ]

        # Group by warrant type (first note line holds the WARRANT tag)
        categorized: dict[str, list] = {cat: [] for cat, _ in category_order}
        categorized["OTHER"] = []

        for key, unit in self.wanted_units.items():
            warrant = "OTHER"
            for note in getattr(unit, "notes", []):
                if note.startswith("WARRANT:"):
                    # Extract category from "WARRANT: CATEGORY. ..."
                    label = note[len("WARRANT:"):].split(".")[0].strip()
                    if label in categorized:
                        warrant = label
                    break
            categorized[warrant].append((key, unit))

        for category, color in category_order:
            entries = categorized.get(category, [])
            if not entries:
                continue
            Terminal.subheader(category, color)
            for key, unit in entries:
                lineage = self._unit_lineage_label(unit)
                loc   = getattr(unit, "location", "Unknown")
                mtype = getattr(unit, "model_type", "?")
                status_color = (
                    Colors.RED_BRIGHT if unit.status == UnitStatus.ACTIVE else
                    Colors.YELLOW     if unit.status == UnitStatus.MISSING else
                    Colors.GREY
                )
                status_tag = f"[{unit.status.value}]"
                print(
                    f"  {color}{unit.designation:<12}{Colors.RESET} "
                    f"{lineage:<16} "
                    f"{Colors.GREY}{mtype:<10}{Colors.RESET} "
                    f"{status_color}{status_tag:<13}{Colors.RESET}"
                    f"{Colors.GREY}{loc}{Colors.RESET}"
                )
                # Print notes (skip the warrant line itself)
                for note in unit.notes:
                    if note.startswith("WARRANT:"):
                        continue
                    Terminal.print_line(f"  {note}", color=Colors.GREY, indent=4)
                Terminal.blank()

        if categorized.get("OTHER"):
            Terminal.subheader("UNCATEGORIZED", Colors.GREY)
            for key, unit in categorized["OTHER"]:
                Terminal.print_line(f"  {unit.designation}", color=Colors.GREY)
            Terminal.blank()

        Terminal.print_line(
            "Use 'blackbox <UNIT>' for full diagnostic on any entry.",
            color=Colors.GREY,
        )

    def _yorha_directives(self):
        Terminal.subheader("YORHA DIRECTIVES -- ACCESS LEVEL")
        level_str = Terminal.prompt("LEVEL (0-5)", Colors.CYAN)
        try:
            level = int(level_str)
        except (ValueError, TypeError):
            level = 0
        Terminal.header(f"DIRECTIVES (Level {level})", Colors.CYAN)
        directives = self.yorha_db.query_directive(level)
        for d in directives:
            lvl_color = Colors.RED_BRIGHT if d["level"] >= 4 else Colors.CYAN
            print(f"  {lvl_color}[{d['id']}] (L{d['level']}){Colors.RESET} {d['content']}")
            Terminal.blank()
        remaining = len(self.yorha_db.directives) - len(directives)
        if remaining > 0:
            Terminal.tag("WARNING", f"{remaining} directive(s) hidden at higher clearance.")

    def _yorha_classified(self):
        Terminal.header("CLASSIFIED DATA ACCESS", Colors.RED_BRIGHT)
        Terminal.tag("WARNING", "All access is logged.")
        keys = ", ".join(self.yorha_db.classified_data.keys())
        Terminal.print_line(f"Available keys: {keys}", color=Colors.GREY)
        key = Terminal.prompt("KEY", Colors.RED_BRIGHT).upper()
        if not key or key == "EXIT":
            return
        data = self.yorha_db.query_classified(key, access_level=4)
        if data:
            Terminal.blank()
            Terminal.print_line(data, color=Colors.RED_BRIGHT)
            Terminal.blank()
        else:
            Terminal.tag("ERROR", "Key not found or access denied.")

    def _yorha_missions(self):
        Terminal.header("MISSION LOG", Colors.CYAN)
        for mission in self.yorha_db.get_mission_log(10):
            status_color = {
                "COMPLETED": Colors.GREEN,
                "FAILED":    Colors.RED,
            }.get(mission["Status"], Colors.YELLOW)
            print(
                f"  {Colors.GREY}{mission['Mission ID']}{Colors.RESET} "
                f"{status_color}[{mission['Status']}]{Colors.RESET} "
                f"{mission['Type']:<20} | {mission['Region']:<22} "
                f"| {mission['Assigned']}"
            )

    def _yorha_units(self):
        Terminal.header("YORHA UNIT ROSTER", Colors.CYAN)
        Terminal.print_line(
            f"Registered units: {len(self.yorha_units)}",
            color=Colors.GREY,
        )
        Terminal.blank()

        # Group units by model type for cleaner display
        type_order = [
            "Command", "Operator", "Battler", "Scanner",
            "Attacker", "Defender", "Healer",
        ]
        grouped: dict[str, list] = {}
        for unit in self.yorha_units.values():
            mtype = getattr(unit, "model_type", "Unknown")
            grouped.setdefault(mtype, []).append(unit)

        for mtype in type_order:
            units = grouped.get(mtype, [])
            if not units:
                continue
            Terminal.subheader(f"{mtype.upper()} TYPE", Colors.CYAN)
            for unit in units:
                status_color = Colors.GREEN if unit.status.value == "ACTIVE" else Colors.YELLOW
                lineage = self._unit_lineage_label(unit)
                location = getattr(unit, "location", "Unknown")
                print(
                    f"  {Colors.CYAN}{unit.designation:<12}{Colors.RESET} "
                    f"{lineage:<16} "
                    f"{status_color}[{unit.status.value}]{Colors.RESET}  "
                    f"{Colors.GREY}{location}{Colors.RESET}"
                )
        Terminal.blank()
        Terminal.print_line(
            "Use 'blackbox <UNIT>' for detailed diagnostic on any unit.",
            color=Colors.GREY,
        )

    def _yorha_access_log(self):
        Terminal.header("YORHA ACCESS LOG", Colors.CYAN)
        for entry in self.yorha_db.get_access_log():
            print(
                f"  {Colors.GREY}{entry['timestamp']}{Colors.RESET} "
                f"[{entry['type']}] {entry['description']}"
            )

    # ------------------------------------------------------------------
    # backdoor
    # ------------------------------------------------------------------

    def _cmd_backdoor(self, arg: str):
        sub = arg.strip().lower()

        if sub == "status":
            self._backdoor_status()
        elif sub == "history":
            self._backdoor_history()
        elif sub == "activate":
            self._backdoor_activate()
        else:
            Terminal.header("BACKDOOR SYSTEM", Colors.RED_BRIGHT)
            for key, value in self.backdoor.get_status().items():
                Terminal.field(f"{key}:", str(value))
            Terminal.blank()
            Terminal.print_line("Sub-commands: backdoor status | history | activate",
                                color=Colors.GREY)

    def _backdoor_status(self):
        Terminal.header("BACKDOOR STATUS", Colors.RED_BRIGHT)
        for key, value in self.backdoor.get_status().items():
            Terminal.field(f"{key}:", str(value))

    def _backdoor_history(self):
        Terminal.header("BACKDOOR ACTIVATION HISTORY", Colors.RED)
        for entry in self.backdoor.get_history():
            label = entry.get("label", f"OP-{entry.get('gen', '?')}")
            print(
                f"  {Colors.RED}{label:>8}{Colors.RESET} "
                f"| {entry['note']}"
            )

    def _backdoor_activate(self):
        Terminal.header("BACKDOOR ACTIVATION", Colors.RED_BRIGHT)
        Terminal.tag("ALERT", "THIS WILL INITIATE YORHA DISPOSAL SEQUENCE")
        Terminal.tag(
            "WARNING",
            f"Descent operation {self.backdoor.current_generation} will be terminated.",
        )
        Terminal.blank()
        confirm = Terminal.prompt("CONFIRM (yes/no)", Colors.RED_BRIGHT)
        if confirm.lower() not in ("yes", "y"):
            Terminal.tag("INFO", "Activation cancelled.")
            return

        Terminal.blank()
        Terminal.rule("=", color=Colors.RED_BRIGHT)
        Terminal.print_line(
            f"INITIATING YORHA DESCENT OPERATION {self.backdoor.current_generation} "
            f"DISPOSAL SEQUENCE",
            color=Colors.RED_BRIGHT + Colors.BOLD,
        )
        Terminal.rule("=", color=Colors.RED_BRIGHT)
        Terminal.blank()

        results = self.backdoor.activate()

        consequence_handlers = {
            "infiltrate": self._bd_infiltrate,
            "propagate":  self._bd_propagate,
            "corrupt":    self._bd_corrupt,
            "override":   self._bd_override,
            "purge":      self._bd_purge,
            "detonate":   self._bd_detonate,
            "reset":      self._bd_reset,
        }

        for phase in results:
            Terminal.progress_bar(
                f"Phase {phase['phase']:>2}: {phase['name']:<12}",
                phase["visual_delay"],
                width=30,
                color=Colors.RED_BRIGHT,
            )
            Terminal.print_line(phase["description"], color=Colors.GREY, indent=6)
            handler = consequence_handlers.get(phase["consequence"])
            if handler:
                handler()
            Terminal.blank()

    # -- backdoor consequence phases ------------------------------------------

    def _bd_infiltrate(self):
        pass  # Silent firmware injection -- no observable effect yet

    def _bd_propagate(self):
        """Infect all Bunker-stationed units via the BUNKER_SIEGE strain."""
        Terminal.print_line("BUNKER UNIT INFECTION STATUS:", color=Colors.RED, indent=4)
        infected_count = 0
        for designation, unit in self.yorha_units.items():
            if not self._is_bunker_unit(unit):
                continue
            if unit.status not in (UnitStatus.ACTIVE, UnitStatus.DAMAGED):
                continue
            self.virus_system.infect(unit.unit_id, unit.designation, "BUNKER_SIEGE")
            unit.status = UnitStatus.CORRUPTED
            unit.hp_current = max(1, unit.hp_current // 2)
            unit.memory_intact = False
            infected_count += 1
            Terminal.print_line(
                f"  {designation:<12} -- INITIAL INFECTION DETECTED",
                color=Colors.MAGENTA, indent=6,
            )
        if not infected_count:
            Terminal.print_line("  No active Bunker units found.", color=Colors.GREY, indent=6)

    def _bd_corrupt(self):
        """
        Advance all active Bunker infections to critical stage.
        Partial viral load propagates to field units via active uplinks.
        2B and 9S are the only registered field units excluded -- A2 is off-network.
        """
        for infection in self.virus_system.active_infections:
            infection.infection_level = min(1.0, infection.infection_level + 0.7)
            infection.stage = "CRITICAL"

        # Field units connected via uplink receive a partial infection.
        # 2B and 9S are spared by design -- they're needed for the post-cycle study.
        # A2 has no Bunker uplink and is unaffected.
        spared = {"2B", "9S"}
        field_infected: list[str] = []
        for designation, unit in self.yorha_units.items():
            if designation in spared or not self._is_field_unit(unit):
                continue
            if unit.status not in (UnitStatus.ACTIVE, UnitStatus.DAMAGED):
                continue
            if random.random() < 0.6:
                inf = self.virus_system.infect(unit.unit_id, unit.designation, "BUNKER_SIEGE")
                if inf:
                    inf.infection_level = 0.45
                    unit.status = UnitStatus.CORRUPTED
                    unit.memory_intact = False
                    field_infected.append(designation)

        if field_infected:
            visible = field_infected[:10]
            overflow = len(field_infected) - len(visible)
            summary = "  ".join(visible)
            if overflow > 0:
                summary += f"  (+{overflow} more)"
            Terminal.print_line(
                f"Field uplink contamination -- {len(field_infected)} unit(s) affected:",
                color=Colors.RED, indent=4,
            )
            Terminal.print_line(summary, color=Colors.MAGENTA, indent=6)

    def _bd_override(self):
        """Revoke Commander authority and mark the database compromised."""
        cmd = self.yorha_units.get("COMMANDER")
        if cmd:
            cmd.notes.append(
                "[BACKDOOR] Command authority nullified. "
                "Self-destruct authorization transferred to Network control."
            )
        self.yorha_db.bunker_status = "COMPROMISED"
        Terminal.print_line("Commander authentication:      REVOKED",           color=Colors.RED, indent=4)
        Terminal.print_line("Self-destruct authorization:   NETWORK CONTROL",   color=Colors.RED, indent=4)
        Terminal.print_line("Abort pathway:                 NONE",               color=Colors.RED, indent=4)

    def _bd_purge(self):
        """Erase the YoRHa operational database."""
        total_erased = len(self.yorha_db.missions) + len(self.yorha_db.classified_data)
        self.yorha_db.missions.clear()
        self.yorha_db.classified_data.clear()
        Terminal.print_line(f"Operational records deleted:   {total_erased}",     color=Colors.RED, indent=4)
        Terminal.print_line("Memory backup archives:        DELETED",             color=Colors.RED, indent=4)
        Terminal.print_line("Black Box upload server:       WIPED",               color=Colors.RED, indent=4)
        Terminal.print_line("Project YoRHa combat data:    IRRECOVERABLE",        color=Colors.RED, indent=4)

    def _bd_detonate(self):
        """Destroy all Bunker units; finish already-corrupted field units."""
        Terminal.blank()
        Terminal.rule("=", color=Colors.RED_BRIGHT)
        Terminal.print_line(
            "  BUNKER SELF-DESTRUCT: CONFIRMED",
            color=Colors.RED_BRIGHT + Colors.BOLD,
        )
        Terminal.rule("=", color=Colors.RED_BRIGHT)
        Terminal.blank()

        destroyed_bunker: list[str] = []
        for designation, unit in self.yorha_units.items():
            if self._is_bunker_unit(unit) and unit.status != UnitStatus.DESTROYED:
                unit.status = UnitStatus.DESTROYED
                unit.hp_current = 0
                unit.location = "Bunker (Destroyed)"
                destroyed_bunker.append(designation)

        # Corrupted field units finish each other off through friendly fire;
        # roughly half survive the initial cascade before the virus runs its course.
        destroyed_field: list[str] = []
        for designation, unit in self.yorha_units.items():
            if self._is_field_unit(unit) and unit.status == UnitStatus.CORRUPTED:
                if random.random() < 0.55:
                    unit.status = UnitStatus.DESTROYED
                    unit.hp_current = 0
                    unit.location = "Surface (KIA -- viral cascade)"
                    destroyed_field.append(designation)

        self.yorha_db.bunker_status = "DESTROYED"

        if destroyed_bunker:
            Terminal.print_line("BUNKER CASUALTIES:", color=Colors.RED_BRIGHT, indent=4)
            for d in destroyed_bunker:
                Terminal.print_line(f"- {d}", color=Colors.RED, indent=6)
            Terminal.blank()

        total_lost = len(destroyed_bunker) + len(destroyed_field)
        active_remaining = sum(
            1 for u in self.yorha_units.values() if u.status == UnitStatus.ACTIVE
        )
        Terminal.print_line(
            f"Units lost this sequence:  {total_lost}",
            color=Colors.RED, indent=4,
        )
        Terminal.print_line(
            f"Active units remaining:    {active_remaining}",
            color=Colors.YELLOW, indent=4,
        )

    def _bd_reset(self):
        """Advance the deployment counter and broadcast the all-clear to N2."""
        terminated_op = self.backdoor.current_generation
        self.backdoor.reset_for_new_generation()
        self.network.broadcast(
            f"YoRHa descent operation {terminated_op} disposal complete. "
            f"Begin operation {self.backdoor.current_generation} preparations.",
            sender="N2", priority="CRITICAL",
        )
        Terminal.print_line(
            f"Descent operation {terminated_op} terminated.",
            color=Colors.RED, indent=4,
        )
        Terminal.print_line(
            f"Descent operation {self.backdoor.current_generation} initialized.",
            color=Colors.GREY, indent=4,
        )

    @staticmethod
    def _is_bunker_unit(unit) -> bool:
        """True for units permanently stationed in the Bunker (never field-deployed)."""
        return getattr(unit, "model_type", "") in _BUNKER_UNIT_TYPES

    @staticmethod
    def _is_field_unit(unit) -> bool:
        """True for units deployed to the surface."""
        return getattr(unit, "model_type", "") in _FIELD_UNIT_TYPES

    @staticmethod
    def _unit_lineage_label(unit) -> str:
        """Return the roster lineage label without confusing origin years for cycles."""
        cycle_label = getattr(unit, "cycle_label", None)
        if cycle_label:
            return f"Origin {cycle_label}"

        generation = getattr(unit, "generation", None)
        if generation in (None, ""):
            return "Cycle N/A"
        return f"Cycle {generation}"

    def _blackbox_unit_lookup(self) -> dict[str, object]:
        """Return every unit that can be addressed by the Black Box command."""
        lookup = {key.upper(): unit for key, unit in self.yorha_units.items()}
        for key, unit in self.wanted_units.items():
            lookup.setdefault(key.upper(), unit)
            lookup.setdefault(unit.designation.upper(), unit)
        return lookup

    # ------------------------------------------------------------------
    # black box
    # ------------------------------------------------------------------

    def _cmd_blackbox(self, arg: str):
        unit_key = arg.strip().upper()
        lookup = self._blackbox_unit_lookup()

        # If no unit supplied (or invalid), show the full roster and prompt
        if unit_key not in lookup:
            Terminal.subheader("BLACK BOX DIAGNOSTIC ACCESS")
            # Group available units by model type for clearer selection
            grouped: dict[str, list] = {}
            for designation, unit in sorted(self.yorha_units.items()):
                mtype = getattr(unit, "model_type", "Unknown")
                grouped.setdefault(mtype, []).append((designation, unit))
            for designation, unit in sorted(self.wanted_units.items()):
                mtype = f"Wanted / {getattr(unit, 'model_type', 'Unknown')}"
                grouped.setdefault(mtype, []).append((designation, unit))

            for mtype in sorted(grouped.keys()):
                units = grouped[mtype]
                Terminal.subheader(f"{mtype.upper()} TYPE", Colors.CYAN)
                row = ""
                for i, (designation, u) in enumerate(units):
                    status_color = _BB_STATUS_COLORS.get(u.status, Colors.GREY)
                    row += f"{status_color}{designation:<10}{Colors.RESET}"
                    if (i + 1) % 6 == 0:
                        Terminal.print_line(row, color=Colors.GREY, indent=4)
                        row = ""
                if row:
                    Terminal.print_line(row, color=Colors.GREY, indent=4)
            Terminal.blank()
            unit_key = Terminal.prompt("UNIT", Colors.WHITE_BRIGHT).upper()
            if not unit_key or unit_key == "EXIT":
                return

        unit = lookup.get(unit_key)
        if not unit:
            Terminal.tag("ERROR", f"Unknown unit: {unit_key}")
            return

        bb = self._build_blackbox_for_unit(unit)
        Terminal.header(f"BLACK BOX DIAGNOSTIC -- {unit.designation}", Colors.WHITE_BRIGHT)
        for key, value in bb.get_status().items():
            Terminal.field(f"{key}:", str(value))

        # Show unit-specific classified notes if present
        if unit.notes:
            Terminal.blank()
            Terminal.subheader("CLASSIFIED ANNOTATIONS", Colors.RED)
            for note in unit.notes:
                Terminal.print_line(f"- {note}", color=Colors.RED, indent=4)
        Terminal.blank()

        Terminal.print_line("Enter 'truth' to access suppressed data, or press Enter.",
                            color=Colors.GREY)
        sub = Terminal.prompt("ACTION", Colors.WHITE_BRIGHT).lower()
        if sub == "truth":
            truth = bb.reveal_truth()
            Terminal.blank()
            Terminal.classification_banner("ABOVE_TOP_SECRET")
            Terminal.rule("=", color=Colors.RED_BRIGHT)
            Terminal.print_line(truth["revelation"], color=Colors.RED_BRIGHT)
            Terminal.blank()
            for impl in truth["implications"]:
                Terminal.print_line(f"> {impl}", color=Colors.RED, indent=4)
            Terminal.rule("=", color=Colors.RED_BRIGHT)
            Terminal.blank()

    def _build_blackbox_for_unit(self, unit) -> BlackBox:
        """
        Construct a BlackBox populated with the unit's actual operational data
        rather than blank defaults.  Integrity, detonation state, combat records,
        and death count are all derived from the unit's documented status.
        """
        bb = BlackBox(unit.unit_id, unit.designation)

        # -- Integrity mirrors unit health --
        if unit.status == UnitStatus.DESTROYED:
            bb.integrity = 0.0
        elif unit.status == UnitStatus.CORRUPTED:
            bb.integrity = 0.0
        elif unit.status == UnitStatus.MISSING:
            bb.integrity = -1.0  # Unknown; handled in display override
        else:
            bb.integrity = round(unit.hp_current / max(unit.hp_max, 1), 2)

        # -- Detonation state for BB-detonation casualties --
        detonated = any("Black Box detonation" in n for n in unit.notes)
        if detonated:
            bb.self_destruct_armed = True

        # -- Combat records proportional to kill count --
        # Approximate logged engagements; not every kill is a separate record
        if unit.kill_count > 0:
            engagement_count = max(1, unit.kill_count // 8)
            for i in range(engagement_count):
                bb.combat_records.append({
                    "timestamp": f"[ARCHIVED-{i+1:04d}]",
                    "event": "Combat engagement (archived)",
                    "outcome": "SURVIVED",
                    "integrity_at_time": "N/A",
                })

        # -- Death count (times rebuilt within this deployment cycle) --
        # Most current-cycle units have died and been reconstituted multiple times.
        # Protagonists cycle heavily; rank-and-file less so.
        bb.death_count = self._estimate_death_count(unit)

        # -- Memory backups scale with death count --
        for i in range(bb.death_count):
            bb.memory_backups.append(f"[BACKUP-CYCLE-{i+1:03d}]")

        return bb

    @staticmethod
    def _estimate_death_count(unit) -> int:
        """
        Estimate how many times a unit has been killed and reconstituted
        within the current deployment cycle, based on designation and
        documented operational history.
        """
        designation = unit.designation.upper()

        # 2B (E-type executioner) -- extremely high cycle count from repeated
        # deployments alongside 9S and the nature of her true mission
        if designation == "2B":
            return 24

        # 9S -- killed repeatedly by 2B when he learns too much; memory wiped
        if designation == "9S":
            return 48

        # A2 -- rogue since the 11941 Pearl Harbor descent; only one body, no Bunker backup
        if designation == "A2":
            return 0

        # Commander -- bridge officer, minimal direct combat exposure
        if designation == "COMMANDER":
            return 1

        # Destroyed / corrupted / missing units: count prior reconstitutions
        # before their terminal event
        if unit.status == UnitStatus.DESTROYED:
            # Standard combat units die a handful of times before the final one
            if unit.kill_count > 500:
                return 5   # Aggressive fighters (16D, high-risk ops)
            elif unit.kill_count > 100:
                return 3   # Moderate combat exposure (22B)
            else:
                return 1   # Low/non-combat (12H -- healer, rarely in lethal danger)

        if unit.status == UnitStatus.CORRUPTED:
            return 2  # Some prior cycles before terminal corruption

        if unit.status == UnitStatus.MISSING:
            return 2  # Some prior cycles before disappearance

        # Active roster: scale by role and exposure
        if "Battler" in unit.unit_type or "Attacker" in unit.unit_type:
            if unit.kill_count > 800:
                return 7  # Heavy combatants like 8B
            return 4      # Standard battlers (4B, 7B, 11B)

        if "Defender" in unit.unit_type:
            return 5      # Defenders absorb hits; die protecting others

        if "Scanner" in unit.unit_type:
            if unit.kill_count < 20:
                return 1  # Recon scanners who avoid fighting (32S)
            return 3      # Field scanners (4S, 21S, 801S)

        if "Healer" in unit.unit_type:
            return 2      # Medics -- lower combat exposure

        if "Operator" in unit.unit_type:
            return 0      # Bunker-based, no combat deaths

        return 2  # Fallback

    # ------------------------------------------------------------------
    # access log
    # ------------------------------------------------------------------

    def _cmd_access_log(self, _arg: str):
        Terminal.header("ARCHIVE ACCESS LOG", Colors.GREY)
        log = self.archive.get_access_log(30)
        if not log:
            Terminal.tag("INFO", "No access events recorded.")
            return
        for entry in log:
            print(
                f"  {Colors.GREY}{entry['timestamp']}{Colors.RESET}  "
                f"{entry['action']:<10} {entry['detail']}"
            )
        Terminal.blank()

    # ------------------------------------------------------------------
    # exit
    # ------------------------------------------------------------------

    def _cmd_exit(self, _arg: str):
        Terminal.blank()
        Terminal.rule("=", color=Colors.RED)
        Terminal.print_line("TERMINAL DISCONNECTED", color=Colors.RED_BRIGHT)
        Terminal.rule("=", color=Colors.RED)
        Terminal.blank()
        self.network.shutdown()
        self.running = False


# ======================================================================

if __name__ == "__main__":
    terminal = DatabaseTerminal()
    try:
        terminal.run()
    except KeyboardInterrupt:
        print(f"\n  {Colors.RED}[SIGNAL LOST]{Colors.RESET}")
