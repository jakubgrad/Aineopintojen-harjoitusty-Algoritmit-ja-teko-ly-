from heapq import * 
    
class Edge:
    def __init__(self, v, weight):
        self.end = v
        self.weight = weight

class Dijkstra:
    def __init__(self,map):
        self.map = map 
        self.number_of_nodes = len(map)*len(map[0])
        self.adjacencylist = [[] for _ in range(self.number_of_nodes)]
        self.num_rows = len(self.map)
        self.len_row = len(self.map[0])
        self.create_edges_from_map()

    def __str__(self):
        return f'Number of nodes: {self.number_of_nodes}'

    def add_edge(self,a,b,x):
        self.adjacencylist[a].append(Edge(b,x))
        self.adjacencylist[b].append(Edge(a,x))

    def edge_number(self, i,j):
        return i*self.len_row+j

    def create_edges_from_map(self):
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


