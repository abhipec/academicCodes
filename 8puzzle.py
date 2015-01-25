#!/usr/bin/python3 
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "codeLibs"))

from bfs import bfsAI
from dfs import dfsAI, iddfs
from utils import calculateInversions, swap

initialState = 'X45738162'
goalState = {'0': '12345678X', '1' : '1238X4765'}



def getActions(state):
	possibleActions = []
	xIndex = state.index('X')
	if xIndex == 0:
		possibleActions.append('DOWN')
		possibleActions.append('RIGHT')
	elif xIndex == 1:
		possibleActions.append("DOWN")
		possibleActions.append("LEFT")
		possibleActions.append("RIGHT")
	elif xIndex == 2:
		possibleActions.append("LEFT")
		possibleActions.append("DOWN")
	elif xIndex == 3:
		possibleActions.append("UP")
		possibleActions.append("RIGHT")
		possibleActions.append("DOWN")
	elif xIndex == 4:
		possibleActions.append("UP")
		possibleActions.append("LEFT")
		possibleActions.append("RIGHT")
		possibleActions.append("DOWN")
	elif xIndex == 5:
		possibleActions.append("UP")
		possibleActions.append("LEFT")
		possibleActions.append("DOWN")
	elif xIndex == 6:
		possibleActions.append("UP")
		possibleActions.append("RIGHT")
	elif xIndex == 7:
		possibleActions.append("UP")
		possibleActions.append("LEFT")
		possibleActions.append("RIGHT")
	elif xIndex == 8:
		possibleActions.append("UP")
		possibleActions.append("LEFT")

	return possibleActions


def applyAction(state, action):
	xIndex = state.index('X')
	if action == 'UP':
		return swap(state, xIndex - 3, xIndex)
	elif action == 'LEFT':
		return swap(state, xIndex - 1, xIndex)
	elif action == 'RIGHT':
		return swap(state, xIndex + 1, xIndex)
	elif action == 'DOWN':
		return swap(state, xIndex + 3, xIndex)


def applyActions(state,actions):
	newStates = []
	for action in actions:
		newStates.append(applyAction(state,action))
	return newStates

goalStateIndex = calculateInversions(initialState)%2

# print(iddfs(initialState, goalState[str(goalStateIndex)], getActions, applyActions, debug = False, depth = 40))
print(bfsAI(initialState, goalState[str(goalStateIndex)], getActions, applyActions, debug = False))