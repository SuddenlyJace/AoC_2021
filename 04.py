import sys
import common

example = '''7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7'''

class Board:
    def __init__(self, board) -> None:
        self.board = board
        self.won = False

    def mark(self, number):
        # Mark number in board with an X
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                if (number == self.board[r][c]):
                    self.board[r][c] = 'X'
                # Check this row for victory condition
                bingo_count = 0
                for i in range(len(self.board[r])):
                    if (self.board[i][c] == 'X'):
                        bingo_count += 1        

                if (bingo_count == 5):
                    self.won = True
                    return self

                # Check this column for victory condition
                bingo_count = 0
                for i in range(len(self.board[c])):
                    if (self.board[r][i] == 'X'):
                        bingo_count += 1

                if (bingo_count == 5):
                    self.won = True
                    return self  

        # Not a winning mark
        return None

    def score(self):
        total = 0
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                if (self.board[r][c] != 'X'):
                    total += int(self.board[r][c])
        return total

    def winner(self):
        return self.won

def main():
    data = common.get_input('input_04.txt').split('\n\n') 
    #data = list(example.split('\n\n'))
    draw_order = data[0].split(',')
    boards = [Board([board_row.split() for board_row in board.split('\n')]) for board in data[1:]]

    winning_draw = -1
    last_draw = -1
    winning_board = None
    last_board = None
    num_winning_boards = 0

    for draw in draw_order:
        for board in boards:
            # Skip completed boards
            if board.winner() != True:
                victory_board = None
                victory_board = board.mark(draw)
                if (victory_board != None):
                    num_winning_boards += 1
                if (num_winning_boards == len(boards) and (last_board == None) and (last_draw == -1)):
                    last_draw = int(draw)
                    last_board = victory_board
                if (victory_board != None) and (winning_board == None) and (winning_draw == -1):
                    winning_board = victory_board
                    winning_draw = int(draw)
    
    if (winning_board == None):
        print('Error')
    else:
        print(winning_draw)
        print(winning_board.score())
        print(winning_draw * winning_board.score())
        print(last_draw)
        print(last_board.score())
        print(last_draw * last_board.score())

if __name__ == '__main__':
    sys.exit(main())