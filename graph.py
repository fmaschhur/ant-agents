from node import Node
from edge import Edge
from math import inf
import random


class Graph(object):

    def __init__(self, params):
        self.x_size = params['size_x']
        self.y_size = params['size_y']
        self.nodes = self.create_nodes()
        if params['thickness']:
            self.edges = self.create_labyrinth_edges(self.x_size, self.y_size, params['dist_min'], params['dist_max'])
        else:
            self.edges = self.create_edges(self.x_size, self.y_size, params['dist_min'], params['dist_max'])

    def create_edges(self, max_x, max_y, dist_min, dist_max):
        edges = []
        for (x, y) in self.nodes:
            me = self.nodes.get((x, y))
            if x < max_x:
                right = self.nodes.get(((x + 1), y))
                edges.append(Edge(me, right, random.randint(dist_min, dist_max)))
            if y < max_y:
                down = self.nodes.get((x, (y + 1)))
                edges.append(Edge(me, down, random.randint(dist_min, dist_max)))
        return edges

    def neighbours_node(self, node):
        x = node.get_x()
        y = node.get_y()
        neighbours = []
        neighbours.append(self.nodes.get((x - 1, y)))
        neighbours.append(self.nodes.get((x + 1, y)))
        neighbours.append(self.nodes.get((x, y - 1)))
        neighbours.append(self.nodes.get((x, y + 1)))
        return [i for i in neighbours if i is not None]

    def create_labyrinth_edges(self, x, y, dist_min, dist_max):
        edges = []
        nodes = list(self.nodes.values())
        current_nodes = []
        current_nodes.append(self.nodes.get((int(x/2), int(y/2))))
        nodes = list(filter(lambda v: v not in current_nodes, nodes))
        while nodes:
            new_current = []
            for node in current_nodes:
                new_current.append(node)
                neighbours = self.neighbours_node(node)
                random.shuffle(neighbours)
                for neighbour in neighbours:
                    if neighbour in nodes:
                        if random.randint(0, 100) > 50:
                            edges.append(Edge(node, neighbour, random.randint(dist_min, dist_max)))
                            new_current.append(neighbour)
                            nodes.remove(neighbour)
            current_nodes = new_current
        return edges

    def create_nodes(self):
        nodes = {}
        for x in range(1, self.x_size + 1):
            for y in range(1, self.y_size + 1):
                add_me = Node([], x, y)
                nodes[(x, y)] = add_me
        return nodes

    def get_distance(self, node_a, node_b):
        return self.get_distance_from_position(Position(node_a), node_b)

    def get_distance_from_position(self, position, node):
        way = self.best_way_from_position(position, node)
        distance = way[0].edge(way[1]).distance
        while distance > 0 and len(way) > 1:
            distance += way[0].edge(way[1]).distance
            way.pop()
        return distance

    def get_position_from_position(self, position, node, distance):
        way = self.best_way_from_position(position, node)
        distance -= way[0].edge(way[1]).distance
        while distance > 0 and len(way) > 1:
            distance -= way[0].edge(way[1]).distance
            way.pop()
        pos = Position(way[0])
        pos.edge = way[0].edge(way[1])
        pos.distance = pos.edge.distance + distance
        return pos

    def best_way_from_position(self, position, node_dest): # TODO besser schreiben
        nodes = list(map(lambda x: [x, inf, None], self.nodes))
        next(x for x in nodes if x[0].equal(position.node))[1] = position.distance
        if position.edge is not None:
            next(x for x in nodes if x[0].equal(position.edge.other_node(position.node)))[1] = position.edge - position.distance
        for i in range(0, 30):
            for node_a in nodes:
                for node_b in nodes:
                    if node_a[0].distance(node_b[0]) + node_b[1] < node_a[1]:
                        node_a[1] = node_a[0].distance(node_b[0]) + node_b[1]
                        node_a[2] = node_b[0]

        return_arr = [node_dest]
        curr = node_dest
        while 1:
            tmp = next(x for x in nodes if x[0].equal(curr))
            return_arr.append(tmp[0])
            curr = tmp[2]
            if tmp[3] is None:
                return return_arr

    def random_node(self):
        a = random.randint(1, self.x_size)
        b = random.randint(1, self.y_size)
        return self.nodes[(a, b)]
