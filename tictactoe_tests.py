import tictactoe

game = tictactoe.Tictactoe()

def test_game_has_board():
    assert game.board != None
    print "passed: game has a board"

def test_board_has_3_rows():
    assert len(game.board) == 3
    print "passed: board has 3 rows"

def test_row_has_3_squares():
    assert len(game.board[0]) == 3
    print "passed: board has 3 squares"

def test_game_has_player():
    assert game.player != None
    print "passed: game has a player"

test_game_has_board()
test_board_has_3_rows()
test_row_has_3_squares()
test_game_has_player()
