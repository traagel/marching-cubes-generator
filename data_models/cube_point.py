class CubePoint:
    def __init__(self, x, y, z, value=0) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.value = value
        self.name = ""

    def midpoint(self, other):
        return CubePoint(
            (self.x + other.x) / 2,
            (self.y + other.y) / 2,
            (self.z + other.z) / 2,
        )

    def distance_euc(self, other):
        return (
            (self.x - other.x) ** 2 + (self.y -
                                       other.y) ** 2 + (self.z - other.z) ** 2
        ) ** (0.5)

    def __str__(self) -> str:
        return str(((self.x, self.y, self.z), self.value))

    def __repr__(self) -> str:
        return str(((self.x, self.y, self.z), self.value))

    def __eq__(self, other):
        if not isinstance(other, CubePoint):
            return False
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def __hash__(self):
        return hash((self.x, self.y, self.z))
