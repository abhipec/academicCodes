#!/usr/bin/python3
def uniformCostSearch(graph, startNode, goalNode, blacklistedNodes):
    # initialize frontiers with start node
    frontiers = {}
    frontiers[startNode] = 0
    # initialize empy explored set
    explored = set()
    # initialize previous dictionary, used for finding shortest path
    prev = {}
    prev[startNode] = startNode
    # initialize path cost and goal reached flag
    pathCost = None
    goalReachedFlag = None

    if goalNode in blacklistedNodes:
        return None, None, None, None
    # loop till frontiers are exausted
    while frontiers.items():
        # find the lowest cost node from frontiers
        item = sorted(frontiers.items(), key=lambda t: t[1])[0]
        # deltete that node from frontier
        frontiers.pop(item[0])
        # add that node to explored set
        explored.add(item[0])
        # check for goal node
        if item[0] == goalNode:
            pathCost = item[1]
            goalReachedFlag = 1
            break
        else :
            # find neighbours of current node
            for nbr in graph.getNbr(item[0]):
                # if neighbour is blacklisted do not add this neighbour
                if nbr in blacklistedNodes:
                    continue
                # if neighbour not in explored set add it to frontier
                if nbr not in explored:
                    # calculate new cost to reach that node
                    newCost = int(graph.getWeight(item[0], nbr)) + int(item[1])
                    # if node not in frontier add it to frontier and update its predecessor in prev dictionary
                    if not frontiers.get(nbr,0):
                        frontiers[nbr] = newCost
                        prev[nbr] = item[0]
                    # if node is in frontier only update it if new cost is less than previous cost
                    elif frontiers[nbr] - newCost > 0:
                        frontiers[nbr] = newCost
                        prev[nbr] = item[0]
    # if algorithm terminates without reaching goal node return
    if goalReachedFlag != 1:
        return None, None, None, None
    # traverse predecessor dictionary to get the shortest path
    path = []
    temp = prev[goalNode]
    path.append(goalNode)
    while temp != startNode:
        path.append(temp)
        temp=prev[temp]
    path.append(startNode)
    path = path[::-1]
    return path, pathCost, frontiers, explored
