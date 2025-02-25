from typing import Dict, List, Any, Union, Optional, Mapping
from BaseClasses import Location, Item, Tutorial, ItemClassification, Region
from worlds.AutoWorld import World, WebWorld
from .Items import item_list, base_id, ItemType
from .Locations import location_list, CTLocation
from .Options import ClusterTruckOptions

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
    skipped_level : List[int] = []
    all_selected_locations : List[CTLocation] = []
    start_level_name : str
    goal_level_name : str

    def generate_early(self) -> None:
        self.goal_level_name = f"{self.options.goal_level.value // 10 + 1}-{self.options.goal_level.value % 10 + 1}"
        self.start_level_name = f"{self.options.start_level.value // 10 + 1}-{self.options.start_level.value % 10 + 1}"
        self.skipped_level =  [(int(skip.split('-')[-1])-1)*10+ int(skip.split('-')[1])-1 for skip in self.options.skipped_levels.value]
        self.all_selected_locations = [location for location in location_list if location
                                  and location.game_id not in self.skipped_level]

        if self.options.ace_rewards.value:
            self.all_selected_locations.extend([CTLocation(f"{i // 10 + 1}-{i % 10 + 1} Ace", len(location_list)+i) for i in range(90) if i not in self.skipped_level])

    def create_item(self, name: str) -> "Item":
        location = item_list[self.item_name_to_id[name] - base_id]
        return ClusterTruckItem(name, self.item_type_classification[location.type], self.item_name_to_id[name], self.player)

    def create_items(self) -> None:
        for location in self.all_selected_locations:
            if location.game_id > len(location_list):
                break # make sure no ace levels get added for fun
            try:
                if location.game_id != self.options.start_level.value:
                    self.multiworld.itempool.append(self.create_item(location.name))
            except Exception as e:
                print(location.name)
                raise e
        trap = list(self.item_name_groups["Traps"])
        filler = list(self.item_name_groups["Filler"])
        if self.options.ace_rewards.value:
            for i in range(90):
                if i not in self.skipped_level and not self.options.goal_level.value:
                    if self.random.random() <= self.options.trap_percent/100:
                        self.multiworld.itempool.append(self.create_item(self.random.choice(trap)))
                    else:
                        self.multiworld.itempool.append(self.create_item(self.random.choice(filler)))

    def create_regions(self) -> None:
        menu_region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions += [menu_region]

        all_selected_locations_copy = self.all_selected_locations.copy()
        self.random.shuffle(all_selected_locations_copy)

        menu_region.locations.append(ClusterTruckLocation(self.player,self.start_level_name,base_id + self.options.start_level.value,menu_region))

        for location in all_selected_locations_copy:
            menu_region.locations.append(ClusterTruckLocation(self.player,location.name,base_id+location.game_id,menu_region))


    def set_rules(self) -> None:
        victory: Location = self.get_location(self.goal_level_name)
        victory.place_locked_item(ClusterTruckItem("Victory",ItemClassification.progression_skip_balancing,None,self.player))
        self.multiworld.completion_condition[self.player] = lambda state: \
            state.has("Victory",self.player)

    def fill_slot_data(self) -> Mapping[str, Any]:
        slot_data : Mapping[str, Any] = {
            "version": "0.0.0",
            "start": self.start_level_name,
            "goal": self.goal_level_name,
            "ace_reward": bool(self.options.ace_rewards.value),
            "base_id": int(base_id),
        }
        return slot_data