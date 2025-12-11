# --- Day 8: Playground ---

import math
import ast

def part_01(points_str_list):
    points = [ast.literal_eval(point) for point in points_str_list]
    circuits = []
    distance = calculate_distances(points)

    distance_list = sorted(distance.items(), key=lambda x: x[1])
    pair_list = [pair_and_distance[0] for pair_and_distance in distance_list[:1000]]
    
    for pair in pair_list:
        found_indices = []
        for i, circuit in enumerate(circuits):
            if pair[0] in circuit or pair[1] in circuit:
                found_indices.append(i)
        
        if not found_indices:
            circuits.append(set(pair))
        elif len(found_indices) == 1:
            circuits[found_indices[0]].update(pair)
        else:
            idx_keep = found_indices[0]
            idx_remove = found_indices[1]
            circuits[idx_keep].update(circuits[idx_remove])
            circuits.pop(idx_remove)
    
    circuits.sort(reverse=True, key=lambda circuit: len(circuit))

    sizes = [len(c) for c in circuits]
    while len(sizes) < 3:
        sizes.append(1)

    return sizes[0] * sizes[1] * sizes[2]

def calculate_distances(points):
    distance = {}
    for point_a in points:
        for point_b in points:
            if point_a == point_b:
                continue
            distance_key = tuple(sorted((point_a, point_b)))
            if distance_key not in distance:
                distance[distance_key] = math.dist(point_a, point_b)
    return distance

def read_input(filepath):
    with open(filepath) as f:
        return f.read().splitlines()

def main():
    junctions_coordinates = read_input("day_08/input.txt")
    print(part_01(junctions_coordinates))

if __name__ == "__main__":
    main()