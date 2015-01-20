def dfs(graph, start , end = 'NaN', marked=[]):
	# if start or end state are already visited, return 
	if start in marked or end in marked:
		return marked
	# add start node in marked list
	marked.append(start)

	# recursively call dfs on all vertex connected to start vertex
	for edge in graph.getVertex(start).getEdges():
		dfs(graph,edge,end,marked)
	# return marked in end, this will show path dfs has followed
	return marked
