
import random

class Graph:

    def __init__(self):
        self.nodes = []

    def addNode(self, val):
        """
        Make a new node if there is not a node with the contents val. Return the
        new node created. If there is a node that exist with the contents val, do
        nothing.
        """
        found = False
        index = -1
        for node in self.nodes:
            if (val == node.val):
                found = True
                index = self.nodes.index(node)
                break

        if (found):
            return self.nodes[index]
        else:
            node = Node(val)
            self.nodes.append(node)
            return node



    def addEdge(self, sourceNode, edgeVal, destNode):
        """
        Add an edge to source node given the destination. The contents of the
        edge is what is going to be written out when randomly writing. If the
        edge already exists, incrament that edges number of occurances (used to
        calculate the weights). If the edge does not exist, just create a new
        edge for that source node.
        """

        found = False
        index = -1
        for edge in sourceNode.edges:
            if (edgeVal == edge.val):
                found = True
                index = sourceNode.edges.index(edge)
                break

        if (found):
            sourceNode.edges[index].numOccurances += 1
        else:
            sourceNode.edges.append(Edge(edgeVal, destNode))
        sourceNode.totalEdges += 1


    def getEdge(self, node):
        """
        Goes thorugh the edges of a given node and picks an edge based on the
        edges probabilities. If there are no edges to the node. Then None is
        returned. After this happens the client should pick a random node in the
        graph.
        """
        if len(node.edges) == 0:
            return None
        return node.pickEdge()


    def getRandomNode(self):
        return random.choice(self.nodes)

    def printHelper(self):
        for node in self.nodes:
            print(node)
            for edge in self.nodes[node].edges:
                print("  ", edge)


class Node:
    def __init__(self, val):
        self.val = list(val)
        # Key: value that edge holds, Value: edge objects
        self.edges = []
        # Thoeretical number of edges from this node. Note: len(edges)
        # doesn't account for the same edge but total edges does. This is
        # used to calculate the probabilities
        self.totalEdges = 0

    def pickEdge(self):
        """
        Pick an edge based on the weights of each edge to be picked.
        """
        self.createWeights()
        r = random.random()
        for edge in self.edges:
            if r < edge.weight:
                return edge
            else:
                r -= edge.weight


    def createWeights(self):
        """
        Goes through edges and sets weights based on the total edges of this
        node and the number of occurences of a given edge.
        """
        for edge in self.edges:
            edge.setWeight(self.totalEdges)




class Edge:
    def __init__(self, val, dest):
        self.val = val
        self.dest = dest
        self.numOccurances = 1
        self.weight = 0

    def setWeight(self, totalEdges):
        self.weight = self.numOccurances / totalEdges

    def getVal(self):
        return val
