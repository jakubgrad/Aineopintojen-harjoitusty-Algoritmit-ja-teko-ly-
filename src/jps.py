from heapq import *
import time
import math

class Node:
    def __init__(self, coordinates, parent=None, direction=None, length=0, heuristic=1000):
        """Class constructor, that creates a new node 

        Args:
            coordinates: a tuple of node's row and column in the grid
            parent: node's parent, so the node from which JPS has reached this node
            direction: direction of search the node is supposed to begin
            length: a variable to keep track and prune when a path's length is greater
                than the minimum distance already found
            heuristic: a variable that makes JPS behave like A* in that it
                first expands nodes that are most promising
        """

        self.parent = parent
        self.direction = direction
        self.position = coordinates
        self.length = length
        self.heuristic = heuristic

    def __str__(self):
        """Generate a string representation of the Node object.

        Returns:
            A string containing information about the node's coordinates,
            its parent's coordinates (if exists), and the direction of scan.
        """

        return (
            f"coordinates {self.position}, "
            f"parent coordinates {self.parent.position if self.parent else None}, "
            f"direction {self.direction}"
        )

    def copy(self):
        """Create a copy of the Node object.

        Returns:
            Node: A new Node object with the same position, parent, direction,
            and length as the original node.
        """
        return Node(self.position, parent=self.parent, direction=self.direction)

    def __lt__(self, other):
        """ A comparison method for nodes. Uses a heuristic function 
            to find the distance to the goal node so that heappoping
            the open_set yields the best jumppoint. If the heuristic
            values of two nodes are the same, priority is to 
            expand the nodes according to their direction

        Args:
            self: the node itself
            other: a node to compare with

        Returns:
            Whether scanning this node is higher in priority
            than scanning the other one
        """


        if isinstance(other, Node):
            if other.heuristic == self.heuristic:
                priorities = {(0, 1): 8, (1, 0): 7, (0, -1): 6, (-1, 0): 5, (1, 1): 4, (1, -1): 3, (-1, -1): 2, (-1, 1): 1}
                return priorities[self.direction] > priorities[other.direction]
            return other.heuristic > self.heuristic

    def __eq__(self, other):
        """ Another comparison method for nodes
            to ensure scanning isn't circular

        Args:
            self: the node itself
            other: a node to compare with

        Returns:
            Whether the nodes are similar enough that  
            they can be considered the same
        """

        if isinstance(other, Node):
            return str(self) == str(other)
        return False


