from dataclasses import dataclass
from Options import PerGameCommonOptions, OptionSet, Toggle, Range

class StartingCheckpoint(Range):
    """
    Choose where you want to start. 21 is right after the tutorial location
    """
    display_name = "Starting Checkpoint"
    range_start = 0
    range_end = 58
    default = 21

class ShowMissingLocationsOnMap(Toggle):
    """
    Choose if you want to show missing locations on the map.
    Recommended to leave on
    """
    display_name = "Show Missing Locations"
    default = True

class AutoEnableModifiers(Range):
    """
    Choose if you want to automatically enable modifiers when received.
    """
    display_name = "Auto Enable Modifiers"
    default = 5
    range_start = 0
    range_end = 10

class DisabledModifierList(OptionSet):
    """
    list as many modifiers you don't want to be enabled when received.
    Please add 'Extreme Rotation' to the list if you don't have your vlegs yet.
    """
    valid_keys = {
        'Extreme Rotation',
        'Slowmo Hookshots',
        'Mars Gravity',
        'Falling Up',
        'Jets Only',
        'Upsidedown World',
        'Jupiter Gravity',
        'Hookshots Only',
        'Sideways World',
        'Sun Gravity',
        'Super Explosions',
        'Zero Gravity',
        'Too Much Jets',
        'Moon Gravity',
        'Infinite Jets',
        'Super Hookshots',
        'Random World Rot On Respawn',
        'TenX Speed',
        'Backwards Jets',
        'Stretchy Hookshots',
        'Hookshots Are Stilts',
        'Bouncy Ground',
        'Ground Is Lava',
        'Gun Only',
        'Gun Always Charged',
        'Gun Rapid Fire',
        'Night Sky',
        'Pitch Black',
        'Foggy',
        'Death On Hard Impact',
        'Palm Jets',
        'Delicate Player',
        'Super Wormy',
    }
    default = ['Falling Up', 'Upsidedown World', 'Gun Only', 'Ground Is Lava', 'TenX Speed']

@dataclass
class JetIslandOptions(PerGameCommonOptions):
    starting_checkpoint : StartingCheckpoint
    show_missing_locations_on_map : ShowMissingLocationsOnMap
    auto_enable_modifiers : AutoEnableModifiers
    dont_auto_use_modifiers : DisabledModifierList