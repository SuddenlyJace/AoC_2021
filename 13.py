import sys
import common

example_1 = '''6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
'''

def parse_input(input):
    lines = input.splitlines()
    idx = lines.index('')
    
    marks = []
    for line in lines[:idx]:
        x, y = line.split(',')
        marks.append((int(x), int(y)))
    
    # Split on '=' and assign the character left and the whole value to the right
    folds = []
    for line in lines[idx + 1:]:
        j = line.index('=')
        folds.append((line[j-1], int(line[j+1:])))

    return marks, tuple(folds)

def print_paper(sparse_matrix):
    # Find matrix size
    max_x = 0
    max_y = 0
    for x, y in sparse_matrix:
        if max_x < x:
            max_x = x
        if max_y < y:
            max_y = y
    max_x += 1
    max_y += 1

    # Fill emtpy matrix
    matrix = [['.' for x in range(max_x)] for y in range(max_y)]

    # Fill in marks (note reverse order on input)
    for y, x in sparse_matrix:
        matrix[x][y] = '#'
    
    # Printing for debug... 
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            print(matrix[x][y], end = '')
        print()

    return matrix

def fold_marks(sparse_matrix, fold):
    flip_map = list(reversed(range(fold[1] + 1)))
    for i in range(len(sparse_matrix)):
        x, y = sparse_matrix[i]
        if fold[0] == 'y' and y > fold[1]:
            sparse_matrix[i] = (x, flip_map[y - fold[1]])
        elif fold[0] == 'x' and x > fold[1]:
            sparse_matrix[i] = (flip_map[x - fold[1]], y)
    
    return sparse_matrix

def solve(sparse_matrix, folds):
    for fold in folds:
        matrix = fold_marks(sparse_matrix, fold)

    return matrix

def main():
    marks, folds = parse_input(example_1)
    test_paper = fold_marks(marks, folds[0])

    assert(len(set(test_paper)) == 17)

    marks, folds = parse_input(common.get_input('input_13.txt'))
    # This doesn't actually work and I don't know why. I had to edit solve() to
    # fin the answer to part 1
    single_fold = fold_marks(marks, folds[0])
    
    paper = solve(marks, folds)
    
    print('Part 1: {}'.format(len(set(single_fold))))
    print('Part 2:')
    print_paper(paper)
        
if __name__ == '__main__':
    sys.exit(main())