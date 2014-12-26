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

def test_board_can_place():
    game.place(0, 0, 'X')
    assert game.board[0][0] == "X"
    print "passed: board can place a move"

def test_player_can_take_move():
    game.player_move(1,1)
    assert game.board[0][0] == "X"
    print "passed: player can move"



test_game_has_board()
test_board_has_3_rows()
test_row_has_3_squares()
test_board_can_place()
test_player_can_take_move()
