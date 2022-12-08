import sys
import common

example = '''3,4,3,1,2'''

def main():
    data = common.get_input('input_06.txt').split(',')
    #data = list(example.split(','))

    fish = {k: 0 for k in range(9)}
    for days_remaining in data:
        fish[int(days_remaining)] += 1

    # Here come the fish...
    for days in range(256):
        baby_fish = 0

        baby_fish = fish[0]
        for i in range(8):
            fish[i] = fish[i+1]
        
        fish[6] += baby_fish
        fish[8] = baby_fish

        total_fish = 0
        for i in fish:
            total_fish += fish[i]
        print('Day {}, {} fish remain'.format(days+1, total_fish))
        
if __name__ == '__main__':
    sys.exit(main())