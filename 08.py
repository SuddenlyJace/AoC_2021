import sys
import common

example = '''be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce'''

digit_map = [
    ['a', 'b', 'c', 'e', 'f', 'g'], 
    ['c', 'f'], 
    ['a', 'c', 'd', 'e', 'g'],
    ['a', 'c', 'd', 'f', 'g'],
    ['b', 'c', 'd', 'f'],
    ['a', 'b', 'd', 'f', 'g'],
    ['a', 'b', 'd', 'e', 'f', 'g'],
    ['a', 'c', 'f'],
    ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    ['a', 'b', 'c', 'd', 'f', 'g']]

# This was found by running char_count(digit_map)
# digit_frequency_of_map = {'a': 8, 'b': 6, 'c': 8, 'd': 7, 'e': 4, 'f': 9, 'g': 7}

def char_count(digit_map):
    count = {char: 0 for char in 'abcdefg'}

    for digit in digit_map:
        for char in digit:
            count[char] += 1

    return count   

def main():
    data = common.get_input('input_08.txt').splitlines()
    #data = list(example.splitlines())

    total_digit_count = [0] * 10
    part2_sum = 0

    for note_line in data:
        input, output = note_line.split('|')
        input_digits = input.split()
        input_digits = [list(d) for d in input_digits]
        output_digits = output.split()
        output_digits = [list(d) for d in output_digits]

        
        out_map = {char: '0' for char in 'abcdefg'}
        in_map= char_count(input_digits)

        # Easy to find these 3 segments from the unique character frequency
        for char, num in in_map.items():
            if (num == 9):
                out_map['f'] = char
            elif (num == 6):
                out_map['b'] = char
            elif (num == 4):
                out_map['e'] = char

        # Sort the input list based on the number of characters in each digit
        input_digits.sort(key=lambda T: len(T))

        # List is sorted so start at the smallest number of characters to digitize
        for digits in input_digits:
            if (len(digits) == len(digit_map[1])):
                temp_digits = [x for x in digits if x not in out_map['f']]
                out_map['c'] = temp_digits[0]
            elif (len(digits) == len(digit_map[4])):
                temp_digits = [x for x in digits if x not in (out_map['b'], out_map['c'], out_map['f'])]
                out_map['d'] = temp_digits[0]
            elif (len(digits) == len(digit_map[7])):
                temp_digits = [x for x in digits if x not in (out_map['c'], out_map['f'])]
                out_map['a'] = temp_digits [0]
            elif (len(digits) == len(digit_map[8])):
                temp_digits = [x for x in digits if x not in (out_map['a'], out_map['b'], out_map['c'], out_map['d'], out_map['e'], out_map['f'])]
                out_map['g'] = temp_digits[0]

        # Output numbers is all output digits as a single list for part 2
        output_numbers = []
        for d in output_digits:
            # I did everything backwards apparently so lets unroll that...
            out_char_list = list(out_map.values())
            idxs = [out_char_list.index(sub) for sub in d]
            # Lookup the key for each index, which is actually the output character
            in_char_list = list(out_map.keys())
            # This only works because keys() and values() should preserve order each time they are called.
            output_digit = [in_char_list[i] for i in idxs]
            
            output_digit.sort()

            # We can compare output_digit and our digit_map to find the index that matches
            # The index is our output number
            number = digit_map.index(output_digit)
            total_digit_count[number] += 1
            output_numbers.append(number)
        
        # Generate a number from the list of digits
        output_number = int(''.join(map(str, output_numbers)))
        part2_sum += output_number

    print(total_digit_count[1]+total_digit_count[4]+total_digit_count[7]+total_digit_count[8])
    print(part2_sum)
        
if __name__ == '__main__':
    sys.exit(main())