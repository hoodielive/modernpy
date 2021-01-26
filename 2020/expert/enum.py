from enum import Enum, Flag, auto

class Weekday(Enum):
    Sunday = 6
    Monday = 0
    Tuesday = 1
    Wednesday = 2
    Thursday = 3
    Friday = 4
    Saturday = 5

class OrderStatus(Enum):
    PENDING = auto()
    PROCESSING = auto()
    PROCESSED = auto()

class Order:
    def __init__(self):
        self.status = OrderStatus.PENDING

    def process(self):
        if self.status == OrderStatus.PENDING:
            raise RuntimeError(
                "Can't processor order that has "
                "been already processed."
            )
        self.status = OrderStatus.PROCESSING
        self.status = OrderStatus.PROCESSED

class Side(Flag):
    GUACAMOLE = auto()
    TORTILLA = auto()
    FRIES = auto()
    BEER = auto()
    POTATO_SALAD = auto()

mexican_sides = Side.GUACAMOLE | Side.BEER | Side.TORTILLA
bavarian_sides = Side.BEER | Side.POTATO_SALAD
common_sides = mexican_sides & bavarian_sides
print(Side.GUACAMOLE in mexican_sides)
print(Side.TORTILLA in bavarian_sides)
print(common_sides)
