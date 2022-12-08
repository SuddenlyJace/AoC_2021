import sys
import common

example_1 = '''NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
'''

example_1_test = '''NCNBCHB
NBCCNBBBCBHCB
NBBBCNCCNBBNBNBBCHBHHBCHB
NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB
'''

def parse_input(input):
    return input.splitlines()

def create_pair_map(insertion_rules):
    pair_map = {}
    for rule in insertion_rules:
        x, y = rule.split(' -> ')
        pair_map[x] = [x[0] + y, y + x[1]]
    
    return pair_map

def create_pairs_from_template(template, pair_map):
    pairs = pair_map.copy()
    # Zero out the map
    for k in pairs:
        pairs[k] = 0
    # Add the template pairs into the dict
    for i in range(len(template)-1):
        pairs[template[i]+template[i+1]] += 1

    # Join the keys of pairs into a single string, then convert to set to remove
    # duplicates, then back to a list
    # Final pair_list is a list of all the characters used in elements
    pair_list = list(set(''.join(list(pairs))))
    elements = {}
    # Zero out elements
    for k in pair_list:
        elements[k] = 0
    # Add the template elements into the dict
    for i in range(len(template)):
        elements[template[i]] += 1

    return pairs, elements

def polymerization(input, steps):
    template = input[0]
    insertion_rules = input[2:]

    pair_map = create_pair_map(insertion_rules)
    pairs, elements = create_pairs_from_template(template, pair_map)

    for i in range(steps):
        # Zero out the temporary dict
        temp = {}
        for k in pairs:
            temp[k] = 0
        
        # Find new pairs
        for pair in pairs:
            elements[pair_map[pair][0][1]] += pairs[pair]
            for x in pair_map[pair]:
                temp[x] += pairs[pair]
        
        pairs = temp
    
    return elements

def main():
    test_data = parse_input(example_1)

    assert(sum(polymerization(test_data, 5).values()) == 97)
    assert(sum(polymerization(test_data, 10).values()) == 3073)
    test_elements = list(polymerization(test_data, 10).values())
    test_elements.sort()
    assert((test_elements[-1] - test_elements[0]) == 1588)


    data = parse_input(common.get_input('input_14.txt'))
    
    elements = list(polymerization(data, 10).values())
    elements.sort()
    print('Part 1: {}'.format((elements[-1] - elements[0])))

    elements = list(polymerization(data, 40).values())
    elements.sort()
    print('Part 2: {}'.format((elements[-1] - elements[0])))
        
if __name__ == '__main__':
    sys.exit(main())