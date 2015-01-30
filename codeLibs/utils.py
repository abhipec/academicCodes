def calculateInversions(data):
	'''	returns number of inversions in a string or a list
		not optimized algo for large string/list length'''
	inversion = 0
	for idx, val in enumerate(data):
		for val2 in data[idx+1:]:
			if val2 != '0' and str(val2) < str(val):
				inversion += 1
	return inversion

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
	if ( end - start ) == 1 and ( start == 2 or start == 5 ):
		distance += 3
	else:
		distance += end - start
	return distance

def calculateManhattanDistance(state, goalState, matrixSize):
	'''	It will calculate Manhattan distance of a state w.r.t goal state
		assuming a square matrix of matrixSize'''
	distance = 0
	for i in range(len(state)):
		if state[i] != '0':
			distance += computeSingleMoveManhattanDistance(i, goalState.find(state[i]), matrixSize)
	return distance

def swap(data, idx1, idx2):
	'''	returns a string with content at location idx1 and idx2 swapped
		if idx1 is greater than idx2 swap them to maintain integrity'''
	if idx1 > idx2:
		tmp = idx1
		idx1 = idx2
		idx2 = tmp
	return data[0:idx1] + data[idx2] + data[idx1+1:idx2] + data[idx1] + data[idx2+1:]

