import sys
import common

example = '''5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
'''
def get_adjacent(heightmap, coord):
    x, y = coord
    adjacent = [(x, y) for x, y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1), (x - 1, y - 1), (x - 1, y + 1), (x + 1, y - 1), (x + 1, y + 1)] \
        if (x != -1) and (x < len(heightmap)) and (y != -1) and (y < len(heightmap[x]))]
    return adjacent

def main():
    data = [list(map(int, col)) for col in list(common.get_input('input_11.txt').splitlines())]
    #data = [list(map(int, col)) for col in list(example.splitlines())]

    dumbo = data
    flashes = 0
    num_flashes_this_time = 0
    c = 0

    while(num_flashes_this_time != (len(dumbo) * len(dumbo[0]))):
        num_flashes_this_time = 0
        # Printing for debugging
        # Mixing str and int because when I print X is easier to visualize than -1 or 10
        print('After step {}:'.format(c))
        for x in range(len(dumbo)):
            for y in range(len(dumbo[x])):
                print(dumbo[x][y], end = '')
            print()
        print()

        # Increment the energy
        for x in range(len(dumbo)):
            for y in range(len(dumbo[x])):
                flash_points = [(x, y)]
                while (flash_points):
                    for point in flash_points:
                        i, j = point
                        if (dumbo[i][j] != 'X'):
                            dumbo[i][j] += 1
                        if (dumbo[i][j] != 'X' and dumbo[i][j] > 9):
                            dumbo[i][j] = 'X'
                            flash_points.extend(get_adjacent(dumbo, (i,j)))
                        flash_points.remove(point)
        
        # FLASH IT UP
        for x in range(len(dumbo)):
            for y in range(len(dumbo[x])):
                if dumbo[x][y] == 'X':
                    flashes += 1
                    num_flashes_this_time += 1
                    dumbo[x][y] = 0

        c += 1

    print('Part 1: {}'.format(flashes))
    print('Part 2: {}'.format(c))
        
if __name__ == '__main__':
    sys.exit(main())