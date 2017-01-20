#!/usr/bin/env python

# Simple implementation of the Conway's Game of Life
# https://en.wikipedia.org/wiki/Conway's_Game_of_Life


from time import sleep

def ask_cells(grid):
	nbCells = int(input("Nb cells ? "))
	for i in range(nbCells):
		print(f"Cell nb {i}")
		x = int(input("X pos ? "))
		y = int(input("Y pos ? "))

		grid[x][y] = 1


def init(grid):
	len = int(input("length ? "))
	hei = int(input("width ? "))

	#len = 5
	#hei = 5

	for i in range(len):
		grid.append([0] * hei)


def around(x, y, grid):
	living = 0

	# x-1,y-1    x-1,y   x-1,y+1
	#   x,y-1      x,y     x,y+1
	# x+1,y-1    x+1,y     x,y+1

	# case: normal
	if x > 0 and y > 0 and x < len(grid)-1 and y < len(grid[x])-1:
		for i in range(3):
			for j in range(3):
				if i != 1 or j != 1:
					living += grid[x-1+i][y-1+j]
		return living

	# case: left
	if x > 0 and x < len(grid)-1 and y == 0:
		for i in range(3):
			for j in range(2):
				if i != 1 or j != 0:
					living += grid[x-1+i][y+j]
		return living

	# case: right
	if x > 0 and x < len(grid)-1 and y == len(grid[x])-1:
		for i in range(3):
			for j in range(2):
				if i != 1 or j != 0:
					living += grid[x-1+i][y-j]
		return living

	# case: top
	if x == 0 and y > 0 and y < len(grid[x])-1:
		for i in range(2):
			for j in range(3):
				if i != 0 or j != 1:
					living += grid[x+i][y-1+j]
		return living

	# case: bottom
	if x == len(grid)-1 and y > 0 and y < len(grid[x])-1:
		for i in range(2):
			for j in range(3):
				if i != 0 or j != 1:
					living += grid[x-i][y-1+j]
		return living

	# case: left-top
	if x == 0 and y == 0:
		for i in range(2):
			for j in range(2):
				if i != 0 or j != 0:
					living += grid[x+i][y+j]
		return living

	# case: right-top
	if x == 0 and y == len(grid[x])-1:
		for i in range(2):
			for j in range(2):
				if i != 0 or j != 0:
					living += grid[x+i][y-j]
		return living

	# case: left-bottom
	if x == len(grid)-1 and y == 0:
		for i in range(2):
			for j in range(2):
				if i != 0 or j != 0:
					living += grid[x-i][y+j]
		return living

	# case: right-bottom
	if x == len(grid)-1 and y == len(grid[x])-1:
		for i in range(2):
			for j in range(2):
				if i != 0 or j != 0:
					living += grid[x-i][y-j]
		return living


def update(grid):
	update = []
	for i in range(len(grid)):
		update.append([0] * len(grid[i]))

	for i in range(len(grid)):
		for j in range(len(grid[i])):
			update[i][j] = grid[i][j]

	for i in range(len(grid)):
		for j in range(len(grid[i])):
			living = around(i,j,grid)

			if living == 3:
				update[i][j] = 1
			elif living != 2 and grid[i][j] == 1:
				update[i][j] = 0

	for i in range(len(grid)):
		for j in range(len(grid[i])):
			grid[i][j] = update[i][j]


def display(grid, sep):
	for i in range(len(grid)):
		res = "|"
		for j in range(len(grid[i])):
			if grid[i][j] == 1:
				res += "O"
			else:
				res += " "
		res += "|"
		print(res)

	print(sep)


def main():
	grid = []

	init(grid)

	# if you want to populate the grid interactively
	ask_cells(grid)

	sep = "+"
	for i in range(len(grid)):
		sep += "-"
	sep += "+"

	print(sep)
	display(grid,sep)

	while True:
		update(grid)
		display(grid,sep)
		sleep(0.5)



if __name__ == "__main__":
	main()
