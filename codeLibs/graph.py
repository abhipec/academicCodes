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


def sampleDirectedGraph():
	g = DirectedGraph()
	return g

def sampleUnDirectedGraph():
	g = UnDirectedGraph()
	g.addEdge('1','2',7)
	g.addEdge('1','3',9)
	g.addEdge('1','6',14)
	g.addEdge('2','3',10)
	g.addEdge('2','4',15)
	g.addEdge('3','4',11)
	g.addEdge('3','6',2)
	g.addEdge('4','5',6)
	g.addEdge('5','6',9)
	g.addEdge('5','7',9)
	g.addEdge('7','8',9)
	g.addEdge('8','9',9)
	g.addEdge('9','10',9)
	return g