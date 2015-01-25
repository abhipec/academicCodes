def bfs(graph, start , end = 'NaN', marked=[]):
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