class JPS:
    """ A class that can finds the shortest path using JPS algorithm
        and creates slides in visual mode for UI

    Attributes:
        map: list of lists of strings, each either "T" for obstacle or "." 
             for free tile
        num_rows: number of rows of the map
        len_row: length of a single row
        open_set: a min heap/priority queue used to keep tracked of nodes to expand
        visual: a flag that tells JPS if it needs to create slides
        ...
        closed_set: set of already expanded nodes
        slides: a list for saving snapshots of algorithm's execution for UI display

    """

    def __init__(self, map):
        """JPS's class constructor

        Args:   
            map: the map on which to run Dijkstra
        """
        self.map = map
        self.num_rows = len(self.map)
        self.len_row = len(self.map[0])
        self.open_set = []
        heapify(self.open_set)
        self.visual = False
        self.start_coordinates = None
        self.goal_coordinates = None
        self.closed_set = []
        self.slides = []
        self.final_node = None
        self.min_distance = 999999999

    def __str__(self):
        """A function used to test if JPS class correctly found the size of map 

        Returns:
            A string describing the size of the map
        """

        return f'Number of rows: {self.num_rows}, Length of a row: {self.len_row}'

    def mark_points_between(self, start_coordinates, end_coordinates):
        """ A function used to mark the path between some start and goal coordinates 
            that lie together on straight or diagonal line.
            Used to mark the path between consecutive jumppoints of JPS after the 
            path to the goal was found

        Args:
            start_coordinates: any coordinates of a points on the map
            end_coordinates:   coordinates of a point that is diagonally or
                               linearly away from start_coordinates' point

        Returns:
            A string describing the size of the map
        """

        if start_coordinates == end_coordinates:
            return None

        vector = self.subtract_tuples(end_coordinates, start_coordinates)

        if self.straight(vector):
            length = abs(vector[0]+vector[1])
            if length == 1:
                return None
            if vector[0] == 0:
                unit_vector = (0, 1) if vector[1] > 0 else (0, -1)
            else:
                unit_vector = (1, 0) if vector[0] > 0 else (-1, 0)
        else:
            length = abs(vector[0])
            if length == 1:
                return None
            unit_vector = (vector[0]/length, vector[1]/length)

        for i in range(0, length):
            coord = self.add_tuples(start_coordinates, (round(
                unit_vector[0]*i), round(unit_vector[1]*i)))
            self.mark(coord, "¤")

    def find_distance(self, path):
        """A function that returns the length of a given path

        Args:
            path: path in the form of coordinates that are on the same 
            diagonal or the same vertical or straight line, e.g.
            [(0,0),(4,4),(5,4),(6,5)]

        Returns:
            The distance taken by going in a straight line or diagonally
            between consecutive points of the path
        """

        total_distance = 0
        def straight_distance(p1, p2): return abs(p2[0]-p1[0]+p2[1]-p1[1])
        def diagonal_distance(p1, p2): return 1.41 * \
            max(abs(p2[0] - p1[0]), abs(p2[1] - p1[1]))

        for i in range(len(path) - 1):
            if self.straight(self.subtract_tuples(path[i], path[i+1])):
                total_distance += straight_distance(path[i], path[i + 1])
            else:
                total_distance += diagonal_distance(path[i], path[i + 1])
        return total_distance

    def recreate_path(self, final_node):
        """ Function used to return the path from start coordinates
            to goal coordinates, which is the position of the final 
            node. 

        Args:
            final_node: the node in position of goal coordinates

        Returns: 
            the length of the path taken by the JPS algorithm
        """

        distance = 0
        last_node = final_node
        path = []
        path.append(final_node.position)

        while True:
            i = last_node.parent

            if i == None:
                break
            else:
                path.append(i.position)
                self.mark(i.position, "¤")
                self.mark_points_between(last_node.position, i.position)
                self.add_slide()
                print(i.position)
                last_node = i

        distance = self.find_distance(path)
        self.mark(self.start_coordinates, "S")
        self.add_slide()
        return distance

    def within_map(self, coordinates):
        """A handy function that tells whether coordinates lie within the map

        Args: 
            coordinates: the coordinates to be checked

        Returns: true or false depending on whether the cooridnates are on the map
        """

        i, j = coordinates
        return True if 0 <= i < self.num_rows and 0 <= j < self.len_row else False

    def free(self, coordinates):
        """ A handy function that tells whether a coordinate is an obstacle or not
            I don't know how should JPS treat fields that it already visited, so
            the function might need changes

        Args: 
            coordinates: the coordinates to be checked

        Returns:  true or false depending on whether the cooridnates are free to
                  create a jumppoint or continue scanning
        """

        i, j = coordinates
        free_tiles = [".", "-", "|", "x", "J"]
        not_free_tiles = ["T"]
        return self.map[i][j] not in not_free_tiles

    def add_tuples(self, coordinates1, coordinates2):
        return (coordinates1[0]+coordinates2[0], coordinates1[1]+coordinates2[1])

    def subtract_tuples(self, coordinates1, coordinates2):
        return (coordinates1[0]-coordinates2[0], coordinates1[1]-coordinates2[1])

    def add_neighbours_of_start_coordinates_to_open_set(self, start_coordinates):
        """ Function used to initiate JPS.
            The first neighbours are added as nodes to the open set

        Args: 
            start_coordinates: where the algorithm begins
        """

        numbers = list(range(1, 9))
        surrounding_squares = [((x % 3)-1, 1-(x//3)) for x in range(0, 9)]
        '''surrounding_squares:
        (-1, 1), ( 0, 1), ( 1, 1),
        (-1, 0), ( 0, 0), ( 1, 0),
        (-1,-1), ( 0,-1), ( 1,-1),
        '''
        surrounding_squares.remove((0, 0))
        '''surrounding_squares:
        (-1, 1), ( 0, 1), ( 1, 1),
        (-1, 0),          ( 1, 0),
        (-1,-1), ( 0,-1), ( 1,-1),
        '''
        nodes = []
        start_node = Node(start_coordinates)

        for coords in surrounding_squares:
            node_position = self.add_tuples(start_coordinates, coords)
            if self.available(node_position):
                heappush(self.open_set, Node(
                        node_position,
                        parent=start_node,
                        direction=coords
                    )
                )

    def straight(self, vector):
        """ A handy function that tells whether a vector goes 
            on a straight line or diagonally

        Args: 
            vector: the vector to be checked

        Returns: true or false depending on whether the vector 
        is a diagonal or a straight line
        """
        return vector[0]*vector[1] == 0

    def produce_neighbours(self, current_node):
        """ Produce the neighbours of the node currently being expanded.
            A central function of the algorithm is checking whether 
            there is any forced neigbours and producing jump points
            for the algorithm. I decided to create a common function
            for creating neighobours around the node currently being
            expanded, which is marked with arrows → and ↗
            Producing neighbours is relative to direction up/down/left/
            /right/up-right/right-down/left-down/left-up, so that 
            all neighbour names like c2, a1 are in sync with direction
            of the scan.

            Straight scan:       Diagonal scan:
            c ■                     c ■  	   	
            b ■  →                  b ■  ↗         
            a ■	                    a ■  ■	■      
              1  2  3                 1  2  3   

        Args:
            current_node: node that is being expanded

        Returns: 
            the neighbours of the node
        """
        d = current_node.direction
        p = current_node.position

        if d == (1, 0) or d == (1, 1):
            neighbours = ((-1, -1), (0, -1), (1, -1),
                          (-1, 0), (0, 0), (1, 0),
                          (-1, 1), (0, 1), (1, 1))

        if d == (0, 1) or d == (-1, 1):
            neighbours = ((1, -1), (1, 0), (1, 1),
                          (0, -1), (0, 0), (0, 1),
                          (-1, -1), (-1, 0), (-1, 1))

        if d == (-1, 0) or d == (-1, -1):
            neighbours = ((1, 1), (0, 1), (-1, 1),
                          (1, 0), (0, 0), (-1, 0),
                          (1, -1), (0, -1), (-1, -1))

        if d == (0, -1) or d == (1, -1):
            neighbours = ((-1, 1), (-1, 0), (-1, -1),
                          (0, 1), (0, 0), (0, -1),
                          (1, 1), (1, 0), (1, -1))

        neighbours = tuple(self.add_tuples(neighbour, p)
                           for neighbour in neighbours)

        return neighbours

    def add_slide(self):
        """ A function that adds a snapshot of the algorithm
            to the slides list that is passed on to UI

        Attributes:
            visual: if False, no slides are added. This is because 
                    I want to make performance tests in the future
        """

        if self.visual:
            rotated_map = [
                [''] * self.num_rows for _ in range(self.len_row)]

            slide = ""
            for i in range(self.num_rows):
                for j in range(self.len_row):
                    rotated_map[self.len_row - j - 1][i] = self.map[i][j]

            for row in rotated_map:
                slide = slide+(" ".join(row))+"\n"
            # print(slide)
            self.slides.append(slide)

    def mark(self, coordinates, character,jumppoint=False):
        """A function that marks a place on the grid with a character

        Args:
            coordinates: coordinates on which to place the character
            character: character to be place
        """

        if self.visual:
            if jumppoint == False:
                arrows = {(1, 1): "↗", (1, -1): "↘", (-1, -1): "↙", (-1, 1): "↖", (1, 0): "→", (-1, 0): "←", (0, 1): "↑", (0, -1): "↓"}
            else: 
                arrows = {(0,0):"G",(1, 1): "⬀", (1, -1): "⬂", (-1, -1): "⬃", (-1, 1): "⬁", (1, 0): "⇨", (-1, 0): "⇦", (0, 1): "⇧", (0, -1): "⇩"}

            i, j = coordinates
            if type(character) == tuple:
                character = arrows[character]
            map_list = self.map[i]
            map_list[j] = character

    def available(self, coordinates):
        """ A handy function that checks if coordinates are both free and
            within the map

        Args:
            coordinates: which coordinates need to be checked

        Returns: whether the tile is free of obstacles and inside the map
        """

        return self.within_map(coordinates) and self.free(coordinates)

    def scan_straight(self, node):
        ''' A function that allows JPS to scan along rows and columns

        Args:
            node: node that is being expanded
        
        Returns:
            0 when it finishes, i.e. it hits a wall or an obstacle

        c ■ 	
        b ■  →          The black squares were already covered
        a ■	
          1  2  3       '''

        print("Scanning straight from node "+str(node))

        self.mark((node.position), node.direction)
        self.add_slide()

        neighbours = self.produce_neighbours(node)
        a1, a2, a3, b1, b2, b3, c1, c2, c3 = neighbours

        if b3 == self.goal_coordinates:
            final_node = Node(self.goal_coordinates,
                              parent=node, direction=None)
            self.final_node = final_node
            self.add_node_to_open_set_if_new(final_node, self.goal_coordinates)
            return 1

        if not self.available(b3):
            return 0
        else:
            if self.available(c3) and not self.available(c2):
                self.add_node_to_open_set_if_new(node, c3)
            if self.available(a3) and not self.available(a2):
                self.add_node_to_open_set_if_new(node, a3)

        next_node = node.copy()
        print(
            f"next_node.position = self.add_tuples({next_node.position},{node.direction})")
        next_node.position = self.add_tuples(
            next_node.position, node.direction)

        next_node.length = node.length+1
        if self.scan_straight(next_node) == 1:
            return 1

    def distance_between_points(self, point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def add_node_to_open_set_if_new(self, current_node, square):

        if square == self.goal_coordinates:
            heuristic = 0 
        else: 
            distance_to_goal = self.distance_between_points(current_node.position, self.goal_coordinates)
            distance_travelled = current_node.length
            heuristic = distance_to_goal + distance_travelled 

        open_node = Node(square, parent=current_node, direction=self.subtract_tuples(
            square, current_node.position), length=current_node.length, heuristic=heuristic)

        if (open_node.position, open_node.direction) in self.closed_set or open_node in self.open_set:
            return False
        else:
            heappush(self.open_set, open_node)
            self.mark(
                open_node.position, open_node.direction, jumppoint=True)
            return True

    def scan_diagonally(self, node):
        """ A function that allows JPS to scan across diagonals.

        Args:
            node: node that is being expanded
        
        Returns:
            0 when it finishes, i.e. it hits a wall or an obstacle

                        I imagine the scan as going right and up in this grid
        c ■  	
        b ■  ↗          The black squares were already covered.
        a ■  ■	■       They are the so-called natural neigbours.
          1  2  3
                        
        """

        self.add_slide()

        neighbours = self.produce_neighbours(
            node)
        a1, a2, a3, b1, b2, b3, c1, c2, c3 = neighbours

        if c3 == self.goal_coordinates:
            self.final_node = Node(self.goal_coordinates,
                              parent=node, direction=None)
            self.add_node_to_open_set_if_new(self.final_node, self.goal_coordinates)
            return 1

        scan_right_node = node.copy()
        scan_right_node.direction = self.subtract_tuples(b3, b2)
        scan_right_node.parent = node
        scan_right_node.length = node.length+1

        #exiting recursion if goal found
        if self.scan_straight(scan_right_node) == 1:
            return 1
        
        scan_up_node = node.copy()
        scan_up_node.direction = self.subtract_tuples(c2, b2)
        scan_up_node.parent = node
        scan_up_node.length = node.length+1

        #exiting recursion if goal found
        if self.scan_straight(scan_up_node) == 1:
            return 1

        self.mark(
            node.position, node.direction)

        if not self.available(b1):
            if self.available(c1):
                self.add_node_to_open_set_if_new(node, c1)
            if self.available(c2):
                self.add_node_to_open_set_if_new(node, c2)
            if self.available(c3):
                self.add_node_to_open_set_if_new(node, c3)
            if self.available(b3):
                self.add_node_to_open_set_if_new(node, b3)

        if not self.available(c2):
            if self.available(c3):
                self.add_node_to_open_set_if_new(node, c3)
            if self.available(b3):
                self.add_node_to_open_set_if_new(node, b3)

        if not self.available(b3):
            if self.available(c3):
                self.add_node_to_open_set_if_new(node, c3)
            if self.available(c2):
                self.add_node_to_open_set_if_new(node, c2)

        if not self.available(a2):
            if self.available(b3):
                self.add_node_to_open_set_if_new(node, b3)
            if self.available(c2):
                self.add_node_to_open_set_if_new(node, c2)
            if self.available(c3):
                self.add_node_to_open_set_if_new(node, c3)
            if self.available(a3):
                self.add_node_to_open_set_if_new(node, a3)

        if not self.available(c3):
            return 0

        next_node = node.copy()
        next_node.position = self.add_tuples(
            next_node.position, node.direction)

        next_node.length = node.length+1.41

        #exiting recursion if goal found
        if self.scan_diagonally(next_node) == 1:
            return 1

    def view_map(self):
        rotated_regular_map = [
            [''] * self.num_rows for _ in range(self.len_row)]

        for i in range(self.num_rows):
            for j in range(self.len_row):
                rotated_regular_map[self.len_row - j - 1][i] = self.map[i][j]

        rmap = ""
        for i, row in enumerate(rotated_regular_map):
            row_with_numbers = [str(self.len_row-i - 1)] + row
            rmap += " ".join(row_with_numbers) + "\n"
        last_row = " ".join(str(i) for i in range(self.num_rows))
        rmap += "  "+last_row + "\n"
        return rmap

    def find_shortest_path(self, start_coordinates, goal_coordinates, slides=[], visual=False):
        """Function that can be called after initializing JPS to find the shortest path

        Args: 
            start_coordinates
            goal_coordinates
            slides: used for presenting snapshots of the algorithm to the UI
            visual: a flag that tells JPS if it should create slides

        Returns:
            The length of the shortest path, and mutating the list in place,
            passes the snapshots of execution to the UI
        """

        self.add_slide()
        self.visual = visual
        self.slides = slides
        self.start_coordinates = start_coordinates
        self.goal_coordinates = goal_coordinates
        if not self.within_map(start_coordinates) or not self.within_map(goal_coordinates):
            print("Start or goal coordinates are out of bounds")
            return 0
        self.mark(start_coordinates, "S")
        self.mark(goal_coordinates, "G")
        if self.start_coordinates == self.goal_coordinates:
            print("Start and goal positions are the same")
            return 0

        self.add_neighbours_of_start_coordinates_to_open_set(start_coordinates)
        distance = 0

        GOAL_FOUND = False

        while True:
            if len(self.open_set) == 0:
                print("Jump points have been exhausted")
                print("Ended execution due to break statement")
                print("Perhaps there is no path to the goal coordinates")
                break
            current_node = heappop(self.open_set)
            if current_node.position == self.goal_coordinates:
                GOAL_FOUND = True
                break
            self.closed_set.append(
                (current_node.position, current_node.direction))
            print(str(f"Current node: {current_node}"))
            if self.straight(current_node.direction):
                self.scan_straight(current_node)
            else:
                self.scan_diagonally(current_node)

        if GOAL_FOUND:
            return self.recreate_path(self.final_node)
        return False
