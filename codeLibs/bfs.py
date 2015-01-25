def bfsGraph(graph, start , end = 'NaN', marked=[]):
	# add start node in marked list and FIFO queue
	queue = [start]
	marked.append(start)
	# loop till queue becomes empty
	while len(queue):
		# explore neighbors of first element of queue 
		for edge in graph.getEdges(queue[0]):
			# if end state found return 
			if edge == end:
				return marked
			# if vertex is not visited before, add it marked list and queue
			elif edge not in marked:
				marked.append(edge)
				queue.append(edge)
		# remove first element from queue
		queue.pop(0)
	# return marked in end, this will show path bfs has followed
	return marked


def bfsAI(initialState, goalState, getActions, applyActions, debug=False):
	'''
	Search for solution using BFS.
	initialState	-- initial state
	goalState		-- goal state
	getActions		-- must be a function object that returns list of actions possible for that state
	applyActions	-- must be function object that returns list of new state after applying actions
	debug 			-- it will print each state at time of exploration
	'''
	discoveredStates = [initialState]
	undiscoveredStates = [initialState]
	count = 0
	while len(undiscoveredStates):
		count += 1
		if debug:
			print(undiscoveredStates[0])
		for state in applyActions(undiscoveredStates[0],getActions(undiscoveredStates[0])):
			if goalState == state:
				if debug:
					print(goalState)
				return count
			elif state not in discoveredStates:
				discoveredStates.append(state)
				undiscoveredStates.append(state)
		undiscoveredStates.pop(0)
	return count


