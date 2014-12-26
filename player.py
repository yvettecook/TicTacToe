def move(self, row, column):
    row -= 1
    column -= 1
    self.game().place(row, column, 'X')
