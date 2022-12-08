import sys
import common

example = '''2199943210
3987894921
9856789892
8767896789
9899965678
'''

def get_adjacent(heightmap, coord):
    x, y = coord
    adjacent = [(x, y) for x, y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)] \
        if (x != -1) and (x < len(heightmap)) and (y != -1) and (y < len(heightmap[x]))]
    return adjacent

def build_basin(heightmap, coord):
    survey_points = [coord]
    points = []
    
    while (survey_points):
        for point in survey_points:
            x, y = point
            height = heightmap[x][y]
            if (height != 9):
                points.append(point)
                new_points = [x for x in get_adjacent(heightmap, point) \
                    if (x not in points) and (x not in survey_points)]
                survey_points.extend(new_points)
            survey_points.remove(point)
    
    return points

def main():
    data = [list(map(int, col)) for col in list(common.get_input('input_09.txt').splitlines())]
    #data = [list(map(int, col)) for col in list(example.splitlines())]
    
    heightmap = data
    lowest_points = []
    basins = []

    # Find low points
    for row in range(len(heightmap)):
        for col in range(len(heightmap[row])):
            adjacent_coords = get_adjacent(heightmap, (row, col))
            adjacent_heights = [heightmap[x][y] for x, y in adjacent_coords]
            if all([heightmap[row][col] < height for height in adjacent_heights]):
                lowest_points.append((row, col))

    # Find basins
    for point in lowest_points:
        basins.append(build_basin(heightmap, point))

    # Find basin sizes
    basin_sizes = [len(basin) for basin in basins]
    basin_sizes.sort(reverse=True)
    basin_total = basin_sizes[0] * basin_sizes[1] * basin_sizes[2]

    print('Part 1: {}'.format(sum([heightmap[x][y] + 1 for x, y in lowest_points])))
    print('Part 2: {}'.format(basin_total))
        
if __name__ == '__main__':
    sys.exit(main())