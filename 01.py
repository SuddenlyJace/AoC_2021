import sys
import common

def solution(data, part):
    count = 0
    
    # Part one is comparing adjacent numbers, with a window of 2
    # Part two is comparing numbers that are 3 apart, with a window of 3. a+b+c ? b+c+d = a ? d
    if part == 1:
        offset = 1
    if part == 2:
        offset = 3

    for i in range(len(data)-offset):
        if data[i+offset] > data[i]:
            count += 1

    print(count)

def main():
    data_strings = common.get_input('input_01.txt').split('\n')
    data = list(map(int, data_strings))
    solution(data, 1)
    solution(data, 2)
    
if __name__ == '__main__':
    sys.exit(main())