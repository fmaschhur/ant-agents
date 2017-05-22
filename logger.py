import tkinter as tk
import math
from datetime import datetime


class Logger:
    def __init__(self, world, tk_root, scale):
        self.world = world
        self.curr_state = None
        self.state_history = []
        self.file = open("log_" + datetime.now().strftime('%H:%M:%S_%d%m%y') + ".txt", "w")

        self.tk_canvas = tk.Canvas(tk_root, width=world.graph.x_size * scale, height=world.graph.y_size * scale)
        self.tk_canvas.pack()
        self.scale = scale

    def write_log(self):
        self.file.write("Cycle "+ str(self.curr_state[0]) + " : Nest =" + " " + str(self.curr_state[1]) + " , " + str(self.curr_state[2]) + "\n\t\t " + str(self.curr_state[3]))
        self.file.write("\n---\n")

    def get_curr_state(self):
        node_states = {}
        edge_states = []
        nest_node = None

        for (x, y) in self.world.graph.nodes:
            node = self.world.graph.nodes[(x, y)]
            node_states[(x, y)] = (node.food, node.value, [])
            if self.world.graph.nodes[(x, y)].nest:
                nest_node = (x, y)
        for ant in self.world.ants:
            ant_state = 1 if ant.carrfood else 0
            node_states[(ant.currpos.x_pos, ant.currpos.y_pos)][2].append(ant_state)
        for carrier in self.world.carriers:
            carrier_state = 2 if carrier.carrfood else 3
            node_states[(ant.currpos.x_pos, ant.currpos.y_pos)][2].append(carrier_state)
        for explorer in self.world.explorers:
            explorer_state = 4 if explorer.carrfood else 5
            node_states[(ant.currpos.x_pos, ant.currpos.y_pos)][2].append(explorer_state)
        for edge in self.world.graph.edges:
            edge_states.append(((edge.node1.x_pos, edge.node1.y_pos), (edge.node2.x_pos, edge.node2.y_pos),
                                edge.food_pheromone, edge.nest_pheromone))

        self.curr_state = (len(self.state_history), nest_node, node_states, edge_states)
        self.state_history.append(self.curr_state)

    def print_curr_state(self):
        print("Cycle", self.curr_state[0], ": Nest =", self.curr_state[1], ",", self.curr_state[2],
              "\n\t\t", self.curr_state[3])
        print('---')

    def draw_curr_state(self):
        canvas = self.tk_canvas
        canvas.delete("all")
        s = self.scale

        nest_node = self.curr_state[1]
        node_states = self.curr_state[2]
        edge_states = self.curr_state[3]

        for edge in edge_states:
            x_1 = edge[0][0]
            y_1 = edge[0][1]
            x_2 = edge[1][0]
            y_2 = edge[1][1]
            food_pheromon = round(edge[2], 2)
            nest_pheromon = round(edge[3], 2)

            canvas.create_line((x_1 - 1) * s + s * 1 / 2, (y_1 - 1) * s + s * 1 / 2,
                               (x_2 - 1) * s + s * 1 / 2, (y_2 - 1) * s + s * 1 / 2)

            if y_1 == y_2:
                if food_pheromon > 0:
                    canvas.create_text((x_1 - 1) * s + s, (y_1 - 1) * s + s * 1/2 - s * 1/10, text=food_pheromon,
                                       fill='red')
                if nest_pheromon > 0:
                    canvas.create_text((x_1 - 1) * s + s, (y_1 - 1) * s + s * 1/2 + s * 1/10, text=nest_pheromon,
                                       fill='blue')
            else:
                if food_pheromon > 0:
                    canvas.create_text((x_1 - 1) * s + s * 1 / 2 - s * 1 / 20, (y_1 - 1) * s + s, text=food_pheromon,
                                       fill='red', anchor=tk.E)
                if nest_pheromon > 0:
                    canvas.create_text((x_1 - 1) * s + s * 1 / 2 + s * 1 / 20, (y_1 - 1) * s + s, text=nest_pheromon,
                                       fill='blue', anchor=tk.W)

        for (x, y) in node_states:
            food_amount = node_states[(x, y)][0]
            if (x, y) == nest_node:
                line_color = 'blue'
                text_color = 'blue'
            elif food_amount > 0:
                line_color = 'red'
                text_color = 'red'
            else:
                line_color = 'black'
                text_color = 'black'
            canvas.create_oval((x - 1) * s + s * 2 / 6, (y - 1) * s + s * 2 / 6,
                               (x - 1) * s + s * 4 / 6, (y - 1) * s + s * 4 / 6, fill='white', outline=line_color)
            if food_amount > 0:
                canvas.create_text((x - 1) * s + s * 1 / 2, (y - 1) * s + s * 1 / 2, text=food_amount, fill=text_color)

            node_ants = node_states[(x, y)][2]
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
