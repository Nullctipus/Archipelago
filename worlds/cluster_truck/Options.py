import random
from dataclasses import dataclass
from Options import Choice, Range, OptionSet, Toggle, PerGameCommonOptions, T

class CTLevelChoice(Choice):
    randomized: bool
    option_1_1 = 0
    option_1_2 = 1
    option_1_3 = 2
    option_1_4 = 3
    option_1_5 = 4
    option_1_6 = 5
    option_1_7 = 6
    option_1_8 = 7
    option_1_9 = 8
    option_1_10 = 9
    option_2_1 = 10
    option_2_2 = 11
    option_2_3 = 12
    option_2_4 = 13
    option_2_5 = 14
    option_2_6 = 15
    option_2_7 = 16
    option_2_8 = 17
    option_2_9 = 18
    option_2_10 = 19
    option_3_1 = 20
    option_3_2 = 21
    option_3_3 = 22
    option_3_4 = 23
    option_3_5 = 24
    option_3_6 = 25
    option_3_7 = 26
    option_3_8 = 27
    option_3_9 = 28
    option_3_10 = 29
    option_4_1 = 30
    option_4_2 = 31
    option_4_3 = 32
    option_4_4 = 33
    option_4_5 = 34
    option_4_6 = 35
    option_4_7 = 36
    option_4_8 = 37
    option_4_9 = 38
    option_4_10 = 39
    option_5_1 = 40
    option_5_2 = 41
    option_5_3 = 42
    option_5_4 = 43
    option_5_5 = 44
    option_5_6 = 45
    option_5_7 = 46
    option_5_8 = 47
    option_5_9 = 48
    option_5_10 = 49
    option_6_1 = 50
    option_6_2 = 51
    option_6_3 = 52
    option_6_4 = 53
    option_6_5 = 54
    option_6_6 = 55
    option_6_7 = 56
    option_6_8 = 57
    option_6_9 = 58
    option_6_10 = 59
    option_7_1 = 60
    option_7_2 = 61
    option_7_3 = 62
    option_7_4 = 63
    option_7_5 = 64
    option_7_6 = 65
    option_7_7 = 66
    option_7_8 = 67
    option_7_9 = 68
    option_7_10 = 69
    option_8_1 = 70
    option_8_2 = 71
    option_8_3 = 72
    option_8_4 = 73
    option_8_5 = 74
    option_8_6 = 75
    option_8_7 = 76
    option_8_8 = 77
    option_8_9 = 78
    option_8_10 = 79
    option_9_1 = 80
    option_9_2 = 81
    option_9_3 = 82
    option_9_4 = 83
    option_9_5 = 84
    option_9_6 = 85
    option_9_7 = 86
    option_9_8 = 87
    option_9_9 = 88
    option_9_10 = 89
    def __init__(self, value: int, randomized: bool = False):
        super().__init__(value)
        self.randomized = randomized

    @classmethod
    def get_option_name(cls, value: T) -> str:
        return cls.name_lookup[value].replace('_', '-')

    @classmethod
    def from_text(cls, text: str) -> Choice:
        text = text.lower()
        if text == "random":
            return cls(random.choice(list(cls.name_lookup)),True)
        for value, option_name in cls.name_lookup.items():
            if option_name == text:
                return cls(value)
        raise KeyError(
            f"Could not find option \"{text}\" for \"{cls.__name__}\", "
            f'known option are {", ".join(f"{option}" for option in cls.name_lookup.values())}'
        )

class StartLevel(CTLevelChoice):
    """Choose the level to start in"""
    display_name = "Start Level"
    default = 0

class GoalLevel(CTLevelChoice):
    """Choose level to complete to finish the game"""
    display_name = "Goal Level"
    default = 89

class GoalRequirement(Range):
    """Choose the number of levels required to unlock the goal"""
    display_name = "Goal Requirement"
    range_start = 5
    range_end = 70
    default = 40

class SkipLevels(OptionSet):
    """List as many levels as you would like to skip completing"""
    display_name = "Skipped Levels"
    valid_keys = {f"{i//10+1}-{i%10+1}" for i in range(90)}
    default = {}


@dataclass
class ClusterTruckOptions(PerGameCommonOptions):
    start_level: StartLevel
    goal_level: GoalLevel
    goal_requirement: GoalRequirement
    skipped_levels: SkipLevels
