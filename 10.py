import sys
import common

example = '''[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
'''
illegal_score = {')': 3, ']': 57, '}': 1197, '>': 25137}
autocomplete_score = {')': 1, ']': 2, '}': 3, '>': 4}


def main():
    data = common.get_input('input_10.txt').splitlines()
    #data = example.splitlines()

    illegal_points = 0
    autocomplete_lines = []

    for line in data:
        chunk = []
        illegal = False

        for c in line:
            if (c == '('):
                chunk.append(')')
            elif (c == '['):
                chunk.append(']')
            elif (c == '{'):
                chunk.append('}')
            elif (c == '<'):
                chunk.append('>')
            else:
                closer = chunk.pop()
                if (c != closer):
                    illegal = True
                    illegal_points += illegal_score[c]
        
        if (not illegal):
            chunk.reverse()
            autocomplete_lines.append(chunk)


    autocomplete_points = []

    for l in autocomplete_lines:
        points = 0
        for c in l:
            points = (points * 5) + autocomplete_score[c]
        autocomplete_points.append(points)
    autocomplete_points.sort()

    print('Part 1: {}'.format(illegal_points))
    print('Part 2: {}'.format(autocomplete_points[int(len(autocomplete_points)/2)]))
        
if __name__ == '__main__':
    sys.exit(main())