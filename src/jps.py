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

class Node:
    def __init__(self, coordinates, parent=None):
        #optionally the class should take the argument "direction"
        """Class constructor, that creates a new node 
        
        Args:
            i: node's row in the grid
            j: node's column in the grid
            parent: node's parent, so the node from which JPS has reached this node
        """
        self.i, self.j = coordinates 
        self.parent = parent

    def position(self):
        return (self.i,self.j)

class JPS:
    def __init__(self, map):
        self.map = map
        self.num_rows = len(self.map)
        self.len_row = len(self.map[0])
        self.open_set = []
        self.start_node = None
        self.goal_node = None
        """Class constructor, that creates a new node 
        
        Attributes:
            map: the grid on which we set off JPS
            open_set: set of nodes to be expanded
            num_rows: number of rows of the map
            len_row: length of a single row
        """

    def __str__(self):
        """A function used to test if JPS class correctly found the size of map 
        
        Returns:
            A string describing the size of the map
        """

        return f'Number of rows: {self.num_rows}, Length of a row: {self.len_row}'


    def jump(self, node):
        #need to tell if jumping straight or horizontally
        pass

    #def scan_horizontally()
    def within_map(self, coordinates):
        i,j = coordinates
        return True if 0 <= i < self.num_rows and 0 <= j < self.len_row else False

    def free(self, coordinates):
        i,j = coordinates
        return self.map[i][j] == "."

    def find_shortest_path(self,start_coordinates,goal_coordinates):
        self.start_node = Node(start_coordinates)
        self.goal_node = Node(goal_coordinates)
        if self.start_node.position() == self.goal_node.position():
            return 0

        add_tuples = lambda x,y:(x[0]+y[0],x[1]+y[1])
        numbers = list(range(1, 9))
        surrounding_squares = [add_tuples(self.start_node.position(), ((x%3)-1,1-(x//3))) for x in range(0,9)]
        surrounding_squares.remove(self.start_node.position())
        nodes = [Node(x, self.start_node) for x in surrounding_squares if self.within_map(x) and self.free(x)]
        self.open_set.extend(nodes)

        return nodes

