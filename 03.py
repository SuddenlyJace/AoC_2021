import sys
import common

example = '''00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010'''

def valid_reading(reading, rating, rating_len):
    valid = True

    for i in range(rating_len):
        if(reading[i] != rating[i]):
            valid = False

    return valid

def find_rating(data, filter, commonality):
    VALID_FILTER = {True, False}
    VALID_COMMONALITY = {'most', 'least'}
    if (filter not in VALID_FILTER):
        raise ValueError("filter must be one of %s." %  VALID_FILTER)
    if (commonality not in VALID_COMMONALITY):
        raise ValueError("commonality must be one of %s." %  VALID_COMMONALITY)

    rating = ''
    rating_len = 0
    first_rating = 0

    # iterate over the binary length of the readings
    for i in range(len(data[0])):
        bits = []
        num_valid_readings = 0

        # iterate over the total number of readings
        for j in data:
            if (filter == False or ((filter == True) and valid_reading(j, rating, rating_len))):
                bits.append(list(j)[i])
                num_valid_readings += 1
                if (num_valid_readings == 1):
                    first_rating = j
        
        if (num_valid_readings == 1):
            rating = first_rating
            break

        # Find the rating       
        ones = bits.count('1')
        zeros = bits.count('0')
        
        if (commonality == 'most'):
            if (ones >= zeros):
                rating += '1'
            elif (zeros > ones):
                rating += '0'
        elif (commonality == 'least'):
            if (zeros > ones):
                rating += '1'
            elif (ones >= zeros):
                rating += '0'
        rating_len += 1

    return rating

def solution(data, part):
    if (part == 1):
        rating_ones = find_rating(data, False, 'most')
        rating_zeros = find_rating(data, False, 'least')
    elif (part == 2):
        rating_ones = find_rating(data, True, 'most')
        rating_zeros = find_rating(data, True, 'least')

    print(rating_ones)
    print(rating_zeros)
    print(int(rating_ones,2) * int(rating_zeros,2))

def main():
    data = common.get_input('input_03.txt').split('\n') 
    #data = list(example.split('\n'))
    solution(data, 1)
    solution(data, 2)

if __name__ == '__main__':
    sys.exit(main())