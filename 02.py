import sys
import common

example = '''forward 5
down 5
forward 8
up 3
down 8
forward 2'''

def solution(data, part):
    distance = 0
    aim = 0
    depth = 0

    for i in data:
        [command, units] = i.split()
        units = int(units)
        if command == 'forward':
            distance += units
            if part == 2:
                depth += units * aim
        elif command == 'up':
            aim -= units
            if part == 1:
                depth -= units
        elif command == 'down':
            aim += units
            if part == 1:
                depth += units

    print(distance*depth)

def main():
    data = common.get_input('input_02.txt').split('\n')
    #data = example.split('\n')
    solution(data, 1)
    solution(data, 2)

if __name__ == '__main__':
    sys.exit(main())