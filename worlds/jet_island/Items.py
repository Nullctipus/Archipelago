from typing import List, Dict, Set
from dataclasses import dataclass
from enum import Enum

base_id = 9003100

class ItemType(Enum):
    Ability = 0
    Stat = 1
    Modifier = 2
    Filler = 3
    Trap = 4


@dataclass
class JIItem:
    name: str
    id : int
    type: ItemType


item_list : List[JIItem] = [
JIItem('Jet Fuel',base_id+0,ItemType.Stat),
JIItem('Jet Force',base_id+1,ItemType.Stat),
JIItem('Hookshot Length',base_id+2,ItemType.Stat),
JIItem('Wind Resistance',base_id+3,ItemType.Stat),
JIItem('Extreme Rotation',base_id+4,ItemType.Modifier),
JIItem('Slowmo Hookshots',base_id+5,ItemType.Modifier),
JIItem('Mars Gravity',base_id+6,ItemType.Modifier),
JIItem('Falling Up',base_id+7,ItemType.Modifier),
JIItem('Jets Only',base_id+8,ItemType.Modifier),
JIItem('Upsidedown World',base_id+9,ItemType.Modifier),
JIItem('Jupiter Gravity',base_id+10,ItemType.Modifier),
JIItem('Hookshots Only',base_id+11,ItemType.Modifier),
JIItem('Sideways World',base_id+12,ItemType.Modifier),
JIItem('Sun Gravity',base_id+13,ItemType.Modifier),
JIItem('Super Explosions',base_id+14,ItemType.Modifier),
JIItem('Zero Gravity',base_id+15,ItemType.Modifier),
JIItem('Too Much Jets',base_id+16,ItemType.Modifier),
JIItem('Moon Gravity',base_id+17,ItemType.Modifier),
JIItem('Infinite Jets',base_id+18,ItemType.Modifier),
JIItem('Super Hookshots',base_id+19,ItemType.Modifier),
JIItem('Random World Rot On Respawn',base_id+20,ItemType.Modifier),
JIItem('TenX Speed',base_id+21,ItemType.Modifier),
JIItem('Backwards Jets',base_id+22,ItemType.Modifier),
JIItem('Stretchy Hookshots',base_id+23,ItemType.Modifier),
JIItem('Hookshots Are Stilts',base_id+24,ItemType.Modifier),
JIItem('Bouncy Ground',base_id+25,ItemType.Modifier),
JIItem('Ground Is Lava',base_id+26,ItemType.Modifier),
JIItem('Gun Only',base_id+27,ItemType.Modifier),
JIItem('Gun Always Charged',base_id+28,ItemType.Modifier),
JIItem('Gun Rapid Fire',base_id+29,ItemType.Modifier),
JIItem('Night Sky',base_id+30,ItemType.Modifier),
JIItem('Pitch Black',base_id+31,ItemType.Modifier),
JIItem('Foggy',base_id+32,ItemType.Modifier),
JIItem('Death On Hard Impact',base_id+33,ItemType.Modifier),
JIItem('Palm Jets',base_id+34,ItemType.Modifier),
JIItem('Delicate Player',base_id+35,ItemType.Modifier),
JIItem('Super Wormy',base_id+36,ItemType.Modifier),
JIItem('Long Shot',base_id+37,ItemType.Ability),
JIItem('Bunny Hop',base_id+38,ItemType.Ability),
JIItem('Super Shot',base_id+39,ItemType.Ability),
JIItem('Hookshot Reel',base_id+40,ItemType.Ability),
JIItem('Auto Charge',base_id+41,ItemType.Ability),
]
filler_list : List[JIItem] = [
    JIItem('10s No Jets',base_id+42,ItemType.Trap),
    JIItem('10s No Hookshots',base_id+43,ItemType.Trap),
    JIItem('10s No Wind',base_id+44,ItemType.Filler),
    JIItem('10s Infinite Jets',base_id+45,ItemType.Filler),
    JIItem('Get Rotated',base_id+46,ItemType.Trap),
    JIItem('Swimming',base_id+47,ItemType.Filler),
]

