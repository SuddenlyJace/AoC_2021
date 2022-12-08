import sys
import common
import statistics

example = '''16,1,2,0,4,2,7,1,2,14'''

def main():
    data = common.get_input('input_07.txt').split(',')
    #data = list(example.split(','))

    crab_positions = [int(pos) for pos in data]
    crab_positions.sort()
    perfect_pos = statistics.median(crab_positions)
    
    basic_sum = 0
    for crab in crab_positions:
        basic_sum += abs(crab - perfect_pos)
    print(basic_sum)
    
    lowest_cost_pos = 0
    fuel_cost = 10000000000000000
    for pos in range(min(crab_positions), max(crab_positions)):
        scaling_sum = 0
        for crab in crab_positions:
            n = abs(crab - pos)
            scaling_sum += (n*(n+1))/2
        if scaling_sum < fuel_cost:
            fuel_cost = scaling_sum
            lowest_cost_pos = pos
    
    print(lowest_cost_pos)
    print(fuel_cost)
if __name__ == '__main__':
    sys.exit(main())