def dfsGraph(graph, start , end = 'NaN', marked=[]):
	# if start or end state are already visited, return 
	if start in marked or end in marked:
		return marked
	# add start node in marked list
	marked.append(start)

	# recursively call dfs on all vertex connected to start vertex
	for edge in graph.getVertex(start).getEdges():
		dfsGraph(graph,edge,end,marked)
	# return marked in end, this will show path dfs has followed
	return marked

def dfsAI(initialState, goalState, getActions, applyActions, debug=False, marked = [], depth = 40, goalReached=False):
	'''
	Search for solution using DFS.
	initialState	-- initial state
	goalState		-- goal state
	getActions		-- must be a function object that returns list of actions possible for that state
	applyActions	-- must be function object that returns list of new state after applying actions
	debug 			-- it will print each state at time of exploration
	'''
	# if initial start or goal state are already visited, return 
	if goalState in marked:
		goalReached = True
		print("goal reached")
	# add initial state in marked list
	marked.append(initialState)	
	if debug:
		print(initialState)
	for state in applyActions(initialState,getActions(initialState)):
		if state not in marked and depth > 0 and not goalReached:
			goalReached = dfsAI(state, goalState, getActions, applyActions, debug, marked, depth - 1, goalReached)
	
	return goalReached


def iddfs(initialState, goalState, getActions, applyActions, debug=False, depth = 10):
	'''
	Iterative deepening depth-first search
	'''
	for i in range(1,depth + 1):
		if dfsAI(initialState, goalState, getActions, applyActions, debug, marked = [],  depth = i):
			return True
	return False	