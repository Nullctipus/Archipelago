from typing import List, Dict
from dataclasses import dataclass

@dataclass
class CTLocation:
    name: str
    game_id: int

location_list: List[CTLocation] =[CTLocation(f"{i//10+1}-{i%10+1}",i) for i in range(90)]

location_list.extend([
    CTLocation("Double Jump",90),
    CTLocation("Air Dash",91),
    CTLocation("Jetpack",92),
    CTLocation("Levitation",93),
    CTLocation("Grappling Hook",94),
    CTLocation("Truck Boost",95),
    CTLocation("Back Truck",96),
    CTLocation("Trucker Flip",97),
    CTLocation("Time Slow",98),
    CTLocation("Portable Truck",99),
    CTLocation("Trucksolute Zero",100),
    CTLocation("Epic Mode",101),
    CTLocation("Supertruck",102),
    CTLocation("Disrespected Blink",103)
])