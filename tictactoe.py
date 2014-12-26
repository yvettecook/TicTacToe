class Tictactoe(object):
    def __init__(self):
        self.board = [[None, None, None],[None, None, None],[None, None, None]]

    def board():
        return self.board

    def place(self, row, column, mark):
        self.board[row][column] = mark

    def player_move(self, row, column):
        row -= 1
        column -= 1
        self.place(row, column, 'X')



# class Player(object):
#     def __init__(self, game):
#         self.game = game
#
#     def game():
#         return self.game
#
#     # def move(self, row, column):
#     #     row -= 1
#     #     column -= 1
#     #     self.game().place(row, column, 'X')
