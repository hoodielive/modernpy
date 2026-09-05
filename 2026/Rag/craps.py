import random 

def die() -> int:
    return random.randint(1, 6)

def craps() -> tuple[int, int]:
    return (die(), die())

def zonk() -> tuple[int, ...]:
    return tuple(die() for x in range(6))
