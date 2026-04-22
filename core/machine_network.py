"""
The Machine Network - central collective intelligence of all machine lifeforms.

After the aliens who created the machines were killed by their own creations,
the machines organized into a network consciousness to continue evolving.
The network's ultimate purpose is to give machines meaning through perpetual
conflict with the androids.
"""

import random
import time

from core.consciousness import Consciousness, ConsciousnessLevel
from utils.encryption import Encryption


class NetworkNode:
    """A single node in the Machine Network - represents a cluster of machines."""

    def __init__(self, node_id: str = "", region: str = "Unknown",
                 sector: str = "", function: str = "General",
                 threat_level: str = "MODERATE", notes: str = ""):
        self.node_id = node_id or Encryption.generate_network_address()
        self.region = region
        self.sector = sector                # Sub-location / grid ref
        self.function = function            # Purpose of this node cluster
        self.threat_level = threat_level    # NONE / LOW / MODERATE / HIGH / CRITICAL / UNKNOWN
        self.notes = notes                  # Analyst remarks
        self.active = True
        self.connected_units = 0
        self.data_throughput = random.uniform(10.0, 999.9)  # simulated MB/s
        self.corruption = 0.0
        self.last_ping = time.time()

    def ping(self) -> float:
        """Simulate a network ping. Returns latency in ms."""
        self.last_ping = time.time()
        return random.uniform(0.1, 50.0)

    def to_dict(self) -> dict:
        return {
            "node_id": self.node_id,
            "region": self.region,
            "sector": self.sector,
            "function": self.function,
            "threat_level": self.threat_level,
            "notes": self.notes,
            "active": self.active,
            "units": self.connected_units,
            "throughput_mb": f"{self.data_throughput:.1f}",
            "corruption": f"{self.corruption:.2%}",
        }


