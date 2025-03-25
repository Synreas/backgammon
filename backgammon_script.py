from random import randint
from os import system

class Dice:
	def dice(self):
		return randint(1,6)


class Checker:
	__position = 0
	__point = None
	__color_symbol = ""
	__isOpen = None
	__onTheBar = None

	def __init__(self, point, color):
		self.__point = point
		self.__position = self.__point.get_number()
		self.__point.add_checker(self)
		self.__point.set_color_symbol(color)
		self.__color_symbol = color
		self.__isOpen = False

	def get_color_symbol(self):
		return self.__color_symbol

	def isOpen(self):
		return self.__isOpen

	def move_to(self, point):
		self.__point.remove_checker(self)
		self.__position = point.get_number()
		lefts = self.__point.get_checker_list()
		if len(lefts) == 0:
			self.__point.set_color_symbol(" ")
		elif len(lefts) == 1:
			lefts[0].set_open()
		point.add_checker(self)
		self.__point = point
		self.__point.set_color_symbol(self.__color_symbol)

		if len(point.get_checker_list()) == 1:
			self.__isOpen = True

		else:
			if len(point.get_checker_list()) == 2:
				point.get_checker_list()[0].set_closed()
			self.__isOpen = False

	def get_hit(self, bar):
		self.__position = 0
		self.__point.set_color_symbol(" ")
		self.__point.remove_checker(self)
		self.__point = "BAR"
		bar.add_checker(self)

	def get_position(self):
		return self.__position

	def set_closed(self):
		self.__isOpen = False

	def set_open(self):
		self.__isOpen = True

class Point:
	__number = 0
	__color_symbol = ""
	__checker_list = None

	def __init__(self, number, color_symbol = " "):
		self.__number = number
		self.__color_symbol = color_symbol
		self.__checker_list = []

	def get_number(self):
		return self.__number

	def get_checker_list(self):
		return self.__checker_list

	def get_color_symbol(self):
		return self.__color_symbol

	def add_checker(self, checker):
		self.__checker_list.append(checker)

	def remove_checker(self, checker):
		self.__checker_list.remove(checker)
		if len(self.__checker_list) == 0:
			self.__color_symbol = " "

	def set_color_symbol(self, symbol):
		self.__color_symbol = symbol

class Bar:
	__color_symbol = ""
	__checker_list = None

	def __init__(self, color_symbol):
		self.__color_symbol = color_symbol
		self.__checker_list = []

	def get_color_symbol(self):
		return self.__color_symbol

	def get_checker_list(self):
		return self.__checker_list

	def add_checker(self, checker):
		self.get_checker_list().append(checker)

	def remove_checker(self, checker):
		self.get_checker_list().remove(checker)


