"""The seven crewed environments the PSI archive ranks fire-safety risk against."""

from typing import List
from models.investigation import Environment

ENVIRONMENTS: List[dict] = [
    {"id": "iss_leo", "label": "ISS (0g LEO)", "oxygen_pct": 20.9, "pressure_psi": 14.7, "gravity": "0 g (LEO)", "color": "#38BDF8"},
    {"id": "lunar_gateway", "label": "Lunar Gateway (0g Cislunar)", "oxygen_pct": 34.0, "pressure_psi": 8.2, "gravity": "0 g (NRHO)", "color": "#A78BFA"},
    {"id": "artemis_moon_base", "label": "Lunar Surface (0.166g)", "oxygen_pct": 30.0, "pressure_psi": 8.2, "gravity": "0.166 g", "color": "#FBBF24"},
    {"id": "mars_transit", "label": "Mars Transit (0g High O2)", "oxygen_pct": 30.0, "pressure_psi": 8.2, "gravity": "0 g (transit)", "color": "#FB923C"},
    {"id": "mars_surface_hab", "label": "Mars Habitat (0.38g)", "oxygen_pct": 26.0, "pressure_psi": 8.2, "gravity": "0.38 g", "color": "#EF4444"},
    {"id": "pressurized_rover", "label": "Pressurized Rover (0.38g)", "oxygen_pct": 28.0, "pressure_psi": 10.2, "gravity": "0.38 g", "color": "#34D399"},
    {"id": "spacesuit_eva", "label": "xEMU Spacesuit (100% O2 Low-P)", "oxygen_pct": 100.0, "pressure_psi": 4.3, "gravity": "0-0.38 g (EVA)", "color": "#E879F9"},
]

ENVIRONMENTS_MODELED = [Environment(**env) for env in ENVIRONMENTS]
