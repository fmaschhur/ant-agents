import tkinter as tk
import math
from position import Position
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
        pass
        # self.file.write("Cycle "+ str(self.curr_state[0]) + " : Nest =" + " " + str(self.curr_state[1]) + " , " + str(self.curr_state[2]) + "\n\t\t " + str(self.curr_state[3]))
        # self.file.write("\n---\n")

    def get_curr_state(self):
        node_states = {}
        edge_states = []

        for (x, y) in self.world.graph.nodes:
            node = self.world.graph.nodes[(x, y)]
            node_states[(x, y)] = (node.job_id(), [])
        for agent in self.world.agents:
            node = agent.position.node
            node_states[(node.x_pos, node.y_pos)][1].append(1)
        for init in self.world.initiators:
            node = init.job.destination
            node_states[(node.x_pos, node.y_pos)][1].append(2)
        for edge in self.world.graph.edges:
            edge_states.append(((edge.node1.x_pos, edge.node1.y_pos), (edge.node2.x_pos, edge.node2.y_pos), edge.length))

        self.curr_state = (len(self.state_history), node_states, edge_states)
        self.state_history.append(self.curr_state)

    def print_curr_state(self):
        pass
        # print("Cycle", self.curr_state[0], ": Nest =", self.curr_state[1], ",", self.curr_state[2],
        #       "\n\t\t", self.curr_state[3])
        # print('---')

    def draw_curr_state(self):
        canvas = self.tk_canvas
        canvas.delete("all")
        s = self.scale
        f_s = int(round(12 * s / 100))  # font size for text output on canvas

        node_states = self.curr_state[1]
        edge_states = self.curr_state[2]

        for edge in edge_states:
            x_1 = edge[0][0]
            y_1 = edge[0][1]
            x_2 = edge[1][0]
            y_2 = edge[1][1]
            distance = round(edge[2], 2)
            # nest_pheromon = round(edge[3], 2)

            canvas.create_line((x_1 - 1) * s + s * 1 / 2, (y_1 - 1) * s + s * 1 / 2,
                               (x_2 - 1) * s + s * 1 / 2, (y_2 - 1) * s + s * 1 / 2)

            if y_1 == y_2:
                if distance > 0:
                    canvas.create_text((x_1 - 1) * s + s, (y_1 - 1) * s + s * 1/2 - s * 1/10, text=distance,
                                        fill='red', font=("Purisa", f_s))
            #     if nest_pheromon > 0:
            #         canvas.create_text((x_1 - 1) * s + s, (y_1 - 1) * s + s * 1/2 + s * 1/10, text=nest_pheromon,
            #                            fill='blue', font=("Purisa", f_s))
            else:
                if distance > 0:
                    canvas.create_text((x_1 - 1) * s + s * 1 / 2 - s * 1 / 20, (y_1 - 1) * s + s, text=distance,
                                        fill='red', anchor=tk.E, font=("Purisa", f_s))
            #     if nest_pheromon > 0:
            #         canvas.create_text((x_1 - 1) * s + s * 1 / 2 + s * 1 / 20, (y_1 - 1) * s + s, text=nest_pheromon,
            #                            fill='blue', anchor=tk.W, font=("Purisa", f_s))

        for (x, y) in node_states:
            #food_amount = node_states[(x, y)][0]
            #node_value = node_states[(x, y)][1]
            if 0:
                line_color = 'blue'
                text_color = 'blue'
            elif 0:#food_amount > 0:
                line_color = 'red'
                text_color = 'red'
            else:
                line_color = 'black'
                text_color = 'black'
            canvas.create_oval((x - 1) * s + s * 2 / 6, (y - 1) * s + s * 2 / 6,
                               (x - 1) * s + s * 4 / 6, (y - 1) * s + s * 4 / 6, fill='white', outline=line_color)
            #if food_amount > 0:
            #    canvas.create_text((x - 1) * s + s * 1 / 2, (y - 1) * s + s * 1 / 2, text=food_amount, fill=text_color,
            #                       font=("Purisa", f_s))

            #if self.task_number == 2:
            #    canvas.create_text((x - 1) * s + s * 4 / 6, (y - 1) * s + s * 2 / 6, text=node_value,
            #                       font=("Purisa", f_s))

            node_agents = node_states[(x, y)][1]
            for i in range(len(node_agents)):
                r = s * 1 / 6 * 7 / 10
                n = self.world.agents_init
                agents_centers = [(math.cos(2 * math.pi / n * x) * r, math.sin(2 * math.pi / n * x) * r)
                               for x in range(0, n)]
                agents_fill_color = 'white'
                agents_line_color = 'black'
                if node_agents[i] == 1:
                    agents_fill_color = 'black'
                    agents_line_color = 'black'
                if node_agents[i] == 2:
                    agents_fill_color = 'green'
                    agents_line_color = 'purple'
                # if node_agents[i] == 3:
                #     agents_fill_color = 'purple'
                #     agents_line_color = 'purple'
                # if node_agents[i] == 4:
                #     agents_fill_color = 'white'
                #     agents_line_color = 'orange'
                # if node_agents[i] == 5:
                #     agents_fill_color = 'orange'
                #     agents_line_color = 'orange'
                canvas.create_oval((x - 1) * s + s * 3 / 6 + agents_centers[i][0] - s * 2 / 3 * 2 / 10,
                                   (y - 1) * s + s * 3 / 6 + agents_centers[i][1] - s * 2 / 3 * 2 / 10,
                                   (x - 1) * s + s * 3 / 6 + agents_centers[i][0] + s * 2 / 3 * 2 / 10,
                                   (y - 1) * s + s * 3 / 6 + agents_centers[i][1] + s * 2 / 3 * 2 / 10,
                                   outline=agents_line_color, fill=agents_fill_color)
