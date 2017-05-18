class Logger:

    def __init__(self, world):
        self.world = world
        self.node_state = [[None for x in range(self.world.graph.x_size)] for y in range(self.world.graph.y_size)]
        self.edge_state = []
        for y in range((self.world.graph.y_size - 1) * 2):
            self.edge_state.append([])
            if y % 2 == 0:
                # self.edge_state[y] = [None for x in range(self.world.graph.x_size - 1)]
                self.edge_state[y] = [None]
            else:
                self.edge_state[y] = [None for x in range(self.world.graph.x_size)]

    def get_state(self):
        graph = self.world.graph
        ants = self.world.ants

        for y in range(graph.y_size):
            for x in range(graph.x_size):
                node_food_state = graph.nodes[(x+1, y+1)].food
                self.node_state[y][x] = (node_food_state, [])
        for ant in ants:
            ant_state = 1 if ant.carrfood else 0
            self.node_state[ant.currpos.y_pos-1][ant.currpos.x_pos-1][1].append(ant_state)

        # TODO: Incomplete, but works because edges are created following this pattern
        # for edge in graph.edges:
        #     x, y
        #     if edge.node1.y_pos == edge.node2.y_pos:
        #         y = (edge.node1.y_pos - 1)
        #         x = (edge.node1.x_pos - 1)
        #     if edge.node1.y_pos < edge.node2.y_pos:
        #         y = (edge.node1.y_pos - 1) * 2
        #         x = (edge.node1.x_pos - 1)
        #     self.edge_state[y][x] = (edge.get_food_pheromone(), edge.get_nest_pheromone())

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

