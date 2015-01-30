from utils import calculateInversions, calculateManhattanDistance, computeSingleMoveManhattanDistance

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

def findCostTillNow(discoveredStates, presentState):
	steps = []
	tmp = discoveredStates.get(presentState).getParent()
	steps.append(tmp)
	while tmp != 'start':
		tmp = discoveredStates.get(tmp).getParent()
		steps.append(tmp)
	return len(steps)

def printSteps(discoveredStates,presentState):
	steps = []
	tmp = discoveredStates.get(presentState).getParent()
	steps.append(tmp)
	while tmp != 'start':
		tmp = discoveredStates.get(tmp).getParent()
		steps.append(tmp)
	print(steps)
	print(len(steps))

def Astar(initialState, goalState, getActions, applyActions, debug = False):
	discoveredStates = {}
	undiscoveredStates = {}
	undiscoveredStates[initialState] = State(initialState, 0, calculateInversions(initialState), 'start')
	discoveredStates[initialState] = State(initialState, 0, calculateInversions(initialState), 'start')

	while len(undiscoveredStates):
		toBeExplored = min(undiscoveredStates.keys(), key=lambda k:undiscoveredStates[k].getTotalCost())
		if debug:
			print(toBeExplored, undiscoveredStates[toBeExplored].getTotalCost())
		for state in applyActions(toBeExplored,getActions(toBeExplored)):
			if goalState == state:
				print("goal reached")
				printSteps(discoveredStates,toBeExplored)
				return
			elif not discoveredStates.get(state,0):
				discoveredStates[state] = State(state, findCostTillNow(discoveredStates,toBeExplored)*0, calculateManhattanDistance(state, goalState, 3), toBeExplored)
				undiscoveredStates[state] = State(state, findCostTillNow(discoveredStates,toBeExplored)*0, calculateManhattanDistance(state, goalState, 3), toBeExplored)
		del undiscoveredStates[toBeExplored]

print(calculateManhattanDistance('412087635', '123456780', 3))
# print(computeSingleMoveManhattanDistance(5,6,3))