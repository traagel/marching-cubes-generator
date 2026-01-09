from mpl_toolkits.mplot3d.art3d import Poly3DCollection

from data_models import Cube
from utils import visualize_single, visualize_all_grid

from utils import generate_settings, chain_to_triangles


def main():
    settings = generate_settings()
    # visualize(cube, midpoints, chains)
    # visualize_all_grid(settings)
    # all_chains_with_config = [(item[0], item[4]) for item in settings]
    # write_to_config(all_chains_with_config)

    cube_empty = Cube()
    midpoint_indices = {}
    for index, edge in enumerate(cube_empty.edges):
        midpoint = cube_empty.vertices[edge[0]].midpoint(
            cube_empty.vertices[edge[1]])
        midpoint_indices[(midpoint.x, midpoint.y, midpoint.z)] = index
    #
    # print(midpoint_indices)
    #
    for i, (config, cube, polygon, midpoints, chains) in enumerate(settings):
        for chain in chains:
            triangles = chain_to_triangles(chain)
            midpoint_indices_list = []
            for triangle in triangles:
                for point in triangle:
                    # print(point)
                    midpoint_indices_list.append(midpoint_indices[point])
            midpoint_indices_list.append(-1)
            # print(config, midpoint_indices_list)
        visualize_single(config, cube, midpoints, chains)


if __name__ == "__main__":
    main()
    # for x in range(10):
    #     print(str(bin(x))[2:])
