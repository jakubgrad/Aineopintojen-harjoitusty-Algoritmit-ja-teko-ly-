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
    def __init__(self, coordinates, parent=None, direction=None):
        """Class constructor, that creates a new node 
        
        Args:
            i: node's row in the grid
            j: node's column in the grid
            parent: node's parent, so the node from which JPS has reached this node
        """
        self.i, self.j = coordinates 
        self.parent = parent
        self.direction = direction

    def __str__(self):
        return f"coordinates ({self.i}, {self.j}), parent coordinates {self.parent.position() if self.parent else None}, direction {self.direction}"

    def copy(self):
        return Node((self.i,self.j),parent=self.parent,direction=self.direction)

    def __lt__(self, other):
        if isinstance(other, Node):
            priorities = {(0,1):8, (1,0):7, (0,-1):6, (-1,0):5, (1,1):4,(1,-1):3,(-1,-1):2,(-1,1):1}
            return priorities[self.direction] > priorities[other.direction]

    def position(self):
        return (self.i,self.j)

    def __eq__(self, other):
        if isinstance(other, Node):
            return str(self) == str(other)
            #return self.i == other.i and self.j == other.j and self.parent.i == other.parent.i and self.parent.j == other.parent.j and self.direction == other.direction
        return False

class JPS:
    def __init__(self, map):
        self.map = map
        self.num_rows = len(self.map)
        self.len_row = len(self.map[0])
        self.open_set = []
        self.start_node = None
        self.goal_node = None
        self.open_set_heap = []
        self.closed_set = []
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

    def recreate_path(self,final_node):
        print(final_node.position())
        ans = str(final_node.position())
        last_node = final_node
        while True:
            i = last_node.parent
            if i == None:
                break 
            else:
                print(i.position())
                ans = ans + str(i.position())
                last_node = i
        return ans

    #def scan_horizontally()
    def within_map(self, coordinates):
        i,j = coordinates
        return True if 0 <= i < self.num_rows and 0 <= j < self.len_row else False

    def free(self, coordinates):
        i,j = coordinates
        free_tiles=[".","-","|","x"]
        return self.map[i][j] in free_tiles

    def add_tuples(self, coordinates1, coordinates2):
        return (coordinates1[0]+coordinates2[0],coordinates1[1]+coordinates2[1])

    def subtract_tuples(self, coordinates1, coordinates2):
        return (coordinates1[0]-coordinates2[0],coordinates1[1]-coordinates2[1])
        
    def add_neighbours_of_start_node_to_open_set(self):
        numbers = list(range(1, 9))
        surrounding_squares = [((x%3)-1,1-(x//3)) for x in range(0,9)]
        '''surrounding_squares:
        (-1, 1), ( 0, 1), ( 1, 1),
        (-1, 0), ( 0, 0), ( 1, 0),
        (-1,-1), ( 0,-1), ( 1,-1),
        '''
        surrounding_squares.remove((0,0))
        '''surrounding_squares:
        (-1, 1), ( 0, 1), ( 1, 1),
        (-1, 0),          ( 1, 0),
        (-1,-1), ( 0,-1), ( 1,-1),
        '''
        nodes = [
          Node(
            self.add_tuples(
                self.start_node.position(),
                x
            ), 
            parent=self.start_node,
            direction=x
            ) 
          for x in surrounding_squares 
            if self.within_map(
                self.add_tuples(
                    self.start_node.position(), 
                    x
                )
               ) 
            and 
              self.free(self.add_tuples(self.start_node.position(), x))]

        #print(nodes)
        print([str(node) for node in nodes])

        self.open_set.extend(nodes)

    def straight(self, coordinates):
        return coordinates[0]*coordinates[1] == 0

    def produce_neighbours_for_scan_straight(self,current_node):
        '''I imagine the scan going rightward in this grid:
        c ■ 	
        b ■  →          The black squares were already covered
        a ■	
          1  2  3 
        '''
        
        turn_counterclockwise_90_degrees = (
            lambda coordinates: (-coordinates[1], coordinates[0])
        )

        turn_clockwise_90_degrees = (
            lambda coordinates: (coordinates[1], -coordinates[0])
        )

        a2 = self.add_tuples(current_node.position(), turn_clockwise_90_degrees(current_node.direction)) 
        a3 = self.add_tuples(a2, current_node.direction)
        b2 = current_node.position()
        b3 = self.add_tuples(current_node.position(),current_node.direction)
        c2 = self.add_tuples(current_node.position(), turn_counterclockwise_90_degrees(current_node.direction)) 
        c3 = self.add_tuples(c2, current_node.direction)
        return (a2,a3,b2,b3,c2,c3)


    def print_map(self):
        for row in reversed(self.map):
            print(row)

    def put_character_on_map(self, coordinates, character):
        i,j = coordinates
        map_list = list(self.map[i])  
        map_list[j] = character
        self.map[i] = ''.join(map_list)  

    def scan_straight(self, current_node):
        '''I imagine it as going rightward in this grid:
        c ■ 	
        b ■  →          The black squares were already covered
        a ■	
          1  2  3 

        '''
        if current_node.direction[0] != 0:
            self.put_character_on_map((current_node.i,current_node.j),"|")
        else:
            self.put_character_on_map((current_node.i,current_node.j),"-")

        self.print_map()
        turn_counterclockwise_90_degrees = (
            lambda coordinates: (-coordinates[1], coordinates[0])
        )
        turn_counterclockwise_90_degrees = lambda coordinates: (-coordinates[1], coordinates[0])

        turn_clockwise_90_degrees = (
            lambda coordinates: (coordinates[1], -coordinates[0])
        )

        print("Scanning straight from node "+str(current_node))
        a2,a3,b2,b3,c2,c3 = self.produce_neighbours_for_scan_straight(current_node)
        available = lambda square : self.within_map(square) and self.free(square)
        if not available(b3):
            return 0 #reached end of map
        else: #tile ahead is free
            if available(c3) and not available(c2):
                new_c3_node_for_open_set_heap = Node(c3,parent=current_node,direction=self.add_tuples(turn_counterclockwise_90_degrees(current_node.direction), current_node.direction))
                heappush(self.open_set_heap,new_c3_node_for_open_set_heap)
                print(f"Heappushed node"+str(new_c3_node_for_open_set_heap))
            if available(a3) and not available(a2):
                new_a3_node_for_open_set_heap = Node(a3,parent=current_node,direction=self.add_tuples(turn_clockwise_90_degrees(current_node.direction), current_node.direction))
                heappush(self.open_set_heap,new_a3_node_for_open_set_heap)
                print(f"Heappushed node"+str(new_a3_node_for_open_set_heap))

        next_node = current_node.copy()
        next_node.i = next_node.i+current_node.direction[0]
        next_node.j = next_node.j+current_node.direction[1]
        self.scan_straight(next_node)

    def produce_neighbours_for_scan_diagonal(self,current_node):
        def turn_45_counterclockwise(vector):
            if vector==(1,1):  
                return (0,1)
            if vector==(-1,1):  
                return (-1,0)
            if vector==(-1,-1):  
                return (0,-1)
            if vector==(1,-1):  
                return (1,0)

        def turn_45_clockwise(vector):
            if vector==(1,1):  
                return (1,0)
            if vector==(1,-1):  
                return (0,-1)
            if vector==(-1,-1):  
                return (-1,0)
            if vector==(-1,1):  
                return (0,1)

        turn_counterclockwise_90_degrees = (
            lambda coordinates: (-coordinates[1], coordinates[0])
        )
        turn_counterclockwise_90_degrees = lambda coordinates: (-coordinates[1], coordinates[0])

        turn_clockwise_90_degrees = (
            lambda coordinates: (coordinates[1], -coordinates[0])
        )

        b1 =  self.add_tuples(current_node.position(),  turn_45_counterclockwise(turn_counterclockwise_90_degrees( current_node.direction)))
        b2 = current_node.position()
        c3 = self.add_tuples(current_node.position(), current_node.direction)
        c2 = self.add_tuples(current_node.position(), turn_45_counterclockwise( current_node.direction))
        c1 = self.add_tuples(current_node.position(),  turn_counterclockwise_90_degrees(current_node.direction))
        b3 = self.add_tuples(current_node.position(), turn_45_clockwise( current_node.direction))
        a2 =  self.add_tuples(current_node.position(),  turn_45_clockwise(turn_clockwise_90_degrees( current_node.direction)))
        a3 = self.add_tuples(current_node.position(),   turn_clockwise_90_degrees( current_node.direction))

        return a2,a3,b1,b2,b3,c1,c2,c3
        
    def scan_diagonally(self, current_node):
        '''I imagine it as going right and up in this grid:
        c ■  	
        b ■  ↗          The black squares were already covered.
        a ■  ■	■       They are the so-called natural neigbours.
          1  2  3 

        '''
        if current_node.direction[1] != 0:
            self.put_character_on_map((current_node.i,current_node.j),"x")
        else:
            self.put_character_on_map((current_node.i,current_node.j),"x")

        self.print_map()
        print("Scanning diagonally from node "+str(current_node))
        a2,a3,b1,b2,b3,c1,c2,c3 = self.produce_neighbours_for_scan_diagonal(current_node)
        scan_right_node = current_node.copy()
        scan_right_node.direction=self.subtract_tuples(b3,b2)
        print(f"scan_right_node.direction=self.subtract_tuples({b3},{b2})")
        self.scan_straight(scan_right_node)
        scan_up_node = current_node.copy()
        scan_up_node.direction=self.subtract_tuples(c2,b2)
        print(f"scan_up_node.direction=self.subtract_tuples({c2},{b2})")
        self.scan_straight(scan_up_node)

        available = lambda square : self.within_map(square) and self.free(square)
        if not available(b1):
            if available(c1):
                new_c1_node_for_open_set_heap = Node(c1,parent=current_node,direction=self.subtract_tuples(c1,current_node.position()))
                heappush(self.open_set_heap,new_c1_node_for_open_set_heap)
                print(f"Heappushed node"+str(new_c1_node_for_open_set_heap))
            if available(c2):
                new_c2_node_for_open_set_heap = Node(c2,parent=current_node,direction=self.subtract_tuples(c2,current_node.position()))
                heappush(self.open_set_heap,new_c2_node_for_open_set_heap)
                print(f"Heappushed node"+str(new_c2_node_for_open_set_heap))

            if available(c3):
                new_c3_node_for_open_set_heap = Node(c3,parent=current_node,direction=self.subtract_tuples(c3,current_node.position()))
                heappush(self.open_set_heap,new_c3_node_for_open_set_heap)
                print(f"Heappushed node"+str(new_c3_node_for_open_set_heap))

            if available(b3):
                new_b3_node_for_open_set_heap = Node(b3,parent=current_node,direction=self.subtract_tuples(b3,current_node.position()))
                heappush(self.open_set_heap,new_b3_node_for_open_set_heap)
                print(f"Heappushed node"+str(new_b3_node_for_open_set_heap))

        if not available(c3):
            return 0

        next_node = current_node.copy()
        next_node.i = next_node.i+current_node.direction[0]
        next_node.j = next_node.j+current_node.direction[1]
        
        self.scan_diagonally(next_node)

    def find_shortest_path(self,start_coordinates,goal_coordinates):
        if not self.within_map(start_coordinates) or not self.within_map(goal_coordinates):
            return 0
        self.put_character_on_map(start_coordinates,"S")
        self.put_character_on_map(goal_coordinates,"G")
        self.start_node = Node(start_coordinates)
        self.goal_node = Node(goal_coordinates)
        if self.start_node.position() == self.goal_node.position():
            return 0

        self.add_neighbours_of_start_node_to_open_set()

        self.open_set_heap = self.open_set[:]
        heapify(self.open_set_heap)
        print("self.open_set_heap")
        print(self.open_set_heap)

        while True:
            if len(self.open_set_heap) == 0:
                return 
            current_node = heappop(self.open_set_heap)
            self.closed_set.append(current_node)
            print(str(f"Current node: {current_node}"))
            if self.straight(current_node.direction):
                print("is straight!")
                self.scan_straight(current_node)
            else:
                self.scan_diagonally(current_node)




