from heapq import * 
    
class Edge:
    """A class with which we can keep track of what edges and with what weights are the neighbours of a node

    Attributes:
        end: the terminating edge
        weight: the weight or cost to access edge
    """

    def __init__(self, v, weight):
        self.end = v
        self.weight = weight
        """Class constructor, that creates a new edge
        
        Args:
            end: the terminating edge
            weight: the weight or cost to access edge
        """

class Dijkstra:
    """A class that can turn arrays describing a map into a graph and find the shortest path using Dijkstra algorithm
    
    Attributes:
        map: an array of rows, each describing a row of squares, where each square is an obstacle or is free
        number_of_nodes: number of nodes in total equal to number of squares
        adjacencylist: an array of arrays, one for each square/node
        num_rows: number of rows of the map
        len_row: length of a single row
    """

    def __init__(self,map):
        self.map = map 
        self.number_of_nodes = len(map)*len(map[0])
        self.adjacencylist = [[] for _ in range(self.number_of_nodes)]
        self.num_rows = len(self.map)
        self.len_row = len(self.map[0])
        self.create_edges_from_map()

    def __str__(self):
        """A function used to test if Dijkstra class correctly found the number of nodes
        
        Returns:
            A string describing the number of nodes 
        """

        return f'Number of nodes: {self.number_of_nodes}'
        
    def add_edge(self,a,b,x):
        """A function used to add an edge between two nodes

        Args:
            a: node on one side
            b: node on the other side
            x: the weight/cost of the edge
        """

        self.adjacencylist[a].append(Edge(b,x))
        self.adjacencylist[b].append(Edge(a,x))

    def edge_number(self, i,j):
        """A handy function for converting a position of a square on the map into a node
    
        Args:
            i: row of the square
            j: column (or index in the row) of the square

        Returns:
            A node number
        """

        return i*self.len_row+j

    def create_edges_from_map(self):
        """A function that turns an array of rows into a graph that can be used by Dijkstra
        
        Is only run once during the initialization of the class
        """

        nrows = self.num_rows
        for i in range(len(self.map)):
            nrows=nrows-1
            for j in range(self.len_row):
                if self.map[i][j] == "T":
                    continue
                else:
                    if j<self.len_row:
                        if self.map[i][j+1] == ".":
                            self.add_edge(self.edge_number(i,j),self.edge_number(i,j+1),1)
                    if self.num_rows !=0:
                        if self.map[i+1][j] == ".":
                            self.add_edge(self.edge_number(i,j),self.edge_number(i+1,j),1)
                        if self.map[i+1][j+1] == ".":
                            self.add_edge(self.edge_number(i,j),self.edge_number(i+1,j+1),1.41)

    def find_shortest_path(self,a,b):
        """Actual implementation of the Dijkstra algorithm

        Args:
            a: starting node
            b: goal node

        Returns:
            The shortest path to 2 decimal digits
        """

        processed = [False] * self.number_of_nodes
        distance = [10000] * self.number_of_nodes
        distance[a]=0
        h=[]
        heapify(h)
        heappush(h, (0,a))
        while len(h)>0:
            next = heappop(h)
            u = next[1]
            if not processed[u]:
                processed[u] = True
                for edge in self.adjacencylist[u]:
                    v = edge.end
                    if distance[v] > distance[u] + edge.weight:
                        distance[v] = distance[u] + edge.weight
                        heappush(h, (distance[v],v))
            
        if distance[b] == 10000:
            distance[b] = -1
        return round(distance[b],2)


