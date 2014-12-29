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
    game.player_move(0,0)
    assert game.board[0][0] == "X"
    print "passed: player can move"

def test_computer_can_take_move():
    wipe_board(game)
    game.computer_move()
    print game.board
    print "passed: computer can move"

def test_cannot_place_on_occupied_square():
    game.place(0,1,'O')
    game.player_move(0,1)
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

def test_player_move_first():
    assert game.turn == 'player'
    print "passed: player move first"

def test_computer_takes_turn_after_player():
    game.player_move(0,1)
    assert game.turn == 'computer'
    print "passed: computer turn after player"

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
test_player_move_first()
test_computer_takes_turn_after_player()
