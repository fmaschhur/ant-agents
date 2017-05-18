class Logger:

    def __init__(self, world):
        self.world = world
        self.node_state = [[None for x in range(self.world.graph.x_size)] for y in range(self.world.graph.y_size)]
        self.edge_state = [[None for x in range((self.world.graph.x_size * 2) - 1)] for y in range(self.world.graph.y_size)]

        # for y in range((self.world.graph.y_size - 1) * 2):
        #     self.edge_state.append([])
        #     if y % 2 == 0:
        #         # self.edge_state[y] = [None for x in range(self.world.graph.x_size - 1)]
        #         self.edge_state[y] = [None]
        #     else:
        #         self.edge_state[y] = [None for x in range(self.world.graph.x_size)]

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
        for edge in graph.edges:
            if edge.node1.y_pos == edge.node2.y_pos and edge.node1.x_pos < edge.node2.x_pos:
                self.edge_state[edge.node1.y_pos - 1][(edge.node1.x_pos * 2) - 1] = (edge.get_food_pheromone(), edge.get_nest_pheromone())
            if edge.node1.y_pos < edge.node2.y_pos and edge.node1.x_pos == edge.node2.x_pos:
                self.edge_state[edge.node1.y_pos - 1][(edge.node1.x_pos - 1) * 2] = (edge.get_food_pheromone(), edge.get_nest_pheromone())

            # x, y
            # if edge.node1.y_pos == edge.node2.y_pos:
            #     y = (edge.node1.y_pos - 1)
            #     x = (edge.node1.x_pos - 1)
            # if edge.node1.y_pos < edge.node2.y_pos:
            #     y = (edge.node1.y_pos - 1) * 2
            #     x = (edge.node1.x_pos - 1)
            # self.edge_state[y][x] = (edge.get_food_pheromone(), edge.get_nest_pheromone())

    def print_state(self):
        for i in range(len(self.node_state)):
            node_row = self.node_state[i]
            edge_row = self.edge_state[i]

            row_str = ''
            for j in range(len(node_row)):
                row_str += '[🍔{:2d} 🐜{:2d}]'.format(node_row[j][0], len(node_row[j][1]))
                if j != len(node_row) - 1:
                    row_str += ' --- 🍔{:4.2f} 🏠{:4.2f} --- '.format(edge_row[(j * 2) + 1][0], edge_row[(j * 2) + 1][1])
            print(row_str)

            edge_row_str_empty = ''
            edge_row_str_values = ''
            if i != len(self.node_state) - 1:
                for j in range(len(node_row)):
                    edge_row_str_empty += '      |                            '
                    edge_row_str_values += '🍔{:4.2f}|🏠{:4.2f}                     '.format(edge_row[j * 2][0], edge_row[j * 2][1])
            print(edge_row_str_empty)
            print(edge_row_str_values)
            print(edge_row_str_empty)

        print('---')



        # print(self.node_state)
        # print(self.edge_state)
        # print ('#edges: ' + str(len(self.world.graph.edges)))
        # edge_coordinates = ''
        # for edge in self.world.graph.edges:
        #     edge_coordinates += str((edge.node1.x_pos, edge.node1.y_pos)) + '->' + str((edge.node2.x_pos, edge.node2.y_pos)) + ', '
        # print(edge_coordinates)
        # print('---------------------------')

        # for row in node_state:
        #     row_string = ''
        #     for node in row:
        #         row_string += 'x - '
        #     print(row_string[:-3])
        #     row_string = ''
        #     for node in row:
        #         row_string += '|   '
        #     print(row_string[:-3])

