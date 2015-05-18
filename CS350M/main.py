from tree import *
from worker import *
import multiprocessing
import graph as graph
import random

# create a sample undirected graph
g = graph.sampleUnDirectedGraph()
# get list of all vertex in graph
vertexList = g.getVertices()
# initialize an empty tree object
tree = Tree()
# choose random node from graph, this will be root node in new tree
root = random.choice(vertexList)
# impliment BFS algorithm to convert graph to tree
queue = [root]
marked = [root]
while len(queue):
    # explore neighbors of first element of queue
    for edge in g.getEdges(queue[0]):
        # if vertex is not visited before, add it marked list and queue
        if edge not in marked:
			# add this edge to tree
            tree.addChild(queue[0],edge)
            marked.append(edge)
            queue.append(edge)
    # remove first element from queue
    queue.pop(0)

# open data source file
f = open('data.txt', 'r')
# read data source file into a list
dataSource = []
for d in filter(None,f.read().split('\n')):
    dataSource.append(int(d))

# find total number of leaf nodes in tree
leafList = sorted(tree.getLeafs())
leafListLength = len(leafList)

# calculate size of data that will be given to each worker process
# last leaf node based on index will receive the extra data if result is
# not integer
dataSize = len(dataSource)/leafListLength

# only run this for main file
if __name__ == '__main__':
    # run one worker process for each node in tree
    for vertex in tree.getVertices():
        # if the node is leaf distribute data to them based on their index
        if vertex in leafList:
            index = leafList.index(vertex)
            if index == leafListLength - 1:
                data = dataSource[index * dataSize:]
            elif index == 0:
                data = dataSource[ : (index + 1) * dataSize]
            else :
                data = dataSource[index * dataSize : (index + 1) * dataSize]
        else :
            data = []
        # create new process with arguments : tree object, its name, data
        p = multiprocessing.Process(target = worker,  args=(tree, vertex,data))
        # start process
        p.start()
