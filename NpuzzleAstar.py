#!/usr/bin/python3 
import os, sys
import math
sys.path.append(os.path.join(os.path.dirname(__file__), "codeLibs"))

from utils import calculateInversions, swapInList
from Astar import Astar

if len(sys.argv) != 2:
	print('Usage: python NpuzzleAstar "1,2,3,4,5,6,7,8,0"')
	exit()

initialState = sys.argv[1]

matrixSize = math.sqrt(len(initialState.split(',')))

if matrixSize != math.floor(matrixSize):
	exit('Enter a square matrix puzzle')

matrixSize = int(matrixSize)
goalState = ''
for i in range(1, matrixSize * matrixSize):
	goalState +=str(i) + ','
goalState += '0'


if matrixSize % 2 == 1:
	if ( calculateInversions(initialState, commaSeperatedString = True) % 2 ) != ( calculateInversions(goalState, commaSeperatedString = True) % 2 ):
		exit('Goal state not reachable from initial state')

def getActions(state, matrixSize):
	'''	It will returns a list of possible actions '''
	possibleActions = []
	state = state.split(',')
	xIndex = state.index('0')
	if xIndex < ( matrixSize * matrixSize - matrixSize ):
		possibleActions.append('DOWN')
	
	if xIndex >= matrixSize:
		possibleActions.append('UP')

	if xIndex % matrixSize == 0:
		possibleActions.append('RIGHT')
	elif xIndex % matrixSize == ( matrixSize - 1):
		possibleActions.append('LEFT')
	else:
		possibleActions.append('LEFT')
		possibleActions.append('RIGHT')

	return possibleActions


def applyAction(state, action, matrixSize):
	state = state.split(',')
	xIndex = state.index('0')
	if action == 'UP':
		return ','.join(swapInList(state, xIndex - matrixSize, xIndex))
	elif action == 'LEFT':
		return ','.join(swapInList(state, xIndex - 1, xIndex))
	elif action == 'RIGHT':
		return ','.join(swapInList(state, xIndex + 1, xIndex))
	elif action == 'DOWN':
		return ','.join(swapInList(state, xIndex + matrixSize, xIndex))


def applyActions(state, actions, matrixSize):
	newStates = []
	for action in actions:
		newStates.append(applyAction(state, action, matrixSize))
	return newStates

# print(iddfs(initialState, goalState[str(goalStateIndex)], getActions, applyActions, debug = True, depth = 40))
result = Astar(initialState, goalState, getActions, applyActions, debug = False, matrixSize = matrixSize)
print(result, len(result))
# print(applyActions(initialState, getActions(initialState, 4), 4))
# print(getActions('234506781', 3))