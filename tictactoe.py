import random

class Tictactoe(object):
    def __init__(self):
        self.board = [[None, None, None],[None, None, None],[None, None, None]]

    def play(self):
        while self.is_win() is False:
            self.print_board()
            self.player_prompt()
            if self.is_win() is True:
                break
            self.computer_move()
        self.print_board()
        print "Game over"

    def player_prompt(self):
        print "> Your move"
        print "> Input row number (0, 1 or 2)"
        print "> Input column number (0, 1 or 2)"
        row = int(raw_input())
        column = int(raw_input())
        self.player_move(row, column)

    def print_board(self):
        for row in self.board:
            print row

    def place(self, row, column, mark):
        if self.board[row][column] == None:
            self.board[row][column] = mark

    def player_move(self, row, column):
        self.place(row, column, 'X')

    def computer_move(self):
        while True:
            row = random.randrange(0,3)
            column = random.randrange(0,3)
            if self.board[row][column] == None:
                self.place(row, column, 'O')
                break
    
    def is_win(self):
        return self.is_vertical_win() or self.is_horizontal_win() or self.is_diagonal_win()

    def is_horizontal_win(self):
        return self.win_in_array(self.board)

    def is_vertical_win(self):
        columns = self.switch_rows_and_columns()
        return self.win_in_array(columns)

    def is_diagonal_win(self):
        diagonals = []
        diagonals.append([self.board[0][0], self.board[1][1], self.board[2][2]])
        diagonals.append([self.board[0][2], self.board[1][1], self.board[2][0]])
        return self.win_in_array(diagonals)

    def win_in_array(self, list):
        results = []
        for each in list:
            result = self.all_same(each)
            results.append(result)
        return any(results)

    def switch_rows_and_columns(self):
        results = []
        all_columns = []
        numbers = range(0,3)
        for column in numbers:
            column_number = column
            columns = []
            for row in numbers:
                columns.append(self.board[row][column_number])
            all_columns.append(columns)
        return all_columns

    def all_same(self, row):
        if any(row) == True:
            return all(x == row[0] for x in row)
        else:
            return False

game = Tictactoe()
game.play()