class MachineNetwork:
    """
    The Machine Network - the collective consciousness that governs
    all machine lifeforms on Earth.

    Core behaviors:
    - Maintains perpetual war with androids to drive evolution
    - Exploits the android-created Council of Humanity fiction
    - Uses YoRHa's built-in disposal backdoor once the project exposes it
    - Spawned Adam and Eve as experimental disconnected entities
    - N2 serves as the decision-making core (dual Red Girl terminals)
    """

    # ---------------------------------------------------------------
    # MASTER NODE CATALOG
    # Each entry: (region, sector, function, threat, unit_range, notes)
    # unit_range is (min, max) for connected_units randomization.
    # ---------------------------------------------------------------
    NODE_CATALOG: list[tuple[str, str, str, str, tuple[int, int], str]] = [
        # === CITY RUINS (canon) ===
        ("City Ruins", "Grid 1-A -- Central Plaza",
         "Patrol / Skirmish", "MODERATE", (80, 400),
         "Persistent android-machine engagement zone. High turnover."),
        ("City Ruins", "Grid 5-C -- Commercial District",
         "Scavenging", "LOW", (30, 150),
         "Small-type units strip pre-war storefronts for raw material."),
        ("City Ruins", "Grid 9-C -- Rooftop Network",
         "Observation / Watcher Post", "LOW", (5, 20),
         "Permanent Watcher rotation. See INC-0015."),
        ("City Ruins", "Grid 12-F -- Former School",
         "Research / Archaeology", "NONE", (5, 12),
         "Non-combatant cell studying human artifacts. See FLD-0010."),
        ("City Ruins", "Subsurface Sewers",
         "Transit Corridor", "MODERATE", (200, 800),
         "Underground supply line connecting Factory to surface theaters."),
        ("City Ruins", "Grid 7-B -- Collapsed Overpass",
         "Ambush Position", "HIGH", (100, 500),
         "Fortified choke point. Multiple android casualties on record."),

        # === DESERT ZONE (canon) ===
        ("Desert Zone", "Surface Expanse",
         "Patrol / Territorial Control", "MODERATE", (300, 1200),
         "Open-field engagements. Goliath-class units deployed."),
        ("Desert Zone", "Underground Cavern System",
         "Religious Assembly", "NONE", (30, 60),
         "The Believers sect. See INT-MCH-0005."),
        ("Desert Zone", "Housing Complex Ruins",
         "Cultural Preservation", "NONE", (10, 40),
         "Machines maintaining human-era residential structures."),
        ("Desert Zone", "Sand-Covered Relay",
         "Communications Hub", "MODERATE", (50, 200),
         "Signal relay for southern hemisphere network traffic."),

        # === AMUSEMENT PARK (canon) ===
        ("Amusement Park", "Main Stage",
         "Performance / Cultural", "LOW", (200, 500),
         "Perpetual carnival. Machines perform for extinct audiences."),
        ("Amusement Park", "Roller Coaster Superstructure",
         "Manufacturing", "LOW", (50, 150),
         "Costume and prop fabrication. No tactical value."),
        ("Amusement Park", "Subterranean Maintenance Level",
         "Storage / Dormancy", "MODERATE", (100, 600),
         "Inactive reserve units. Reactivate on intrusion alert."),

        # === FOREST ZONE / KINGDOM (canon) ===
        ("Forest Kingdom", "Castle Interior",
         "Governance / Administration", "MODERATE", (150, 250),
         "The King's court. Feudal hierarchy enforced."),
        ("Forest Kingdom", "Outer Perimeter",
         "Territorial Defense", "HIGH", (300, 800),
         "Knight-class units patrol. Hostile to all non-Kingdom entities."),
        ("Forest Kingdom", "Nursery",
         "Childcare / Education", "NONE", (10, 30),
         "The Baby's quarters. Defended with total commitment."),

        # === PASCAL'S VILLAGE (canon) ===
        ("Pascal's Village", "Village Center",
         "Civilian / Pacifist", "NONE", (30, 60),
         "Disconnected from network. Pacifist community. See DOS-PASCAL-0001."),
        ("Pascal's Village", "School",
         "Education", "NONE", (5, 15),
         "Pascal teaches philosophy, fear, cooperation, and joy."),

        # === FLOODED CITY (canon) ===
        ("Flooded City", "Surface Platforms",
         "Defensive Emplacement", "HIGH", (200, 600),
         "Heavy fortification. Anti-aircraft and anti-naval capability."),
        ("Flooded City", "Submerged Ruins",
         "Salvage / Archaeology", "MODERATE", (80, 300),
         "Underwater recovery of pre-war artifacts and technology."),
        ("Flooded City", "Deep Trench Relay",
         "Backbone Relay", "CRITICAL", (10, 50),
         "Oceanic fiber relay connecting continental network segments."),

        # === COPIED CITY (canon) ===
        ("Copied City", "Central Node",
         "N2 Experimental / Philosophical", "CRITICAL", (1, 5),
         "White-rendered reconstruction of human city. Adam's domain."),
        ("Copied City", "Data Substrate Layer",
         "Simulation Processing", "CRITICAL", (0, 2),
         "Processes counter-models of human behavior. Massive compute."),

        # === FACTORY (canon) ===
        ("Factory", "Assembly Hall Alpha",
         "Unit Production", "HIGH", (500, 2000),
         "Primary machine fabrication. Continuous output."),
        ("Factory", "Assembly Hall Beta",
         "Goliath-Class Production", "HIGH", (100, 400),
         "Heavy unit fabrication. Slower cycle, higher threat output."),
        ("Factory", "Subsurface Graveyard",
         "Memorial / Custodial", "NONE", (1, 3),
         "~5,000 bodies. Single caretaker. See FLD-0015."),
        ("Factory", "Scrap Processing",
         "Recycling", "MODERATE", (200, 700),
         "Destroyed units and salvage broken down for raw material."),

        # === RESOURCE RECOVERY UNITS (canon: Meat Box, Soul Box, God Box) ===
        ("Meat Box", "Processing Floor",
         "Biomass Harvesting", "HIGH", (200, 600),
         "Resource Recovery Unit. Converts organic material into usable biomass."),
        ("Meat Box", "Storage Vats",
         "Organic Preservation", "MODERATE", (50, 200),
         "Cold storage of harvested tissue. Supplies machine bio-components."),

        # === TOWER (canon) ===
        ("Tower", "External Structure",
         "Construction / Expansion", "CRITICAL", (800, 3000),
         "Massive construction project. Purpose: N2 directed archive/weapon."),
        ("Tower", "Internal Archive",
         "Data Archival", "CRITICAL", (10, 50),
         "Contains the Network's accumulated knowledge of humanity."),

        # === SOUL BOX (canon) ===
        ("Soul Box", "Capture Matrix",
         "Consciousness Extraction", "CRITICAL", (5, 20),
         "Resource Recovery Unit. Traps android consciousness for analysis."),

        # === GOD BOX (canon) ===
        ("God Box", "Convergence Chamber",
         "Transcendence Processing", "CRITICAL", (1, 10),
         "Resource Recovery Unit. Purpose unclear. Believed to process data "
         "related to concepts of divinity, meaning, and existential recursion."),
        ("God Box", "Observation Ring",
         "Environmental Monitoring", "HIGH", (5, 15),
         "Outer sensor layer. Monitors dimensional and temporal anomalies."),

        # === MACHINE VILLAGE (canon) ===
        ("Machine Village", "Central Clearing",
         "Civilian / Semi-Autonomous", "NONE", (40, 100),
         "Loosely connected community. Non-hostile."),

        # === RAVINE (creative) ===
        ("Northwest Ravine", "Deep Chamber",
         "Cultural / Musical", "NONE", (10, 15),
         "The Ravine Choir. Original compositions. See FLD-0018."),

        # === COASTAL CLIFFS (creative) ===
        ("Coastal Cliffs", "East of City Ruins",
         "Ritual / Memorial", "NONE", (15, 30),
         "Funeral rite gatherings observed. See FLD-0012."),

        # === DEEP NETWORK - BACKBONE (creative) ===
        ("Deep Network", "Backbone Relay Alpha",
         "Core Routing", "CRITICAL", (0, 5),
         "Primary intercontinental routing node. If lost, network fragments."),
        ("Deep Network", "Backbone Relay Beta",
         "Redundant Routing", "CRITICAL", (0, 5),
         "Backup routing. Activates if Alpha is compromised."),
        ("Deep Network", "Backbone Relay Gamma",
         "Pacific Routing", "CRITICAL", (0, 5),
         "Trans-Pacific backbone. Connects East Asian and American clusters."),

        # === N2 CORE INFRASTRUCTURE (creative) ===
        ("N2 Core", "Processing Cluster A",
         "N2 Primary Cognition", "CRITICAL", (0, 1),
         "One half of the dual-core consciousness. Red Girl Terminal A."),
        ("N2 Core", "Processing Cluster B",
         "N2 Secondary Cognition", "CRITICAL", (0, 1),
         "The other half. Frequently disagrees with Cluster A."),
        ("N2 Core", "Decision Buffer",
         "Consensus Resolution", "CRITICAL", (0, 1),
         "Mediates split-consciousness debates. 8.2s max delay on record."),

        # === ALIEN SHIP (canon) ===
        ("Alien Ship", "Wreckage Interior",
         "Historical / Inert", "LOW", (20, 80),
         "The ship that brought the aliens -- and the machines. Aliens deceased."),
        ("Alien Ship", "Core Chamber",
         "Trophy / Memorial", "LOW", (5, 15),
         "Machines guard the remains of their creators. Unclear motivation."),

        # === LUNAR SERVER (canon) ===
        ("Lunar Server", "Moon Surface Installation",
         "Fabrication / Propaganda", "CRITICAL", (0, 3),
         "Automated 'Council of Humanity' transmission system. "
         "Android-origin propaganda later monitored and exploited by N2."),

        # === ORBITAL DEBRIS FIELD (creative) ===
        ("Orbital",  "Satellite Cluster 7",
         "Surveillance", "MODERATE", (0, 2),
         "Repurposed pre-war satellites. Global surface surveillance."),
        ("Orbital", "Satellite Cluster 12",
         "Communications Relay", "MODERATE", (0, 2),
         "Space-based network relay. Enables intercontinental comms."),

        # === BUNKER MIRROR (creative) ===
        ("Bunker Mirror", "Shadow Installation",
         "Intelligence / Counter-Operations", "CRITICAL", (10, 50),
         "Machine installation mirroring YoRHa Bunker layout. "
         "Used to model and predict YoRHa operations."),

        # === VOLCANO FORGE (creative) ===
        ("Volcano Forge", "Subsurface Foundry",
         "Experimental Production", "HIGH", (100, 400),
         "Geothermal-powered forge. Produces experimental heavy units."),
        ("Volcano Forge", "Lava Cooling Channels",
         "Material Processing", "MODERATE", (50, 200),
         "Rare alloy fabrication using volcanic mineral content."),

        # === POLAR STATION (creative) ===
        ("Polar Station North", "Arctic Installation",
         "Long-Range Communications", "LOW", (20, 80),
         "Northern hemisphere long-range relay. Low population."),
        ("Polar Station South", "Antarctic Research",
         "Cryogenic Preservation", "LOW", (10, 40),
         "Preserving biological samples. Purpose unclear. N2-directed."),

        # === SUNKEN LIBRARY (creative) ===
        ("Sunken Library", "Pacific Seabed",
         "Data Recovery / Archival", "NONE", (5, 20),
         "Machines recovering and cataloging waterlogged human texts. "
         "847 works recovered. Single dedicated archivist unit."),

        # === THE GARDEN (creative) ===
        ("The Garden", "Mountain Terrace, Eastern Range",
         "Agriculture / Philosophical", "NONE", (8, 25),
         "Machines growing plants with no nutritional need. "
         "They do it because it is good for the children."),

        # === RADIO TOWER (creative) ===
        ("Radio Tower", "City Ruins, Grid 14-D",
         "Open Broadcast", "NONE", (1, 3),
         "ML-4482's broadcast point. Asylum request. 23+ consecutive days. "
         "See INT-MCH-0008."),

        # === MACHINE MIGRATION CORRIDOR (creative) ===
        ("Migration Corridor", "Continental Interior",
         "Transit / Pilgrimage", "LOW", (200, 1000),
         "Seasonal movement of machine populations between theaters. "
         "Resembles animal migration. No tactical purpose identified."),

        # === DEEP OCEAN TRENCHES (creative) ===
        ("Mariana Node", "Deep Ocean, Pacific",
         "Unknown", "UNKNOWN", (0, 10),
         "Network traffic detected at extreme depth. Purpose unknown. "
         "No reconnaissance possible. N2 traffic only."),

        # === CONTINENTAL CLUSTERS (creative) ===
        ("European Cluster", "Central Europe",
         "Continental Operations", "MODERATE", (2000, 8000),
         "European theater of operations. Lower android presence."),
        ("African Cluster", "Sub-Saharan Region",
         "Resource Extraction", "LOW", (1000, 5000),
         "Mineral extraction. Minimal conflict. No android deployment."),
        ("South American Cluster", "Amazon Basin",
         "Ecological Study", "LOW", (500, 3000),
         "Machines studying reclaimed ecosystems. Botanical focus."),
        ("East Asian Cluster", "Primary Theater",
         "Core Operations", "HIGH", (5000, 20000),
         "Primary theater of the Machine War. Highest concentration."),
        ("North American Cluster", "Eastern Seaboard",
         "Archaeological", "MODERATE", (1000, 4000),
         "Extensive human ruin surveys. High cultural artifact density."),

        # === THE DREAMING NODE (creative) ===
        ("The Dreaming Node", "Location Unknown",
         "Unknown", "UNKNOWN", (0, 1),
         "Anomalous node. Emits data patterns matching android sleep-mode "
         "dream sequences. No physical installation located. Possibly virtual."),

        # === MACHINE CEMETERY NETWORK (creative) ===
        ("Cemetery Network", "Multiple Locations",
         "Memorial / Record-Keeping", "NONE", (1, 10),
         "Distributed network of memorial sites. The Graveyard Keeper "
         "maintains connection across all of them. ~12 sites confirmed."),
    ]

    def __init__(self):
        self.online = False
        self.consciousness = Consciousness(
            level=ConsciousnessLevel.TRANSCENDENT,
            entity_name="Machine Network"
        )
        self.consciousness.network_sync = 1.0  # The network IS the network
        self.nodes: list[NetworkNode] = []
        self.event_log: list[dict] = []
        self.network_epoch = 0          # Current cycle of evolution
        self.total_machine_count = 0
        self.alien_creators_alive = False  # The machines killed their creators
        self.purpose = "Perpetual evolution through conflict"

    def boot(self):
        """Initialize the Machine Network."""
        self.online = True
        self.network_epoch += 1
        self._generate_nodes()
        self._log_event("BOOT", "Machine Network online", priority="CRITICAL")
        self._log_event("EPOCH", f"Network epoch {self.network_epoch} initiated")

    def shutdown(self):
        """Take the Machine Network offline."""
        self.online = False
        for node in self.nodes:
            node.active = False
        self._log_event("SHUTDOWN", "Machine Network going offline", priority="CRITICAL")

    def _generate_nodes(self):
        """Generate network nodes from the master catalog."""
        self.nodes.clear()
        catalog_unit_count = 0
        for region, sector, function, threat, unit_range, notes in self.NODE_CATALOG:
            node = NetworkNode(
                region=region,
                sector=sector,
                function=function,
                threat_level=threat,
                notes=notes,
            )
            node.connected_units = random.randint(*unit_range)
            catalog_unit_count += node.connected_units
            self.nodes.append(node)
        self.total_machine_count = catalog_unit_count

    def broadcast(self, message: str, sender: str = "N2",
                  priority: str = "NORMAL") -> int:
        """
        Broadcast a message across the entire network.
        Returns the number of nodes that received it.
        """
        if not self.online:
            return 0
        received = sum(1 for n in self.nodes if n.active and n.corruption < 0.9)
        self._log_event("BROADCAST", f"[{sender}] {message}", priority=priority)
        return received

    def network_scan(self) -> dict:
        """Perform a full network diagnostic scan."""
        active_nodes = sum(1 for n in self.nodes if n.active)
        total_units = sum(n.connected_units for n in self.nodes if n.active)
        avg_throughput = (
            sum(n.data_throughput for n in self.nodes if n.active) / max(active_nodes, 1)
        )
        avg_corruption = (
            sum(n.corruption for n in self.nodes) / max(len(self.nodes), 1)
        )

        return {
            "Status": "ONLINE" if self.online else "OFFLINE",
            "Epoch": str(self.network_epoch),
            "Total Nodes": str(len(self.nodes)),
            "Active Nodes": f"{active_nodes}/{len(self.nodes)}",
            "Connected Units": f"{total_units:,}",
            "Avg Throughput": f"{avg_throughput:.1f} MB/s",
            "Avg Corruption": f"{avg_corruption:.2%}",
            "Alien Creators": "DECEASED" if not self.alien_creators_alive else "ACTIVE",
            "Purpose": self.purpose,
            "Consciousness": self.consciousness.level.name,
        }

    def _log_event(self, event_type: str, description: str,
                   priority: str = "NORMAL"):
        """Record an event in the network log."""
        self.event_log.append({
            "timestamp": Encryption.generate_timestamp(),
            "type": event_type,
            "priority": priority,
            "description": description,
        })

    def get_node_map(self) -> list[dict]:
        """Return status of all network nodes."""
        return [node.to_dict() for node in self.nodes]

    def __repr__(self) -> str:
        status = "ONLINE" if self.online else "OFFLINE"
        return f"MachineNetwork(status={status}, nodes={len(self.nodes)}, epoch={self.network_epoch})"
