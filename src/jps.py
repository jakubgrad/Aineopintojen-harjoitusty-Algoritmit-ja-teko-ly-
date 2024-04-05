from heapq import *
import time


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
        self.parent = parent
        self.direction = direction
        self.position = coordinates

    def __str__(self):
        return f"coordinates {self.position}, parent coordinates {self.parent.position if self.parent else None}, direction {self.direction}"

    def copy(self):
        return Node(self.position, parent=self.parent, direction=self.direction)

    def __lt__(self, other):
        if isinstance(other, Node):
            priorities = {(0, 1): 8, (1, 0): 7, (0, -1): 6, (-1, 0): 5, (1, 1): 4, (1, -1): 3, (-1, -1): 2, (-1, 1): 1}
            return priorities[self.direction] > priorities[other.direction]

    def __eq__(self, other):
        if isinstance(other, Node):
            return str(self) == str(other)
        return False


class JPS:
    def __init__(self, map):
        self.map = [list(row) for row in map]
        # self.color_map = [list(row) for row in map]
        self.color_map = [['' for _ in range(len(row))] for row in map]

        self.num_rows = len(self.map)
        self.len_row = len(self.map[0])
        self.open_set = []
        self.start_node = None
        self.goal_coordinates = None
        self.open_set_heap = []
        self.closed_set = []
        self.arrows = {(1, 1): "↗", (1, -1): "↘", (-1, -1): "↙", (-1, 1): "↖", (1, 0): "→", (-1, 0): "←", (0, 1): "↑", (0, -1): "↓"}
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

    def color(self, coordinates, color):
        colors = {
            "r": '\033[91m',
            "g": '\033[92m',
            "y": '\033[93m',
            "b": '\033[94m',
            "m": '\033[95m',  # magenta
            "c": '\033[96m',  # cyan
            "w": '\033[97m',  # white
            "reset": '\033[0m'  # reset
        }
        background_colors = {
            "r": '\033[41m',  # red
            "g": '\033[42m',  # green
            "y": '\033[43m',  # yellow
            "b": '\033[44m',  # blue
            "m": '\033[45m',  # magenta
            "c": '\033[46m',  # cyan
            "w": '\033[47m',  # white
            "reset": '\033[0m'  # reset
        }
        i, j = coordinates
        self.color_map[i][j] = background_colors[color]

    def recreate_path(self, final_node):
        print(final_node.position)
        ans = str(final_node.position)
        last_node = final_node
        while True:
            i = last_node.parent
            if i == None:
                break
            else:
                print(i.position)
                self.color(i.position, "r")
                ans = ans + str(i.position)
                last_node = i
        return ans

    def within_map(self, coordinates):
        i, j = coordinates
        return True if 0 <= i < self.num_rows and 0 <= j < self.len_row else False

    def free(self, coordinates):
        i, j = coordinates
        free_tiles = [".", "-", "|", "x"]
        not_free_tiles = ["T"]
        return self.map[i][j] not in not_free_tiles

    def add_tuples(self, coordinates1, coordinates2):
        return (coordinates1[0]+coordinates2[0], coordinates1[1]+coordinates2[1])

    def subtract_tuples(self, coordinates1, coordinates2):
        return (coordinates1[0]-coordinates2[0], coordinates1[1]-coordinates2[1])

    def add_neighbours_of_start_node_to_open_set(self):
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
        nodes = [
            Node(
                self.add_tuples(
                    self.start_node.position,
                    x
                ),
                parent=self.start_node,
                direction=x
            )
            for x in surrounding_squares
            if self.within_map(
                self.add_tuples(
                    self.start_node.position,
                    x
                )
            )
            and
            self.free(self.add_tuples(self.start_node.position, x))]
        print([str(node) for node in nodes])
        self.open_set.extend(nodes)

    def straight(self, coordinates):
        return coordinates[0]*coordinates[1] == 0

    def turn_counterclockwise_90_degrees(self, coordinates):
        return (-coordinates[1], coordinates[0])

    def turn_clockwise_90_degrees(self, coordinates):
        return (coordinates[1], -coordinates[0])

    def produce_neighbours(self, current_node):
        '''Straight scan:
        c ■ 	
        b ■  →          
        a ■	
          1  2  3 
        Diagonal scan:
        c ■  	
        b ■  ↗          
        a ■  ■	■      
          1  2  3   '''

        # copying the node to not introduce changes to the original one
        node = current_node.copy()
        if not self.straight(node.direction):
            node.direction = self.turn_45_clockwise(node.direction)
        b1 = self.subtract_tuples(node.position, node.direction)
        b2 = node.position
        b3 = self.add_tuples(node.position, node.direction)
        c2 = self.add_tuples(
            node.position, self.turn_counterclockwise_90_degrees(node.direction))
        c3 = self.add_tuples(c2, node.direction)
        a1 = self.subtract_tuples(self.add_tuples(b2, b2), c3)
        a2 = self.add_tuples(
            node.position, self.turn_clockwise_90_degrees(node.direction))
        a3 = self.add_tuples(a2, node.direction)
        c1 = self.subtract_tuples(self.add_tuples(b2, b2), a3)

        return (a1, a2, a3, b1, b2, b3, c1, c2, c3)

    def merge_maps(self, map_list, map_list2):
        result_map = []
        for i in range(len(map_list)):
            row = []
            for j in range(len(map_list[0])):
                row.append(map_list[i][j]+map_list2[i][j]+'\033[0m')
            result_map.append(row)
        return result_map

    def print_map(self, wait_time=0.2):
        map_list = self.merge_maps(self.color_map, self.map)
        rotated_map_list = [[''] * self.num_rows for _ in range(self.len_row)]

        for i in range(self.num_rows):
            for j in range(self.len_row):
                rotated_map_list[self.len_row - j - 1][i] = map_list[i][j]

        for row in rotated_map_list:
            print(" ".join(row))
        time.sleep(wait_time)

    def put_character_on_map(self, coordinates, character):
        i, j = coordinates
        map_list = self.map[i]
        map_list[j] = character

    def available(self, square):
        return self.within_map(square) and self.free(square)

    def scan_straight(self, current_node):
        print("Scanning straight from node "+str(current_node))
        '''I imagine it as going rightward in this grid:
        c ■ 	
        b ■  →          The black squares were already covered
        a ■	
          1  2  3       '''
        self.put_character_on_map(
            (current_node.position), self.arrows[current_node.direction])

        self.print_map()
        a1, a2, a3, b1, b2, b3, c1, c2, c3 = self.produce_neighbours(
            current_node)

        if self.goal_coordinates in [a1, a2, a3, b1, b2, b3, c1, c2, c3]:
            final_node = Node(self.goal_coordinates,
                              parent=current_node, direction=None)
            self.recreate_path(final_node)
            return 1

        if not self.available(b3):
            return 0  # reached end of map
        else:  # tile ahead is free
            if self.available(c3) and not self.available(c2):
                self.add_node_to_open_set_if_new(current_node, c3)
            if self.available(a3) and not self.available(a2):
                self.add_node_to_open_set_if_new(current_node, a3)

        next_node = current_node.copy()
        print(
            f"next_node.position = self.add_tuples({next_node.position},{current_node.direction})")
        next_node.position = self.add_tuples(
            next_node.position, current_node.direction)
        self.scan_straight(next_node)

    def turn_45_counterclockwise(self, vector):
        values = {(1, 1): (0, 1), (-1, 1): (-1, 0),
                  (-1, -1): (0, -1), (1, -1): (1, 0)}
        return values.get(vector)

    def turn_45_clockwise(self, vector):
        values = {(1, 1): (1, 0), (1, -1): (0, -1),
                  (-1, -1): (-1, 0), (-1, 1): (0, 1)}
        return values.get(vector)

    def turn_counterclockwise_90_degrees(self, coordinates):
        return (-coordinates[1], coordinates[0])

    def turn_clockwise_90_degrees(self, coordinates):
        return (coordinates[1], -coordinates[0])

    def add_node_to_open_set_if_new(self, current_node, square):
        open_node = Node(square, parent=current_node, direction=self.subtract_tuples(
            square, current_node.position))
        if open_node in self.closed_set:
            return False
        else:
            heappush(self.open_set_heap, open_node)
            print(f"Heappushed node"+str(open_node))
            self.color(open_node.position, "y")
            return True

    def scan_diagonally(self, current_node):
        '''I imagine it as going right and up in this grid:
        c ■  	
        b ■  ↗          The black squares were already covered.
        a ■  ■	■       They are the so-called natural neigbours.
          1  2  3'''
        self.print_map()
        print("Scanning diagonally from node "+str(current_node))
        a1, a2, a3, b1, b2, b3, c1, c2, c3 = self.produce_neighbours(
            current_node)
        scan_right_node = current_node.copy()
        scan_right_node.direction = self.subtract_tuples(b3, b2)
        scan_right_node.parent = current_node
        print(f"scan_right_node.direction=self.subtract_tuples({b3},{b2})")
        self.scan_straight(scan_right_node)
        scan_up_node = current_node.copy()
        scan_up_node.direction = self.subtract_tuples(c2, b2)
        scan_up_node.parent = current_node
        print(f"scan_up_node.direction=self.subtract_tuples({c2},{b2})")
        self.scan_straight(scan_up_node)
        self.put_character_on_map(
            (current_node.position), self.arrows[current_node.direction])
        if not self.available(b1):
            if self.available(c1):
                self.add_node_to_open_set_if_new(current_node, c1)
            if self.available(c2):
                self.add_node_to_open_set_if_new(current_node, c2)
            if self.available(c3):
                self.add_node_to_open_set_if_new(current_node, c3)
            if self.available(b3):
                self.add_node_to_open_set_if_new(current_node, b3)
        if not self.available(c3):
            return 0

        next_node = current_node.copy()
        next_node.position = self.add_tuples(
            next_node.position, current_node.direction)
        self.scan_diagonally(next_node)

    def find_shortest_path(self, start_coordinates, goal_coordinates):
        self.goal_node = Node(goal_coordinates)
        self.start_node = Node(start_coordinates)
        self.start_coordinates = start_coordinates
        self.goal_coordinates = goal_coordinates
        if not self.within_map(start_coordinates) or not self.within_map(goal_coordinates):
            print("Start or goal coordinates are out of bounds")
            return 0
        self.put_character_on_map(start_coordinates, "S")
        self.put_character_on_map(goal_coordinates, "G")
        if self.start_coordinates == self.goal_coordinates:
            print("Start and goal positions are the same")
            return 0

        self.add_neighbours_of_start_node_to_open_set()
        self.open_set_heap = self.open_set[:]
        heapify(self.open_set_heap)

        while True:
            if len(self.open_set_heap) == 0:
                print("Jump points have been exhausted")
                return
            current_node = heappop(self.open_set_heap)
            self.closed_set.append(current_node.copy())
            print(str(f"Current node: {current_node}"))
            if self.straight(current_node.direction):
                self.scan_straight(current_node)
            else:
                self.scan_diagonally(current_node)
