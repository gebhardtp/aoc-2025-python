# --- Day 9: Movie Theater ---

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

def read_input(filepath):
    with open(filepath) as f:
        return f.read().splitlines()

def main():
    red_tiles = read_input('day_09/input.txt')
    result = part_01(red_tiles)
    if result: print(result)

if __name__ == '__main__':
    main()