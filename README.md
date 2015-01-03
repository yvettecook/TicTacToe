## TicTacToe

#### *Coding Kata, tested and written in Python*

Simple command line game where player place either a 'O' or a 'X' in a 3x3 grid. The player who succeeds in placing three marks in a horizontal, vertical, or diagonal row wins the game.

- [x] Stage 1: Build a command-line playable game against the computer.

- [ ] Stage 2: Make the computer unbeatable.

#### Context

First attempt to build my own program in Python - so do forgive any ugliness!

I started learning Python this week - doing this kata will help me put this learning into practice.

#### To play

1. `$ git clone git@github.com:yvettecook/TicTacToe.git`

2. Change to the directory

3. `$ python tictactoe.py`

Enjoy!

#### Tools

* Python
* Python `assert` for testing
* Random Library

#### Design Choices & Learning
---

Grid as an array of 3 arrays: [ [ x, o, o ], [ x, o, o ], [ o, x, x ] ]

*With hindsight, a single array of 9 may have reduced complexity.*

---

Single class of game, rather than separating out board, player, computer.

*This was a conscious choice to focus on learning Python methods and syntax with a single class, rather than getting tangled in inter-class dependencies. Will use separate classes next time. Promise.*

---

Have touched on list comprehensions, but need to read more!
