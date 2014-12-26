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

    def is_horizontal_win(self):
        results = []
        for row in self.board:
            result = self.all_same(row)
            results.append(result)
        return any(results)

    def all_same(self, row):
        if any(row) == True:
            return all(x == row[0] for x in row)
        else:
            return False
