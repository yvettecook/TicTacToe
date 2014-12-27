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

def test_computer_can_take_move():
    game.computer_move(3,1)
    assert game.board[2][0] == "O"
    print "passed: computer can move"

def test_cannot_place_on_occupied_square():
    game.computer_move(1,2)
    game.player_move(1,2)
    assert game.board[0][1] == "O"
    print "passed: cannot place on occupied square"

def test_can_identify_horizontal_win():
    wipe_board(game)
    assert game.is_horizontal_win() == False
    game.place(2,0,'X')
    game.place(2,1,'X')
    game.place(2,2,'X')
    assert game.is_horizontal_win() == True
    print "passed: horizontal win identified"

def test_can_identify_vertical_win():
    wipe_board(game)
    assert game.is_vertical_win() == False
    game.place(0,0,'O')
    game.place(1,0,'O')
    game.place(2,0,'O')
    assert game.is_vertical_win() == True
    print "passed: vertical win identified"

def test_can_identify_diagonal_win():
    wipe_board(game)
    assert game.is_diagonal_win() == False
    game.place(0,0,'X')
    game.place(1,1,'X')
    game.place(2,2,'X')
    assert game.is_diagonal_win() == True
    print "passed: diagonal win identified"

def wipe_board(game):
    game.board = [[None, None, None],[None, None, None],[None, None, None]]


test_game_has_board()
test_board_has_3_rows()
test_row_has_3_squares()
test_board_can_place()
test_player_can_take_move()
test_computer_can_take_move()
test_cannot_place_on_occupied_square()
test_can_identify_horizontal_win()
test_can_identify_vertical_win()
test_can_identify_diagonal_win()
