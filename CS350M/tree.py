class Vertex:
    def __init__(self,name):
        self.name = name
        self.children = []
        self.parent = None

    def addChild(self,child):
        self.children.append(child)

    def getChildren(self):
        return self.children

    def addParent(self, parent):
        self.parent = parent

    def getParent(self):
        return self.parent

    def __unicode__(self):
        return self.name

class Tree:

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

    def getChildren(self,vertex):
        tmp = self.getVertex(vertex)
        if tmp:
            return tmp.getChildren()
        else :
            return None

    def addChild(self,vertex, child):
        if vertex not in self.vertices.keys():
            self.addVertex(vertex)

        if child not in self.vertices.keys():
            self.addVertex(child)

        self.vertices[vertex].addChild(child)
        self.vertices[child].addParent(vertex)

    def getParent(self,vertex):
        if vertex not in self.vertices.keys():
            return None
        return self.vertices[vertex].getParent()

    def getLeafs(self):
        return filter(lambda key : not self.getChildren(key), self.vertices.keys())

