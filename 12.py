import sys
import common

example_1 = '''start-A
start-b
A-c
A-b
b-d
A-end
b-end
'''

example_2 = '''dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
'''

example_3 = '''fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
'''

def find_every_path(cave_system, bonus_cave):
    paths = [['start']]
    all_paths_found = False

    while (all_paths_found == False):
        ended_path_count = 0
        for path_count, path in enumerate(paths):
            if path[-1] != 'end':
                # If this is the bonus cave we need to mark it visited
                if path[-1] == bonus_cave:
                    if path[0] == 'start':
                        path[0] = '1'
                    elif path[0] == '1':
                        path[0] = '2'

                # We need to add back in the larger caves after set removal of visited nodes
                large_caves = [node for node in cave_system[path[-1]] if node.isupper()]

                new_paths = cave_system[path[-1]] - set(path) - {'start'}
                new_paths = set.union(new_paths, set(large_caves))
                
                # We need to re-add the bonus cave if we have not visited it twice yet
                # To do this we are modifying the first node in path 'start' to
                # signal that we have or have not visited the bonus yet
                if path[0] == '1':
                    # We need to make sure the bonus cave is actually connected to
                    # this node before adding it into the paths
                    if bonus_cave in cave_system[path[-1]]:
                        new_paths.add(bonus_cave)

                #print(path[0], cave_system[path[-1]], "Paths: ", new_paths)
                if not new_paths:
                    # There is no where to go...
                    paths.remove(path)
                #print('{} : {}'.format(path[-1], new_paths))
                first_new_node = ''
                for i, node in enumerate(new_paths):                    
                    if i == 0:
                        # We can't modify path yet, or we won't be able to duplicate it
                        first_new_node = node
                    else:
                        new_path = path.copy()
                        new_path.append(node)
                        paths.append(new_path)
                # Now we can add the first new node to the path list
                path.append(first_new_node)
            else:
                ended_path_count += 1
        #print(paths)
        #print('path count {} : ends paths {}'.format(path_count + 1, ended_path_count))
        if ended_path_count == (path_count + 1):
            all_paths_found = True     
    return paths

def build_system(caves):
    system = {}
    for path in caves:
        nodes = path.split('-')
        # Add the node connection to both nodes present
        # Assuming that duplicates don't exist in the connections
        if nodes[0] in system:
            system[nodes[0]].add(nodes[1])
        else:
            system[nodes[0]] = {nodes[1]}
        if nodes[1] in system:
            system[nodes[1]].add(nodes[0])
        else:
            system[nodes[1]] = {nodes[0]}

    return system

def calculate_paths(cave_input):
    cave_system = build_system(cave_input)
    print(cave_system)
    return len(find_every_path(cave_system, ''))

def calculate_paths_p2(cave_input):
    cave_system = build_system(cave_input)
    print(cave_system)
    all_paths = []
    for bonus in cave_system.keys():
        if bonus.islower() and bonus != 'start' and bonus != 'end':
            print('bonus', bonus)
            new_paths = find_every_path(cave_system, bonus)
            # Reset path[0] so that we can deconflict
            for path in new_paths:
                path[0] = 'start'
            all_paths.extend(x for x in new_paths if x not in all_paths)
    
    all_paths.sort()
    return(len(all_paths))
    
    

def parse_input(input):
    return input.splitlines()

def main():
    data = parse_input(common.get_input('input_12.txt'))
    test_data_1 = parse_input(example_1)
    test_data_2 = parse_input(example_2)
    test_data_3 = parse_input(example_3)

    assert(calculate_paths(test_data_1) == 10)
    assert(calculate_paths(test_data_2) == 19)
    assert(calculate_paths(test_data_3) == 226)
    print('Part 1: {}'.format(calculate_paths(data)))

    assert(calculate_paths_p2(test_data_1) == 36)
    assert(calculate_paths_p2(test_data_2) == 103)
    assert(calculate_paths_p2(test_data_3) == 3509)
    print('Part 2: {}'.format(calculate_paths_p2(data)))
        
if __name__ == '__main__':
    sys.exit(main())