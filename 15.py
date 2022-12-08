import sys
import heapq
import common

example_1 = '''1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
'''

def parse_input(input):
    return [list(map(int, col)) for col in input.splitlines()]

def get_adjacent(matrix, coord):
    x, y = coord
    # Just going to try and assume that the fastest way to the end is a
    # straight line (diagonal), because doubling back would cost at least
    # 4 more moves (and could always be tackled from a point from above).
    # This would require a pregenerated path 
    # This means only connect the down and right edge nodes in the graph.
    adjacent = [(x, y) for x, y in [(x + 1, y), (x, y + 1)] \
        if (x < len(matrix)) and (y < len(matrix[x]))]
    return adjacent

def calculate_risk(path):
    
    return sum(path)

def find_path(cavern):
    
    graph = []
    for x in range(len(input)):
        for y in range(len(input[x])):
            risk = input[x][y]
    return([1,2,3])

# Apparently wikipedia says the best run time complexity is when this is
# implemented with a heap min-priority queue. So do this with a heapq.
def dijkstras(matrix):
    unvisited = []

def main():
    test_data = parse_input(example_1)

    graph = build_graph(test_data)
    path = find_path(graph)
    assert(calculate_risk(path) == 40)

    data = parse_input(common.get_input('input_15.txt'))
    graph = build_graph(data)
    path = find_path(graph)
    print('Part 1: {}'.format(calculate_risk(path)))
    print('Part 2: {}'.format(0))
        
if __name__ == '__main__':
    sys.exit(main())