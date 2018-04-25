import Graph
import pickle
import argparse
from urllib import request
from enum import Enum
import sys

class Tokenization(Enum):
    word = 1
    character = 2
    byte = 3
    none = 4


class RandomWriter(object):
    """A Markov chain based random data generator.
    """

    def __init__(self, level, tokenization=None):
        """Initialize a random writer.

        Args:
          level: Number of tokens to take in on.
          tokenization: A tokenization enum. Determines what tokenization
          should be based on

        """
        self.level = level
        self.tokenization = tokenization
        self.graph = Graph.Graph()


    def generate(self):
        """Generate tokens using the built model.

        Yield random tokens using the build model. The generator can output
        tokens indefinitly.
        If node does not have any edges, a new random node will be picked.
        
        TODO: instead of picking a random, pick one that has the next tense

        """
        #Pick a random node, only happens for generation of first token
        node = self.graph.getRandomNode()
        while True:
            edge = self.graph.getEdge(node)
            #There was no edges for the node, so pick another random node
            while edge is None:
                node = self.graph.getRandomNode()
                edge = self.graph.getEdge(node)
            yield edge.val
            # Actual traverse
            node = edge.dest

    def generate_file(self, filename, amount):
        """Write a file using the model.

        Args:
          filename: The name of the file to write output to.
          amount: The number of tokens to write.

        Character and byte tokens just output them sequentially, but the other
        tokens have spaces in between them.

        """
        gen = self.generate()
        with open(filename, 'w', encoding='utf-8') as fi:
            for i in range(amount):
                fi.write(str(next(gen)))
                fi.write(" ")


    def train(self, data):
        """Compute the probabilities based on the data given.

        If the tokenization mode is none, data must be an iterable. 
        If the tokenization mode is character or word, then data must be
        a string. 
        If the tokenization mode is byte, then data must be a bytes. 
        If the type is wrong raise TypeError.

        """
        #cat = ''
        #with open(data, 'r', encoding='utf-8') as fi:
        #    cat += fi.read()
        #    

        ##print(cat)

        #cat = cat.split(' ')
        ##print(cat)

        cat = data.split(' ')

        it = iter(cat)

        currentNodeData = []

        for i in range(self.level):
            try:
                currentNodeData.append(next(it))
            except Exception as e:
                raise AttributeError("Level was too high for given data set")

        prevNode = self.graph.addNode(currentNodeData)


        # Creates all nodes
        while True:
            try:
                windowVal = next(it)
                #print('window val is:', windowVal)
            except Exception:
                break #reached the end of data
            currentNodeData.append(windowVal)
            currentNodeData.pop(0)
            # make a node with the currentNodeData
            currentNode = self.graph.addNode(currentNodeData)
            self.graph.addEdge(prevNode, windowVal, currentNode)
            prevNode = currentNode




def trainModel(text):
    rr.train(text) 

def generate_tweet(num_words):
    """Write a file using the model.

    Args:
      filename: The name of the file to write output to.
      amount: The number of tokens to write.

    Character and byte tokens just output them sequentially, but the other
    tokens have spaces in between them.

    """

    result = ""
    gen = rr.generate()
    for i in range(num_words):
        result += (str(next(gen)))
        result += (" ")
    return result


#rr = RandomWriter(1, Tokenization.word)
#trainModel("This is a thing that has a this a what we want")
#print(generate_tweet(10))

