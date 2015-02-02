#!/bin/python

def getCoordinate(grid, symbol):
	for i in range(len(grid)):
		try:
			idx = grid[i].index(symbol)
			return (i,idx)
		except:
			pass
	return ""
    
def displayPathtoPrincess(n,grid):
#print all the moves here
    princessX, princessY = getCoordinate(grid, 'p')
    botX, botY = getCoordinate(grid, 'm')
    while princessX != botX or princessY != botY:
        if princessX < botX:
            print("UP")
            botX -= 1
        elif princessX > botX:
            print("DOWN")
            botX += 1
        elif princessY > botY:
            print("RIGHT")
            botY += 1
        elif princessY < botY:
            print("LEFT")
            botY -= 1



m = input()
grid = []
for i in xrange(0, m):
    grid.append(raw_input().strip())

displayPathtoPrincess(m,grid)




