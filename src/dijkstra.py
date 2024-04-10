
from heapq import *


class Presentation:
    def __init__(self, map):
        self.map = [list(row) for row in map]
        self.num_rows = len(self.map)
        self.len_row = len(self.map[0])
        self.slides = []

    def __str__(self):
        return str(self.map)

    def mark(self, coordinates):
        i, j = coordinates
        self.map[i][j] = "A"

    def print_map(self):
        rotated_map_list = [[''] * self.num_rows for _ in range(self.len_row)]
        rotated_regular_map = [[''] * self.num_rows for _ in range(self.len_row)]

        for i in range(self.num_rows):
            for j in range(self.len_row):
                rotated_regular_map[self.len_row - j - 1][i] = self.map[i][j]

        rmap = ""
        for row in rotated_regular_map:
            rmap = rmap + (" ".join(row)) + "\n"

        return rmap


class Edge:
    """A class with which we can keep track of what edges and with what weights are the neighbours of a node

    Attributes:
        end: the terminating edge
        weight: the weight or cost to access edge
    """

    def __init__(self, coordinates, weight):
        self.end = coordinates
        self.weight = weight


class Dijkstra:
    """A class that can turn arrays describing a map into a graph and find the shortest path using Dijkstra algorithm

    Attributes:
        map: an array of rows, each describing a row of squares, where each square is an obstacle or is free
        number_of_nodes: number of nodes in total equal to number of squares
        adjacencylist: an array of arrays, one for each square/node
        num_rows: number of rows of the map
        len_row: length of a single row
    """

    def __init__(self, map):
        self.presentation = Presentation(map)
        self.map = [list(row) for row in map]
        self.number_of_nodes = len(map) * len(map[0])
        self.adjacencylist = [[] for _ in range(self.number_of_nodes)]
        self.num_rows = len(self.map)
        self.len_row = len(self.map[0])
        self.create_edges_from_map()
        self.slides = False

    def __str__(self):
        """A function used to test if Dijkstra class correctly found the number of nodes

        Returns:
            A string describing the number of nodes 
        """

        return f'Number of nodes: {self.number_of_nodes}'

    def add_edge(self, a, b, x):
        """A function used to add an edge between two nodes

        Args:
            a: node on one side
            b: node on the other side
            x: the weight/cost of the edge
        """

        self.adjacencylist[a].append(Edge(b, x))
        self.adjacencylist[b].append(Edge(a, x))

    def coordinates_to_node(self, coordinates):
        """A handy function for converting coordinates into a node number

        Args:
            coordinates: tuple of (i, j) representing row and column indices

        Returns:
            A node number
        """

        i, j = coordinates
        return i * self.len_row + j

    def create_edges_from_map(self):
        """A function that turns an array of rows into a graph that can be used by Dijkstra

        It is only run once during the initialization of the class
        """

        nrows = self.num_rows
        lrow = self.len_row
        map = self.presentation.map

        for i in range(nrows):
            nrows = nrows - 1
            for j in range(lrow):
                if map[i][j] == "T":
                    continue
                else:
                    if j < lrow:
                        if map[i][j + 1] == ".":
                            self.add_edge(self.coordinates_to_node((i, j)),
                                          self.coordinates_to_node((i, j + 1)), 1)
                    if nrows != 0:
                        if map[i + 1][j] == ".":
                            self.add_edge(self.coordinates_to_node((i, j)),
                                          self.coordinates_to_node((i + 1, j)), 1)
                        if map[i + 1][j + 1] == ".":
                            self.add_edge(self.coordinates_to_node((i, j)),
                                          self.coordinates_to_node((i + 1, j + 1)), 1.41)

    def find_shortest_path(self, start_coordinates, end_coordinates, slides=False):
        """Actual implementation of the Dijkstra algorithm

        Args:
            start_coordinates: starting coordinates (i, j)
            end_coordinates: goal coordinates (i, j)

        Returns:
            The shortest path to 2 decimal digits
        """

        a = self.coordinates_to_node(start_coordinates)
        b = self.coordinates_to_node(end_coordinates)
        processed = [False] * self.number_of_nodes
        distance = [10000] * self.number_of_nodes
        distance[a] = 0
        h = []
        heapify(h)
        heappush(h, (0, a))
        while len(h) > 0:
            next = heappop(h)
            u = next[1]
            if not processed[u]:
                processed[u] = True
                for edge in self.adjacencylist[u]:
                    v = edge.end
                    if distance[v] > distance[u] + edge.weight:
                        distance[v] = distance[u] + edge.weight
                        heappush(h, (distance[v], v))

        if distance[b] == 10000:
            distance[b] = -1
        return round(distance[b], 2)
