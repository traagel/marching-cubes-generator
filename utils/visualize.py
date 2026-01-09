import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from .cube_solver import chain_to_triangles
import string


class Vec3:
    def __init__(self, point):
        self.x = point[0]
        self.y = point[1]
        self.z = point[2]

    def add(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Vec3((x, y, z))

    def subtract(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return Vec3((x, y, z))

    def divide_scalar(self, scalar):
        return Vec3((self.x / scalar, self.y / scalar, self.z / scalar))

    def cross(self, other):
        x = self.y * other.z - self.z * other.y
        y = self.z * other.x - self.x * other.z
        z = self.x * other.y - self.y * other.x
        return Vec3((x, y, z))

    def mid(self, other):
        x = self.add(other).x
        y = self.add(other).y
        z = self.add(other).z
        return Vec3((x / 2, y / 2, z / 2))

    def len(self):
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5


def color_map(i):
    colormap = {
        0: "k",
        1: "b",
        2: "g",
        3: "r",
        4: "c",
        5: "m",
        6: "y",
    }

    return colormap[i]


def find_midpoint(v0, v1):
    return ((v0.x + v1.x) / 2, (v0.y + v1.y) / 2, (v0.z + v1.z) / 2)


def visualize_single(config, cube, midpoints, chains):
    print(f"Visualizing config: {config}")
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    letter_map = list(string.ascii_uppercase)

    # Draw cube edges
    for i, edge in enumerate(cube.edges):
        v0, v1 = cube.vertices[edge[0]], cube.vertices[edge[1]]
        ax.plot([v0.x, v1.x], [v0.y, v1.y], [v0.z, v1.z], "b-", alpha=0.3)
        (x, y, z) = find_midpoint(v0, v1)
        ax.text(x, y, z, i)

    # Draw vertices (active in red)
    for i, v in enumerate(cube.vertices):
        color = "red" if v.value == 1 else "blue"
        ax.scatter(v.x, v.y, v.z, c=color, s=50)
        ax.text(v.x + 0.05, v.y + 0.05, v.z, letter_map[i], c=color)

    # Draw midpoints
    for m in midpoints:
        ax.scatter(m.x, m.y, m.z, c="green", s=20, marker="^")

    # Draw triangles
    for index, chain in enumerate(chains):
        triangles = chain_to_triangles(chain, cube)
        for triangle in triangles:
            p0, p1, p2 = triangle[0], triangle[1], triangle[2]
            p0 = Vec3(p0)
            p1 = Vec3(p1)
            p2 = Vec3(p2)

            ax.plot([p0.x, p1.x], [p0.y, p1.y], [p0.z, p1.z], c="gray")
            ax.plot([p1.x, p2.x], [p1.y, p2.y], [p1.z, p2.z], c="gray")
            ax.plot([p2.x, p0.x], [p2.y, p0.y], [p2.z, p0.z], c="gray")

            mid = p0.add(p1).add(p2).divide_scalar(3)
            dir = p1.subtract(p0).cross(p2.subtract(p0))

            norm = dir.divide_scalar(dir.len()).divide_scalar(3)
            ax.scatter(mid.x, mid.y, mid.z, c="green", s=50)
            ax.quiver(
                mid.x,
                mid.y,
                mid.z,  # Arrow start point
                norm.x,
                norm.y,
                norm.z,  # Arrow direction vector
                color="g",
                linewidth=2,
                arrow_length_ratio=0.3,  # Arrow head size relative to length
            )

        ax.add_collection(Poly3DCollection(triangles)).set_alpha(0.3)

    # Draw polygon edges
    for index, chain in enumerate(chains):
        for edge_index, edge_list in enumerate(chain):
            pts = edge_list
            if len(pts) == 2:
                ax.plot(
                    [pts[0].x, pts[1].x],
                    [pts[0].y, pts[1].y],
                    [pts[0].z, pts[1].z],
                    f"{color_map(index)}-",
                    linewidth=2,
                    zorder=50,
                )
                ax.text(
                    pts[0].x - 0.05,
                    pts[0].y - 0.05,
                    pts[0].z - 0.05,
                    f"{edge_index}",
                    fontsize=8,
                    color="red",
                    zorder=100,
                )
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    # plt.show()
    plt.savefig(
        f"output/configuration{config}.png", dpi=300, bbox_inches="tight")


def visualize_all_grid(settings):
    fig = plt.figure(figsize=(32, 32))

    for i, (config, cube, polygon, midpoints, chains) in enumerate(settings):
        ax = fig.add_subplot(16, 16, i + 1, projection="3d")

        for edge in cube.edges:
            v0, v1 = cube.vertices[edge[0]], cube.vertices[edge[1]]
            ax.plot([v0.x, v1.x], [v0.y, v1.y], [v0.z, v1.z], "b-", alpha=0.3)

        for v in cube.vertices:
            color = "red" if v.value == 1 else "blue"
            ax.scatter(v.x, v.y, v.z, c=color, s=50)

        for m in midpoints:
            ax.scatter(m.x, m.y, m.z, c="green", s=100, marker="^")

        for index, chain in enumerate(chains):
            for edge_index, edge_list in enumerate(chain):
                pts = edge_list
                if len(pts) == 2:
                    ax.plot(
                        [pts[0].x, pts[1].x],
                        [pts[0].y, pts[1].y],
                        [pts[0].z, pts[1].z],
                        f"{color_map(index)}-",
                        linewidth=2,
                    )
                    ax.text(
                        pts[0].x,
                        pts[0].y,
                        pts[0].z,
                        f"{edge_index}",
                        fontsize=8,
                        color="red",
                    )
        for index, chain in enumerate(chains):
            triangles = chain_to_triangles(chain, cube)
            
            # Draw triangles with normals
            for triangle in triangles:
                p0, p1, p2 = triangle[0], triangle[1], triangle[2]
                p0 = Vec3(p0)
                p1 = Vec3(p1)
                p2 = Vec3(p2)

                # Calculate centroid and normal
                mid = p0.add(p1).add(p2).divide_scalar(3)
                dir = p1.subtract(p0).cross(p2.subtract(p0))
                
                # Only draw normal if triangle has area (avoid division by zero)
                if dir.len() > 1e-6:
                    norm = dir.divide_scalar(dir.len()).divide_scalar(5)  # Scale down for grid view
                    ax.quiver(
                        mid.x, mid.y, mid.z,
                        norm.x, norm.y, norm.z,
                        color="red",
                        alpha=0.7,
                        arrow_length_ratio=0.5
                    )
            
            ax.add_collection(Poly3DCollection(triangles)).set_alpha(0.3)

        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_zlim(0, 1)
        ax.set_title(f"{config}: {str(bin(config))[2:].zfill(8)}", fontsize=6)
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        ax.grid(True)

    plt.tight_layout()
    plt.savefig("output/all_cube_configurations.png",
                dpi=300, bbox_inches="tight")
    plt.close()
    print("All configurations saved to all_cube_configurations.png")
