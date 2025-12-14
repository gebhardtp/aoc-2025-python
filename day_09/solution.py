# --- Day 9: Movie Theater ---

import ast
from shapely.geometry import Polygon, box

def part_01(red_tiles):
    largest_area = float('-inf')

    for tile_a in red_tiles:
        for tile_b in red_tiles:
            if tile_a == tile_b:
                continue
            area = get_rectangle_area(tile_a, tile_b)
            if area > largest_area:
                largest_area = area

    return largest_area

def get_rectangle_area(tile_a, tile_b):
    corner_a = tile_a.split(',')
    corner_b = tile_b.split(',')
    side_a = abs(int(corner_a[0]) - int(corner_b[0])) + 1
    side_b = abs(int(corner_a[1]) - int(corner_b[1])) + 1
    return side_a * side_b

def part_02(red_tiles):
    largest_area = float('-inf')
    points = [ast.literal_eval(point) for point in red_tiles]
    main_polygon = Polygon(points)

    for point_a in points:
        for point_b in points:
            if point_a == point_b:
                continue
            width = abs(point_a[0] - point_b[0]) + 1
            height = abs(point_a[1] - point_b[1]) + 1
            area = width * height
            
            if area > largest_area:
                min_x = min(point_a[0], point_b[0])
                max_x = max(point_a[0], point_b[0])
                min_y = min(point_a[1], point_b[1])
                max_y = max(point_a[1], point_b[1])
                rectangle = box(min_x, min_y, max_x, max_y)
                if main_polygon.covers(rectangle):
                    largest_area = area

    return largest_area

def read_input(filepath):
    with open(filepath) as f:
        return f.read().splitlines()

def main():
    red_tiles = read_input('day_09/input.txt')
    # if result := part_01(red_tiles): print(result)
    if result := part_02(red_tiles): print(result)
    

if __name__ == '__main__':
    main()