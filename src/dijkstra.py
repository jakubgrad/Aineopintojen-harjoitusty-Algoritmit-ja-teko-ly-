from heapq import heapify, heappush, heappop

class Edge:
    """A class with which we can keep track of what edges and with what weights
       are the neighbours of a node

    Attributes:
        end: the terminating edge
        weight: the weight or cost to access edge
    """

    def __init__(self, v, weight):
        """Class constructor, that creates a new edge
        Args:
            v: the terminating edge
            weight: the weight or cost to access edge

        Parameters:
            end: the terminating edge
            weight: the weight or cost to access edge
        """

        self.end = v
        self.weight = weight


class Dijkstra:
    """A class that can turn arrays describing a map into a graph
       and find the shortest path using Dijkstra algorithm

    Attributes:
        map: an array of rows, each describing a row of squares, where each square
            is an obstacle or is free
        number_of_nodes: number of nodes in total equal to number of squares
        adjacencylist: an array of arrays, one for each square/node
        num_rows: number of rows of the map
        len_row: length of a single row
    """

    def __init__(self, source_map):
        """Dijkstra's class constructor

        Args:   
            map: the map on which to run Dijkstra
        """

        self.map = source_map
        self.slide_map = source_map
        self.slides = []
        self.number_of_nodes = len(source_map)*len(source_map[0])
        self.adjacencylist = [[] for _ in range(self.number_of_nodes)]
        self.len_row = len(self.map[0])
        self.vertices = []
        self.visual = False
        heapify(self.vertices)
        self.create_edges_from_map()

    def mark(self, coordinates, mark):
        """A function that marks a place on the grid with a character

        Args:
            coordinates: coordinates on which to place the character
            character: character to be place
        """

        if self.visual:
            i, j = coordinates
            self.slide_map[i][j] = mark

    def add_slide(self):
        """ A function that adds a snapshot of the algorithm
            to the slides list that is passed on to UI

        Attributes:
            visual: if False, no slides are added. This is because 
                    I want to make performance tests in the future
        """

        if self.visual:
            rotated_regular_map = [
                [''] * len(self.map) for _ in range(self.len_row)]

            for i in range(len(self.map)):
                for j in range(self.len_row):
                    rotated_regular_map[self.len_row -
                                        j - 1][i] = self.slide_map[i][j]

            rmap = ""
            for row in rotated_regular_map:
                rmap = rmap + (" ".join(row)) + "\n"

            self.slides.append(rmap)

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

        if a not in self.vertices:
            heappush(self.vertices,  a)
        if b not in self.vertices:
            heappush(self.vertices,  b)

        self.adjacencylist[a].append(Edge(b, x))
        self.adjacencylist[b].append(Edge(a, x))

    def edge_number(self, i, j):
        """A handy function for converting a position of a square on the map into a node number

        Args:
            i: row of the square
            j: column (or index in the row) of the square

        Returns:
            A node number
        """

        return i*self.len_row+j

    def coordinates(self, node_number):
        """A handy function for converting a node number into a position of a square on the map

        Args:
            node_number, used to uniquely identify a field

        Returns:
            A tuple of (i,j), where
                i: row of the square
                j: column (or index in the row) of the square
        """

        i = node_number // self.len_row
        j = node_number % self.len_row
        return (i, j)

    def within_map(self, coordinates):
        """A handy function that tells whether coordinates lie within the map

        Args: 
            coordinates: the coordinates to be checked

        Returns: true or false depending on whether the cooridnates are on the map
        """

        i, j = coordinates
        if 0 <= i < len(self.map) and 0 <= j < self.len_row:
            return True
        return False

    def create_edges_from_map(self):
        """A function that turns an array of rows into a graph that can be used by Dijkstra

        Is only run once during the initialization of the class
        """

        nrows = len(self.map)
        for i in range(nrows):
            for j in range(self.len_row):
                if self.map[i][j] == "T":
                    continue
                if self.within_map((i, j+1)) and j < self.len_row and self.map[i][j+1] == ".":
                    self.add_edge(self.edge_number(i, j),
                                  self.edge_number(i, j+1), 1)

                if self.within_map((i+1, j)) and self.map[i+1][j] == ".":
                    self.add_edge(self.edge_number(i, j),
                                  self.edge_number(i+1, j), 1)

                if self.within_map((i+1, j+1)) and self.map[i+1][j+1] == ".":
                    self.add_edge(self.edge_number(i, j),
                                  self.edge_number(i+1, j+1), 1.41)

    def find_shortest_path(self, start_coordinates, end_coordinates, slides=False, visual=False):
        """Actual implementation of the Dijkstra algorithm

        Args:
            a: starting node
            b: goal node

        Returns:
            The shortest path to 2 decimal digits
        """

        self.slides = slides
        self.visual = visual

        a = self.edge_number(*start_coordinates)
        b = self.edge_number(*end_coordinates)

        if a == b:
            return None

        processed = [False] * self.number_of_nodes
        distance = [10000] * self.number_of_nodes
        distance[a] = 0
        h = []
        heapify(h)
        heappush(h, (0, a))

        while len(h) > 0:
            next_node = heappop(h)
            u = next_node[1]
            processed[u] = True
            self.mark(self.coordinates(u), "V")
            self.add_slide()
            for edge in self.adjacencylist[u]:
                v = edge.end
                if distance[v] > distance[u] + edge.weight:
                    distance[v] = distance[u] + edge.weight
                    heappush(h, (distance[v], v))
            if u == b:
                break

        self.mark(start_coordinates, "S")
        self.mark(end_coordinates, "G")
        self.add_slide()

        if distance[b] == 10000:
            distance[b] = -1
        return round(distance[b], 2)
