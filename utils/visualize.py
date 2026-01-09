import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from .cube_solver import chain_to_triangles


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


def visualize_single(config, cube, midpoints, chains):
    print(f"Visualizing config: {config}")
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    # Draw cube edges
    for edge in cube.edges:
        v0, v1 = cube.vertices[edge[0]], cube.vertices[edge[1]]
        ax.plot([v0.x, v1.x], [v0.y, v1.y], [v0.z, v1.z], "b-", alpha=0.3)

    # Draw vertices (active in red)
    for v in cube.vertices:
        color = "red" if v.value == 1 else "blue"
        ax.scatter(v.x, v.y, v.z, c=color, s=50)

    # Draw midpoints
    for m in midpoints:
        ax.scatter(m.x, m.y, m.z, c="green", s=100, marker="^")

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
                )
                ax.text(
                    pts[0].x,
                    pts[0].y,
                    pts[0].z,
                    f"{edge_index}",
                    fontsize=8,
                    color="red",
                )
    # Draw triangles
    for index, chain in enumerate(chains):
        triangles = chain_to_triangles(chain)
        ax.add_collection(Poly3DCollection(triangles)).set_alpha(0.3)

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
            triangles = chain_to_triangles(chain)
            ax.add_collection(Poly3DCollection(triangles)).set_alpha(0.3)

        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_zlim(0, 1)
        ax.set_title(f"{config}: {str(bin(config))[2:].zfill(8)}", fontsize=6)
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        ax.grid(True)
    # plt.tight_layout()
    # plt.show()
    plt.tight_layout()
    plt.savefig("output/all_cube_configurations.png",
                dpi=300, bbox_inches="tight")
    plt.close()
    print("All configurations saved to all_cube_configurations.png")
