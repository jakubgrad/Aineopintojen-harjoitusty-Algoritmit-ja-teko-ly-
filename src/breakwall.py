from heapq import * 

class Edge:
    def __init__(self, v, weight):
        self.end = v
        self.weight = weight

class BestRoute:
    def __init__(self,n,r):
        self.r = r
        self.h = []
        self.adjacencylist=[]
        self.n=n
        #self.adjacencylist.append([])
        for i in range(1,n+2):
            self.adjacencylist.append([])
        
    def add_road(self,a,b,x):
        self.adjacencylist[a].append(Edge(b,x))
        self.adjacencylist[b].append(Edge(a,x))

    def find_route(self,a,b):
        return self.dijkstra(a,b);

    def dijkstra(self,a,b): #we get distance[v] to every v from a.
        distance=[]
        processed=[]
        for i in range(1,self.n+2):
            distance.append(100000)
            processed.append(False)
        distance[a] = 0
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
        ad = 1
        #print(self.adjacencylist[ad][0].end,self.adjacencylist[ad][0].weight,self.adjacencylist[ad][1].end,self.adjacencylist[ad][1].weight,self.adjacencylist[ad][2].end,self.adjacencylist[ad][2].weight)
        return distance[b]//2   
    
def count(r):
    m = len(r)-2
    n = len(r[0])-2
    br = BestRoute(n*m,r)
    for i in range(1,m+1):
        for j in range(1,n+1):
            if r[i][j] == "A":
                A = (i-1)*n + (j-1)
            if r[i][j] == "B":
                B = (i-1)*n + (j-1)

    for i in range(1,m+1):
        for j in range(1,n+1):
            if r[i+1][j] == "#":
                pass
            elif r[i+1][j] == "*" and r[i][j] == "*": #r[i+1][j] == "." or r[i+1][j] == "B" or r[i+1][j] == "A":
                br.add_road((i-1)*n + (j-1),(i)*n + (j-1),2)
            elif r[i+1][j] == "*" or r[i][j] == "*": #r[i+1][j] == "." or r[i+1][j] == "B" or r[i+1][j] == "A":
                br.add_road((i-1)*n + (j-1),(i)*n + (j-1),1)
            else:
                br.add_road((i-1)*n + (j-1),(i)*n + (j-1),0)
            if r[i][j+1] == "#":
                pass
            elif r[i][j+1] == "*" and r[i][j] == "*":#r[i][j+1] == "." or r[i][j+1] == "B" or r[i][j+1] == "A":
                br.add_road((i-1)*n + (j-1),(i-1)*n + (j),2)
            elif r[i][j+1] == "*" or r[i][j] == "*":#r[i][j+1] == "." or r[i][j+1] == "B" or r[i][j+1] == "A":
                br.add_road((i-1)*n + (j-1),(i-1)*n + (j),1)
            else:
                br.add_road((i-1)*n + (j-1),(i-1)*n + (j),0)
                
            
    print(f"A: {A}")
    print(f"B: {B}")
    return br.find_route(A,B)+1



