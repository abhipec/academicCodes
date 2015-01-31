from utils import calculateManhattanDistance

class State:
	def __init__(self, name, costSoFar, estimatedCost, parent):
		self.name = name
		self.costSoFar = costSoFar
		self.estimatedCost = estimatedCost
		self.parent = parent

	def getCostSoFar(self):
		return self.costSoFar

	def getEstimatedCost(self):
		return self.estimatedCost

	def getTotalCost(self):
		return self.estimatedCost + self.costSoFar

	def getName(self):
		return self.name

	def getParent(self):
		return self.parent

	def __unicode__(self):
		return self.name

def findCostTillNow(discoveredStates, presentState, costWeight = 1):
	'''	It backtracks from presentState till start state by following each state parent and return path length multiplied by weight of each step'''
	steps = []
	tmp = discoveredStates.get(presentState).getParent()
	steps.append(tmp)
	while tmp != 'start':
		tmp = discoveredStates.get(tmp).getParent()
		steps.append(tmp)
	return (len(steps) + 1 ) * costWeight

def getSteps(discoveredStates, presentState):
	'''	It backtracks from presentState till it reaches start state and returns path followed'''
	steps = [presentState]
	tmp = discoveredStates.get(presentState).getParent()
	steps.append(tmp)
	while tmp != 'start':
		tmp = discoveredStates.get(tmp).getParent()
		steps.append(tmp)
	return steps

def Astar(initialState, goalState, getActions, applyActions, debug = False, matrixSize = 3):
	discoveredStates = {}
	undiscoveredStates = {}
	undiscoveredStates[initialState] = State(initialState, 0, calculateManhattanDistance(initialState, goalState, matrixSize), 'start')
	discoveredStates[initialState] = State(initialState, 0, calculateManhattanDistance(initialState, goalState, matrixSize), 'start')
	if initialState == goalState:
		return [goalState]
	while len(undiscoveredStates):
		toBeExplored = min(undiscoveredStates.keys(), key=lambda k:undiscoveredStates[k].getTotalCost())
		if debug:
			print(toBeExplored, undiscoveredStates[toBeExplored].getTotalCost())
		for state in applyActions(toBeExplored,getActions(toBeExplored, matrixSize), matrixSize):
			if goalState == state:
				discoveredStates[state] = State(state, findCostTillNow(discoveredStates,toBeExplored, 0.17), calculateManhattanDistance(state, goalState, matrixSize), toBeExplored)
				return getSteps(discoveredStates,state)
			elif not discoveredStates.get(state,0):
				discoveredStates[state] = State(state, findCostTillNow(discoveredStates,toBeExplored, 0.17), calculateManhattanDistance(state, goalState, matrixSize), toBeExplored)
				undiscoveredStates[state] = State(state, findCostTillNow(discoveredStates,toBeExplored, 0.17), calculateManhattanDistance(state, goalState, matrixSize), toBeExplored)
		del undiscoveredStates[toBeExplored]