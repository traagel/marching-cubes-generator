from data_models import CubePoint, Cube

import string


def check_midpoint(vertex_a: CubePoint, vertex_b: CubePoint):
    if vertex_a.value != vertex_b.value:
        midpoint = vertex_a.midpoint(vertex_b)
        print(f"Active midpoint found: {midpoint}")
        midpoint.value = 1
        return midpoint


def solve_cube(cube):
    midpoints = set()

    polygon = []

    for face_index, face in enumerate(cube.faces):
        print(f"Face: {cube.face_indices[face_index]}")
        face_midpoints = set()
        active_points = set()
        for edge in face:
            edge_start = cube.vertices[edge[0]]
            edge_end = cube.vertices[edge[1]]
            print(f"Edge between {edge_start, edge_end}")
            active_midpoint = check_midpoint(edge_start, edge_end)
            if active_midpoint:
                face_midpoints.add(active_midpoint)
                midpoints.add(active_midpoint)
                for point in [edge_start, edge_end]:
                    if point.value == 1:
                        active_points.add(point)
        midpoint_count = len(face_midpoints)
        if midpoint_count > 1:
            print("\nMidpoints:")
            print(f"Face midpoints: {face_midpoints}")
            if midpoint_count == 2:
                print(f"Connect midpoints {face_midpoints}")
                polygon.append(face_midpoints)
            if midpoint_count == 4:
                print(f"Active points: {active_points}")
                print(f"Distances:")
                for active_point in active_points:
                    diagonal_edges = set()
                    for face_midpoint in face_midpoints:
                        print(f"Dist ({active_point}), ({face_midpoint})")
                        dist = active_point.distance_euc(face_midpoint)
                        print(dist)
                        if dist == 0.5:
                            diagonal_edges.add(face_midpoint)
                    if len(diagonal_edges) > 1:
                        polygon.append(diagonal_edges)

            print("\n")
    return polygon, midpoints


def generate_settings():
    settings = []

    for config in range(0, 256):
        cube = Cube()
        bits = str(bin(config))[2:].zfill(8)[
            ::-1
        ]  # Reverse to match LSB->MSB convention
        for i, bit in enumerate(bits):
            cube.vertices[i].value = int(bit)
        polygon, midpoints = solve_cube(cube)
        map_pairs_to_letters(polygon)
        chains = find_closed_loops(polygon)
        settings.append((config, cube, polygon, midpoints, chains))
    return settings


def map_pairs_to_letters(polygon):
    letters = list(string.ascii_uppercase)
    index = 0
    mapping = {}
    for pair in polygon:
        pair = list(pair)
        for el in pair:
            if el not in mapping:
                mapping[el] = letters[index]
                index += 1

    return mapping


def write_to_config(chains):
    for config, chain in chains:
        print(config, chain)


def print_list_pairs(polygon_list_pairs):
    for pair in polygon_list_pairs:
        print_pair_names(pair)


def print_pair_names(pair):
    print(f"Pair:{pair[0].name} -> {pair[1].name}")


def find_closed_loops(polygon):
    print("Finding closed loops:")
    polygon_list_pairs = []
    chains = []
    mapping = map_pairs_to_letters(polygon)
    for pair in polygon:
        pair = list(pair)
        polygon_list_pairs.append(pair)
        for el in pair:
            el.name = mapping[el]

    chains = []
    while True:
        print(f"Chain {len(chains)}")
        chain = find_chain(polygon_list_pairs, chains)
        if chain is None:
            break
        else:
            chains.append(chain)
    print(f"Final chains: {chains}")
    print(f"Chain count {len(chains)}")
    for chain in chains:
        for pair in chain:
            print(f"DEBUG Pair:")
            print(pair)
            print(pair[0].name, pair[1].name)
        print(f"Chain length: {len(chain)}")
    return chains


def find_chain(polygon_list_pairs, chains):
    if len(polygon_list_pairs) == 0:
        return None

    print(f"Elements in polygon {len(polygon_list_pairs)}")
    first_pair = polygon_list_pairs.pop(0)
    print("First pair:")
    print_pair_names(first_pair)

    chain = [first_pair]
    current_end = first_pair[1]  # Track current chain endpoint

    # Build chain forward from endpoint
    while True:
        found = False
        for idx, pair in enumerate(polygon_list_pairs):
            # Check if pair connects to current endpoint
            if pair[0] == current_end:
                chain.append(pair)
                current_end = pair[1]
                polygon_list_pairs.pop(idx)
                found = True
                break
            elif pair[1] == current_end:
                # Reverse pair to maintain direction
                chain.append([pair[1], pair[0]])
                current_end = pair[0]
                polygon_list_pairs.pop(idx)
                found = True
                break

        if not found:
            break

    print(f"Built chain with {len(chain)} edges")
    return chain


def chain_to_triangles(chain, cube=None):
    vertex_list = chain_to_vertex_list(chain)
    triangles = triangulate_vertex_list(vertex_list, cube)
    triangles_3 = []
    for triangle in triangles:
        triangle_3 = []
        for point in triangle:
            triangle_3.append((point.x, point.y, point.z))
        triangles_3.append(triangle_3)

    return triangles_3


def chain_to_vertex_list(chain):
    if not chain:
        return []

    ordered = [chain[0][0], chain[0][1]]

    for pair in chain[1:]:
        if pair[0] not in ordered:
            ordered.append(pair[0])
        if pair[1] not in ordered:
            ordered.append(pair[1])
    return ordered


def triangulate_vertex_list(vertex_list, cube=None):
    triangles = []
    for i in range(1, len(vertex_list) - 1):
        p0, p1, p2 = vertex_list[0], vertex_list[i], vertex_list[i + 1]
        
        # If cube is provided, check winding order
        if cube is not None:
            # Calculate triangle centroid
            centroid_x = (p0.x + p1.x + p2.x) / 3
            centroid_y = (p0.y + p1.y + p2.y) / 3
            centroid_z = (p0.z + p1.z + p2.z) / 3
            
            # Find closest active vertex
            closest_active = None
            min_dist = float('inf')
            for vertex in cube.vertices:
                if vertex.value == 1:  # Active vertex
                    dist = ((vertex.x - centroid_x)**2 + 
                           (vertex.y - centroid_y)**2 + 
                           (vertex.z - centroid_z)**2)**0.5
                    if dist < min_dist:
                        min_dist = dist
                        closest_active = vertex
            
            if closest_active:
                # Calculate current normal (p1-p0) × (p2-p0)
                v1 = CubePoint(p1.x - p0.x, p1.y - p0.y, p1.z - p0.z)
                v2 = CubePoint(p2.x - p0.x, p2.y - p0.y, p2.z - p0.z)
                normal = CubePoint(
                    v1.y * v2.z - v1.z * v2.y,
                    v1.z * v2.x - v1.x * v2.z,
                    v1.x * v2.y - v1.y * v2.x
                )
                
                # Vector from centroid to closest active vertex
                to_active = CubePoint(
                    closest_active.x - centroid_x,
                    closest_active.y - centroid_y,
                    closest_active.z - centroid_z
                )
                
                # Dot product: if positive, normal points toward active vertex
                dot_product = normal.x * to_active.x + normal.y * to_active.y + normal.z * to_active.z
                
                # If pointing toward active vertex, flip triangle order
                if dot_product > 0:
                    triangles.append((p0, p2, p1))  # Flipped
                else:
                    triangles.append((p0, p1, p2))  # Normal order
            else:
                triangles.append((p0, p1, p2))  # No active vertices, use normal order
        else:
            triangles.append((p0, p1, p2))  # No cube provided, use normal order
    
    return triangles
