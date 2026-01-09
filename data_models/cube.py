from . import CubePoint


class Cube:
    def __init__(self):
        self.vertices = [
            CubePoint(0, 0, 0),
            CubePoint(1, 0, 0),
            CubePoint(1, 1, 0),
            CubePoint(0, 1, 0),
            CubePoint(0, 0, 1),
            CubePoint(1, 0, 1),
            CubePoint(1, 1, 1),
            CubePoint(0, 1, 1),
        ]
        self.edges = [
            # bottom
            (0, 1),
            (1, 2),
            (2, 3),
            (0, 3),
            # top
            (4, 5),
            (5, 6),
            (6, 7),
            (4, 7),
            # sides
            (0, 4),
            (1, 5),
            (2, 6),
            (3, 7),
        ]

        self.faces = [
            # Z=0
            # [0, 1, 2, 3],
            [(0, 1), (1, 2), (2, 3), (3, 0)],
            # Z=1
            # [4, 5, 6, 7],
            [(4, 5), (5, 6), (6, 7), (7, 4)],
            # X=0
            # [0, 3, 4, 7],
            [(0, 3), (3, 7), (7, 4), (4, 0)],
            # X=1
            # [1, 2, 5, 6],
            [(1, 2), (2, 6), (6, 5), (5, 1)],
            # Y=0
            # [0, 1, 4, 5],
            [(0, 1), (1, 5), (5, 4), (4, 0)],
            # Y=1 [2, 3, 7, 6],
            [(3, 2), (2, 6), (6, 7), (7, 3)],
        ]

        self.face_indices = {
            0: "Z=0",
            1: "Z=1",
            2: "X=0",
            3: "X=1",
            4: "Y=0",
            5: "Y=1",
        }

        self.active_midpoints = set()