class Board:
	areas = 4
	area_points = 6
	__points = None
	__name1 = None
	__name2 = None
	__bar1 = None
	__bar2 = None
	__game_finished = None

	"""

[]-12-11-10-9--8--7-BAR-6--5--4--3--2--1-[]
[][ ][ ][ ][ ][ ][ ][B][ ][ ][ ][ ][ ][ ][]
[][ ][ ][ ][ ][ ][ ][B][ ][ ][ ][ ][ ][ ][]
[][ ][ ][ ][ ][ ][ ][B][ ][ ][ ][ ][ ][ ][]
[][ ][ ][ ][ ][ ][ ][B][ ][ ][ ][ ][ ][ ][]
[][ ][ ][ ][ ][ ][ ][B][ ][ ][ ][ ][ ][ ][]
[][ ][ ][ ][ ][ ][ ][B][ ][ ][ ][ ][ ][ ][]
[][ ][ ][ ][ ][ ][ ][B][ ][ ][ ][ ][ ][ ][]
[][B][B][B][B][B][B]BAR[B][B][B][B][B][B][]
[][ ][ ][ ][ ][ ][ ][B][ ][ ][ ][ ][ ][ ][]
[][ ][ ][ ][ ][ ][ ][B][ ][ ][ ][ ][ ][ ][]
[][ ][ ][ ][ ][ ][ ][B][ ][ ][ ][ ][ ][ ][]
[][ ][ ][ ][ ][ ][ ][B][ ][ ][ ][ ][ ][ ][]
[][ ][ ][ ][ ][ ][ ][B][ ][ ][ ][ ][ ][ ][]
[][ ][ ][ ][ ][ ][ ][B][ ][ ][ ][ ][ ][ ][]
[][ ][ ][ ][ ][ ][ ][B][ ][ ][ ][ ][ ][ ][]
[]13-14-15-16-17-18-BAR-19-20-21-22-23-24[]

	"""

	def __init__(self, pointlist, name1, name2, bar1, bar2):
		self.__points = [0] + [x for x in pointlist]
		self.__name1 = name1
		self.__name2 = name2
		self.__bar1 = bar1
		self.__bar2 = bar2
		self.__game_finished = False

	def get_bar1(self):
		return self.__bar1

	def get_bar2(self):
		return self.__bar2

	def get_bar(self, symbol):
		if self.get_bar1().get_color_symbol() == symbol:
			return self.get_bar1()
		elif self.get_bar2().get_color_symbol() == symbol:
			return self.get_bar2()

	def is_finished(self):
		return self.__game_finished

	def clear(self):
		system("cls || clear")

	def print(self, n = 7):
		print(f"{self.__name1:^43}")
		print("[]-12-11-10-9--8--7-BAR-6--5--4--3--2--1-[]")

		checkersonpoints = [0]

		for i in range(1, 25):
			checkersonpoints.append(len(self.__points[i].get_checker_list()))

		for x in range(n):
			print("[]", end="")
			for i in range(12, 0, -1):
				if checkersonpoints[i] > 0:
					checkersonpoints[i] -= 1
					print(f"[{self.__points[i].get_color_symbol()}]", end="")
				else:
					print("[ ]", end="")

				if i == 7:
					barlefts = self.get_bar1().get_checker_list()
					if len(barlefts) + x >= n:
						print(f"[{barlefts[0].get_color_symbol()}]", end="")
					else:
						print("[B]", end="")

			print("[]")

		print("[][B][B][B][B][B][B]BAR[B][B][B][B][B][B][]")

		for x in range(n):
			print("[]", end="")
			for i in range(13, 25):
				if checkersonpoints[i] + x == n:
					checkersonpoints[i] -= 1
					print(f"[{self.__points[i].get_color_symbol()}]", end="")
				else:
					print("[ ]", end="")

				if i == 18:
					barlefts = self.get_bar2().get_checker_list()
					if len(barlefts) > x:
						print(f"[{barlefts[0].get_color_symbol()}]", end="")
					else:
						print("[B]", end="")

			print("[]")

		print("[]13-14-15-16-17-18-BAR-19-20-21-22-23-24[]")
		print(f"{self.__name2:^43}")

	def refresh(self, dices = None):
		self.clear()
		self.print()
		self.print_dices(dices)

	def print_dices(self, dices=None):
		print(f"Your dices are: {dices[:]}" if dices is not None else "") 

class Player:
	global points
	__name = None
	__checkers = None
	__color_symbol = None
	__home_board = None
	__bar = None
	points = None
	board = None

	def __init__(self, name, checkers, _points, bar):
		self.__name = name
		self.__checkers = [x for x in checkers]
		self.__color_symbol = self.__checkers[0].get_color_symbol()
		if  self.__color_symbol == "X":
			self.__home_board = "DESC" # (1,6) descending

		else:
			self.__home_board = "ASC" # (19,24) ascending
		self.points = _points
		self.__bar = bar

	def get_name(self):
		return self.__name

	def get_checkers(self):
		return self.__checkers

	def get_color_symbol(self):
		return self.__color_symbol

	def get_home_board(self):
		return self.__home_board

	def get_bar(self):
		return self.__bar

	def set_board(self, board):
		self.board = board

	def play(self, dices):
		global points
		def get_point(position):
			for i in self.points:
				if i.get_number() == position:
					return i

		def get_move(number="first"):
			move = input(f"{self.get_name()}'s {number} move: ")

			try:
				move = int(move)

			except:
				print("Enter a valid number")
				move = get_move(number)

			else:
				if not check_move(get_point(move))[0] or get_point(move).get_color_symbol() == " ":
					print(f"Pick from your symbol ({self.get_color_symbol()})")
					move = get_move(number)

			finally:
				return move


		def check_move(position):
			return (position.get_color_symbol() == self.get_color_symbol() or \
			position.get_color_symbol() == " ", position.get_checker_list()[0].isOpen() \
			if len(position.get_checker_list()) > 0 else False)
		print("")
		for i in range(len(dices)):
			text = ""
			match i:
				case 0:
					text = "first"

				case 1:
					text = "second"

				case 2:
					text = "third"

				case 3:
					text = "fourth"

				case _:
					text = "?????"

			move1 = get_move(text)
			point1 = get_point(move1 + dices[i] * (1 if self.get_home_board() == "ASC" else -1))
			isOK = check_move(point1)

			while not(isOK[0] or isOK[1]):
				print(isOK)
				move1 = get_move(text)
				point1 = get_point(move1 + dices[i] * (1 if self.get_home_board() == "ASC" else -1))
				isOK = check_move(point1)

			if isOK == (False, True):
				point1.get_checker_list()[0].get_hit(self.board.get_bar(point1.get_checker_list()[0].get_color_symbol()))
				get_point(move1).get_checker_list()[-1].move_to(point1)

			else:
				get_point(move1).get_checker_list()[-1].move_to(point1)


			self.board.refresh(dices)
		dices.clear()









