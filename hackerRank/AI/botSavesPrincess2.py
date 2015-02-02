#!/bin/python

def getCoordinate(grid):
	for i in range(len(grid)):
		try:
			idx = grid[i].index('p')
			return (i,idx)
		except:
			pass
	return ""

def nextMove(n,r,c,grid):
    princessX, princessY = getCoordinate(grid)
    if princessY > c:
    	return "RIGHT"
    elif princessY < c:
    	return "LEFT"
    if princessX < r:
    	return "UP"
    elif princessX > r:
    	return "DOWN"

n = input()
r,c = [int(i) for i in raw_input().strip().split()]
grid = []
for i in xrange(0, n):
    grid.append(raw_input())

print nextMove(n,r,c,grid)
