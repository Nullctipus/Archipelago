
def format_level_name(level: int) -> str:
    if level <= 89:
        return f"{level // 10 + 1}-{level % 10 + 1}"
    elif level <= 99:
        return f"h-{level % 10 + 1}"
    elif level <= 104:
        return f"c-{level % 10 + 1}"
    else:
        raise ValueError(f"Level {level} not supported")


def parse_level_name(level_name: str) -> int:
    s = level_name.split('-')
    if s[0][0] == 'h':
        return 89 + int(s[1])
    elif s[0][0] == 'c':
        return 99 + int(s[1])
    else:
        return (int(s[0]) - 1) * 10 + int(s[1]) - 1
