import tictactoe

game = tictactoe.Tictactoe()

def test_game_has_board():
    assert game.board != None
    print "passed: game has a board"

def test_board_has_3_rows():
    assert len(game.board) == 3
    print "passed: board has 3 rows"

test_game_has_board()
test_board_has_3_rows()
