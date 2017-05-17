import world.main as main


class Logger:

    node_state = None
    edge_state = None

    @staticmethod
    def get_state(self):
        graph = main.ant_world.graph_obj
        ants = main.ant_world.ants

        for y in range(1, graph.y):
            for x in range(1, graph.x):
                food_state = graph.nodes[(x,y)].food
                node_ants = []
                for ant in ants:
                    if ant.currpos == graph.nodes[(x,y)]:
                        ant_state = 1 if ant.carrfood else 0
                        node_ants.append(ant_state)
            self.node_state.append((food_state, node_ants))

    @staticmethod
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

