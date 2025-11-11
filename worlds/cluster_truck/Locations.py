from typing import List, Dict
from dataclasses import dataclass


from .Helpers import format_level_name, parse_level_name

@dataclass
class CTLocation:
    name: str
    game_id: int


location_list: List[CTLocation] = [CTLocation(format_level_name(i), i) for i in range(105)]

location_list.extend([
    CTLocation("Double Jump", 105),
    CTLocation("Air Dash", 106),
    CTLocation("Jetpack", 107),
    CTLocation("Levitation", 108),
    CTLocation("Grappling Hook", 109),
    CTLocation("Truck Boost", 110),
    CTLocation("Back Truck", 111),
    CTLocation("Trucker Flip", 112),
    CTLocation("Time Slow", 113),
    CTLocation("Portable Truck", 114),
    CTLocation("Trucksolute Zero", 115),
    CTLocation("Epic Mode", 116),
    CTLocation("Supertruck", 117),
    CTLocation("Disrespected Blink", 118)
])
