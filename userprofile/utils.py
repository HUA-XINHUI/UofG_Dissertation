LEVEL_REQUIREMENTS = [
    0,
    100,
    250,
    450,
    700,
]

def get_level(experience):
    for level, required_exp in reversed(
        list(enumerate(LEVEL_REQUIREMENTS, start=1))
    ):
        if experience >= required_exp:
            return level

def get_exp_to_next_level(experience):
    level = get_level(experience)
    return LEVEL_REQUIREMENTS[level]