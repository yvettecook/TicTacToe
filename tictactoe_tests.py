import tictactoe

def test_game_has_board():
    game = tictactoe.Tictactoe()
    assert game.board == [[],[],[]]
    print "passed: game has a board"

test_game_has_board()
