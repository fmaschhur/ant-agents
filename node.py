class Node(object):

    def __init__(self, food, edges):    # initializes a single node and associates a list of edges to it
        self.food = food            # int, x if nest, 0 else
        self.edges = edges          # list of edges, can be empty, argument has to be 'None' for this to happen

