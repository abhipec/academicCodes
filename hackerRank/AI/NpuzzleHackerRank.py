def computeSingleMoveManhattanDistance(start, end, matrixSize):
	'''	It returns number of moves required to reach end state from start state in a matrix environment'''
	if start > end:
		tmp = start
		start = end
		end = tmp
	distance = 0
	while ( end - start ) >= matrixSize:
		end -= matrixSize
		distance += 1
	if ( end - start ) == 1 and ( start % matrixSize == ( matrixSize - 1 ) ):
		distance += matrixSize
	else:
		distance += end - start
	return distance

def calculateManhattanDistance(state, goalState, matrixSize, commaSeperatedString = True):
	'''	It will calculate Manhattan distance of a state w.r.t goal state
		assuming a square matrix of matrixSize'''
	if commaSeperatedString:
		state = state.split(',')
		goalState = goalState.split(',')
	distance = 0
	for i in range(len(state)):
		if state[i] != '0':
			distance += computeSingleMoveManhattanDistance(i, goalState.index(state[i]), matrixSize)
	return distance


def swapInList(data, idx1, idx2):
	'''	swap elements at index idx1 and idx2 of a clone list'''
	# create a copy of list
	data1 = list(data)
	# swap elements in cloned list
	tmp = data1[idx1]
	data1[idx1] = data1[idx2]
	data1[idx2] = tmp
	# return swapped cloned list
	return data1

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
	steps.pop()
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
				discoveredStates[state] = State(state, findCostTillNow(discoveredStates,toBeExplored, 0.1), calculateManhattanDistance(state, goalState, matrixSize), toBeExplored)
				return getSteps(discoveredStates,state)
			elif not discoveredStates.get(state,0):
				discoveredStates[state] = State(state, findCostTillNow(discoveredStates,toBeExplored, 0.1), calculateManhattanDistance(state, goalState, matrixSize), toBeExplored)
				undiscoveredStates[state] = State(state, findCostTillNow(discoveredStates,toBeExplored, 0.1), calculateManhattanDistance(state, goalState, matrixSize), toBeExplored)
		del undiscoveredStates[toBeExplored]



matrixSize = int(input())
initialState = ''
for i in range(1, matrixSize * matrixSize):
	initialState +=str(input()) + ','
initialState += str(input())


goalState = ''
for i in range(0, matrixSize * matrixSize - 1):
	goalState +=str(i) + ','
goalState += str(matrixSize * matrixSize - 1)



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

def getMove(start, end, matrixSize):
	start = start.split(',')
	end = end.split(',')
	startX = start.index('0')
	endX = end.index('0')
	difference = endX - startX
	if difference == 1:
		return 'RIGHT'
	elif difference == -1:
		return 'LEFT'
	elif difference == matrixSize:
		return 'DOWN'
	else:
		return 'UP'

	


result = Astar(initialState, goalState, getActions, applyActions, debug = False, matrixSize = matrixSize)
print(len(result) - 1 )
reverse = list(reversed(result))
for i in range(len(reverse) - 1):
	print(getMove(reverse[i],reverse[i+1],matrixSize))
