from typing import Dict, List, Any, Union, Optional, Mapping
from BaseClasses import Location, Item, Tutorial, ItemClassification, Region, CollectionState
from worlds.AutoWorld import World, WebWorld
from ..generic.Rules import set_rule

from .Items import base_id, item_list, filler_list, ItemType, JIItem
from .Locations import location_list, JILocation
from .Options import JetIslandOptions


class JetIslandItem(Item):
    game = "Jet Island"

    def __init__(self, name: str, classification: ItemClassification, code: Optional[int], player: int) -> None:
        super().__init__(name, classification, code, player)

class JetIslandLocation(Location):
    game = "Jet Island"

class JetIsland(World):
    game = "Jet Island"

    item_name_to_id = {item.name:(item.id) for item in (item_list + filler_list)}
    location_name_to_id = {loc.name: (loc.id) for loc in location_list}
    allItems = item_list + filler_list

    options_dataclass = JetIslandOptions
    options = JetIslandOptions

    item_type_classification : Dict[ItemType,ItemClassification] = {
        ItemType.Ability: ItemClassification.progression,
        ItemType.Stat: ItemClassification.useful,
        ItemType.Modifier: ItemClassification.skip_balancing,
        ItemType.Filler: ItemClassification.filler,
        ItemType.Trap: ItemClassification.trap,
    }
    activeModifiers : List[JIItem]

    def generate_early(self) -> None:
        list = item_list[4:-5]
        self.activeModifiers = [item for item in list if item.name not in self.options.dont_auto_use_modifiers]
        if len(list) - len(self.activeModifiers) != len(self.options.dont_auto_use_modifiers.value):
            excluded_items = [item for item in list if item.name in self.options.dont_auto_use_modifiers]
            excluded_names = {item.name for item in excluded_items}
            expected_names = set(self.options.dont_auto_use_modifiers.value)
            not_found = expected_names - excluded_names
            print(f"modifier(s) {not_found} not found in modifier list\nchoose from the following:\n{list}")
            raise Exception("Invalid dont_auto_use_modifiers")

    def get_filler_item_name(self) -> str:
        return self.random.choice(filler_list).name

    def create_item(self, name: str) -> "Item":
        item_data = self.allItems[self.item_name_to_id[name]-base_id]
        return JetIslandItem(name, self.item_type_classification[item_data.type], item_data.id, self.player)

    def create_items(self) -> None:
        self.multiworld.itempool += [self.create_item('Jet Force') for _ in range(5)]
        self.multiworld.itempool += [self.create_item('Jet Fuel') for _ in range(5)]
        self.multiworld.itempool += [self.create_item('Hookshot Length') for _ in range(5)]
        self.multiworld.itempool += [self.create_item('Wind Resistance') for _ in range(5)]

        for item in self.activeModifiers:
            self.multiworld.itempool.append(self.create_item(item.name))

        for item in item_list[-5:]:
            self.multiworld.itempool.append(self.create_item(item.name))

        for _ in self.options.dont_auto_use_modifiers.value:
            self.multiworld.itempool.append(self.create_item(self.get_filler_item_name()))

        boss: Location = self.multiworld.get_location('Boss Killed', self.player)
        boss.place_locked_item(JetIslandItem('Victory',ItemClassification.progression,None,self.player))

    def create_regions(self) -> None:
        menu_region = Region('Menu', self.player, self.multiworld)
        self.multiworld.regions.append(menu_region)

        location_copy = location_list[:-1].copy()
        last = location_list[-1]
        self.random.shuffle(location_copy)

        for loc in location_copy:
            menu_region.locations.append(JetIslandLocation(self.player, loc.name, loc.id, menu_region))

        menu_region.locations.append(JetIslandLocation(self.player, last.name, None, menu_region))

    def set_rules(self) -> None:
        self.multiworld.completion_condition[self.player] = lambda state: state.has_all(
            ['Long Shot', 'Bunny Hop', 'Super Shot', 'Hookshot Reel'],self.player)

    def fill_slot_data(self) -> Mapping[str, Any]:
        return {
            "base_id": int(base_id),
            "show_map_points" : bool(self.options.show_missing_locations_on_map.value),
            "auto_modifier" : int(self.options.auto_enable_modifiers.value),
            "starting_checkpoint": int(self.options.starting_checkpoint.value),
        }