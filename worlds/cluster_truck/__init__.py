from typing import Dict, List, Any, Union, Optional, Mapping
from BaseClasses import Location, Item, Tutorial, ItemClassification, Region
from worlds.AutoWorld import World, WebWorld
from .Items import item_list, base_id, ItemType
from .Locations import location_list, CTLocation
from .Options import ClusterTruckOptions
from ..generic.Rules import set_rule


class ClusterTruckItem(Item):
    game = "ClusterTruck"

    def __init__(self, name: str, classification: ItemClassification, code: Optional[int], player: int) -> None:
        super().__init__(name, classification, code, player)

class ClusterTruckLocation(Location):
    game = "ClusterTruck"


class ClusterTruckWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "a guide to setting up ClusterTruck randomizer and connecting to an Archipelago Multiworld",
        "English",
        "en_setup.md",
        "setup/en",
        ["Nullctipus"]
    )]

class ClusterTruckWorld(World):
    """ClusterTruck is a new kind of platformer on-top of a speeding highway!"""

    game = "ClusterTruck"
    web = ClusterTruckWeb()

    item_name_to_id = {item.name:(base_id+index) for index,item in enumerate(item_list)}
    location_name_to_id = {loc.name: (base_id+index) for index,loc in enumerate(location_list)}

    item_name_groups = {
        "Abilities": {item.name for item in item_list if item.type == ItemType.Ability},
        "Levels": {item.name for item in item_list if item.type == ItemType.Level},
        "Traps": {item.name for item in item_list if item.type == ItemType.Trap},
        "Filler": {item.name for item in item_list if item.type == ItemType.Filler},
    }
    options_dataclass = ClusterTruckOptions
    options = ClusterTruckOptions

    item_type_classification : Dict[ItemType,ItemClassification] = {
        ItemType.Ability: ItemClassification.useful,
        ItemType.Level: ItemClassification.progression_skip_balancing,
        ItemType.Trap: ItemClassification.trap,
        ItemType.Filler: ItemClassification.filler,
    }
    skipped_level : List[int]
    all_selected_locations : List[CTLocation]
    start_level_name : str
    goal_level_name : str

    def generate_early(self) -> None:
        self.goal_level_name = f"{self.options.goal_level.value // 10 + 1}-{self.options.goal_level.value % 10 + 1}"
        self.start_level_name = f"{self.options.start_level.value // 10 + 1}-{self.options.start_level.value % 10 + 1}"
        self.skipped_level =  [(int(skip.split('-')[0])-1)*10+ int(skip.split('-')[1])-1
                               for skip in self.options.skipped_levels.value]
        self.all_selected_locations = [location for location in location_list if location
                                  and location.game_id not in self.skipped_level
                                    and location.game_id != self.options.goal_level.value]

    def get_filler_item_name(self) -> str:
        if self.random.random() <= self.options.trap_percentage.value:
            return self.random.choice([item.name for item in item_list if item.type == ItemType.Trap])
        return self.random.choice([item.name for item in item_list if item.type == ItemType.Filler])

    def create_item(self, name: str) -> "Item":
        location = item_list[self.item_name_to_id[name] - base_id]
        return ClusterTruckItem(name, self.item_type_classification[location.type],
                                self.item_name_to_id[name], self.player)

    def create_items(self) -> None:
        for location in self.all_selected_locations:
            if location.game_id > len(location_list):
                break
            try:
                if (location.game_id != self.options.start_level.value
                        and location.game_id != self.options.goal_level.value):
                    self.multiworld.itempool.append(self.create_item(location.name))
            except Exception as e:
                print(location.name)
                raise e

        victory: Location = self.get_location(self.goal_level_name)
        victory.place_locked_item(ClusterTruckItem("Victory",ItemClassification.progression_skip_balancing
                                                   ,None,self.player))

        # there needs to be one more item /shrug
        self.multiworld.itempool.append(self.create_item(self.get_filler_item_name()))

    def create_regions(self) -> None:
        menu_region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions += [menu_region]

        all_selected_locations_copy = self.all_selected_locations.copy()
        self.random.shuffle(all_selected_locations_copy)

        for location in all_selected_locations_copy:
            menu_region.locations.append(ClusterTruckLocation(
                self.player,location.name,base_id+location.game_id,menu_region))

        menu_region.locations.append(ClusterTruckLocation(self.player,self.goal_level_name,None,menu_region))

    def set_rules(self) -> None:
        for i in range(90):
            if i == self.options.start_level.value or i == self.options.goal_level.value or i in self.skipped_level:
                continue
            name = f"{i//10+1}-{i%10+1}"
            set_rule(self.get_location(name),lambda state, name=name: state.has(name, self.player))
        self.multiworld.completion_condition[self.player] = lambda state: state.has_from_list_unique(
            [item.name for item in item_list if item.type == ItemType.Level and item.name is not self.goal_level_name and
             item.name is not self.start_level_name and item.name not in self.options.skipped_levels.value],
            self.player,self.options.goal_requirement.value)

    def fill_slot_data(self) -> Mapping[str, Any]:
        slot_data : Mapping[str, Any] = {
            "version": "1.2.0",
            "start": self.start_level_name,
            "goal": self.goal_level_name,
            "goal_requirement": int(self.options.goal_requirement.value),
            "point_multiplier" : int(self.options.point_multiplier.value),
            "deathlink_amnesty" : int(self.options.deathlink_amnesty.value),
            "base_id": int(base_id),
        }
        return slot_data