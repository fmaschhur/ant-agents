class Logger:

    def __init__(self, world):
        self.world = world
        self.node_state = [[None for i in range(self.world.graph.x_size)] for j in range(self.world.graph.y_size)]
        self.edge_state = []

    def get_state(self):
        graph = self.world.graph
        ants = self.world.ants

        # for node in graph.get_nodes():
        #      node_food = node.get_food()
        #      node.get_x_y()

        for y in range(1, graph.y_size):
            for x in range(1, graph.x_size):
                node_food_state = graph.nodes[(x, y)].food
                node_ants = []
                # for ant in ants:
                #     if ant.currpos == graph.get_node(x, y):
                #         ant_state = 1 if ant.carrfood else 0
                #         node_ants.append(ant_state)
                self.node_state[y][x] = (node_food_state, node_ants)

    def print_state(self):
        print(self.node_state)



        # for row in node_state:
        #     row_string = ''
        #     for node in row:
        #         row_string += 'x - '
        #     print(row_string[:-3])
        #     row_string = ''
        #     for node in row:
        #         row_string += '|   '
        #     print(row_string[:-3])

