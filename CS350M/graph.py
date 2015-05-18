class Vertex:

    def __init__(self,name):
        self.name = name
        self.edges = {}

    def addEdge(self,nbr,weight=0):
        self.edges[nbr] = weight

    def getEdges(self):
        return self.edges.keys()

    def getWeight(self,nbr):
        return self.edges.get(nbr)

    def __unicode__(self):
        return self.name

class DirectedGraph:

    def __init__(self):
        self.vertices = {}

    def addVertex(self,vertex):
        v = Vertex(vertex)
        self.vertices[vertex] = v

    def getVertices(self):
        return self.vertices.keys()

    def getVertex(self,vertex):
        if vertex in self.vertices.keys():
            return self.vertices[vertex]
        else:
            return None

    def getEdges(self,vertex):
        tmp = self.getVertex(vertex)
        if tmp:
            return tmp.getEdges()

    def addEdge(self,vertex,nbr,weight=0):
        if nbr not in self.vertices.keys():
            self.addVertex(nbr)
        if vertex not in self.vertices.keys():
            self.addVertex(vertex)

        self.vertices[vertex].addEdge(nbr,weight)

    def getNbr(self,vertex):
        if vertex not in self.vertices.keys():
            return None
        return self.vertices[vertex].getEdges()

    def getWeight(self,v1,v2):
        return self.vertices[v1].getWeight(v2)

class UnDirectedGraph(DirectedGraph):

    def addEdge(self,vertex,nbr,weight=0):
        if nbr not in self.vertices.keys():
            self.addVertex(nbr)
        if vertex not in self.vertices.keys():
            self.addVertex(vertex)

        self.vertices[vertex].addEdge(nbr,weight)
        self.vertices[nbr].addEdge(vertex,weight)

def sampleUnDirectedGraph():
    g = UnDirectedGraph()
    g.addEdge('10001','10002')
    g.addEdge('10001','10003')
    g.addEdge('10001','10006')
    g.addEdge('10002','10003')
    g.addEdge('10002','10004')
    g.addEdge('10003','10004')
    g.addEdge('10003','10006')
    g.addEdge('10004','10005')
    g.addEdge('10005','10006')
    g.addEdge('10005','10007')
    g.addEdge('10007','10008')
    g.addEdge('10008','10009')
    g.addEdge('10009','10010')
    return g
