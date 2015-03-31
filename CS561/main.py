from graph import *
from ucs import uniformCostSearch
# initiate a graph object
graph = DirectedGraph()

# read graph from file
with open('graph.txt','r') as dataFile:
    # split complete files into lines and filter empty lines
    lines = filter(None,dataFile.read().split('\n'))
    # enumerate over lines
    for vertex1, value in enumerate(lines):
        # extract vertex from lines
        nodes = filter(None,value.split('\t'))
        for vertex2, node in enumerate(nodes):
            # non zero means there is a edge
            if node !='0' :
                graph.addEdge(str(vertex1 + 1),str(vertex2 + 1),node)
# initize blacklist dictionary
blacklist = {}
# update blacklist dictionary from file
with open('blacklist.txt','r') as dataFile:
    lines = filter(None,dataFile.read().split('\n'))
    for vertex1, value in enumerate(lines):
        nodes = filter(None,value.split(' '))
        blacklist[str(vertex1 + 1)] = nodes[1:]

# ask user to enter start and goal node
startNode = raw_input('Enter start node\t')
goalNode = raw_input('Enter goal node \t')

# call uniform cost search function
path, pathCost, frontiers, explored = uniformCostSearch(graph,startNode,goalNode,blacklist[startNode])

# display results
if not path:
    print("path does not exists")
    exit()
print("path from start node to goal node is")
print(path)
print("path cost is, " + str(pathCost))

print("explored set is")
print(explored)

print("frontiers are")
print(frontiers)
