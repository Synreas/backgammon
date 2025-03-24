from backgammon_script import *

"""

[]-12-11-10-9--8--7-BAR-6--5--4--3--2--1-[]
[][O][ ][ ][ ][X][ ][B][X][ ][ ][ ][ ][O][]
[][O][ ][ ][ ][X][ ][B][X][ ][ ][ ][ ][O][]
[][O][ ][ ][ ][X][ ][B][X][ ][ ][ ][ ][ ][]
[][O][ ][ ][ ][ ][ ][B][X][ ][ ][ ][ ][ ][]
[][O][ ][ ][ ][ ][ ][B][X][ ][ ][ ][ ][ ][]
[][ ][ ][ ][ ][ ][ ][B][ ][ ][ ][ ][ ][ ][]
[][ ][ ][ ][ ][ ][ ][B][ ][ ][ ][ ][ ][ ][]
[][B][B][B][B][B][B]BAR[B][B][B][B][B][B][]
[][ ][ ][ ][ ][ ][ ][B][ ][ ][ ][ ][ ][ ][]
[][ ][ ][ ][ ][ ][ ][B][ ][ ][ ][ ][ ][ ][]
[][X][ ][ ][ ][ ][ ][B][O][ ][ ][ ][ ][ ][]
[][X][ ][ ][ ][ ][ ][B][O][ ][ ][ ][ ][ ][]
[][X][ ][ ][ ][O][ ][B][O][ ][ ][ ][ ][ ][]
[][X][ ][ ][ ][O][ ][B][O][ ][ ][ ][ ][X][]
[][X][ ][ ][ ][O][ ][B][O][ ][ ][ ][ ][X][]
[]13-14-15-16-17-18-BAR-19-20-21-22-23-24[]

"""

points = []
x_checkers = []
o_checkers = []

for i in range(1, 25):
	points.append(Point(i))

for i in range(5):
	x_checkers.append(Checker(points[12], "X"))
	x_checkers.append(Checker(points[5], "X"))
	o_checkers.append(Checker(points[11], "O"))
	o_checkers.append(Checker(points[18], "O"))

for i in range(3):
	x_checkers.append(Checker(points[7], "X"))
	o_checkers.append(Checker(points[16], "O"))

for i in range(2):
	x_checkers.append(Checker(points[23], "X"))
	o_checkers.append(Checker(points[0], "O"))

player1 = Player("Player 1", x_checkers)
player2 = Player("Player 2", o_checkers)
board = Board(points, player1.get_name(), player2.get_name())
dice1 = Dice()
dice2 = Dice()
board.clear()
board.print()

moves = []

moves.append(dice1.dice())
moves.append(dice2.dice())
if moves[0] < moves[1]:
	moves[0], moves[1] = moves[1], moves[0]
elif moves[0] == moves[1]:
	moves.append(moves[0])
	moves.append(moves[0])
print(moves)
player1.play(moves)

board.clear()
board.print()
