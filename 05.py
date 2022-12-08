import sys
import common

example = '''0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
'''

def is_diagonal(x1, y1, x2, y2) -> bool:
    if (x1 != x2) and (y1 != y2):
        return True
    else:
        return False

def draw(diagram, x1, y1, x2, y2):   
    if (y2 == y1):
        # Horizontal
        if (x2 > x1):
            for x in range(x1, x2 + 1):
                diagram[x][y1] += 1
        if (x1 > x2):
            for x in range(x2, x1 + 1):
                diagram[x][y1] += 1
    elif (x2 == x1):
        # Vertical
        if (y2 > y1):
            for y in range(y1, y2 + 1):
                diagram[x1][y] += 1
        if (y1 > y2):
            for y in range(y2, y1 + 1):
                diagram[x1][y] += 1
    else:
        # Diagonal
        # For sample data all X and Y distances are equal,
        # so we don't have to deal with floats
            # Testing if sample set has even X and Y distances
            #if (abs(x2-x1) != abs(y2-y1)):
            #    print('OH NOOOOOO WHAT IS HAPPENING, FLOATS ARE COMING!!!')
        
        # Confirmed the sample set X distance == Y distance
        if (x2 > x1):
            for i in range(x1, x2 + 1):
                if (y2 > y1):
                    y = y1 + (i - x1)
                    x = x1 + (i - x1)
                if (y2 < y1):
                    y = y1 - (i - x1)
                    x = x1 + (i - x1)
                diagram[x][y] += 1
        if (x1 > x2):
            for i in range(x2, x1 + 1):
                if (y2 > y1):
                    y = y1 + (i - x2)
                    x = x2 - (i - x1)
                if (y2 < y1):
                    y = y1 - (i - x2)
                    x = x2 - (i - x1)
                diagram[x][y] += 1




    return diagram

def print_diagram(diagram, overlap_num):
    count = 0

    for i in range(len(diagram)):
        for j in range(len(diagram[i])):
            if diagram[j][i] == 0:
                print('.', end = '')
            else:
                if (diagram[j][i] >= overlap_num):
                    count += 1
                print(diagram[j][i], end = '')
        print()

    print()
    print(count)

def main():
    data = common.get_input('input_05.txt').splitlines()
    #data = list(example.splitlines())
    bigness = 1000
    diagram_1 = [([0 for y in range(bigness)]) for x in range(bigness)]
    diagram_2 = [([0 for y in range(bigness)]) for x in range(bigness)]

    for coordinates in data:
        coordinate_pair = coordinates.split('->')
        x1, y1 = [int(coord.strip()) for coord in coordinate_pair[0].split(',')]
        x2, y2 = [int(coord.strip()) for coord in coordinate_pair[1].split(',')]
        if not is_diagonal(x1, y1, x2, y2):
            draw(diagram_1, x1, y1, x2, y2)
        draw(diagram_2, x1, y1, x2, y2)
    
    print_diagram(diagram_1, 2)
    print_diagram(diagram_2, 2)
        

if __name__ == '__main__':
    sys.exit(main())