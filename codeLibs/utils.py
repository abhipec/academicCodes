def calculateInversions(data, commaSeperatedString = False):
	'''	returns number of inversions in a string or a list
		not optimized algo for large string/list length'''
	if commaSeperatedString:
		data = data.split(',')
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

def swapInString(data, idx1, idx2):
	'''	returns a string with content at location idx1 and idx2 swapped
		if idx1 is greater than idx2 swap them to maintain integrity'''
	if idx1 > idx2:
		tmp = idx1
		idx1 = idx2
		idx2 = tmp
	return data[0:idx1] + data[idx2] + data[idx1+1:idx2] + data[idx1] + data[idx2+1:]

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
