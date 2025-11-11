from typing import List, Dict, Set
from dataclasses import dataclass
from enum import Enum

from .Helpers import format_level_name, parse_level_name

base_id = 9002100

class ItemType(Enum):
    Ability = 0
    Level = 1
    Trap = 2
    Filler = 3


@dataclass
class CTItem:
    name: str
    type: ItemType


item_list: List[CTItem] = [CTItem(format_level_name(i),ItemType.Level) for i in range(105)]

item_list.extend([
    CTItem("Double Jump", ItemType.Ability),
    CTItem("Air Dash", ItemType.Ability),
    CTItem("Jetpack", ItemType.Ability),
    CTItem("Levitation", ItemType.Ability),
    CTItem("Grappling Hook", ItemType.Ability),
    CTItem("Truck Boost", ItemType.Ability),
    CTItem("Back Truck", ItemType.Ability),
    CTItem("Trucker Flip", ItemType.Ability),
    CTItem("Time Slow", ItemType.Ability),
    CTItem("Portable Truck", ItemType.Ability),
    CTItem("Trucksolute Zero", ItemType.Ability),
    CTItem("Epic Mode", ItemType.Ability),
    CTItem("Supertruck", ItemType.Ability),
    CTItem("Disrespected Blink", ItemType.Ability),

    CTItem("+1000p",ItemType.Filler),
    CTItem("Infinite Stamina",ItemType.Filler),
    CTItem("Impulse",ItemType.Trap),
    CTItem("Brake",ItemType.Trap),
])