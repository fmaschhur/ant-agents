import tkinter as tk
import math


class Logger:
    def __init__(self, world, tk_root, scale):
        self.world = world
        self.curr_state = None
        self.state_history = []

        self.tk_canvas = tk.Canvas(tk_root, width=world.graph.x_size * scale, height=world.graph.y_size * scale)
        self.tk_canvas.pack()
        self.scale = scale

        # self.node_state = [[None for x in range(self.world.graph.x_size)] for y in range(self.world.graph.y_size)]
        # self.edge_state = [[None for x in range((self.world.graph.x_size * 2) - 1)] for y in range(self.world.graph.y_size)]

    def get_curr_state(self):
        node_states = {}
        edge_states = []

        for (x, y) in self.world.graph.nodes:
            node_states[(x, y)] = (self.world.graph.nodes[(x, y)].food, [])
        for ant in self.world.ants:
            ant_state = 1 if ant.carrfood else 0
            node_states[(ant.currpos.x_pos, ant.currpos.y_pos)][1].append(ant_state)
        for edge in self.world.graph.edges:
            edge_states.append(((edge.node1.x_pos, edge.node1.y_pos), (edge.node2.x_pos, edge.node2.y_pos),
                                edge.food_pheromone, edge.nest_pheromone))

        self.curr_state = (len(self.state_history), node_states, edge_states)
        self.state_history.append(self.curr_state)

        # for y in range(graph.y_size):
        #     for x in range(graph.x_size):
        #         node_food_state = graph.nodes[(x+1, y+1)].food
        #         self.node_state[y][x] = (node_food_state, [])
        # for ant in ants:
        #     ant_state = 1 if ant.carrfood else 0
        #     self.node_state[ant.currpos.y_pos-1][ant.currpos.x_pos-1][1].append(ant_state)
        #
        # # TODO: Incomplete, but works because edges are created following this pattern
        # for edge in graph.edges:
        #     if edge.node1.y_pos == edge.node2.y_pos and edge.node1.x_pos < edge.node2.x_pos:
        #         self.edge_state[edge.node1.y_pos - 1][(edge.node1.x_pos * 2) - 1] = (edge.get_food_pheromone(), edge.get_nest_pheromone())
        #     if edge.node1.y_pos < edge.node2.y_pos and edge.node1.x_pos == edge.node2.x_pos:
        #         self.edge_state[edge.node1.y_pos - 1][(edge.node1.x_pos - 1) * 2] = (edge.get_food_pheromone(), edge.get_nest_pheromone())

    def print_curr_state(self):
        print("Cycle", self.curr_state[0], ":", self.curr_state[1], "\n\t\t", self.curr_state[2])

        # for i in range(len(self.node_state)):
        #     node_row = self.node_state[i]
        #     edge_row = self.edge_state[i]
        #
        #     row_str = ''
        #     for j in range(len(node_row)):
        #         row_str += '[🍔{:2d} 🐜{:2d}]'.format(node_row[j][0], len(node_row[j][1]))
        #         if j != len(node_row) - 1:
        #             row_str += ' --- 🍔{:4.2f} 🏠{:4.2f} --- '.format(edge_row[(j * 2) + 1][0], edge_row[(j * 2) + 1][1])
        #     print(row_str)
        #
        #     edge_row_str_empty = ''
        #     edge_row_str_values = ''
        #     if i != len(self.node_state) - 1:
        #         for j in range(len(node_row)):
        #             edge_row_str_empty += '      |                            '
        #             edge_row_str_values += '🍔{:4.2f}|🏠{:4.2f}                     '.format(edge_row[j * 2][0], edge_row[j * 2][1])
        #     print(edge_row_str_empty)
        #     print(edge_row_str_values)
        #     print(edge_row_str_empty)

        print('---')

    def draw_curr_state(self):
        canvas = self.tk_canvas
        canvas.delete("all")
        s = self.scale

        node_states = self.curr_state[1]
        edge_states = self.curr_state[2]

        for edge in edge_states:
            x_1 = edge[0][0]
            y_1 = edge[0][1]
            x_2 = edge[1][0]
            y_2 = edge[1][1]
            canvas.create_line((x_1 - 1) * s + s * 1 / 2, (y_1 - 1) * s + s * 1 / 2,
                               (x_2 - 1) * s + s * 1 / 2, (y_2 - 1) * s + s * 1 / 2)
            # if edge[2][0]:
            #     # TODO PRINT FOODPHEROMONE
            # if edge[2][1]:
            #     # TODO PRINT NESTPHEROMONE
            # if y_1 == y_2:
            #     canvas.create_text((x_1 - 1) * s + s, (y_1  -1))

        for (x, y) in node_states:
            canvas.create_oval((x - 1) * s + s * 2 / 6, (y - 1) * s + s * 2 / 6,
                               (x - 1) * s + s * 4 / 6, (y - 1) * s + s * 4 / 6, fill='white')
            food_amount = node_states[(x, y)][0]
            if food_amount > 0:
                canvas.create_text((x - 1) * s + s * 1 / 2, (y - 1) * s + s * 1 / 2, text=food_amount)

            node_ants = node_states[(x, y)][1]
            for i in range(len(node_ants)):
                r = s * 1 / 6 * 7 / 10
                n = self.world.ants_max
                ant_centers = [(math.cos(2 * math.pi / n * x) * r, math.sin(2 * math.pi / n * x) * r)
                               for x in range(0, n + 1)]
                ant_fill_color = 'black'
                ant_line_color = 'black'
                if node_ants[i] == 1:
                    ant_fill_color = 'red'
                    ant_line_color = 'red'
                canvas.create_oval((x - 1) * s + s * 3 / 6 + ant_centers[i][0] - s * 1 / 3 * 1 / 10,
                                   (y - 1) * s + s * 3 / 6 + ant_centers[i][1] - s * 1 / 3 * 1 / 10,
                                   (x - 1) * s + s * 3 / 6 + ant_centers[i][0] + s * 1 / 3 * 1 / 10,
                                   (y - 1) * s + s * 3 / 6 + ant_centers[i][1] + s * 1 / 3 * 1 / 10,
                                   outline=ant_line_color, fill=ant_fill_color)
