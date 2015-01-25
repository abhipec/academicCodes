#!/usr/bin/python3 
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "codeLibs"))

from graph import *
from dfs import *


initialState = 'X45738162'
goalState = {'0': '12345678X', '1' : '1238X4765'}


def calculateInversions(state):
	inversion = 0
	for idx, val in enumerate(state):
		for val2 in state[idx+1:]:
			if val2 != 'X' and str(val2) < str(val):
				inversion += 1
	return inversion


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

def swap(state, idx1, idx2):
	# if idx1 is greater than idx2 swap them to maintain integrity
	if idx1 > idx2:
		tmp = idx1
		idx1 = idx2
		idx2 = tmp
	return state[0:idx1] + state[idx2] + state[idx1+1:idx2] + state[idx1] + state[idx2+1:]

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



def search(initialState):
	count = 0
	discoveredStates = [initialState]
	undiscoveredStates = [initialState]
	while len(undiscoveredStates):
		count += 1
		print(undiscoveredStates[0])
		actions = getActions(undiscoveredStates[0])
		for action in actions:
			newState = applyAction(undiscoveredStates[0],action)
			if goalState[str(goalStateIndex)] == newState:
				print("goal reached")
				return count
			elif newState not in discoveredStates:
				undiscoveredStates.append(newState)
				discoveredStates.append(newState)
		undiscoveredStates.pop(0)
	return count



			
goalStateIndex = calculateInversions(initialState)%2



print(search(initialState))
