class Tictactoe(object):
    def __init__(self):
        self.board = [[None, None, None],[None, None, None],[None, None, None]]

    def board():
        return self.board

    def place(self, row, column, mark):
        if self.board[row][column] == None:
            self.board[row][column] = mark

    def player_move(self, row, column):
        row -= 1
        column -= 1
        self.place(row, column, 'X')

    def computer_move(self, row, column):
        row -= 1
        column -= 1
        self.place(row, column, 'O')
