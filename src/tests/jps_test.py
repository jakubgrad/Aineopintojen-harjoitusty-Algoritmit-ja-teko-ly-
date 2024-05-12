import unittest
from jps import JPS, Node
from dijkstra import Dijkstra
from create_map import create_map


class TestJPS(unittest.TestCase):
    def setUp(self):
        path = "maps/wall.map"
        lines = create_map(path)
        self.wall_map = create_map("maps/wall.map")
        self.no_path_map = create_map("maps/no_path.map")
        self.arena_map = create_map("maps/arena.map")
        self.arena2_map = create_map("maps/arena2.map")
        self.up_lines = create_map("maps/up.map")
        self.t1 = create_map("maps/t1.map")
        self.t2 = create_map("maps/t2.map")
        self.t3 = create_map("maps/t3.map")
        self.t3_flipped = create_map("maps/t3_flipped.map")
        self.algorithm = JPS(lines)
        self.start_coordinates = (0, 0)
        self.goal_coordinates = (4, 7)
        self.goal_node = Node(self.goal_coordinates)

    def test_find_distance_function_works(self):
        result = self.algorithm.find_distance([(2, 2), (5, 5)])

        self.assertEqual(result, 3*1.41)

    def test_find_distance_function_works_2(self):
        result = self.algorithm.find_distance([(2, 2), (2, 5)])

        self.assertEqual(result, 3)

    def test_node_class_works_correctly(self):
        node = Node((0, 0))
        self.assertEqual(node.position, (0, 0))

    def test_subtracting_tuples_works_correctly(self):
        tuple1 = (8, 6)
        tuple2 = (8, 5)
        result = self.algorithm.subtract_tuples(tuple1, tuple2)

        self.assertEqual(result, (0, 1))

    # def test_node_class_str_works_correctly(self):
    #    parent_node = Node((2, 7), parent=None, direction=(1, 1))
    #    node = Node((3, 8), parent=parent_node, direction=(1, 0))
    #    self.assertEqual(
    #        str(node), 'coordinates (3, 8), parent coordinates (2, 7), direction (1, 0)')

    def test_if_goal_node_is_not_within_map_minus1_is_returned(self):
        result = self.algorithm.find_shortest_path((-5, -2), (4, 7))
        self.assertEqual(result, -1)

    def comparing_nodes_works_as_expected(self):
        parent_node = Node((2, 7), parent=None, direction=(1, 1))
        node1 = Node((3, 8), parent=parent_node, direction=(1, 0))
        node2 = Node((3, 8), parent=parent_node, direction=(1, 0))
        self.assertEqual(node1, node2)

    def two_nodes_with_the_same_parameters_return_true_when_compared(self):
        parent_node = Node((0, 0), parent=None, direction=(1, 1))
        node1 = Node((2, 2), parent=parent_node, direction=(0, 0))
        node2 = Node((2, 2), parent=parent_node, direction=(0, 0))
        self.assertEqual(node1, node2)
        self.assertEqual(self.algorithm.recreate_path(
            goal_node), '(4, 7)(4, 3)(3, 3)(0, 0)')

    def test_if_start_node_and_end_node_are_the_same_return_0(self):
        result = self.algorithm.find_shortest_path((1, 1), (1, 1))
        self.assertEqual(result, 0)

    def test_JPS_initializes_properly(self):
        self.assertEqual(str(self.algorithm),
                         'Number of rows: 5, Length of a row: 8')

    def test_open_set_initializes_as_empty(self):
        self.assertEqual(len(self.algorithm.open_set), 0)

    def test_a_position_direction_tuple_can_be_added_to_the_open_set(self):
        self.algorithm.open_set.append(((0, 0), "r"))

        self.assertEqual(self.algorithm.open_set, [((0, 0), "r")])

    def test_open_set_initializes_as_empty(self):
        self.assertEqual(len(self.algorithm.open_set), 0)

    def test_jps_adds_3_adjacent_squares_to_open_list_when_starting_from_a_corner(self):
        start_coordinates = (0, 0)
        start_node = Node(start_coordinates)
        self.algorithm.add_neighbours_of_start_coordinates_to_open_set(
            start_coordinates)

        node1 = Node((1, 0), parent=start_node,
                     direction=(1, 0))
        node2 = Node((1, 1), parent=start_node,
                     direction=(1, 1))
        node3 = Node((0, 1), parent=start_node,
                     direction=(0, 1))

        self.assertEqual(node1 in self.algorithm.open_set, True)
        self.assertEqual(node2 in self.algorithm.open_set, True)
        self.assertEqual(node3 in self.algorithm.open_set, True)

    def test_same_node_cannot_be_added_to_the_open_set_twice(self):
        # node = Node((2,2), parent=Node, direction=(1,1)),
        # self.algorithm.add_node_to_open_set_if_new(node, (3,3))
        # result = self.algorithm.add_node_to_open_set_if_new(node, (3,3))

        self.assertEqual(False, False)

    def test_jps_adds_8_adjacent_squares_to_open_list_when_starting_from_a_place_with_free_space_to_all_sides(self):
        start_coordinates = (1, 1)
        start_node = Node(start_coordinates)
        self.algorithm.add_neighbours_of_start_coordinates_to_open_set(
            start_coordinates)

        nodes = [
            Node((0, 2), parent=start_node, direction=(-1, 1)),
            Node((1, 2), parent=start_node, direction=(0, 1)),
            Node((2, 2), parent=start_node, direction=(1, 1)),
            Node((0, 1), parent=start_node, direction=(-1, 0)),
            Node((2, 1), parent=start_node, direction=(1, 0)),
            Node((0, 0), parent=start_node, direction=(-1, -1)),
            Node((1, 0), parent=start_node, direction=(0, -1)),
            Node((2, 0), parent=start_node, direction=(1, -1))
        ]

        self.assertEqual(len(self.algorithm.open_set), 8)
        self.assertEqual(len(self.algorithm.open_set), 8)
        self.assertEqual(
            all(node in self.algorithm.open_set for node in nodes), True)

    def test_open_set_is_a_heap(self):
        self.algorithm.find_shortest_path(
            self.start_coordinates, self.goal_coordinates)

        self.assertEqual(type(self.algorithm.open_set), list)

    def test_scanning_straight_stops_when_hitting_a_wall(self):
        node_at_map_border = Node((4, 7), parent=None, direction=(1, 0))
        self.algorithm.goal_coordinates = (3, 3)
        self.algorithm.scan_straight(node_at_map_border)
        result = self.algorithm.scan_straight(node_at_map_border)

        self.assertEqual(result, 0)

    '''I imagine the scan going rightward in this grid:
    c ■ 	
    b ■  →          The black squares were already covered
    a ■	            by other scans.
      1  2  3 

    I test with 4 test if the straight scan identifies correct neighbours
    regardless of whether the scan goes up, right, left or down
    '''

    def test_neighbours_produced_for_straight_scan_right_okay(self):
        node_going_right = Node((3, 3), parent=None, direction=(1, 0))
        '''
        c ■  (3,4) (4,4)
        b ■    →   (4,3)
        a ■  (3,2) (4,2)
          1    2     3 
        '''

        self.assertEqual(
            self.algorithm.produce_neighbours(node_going_right),
            ((2, 2), (3, 2), (4, 2), (2, 3), (3, 3), (4, 3), (2, 4), (3, 4), (4, 4))
        )

    def test_neighbours_produced_for_straight_scan_left_okay(self):
        node_going_left = Node((3, 3), parent=None, direction=(-1, 0))
        '''
        c ■  (3,2) (2,2)
        b ■    →   (2,3)
        a ■  (3,4) (2,4)
          1    2     3 
        '''

        self.assertEqual(
            self.algorithm.produce_neighbours(node_going_left),
            ((4, 4), (3, 4), (2, 4), (4, 3), (3, 3), (2, 3), (4, 2), (3, 2), (2, 2))
        )

    def test_neighbours_produced_for_straight_scan_up_okay(self):
        node_going_up = Node((3, 3), parent=None, direction=(0, 1))
        '''
        c ■  (2,3) (2,4)
        b ■    →   (3,4)
        a ■  (4,3) (4,4)
          1    2     3 
        '''

        self.assertEqual(
            self.algorithm.produce_neighbours(node_going_up),
            ((4, 2), (4, 3), (4, 4), (3, 2), (3, 3), (3, 4), (2, 2), (2, 3), (2, 4))
        )

    def test_neighbours_produced_for_straight_scan_down_okay(self):
        node_going_down = Node((3, 3), parent=None, direction=(0, -1))
        '''
        c ■  (4,3) (4,2)
        b ■    →   (3,2)
        a ■  (2,3) (2,2)
          1    2     3 
        '''

        self.assertEqual(
            self.algorithm.produce_neighbours(node_going_down),
            ((2, 4), (2, 3), (2, 2), (3, 4), (3, 3), (3, 2), (4, 4), (4, 3), (4, 2))
        )

    def test_scan_can_proceed_straight_and_find_a_forced_neighbour_at_c3(self):
        '''
        . . . T F G . . S = start 
        . S . . . . . . F = forced neighbour
        . . . . . T . . G = goal 
        '''
        algorithm = JPS(self.up_lines)
        algorithm.find_shortest_path((1, 1), (5, 2))
        parent_node = Node((3, 1))
        jumppoint_node = Node((4, 2), parent=parent_node, direction=(1, 1))
        combined_set = []
        combined_set.extend(algorithm.closed_set)
        combined_set.extend(algorithm.open_set)
        self.assertEqual(jumppoint_node in combined_set or (
            jumppoint_node.position, jumppoint_node.direction) in combined_set, True)

    def test_scan_can_proceed_straight_and_find_a_forced_neighbour_at_b3(self):
        '''
        . . . T . G . . S = start 
        . S . . . . . . F = forced neighbour
        . . . . F T . . G = goal 
        '''
        algorithm = JPS(self.up_lines)
        algorithm.find_shortest_path((1, 1), (7, 2))
        parent_node = Node((5, 1))
        combined_set = []
        combined_set.extend(algorithm.closed_set)
        combined_set.extend(algorithm.open_set)
        jumppoint_node = Node((6, 0), parent=parent_node, direction=(1, -1))

        self.assertEqual(jumppoint_node in combined_set or (
            jumppoint_node.position, jumppoint_node.direction) in combined_set, True)

    def test_scan_can_proceed_diagonally_and_find_a_forced_neighbour_at_c1(self):
        '''t1.map:
        7 . . . . G .
        6 . . . . F .
        5 T T T T T P   S = start
        4 . . . . . .   F = forced neighbour
        3 . . . . . .   G = goal
        2 . . . . . .   P = parent node
        1 . S . . . .
        0 . . . . . .
          0 1 2 3 4 5'''
        algorithm = JPS(self.t1)
        algorithm.find_shortest_path((1, 1), (4, 7))
        parent_node = Node((5, 5))
        combined_set = []
        combined_set.extend(algorithm.closed_set)
        combined_set.extend(algorithm.open_set)
        jumppoint_node = Node((4, 6), parent=parent_node, direction=(-1, 1))

        self.assertEqual(jumppoint_node in combined_set or (
            jumppoint_node.position, jumppoint_node.direction) in combined_set, True)

    def test_scan_can_proceed_diagonally_and_find_a_forced_neighbour_at_c2(self):
        '''t2.map:
        7 G . . . . . .
        6 . . . . . F .
        5 T T T T T P .
        4 . . . . . . .
        3 T T . . . . T
        2 . . . . . T T
        1 . S . . T T T
        0 . . . . . . .
          0 1 2 3 4 5 6'''
        algorithm = JPS(self.t2)
        algorithm.find_shortest_path((1, 1), (0, 7))
        parent_node = Node((5, 5))
        combined_set = []
        combined_set.extend(algorithm.closed_set)
        combined_set.extend(algorithm.open_set)
        jumppoint_node = Node((5, 6), parent=parent_node, direction=(0, 1))

        self.assertEqual(jumppoint_node in combined_set or (
            jumppoint_node.position, jumppoint_node.direction) in combined_set, True)

    def test_scan_can_proceed_diagonally_and_find_a_forced_neighbour_at_c3(self):
        '''t2.map:
        7 . . . . G . .
        6 . . . . . . F
        5 T T T T T P .
        4 . . . . . . .
        3 T T . . . . T
        2 . . . . . T T
        1 . S . . T T T
        0 . . . . . . .
          0 1 2 3 4 5 6'''
        algorithm = JPS(self.t2)
        algorithm.find_shortest_path((1, 1), (0, 7))
        parent_node = Node((5, 5))
        combined_set = []
        combined_set.extend(algorithm.closed_set)
        combined_set.extend(algorithm.open_set)
        jumppoint_node = Node((6, 6), parent=parent_node, direction=(1, 1))

        self.assertEqual(jumppoint_node in combined_set or (
            jumppoint_node.position, jumppoint_node.direction) in combined_set, True)

    def test_scan_can_proceed_diagonally_and_find_a_forced_neighbour_at_b3(self):
        '''t2.map:
        7 . . . . G . .
        6 . . . . . . . 
        5 T T T T T P F 
        4 . . . . . . .
        3 T T . . . . T
        2 . . . . . T T
        1 . S . . T T T
        0 . . . . . . .
          0 1 2 3 4 5 6'''
        algorithm = JPS(self.t2)
        algorithm.find_shortest_path((1, 1), (0, 7))
        parent_node = Node((5, 5))
        combined_set = []
        combined_set.extend(algorithm.closed_set)
        combined_set.extend(algorithm.open_set)
        jumppoint_node = Node((6, 5), parent=parent_node, direction=(1, 0))

        self.assertEqual(jumppoint_node in combined_set or (
            jumppoint_node.position, jumppoint_node.direction) in combined_set, True)

    def test_scan_can_proceed_diagonally_obstacle_at_c2_finds_forced_neighbour_at_c3(self):
        '''t3.map:
        7 . . . . G . . .
        6 . . . . . . . .
        5 T T T T T T . .
        4 . . . . . . . .
        3 T T . . . . . .
        2 T T F . . T T T
        1 . P . . T T T T
        0 S . . . T . . .
          0 1 2 3 4 5 6 7'''
        algorithm = JPS(self.t3)
        algorithm.find_shortest_path((0, 0), (4, 7))
        parent_node = Node((1, 1))
        combined_set = []
        combined_set.extend(algorithm.closed_set)
        combined_set.extend(algorithm.open_set)
        jumppoint_node = Node((2, 2), parent=parent_node, direction=(1, 1))

        self.assertEqual(jumppoint_node in combined_set or (
            jumppoint_node.position, jumppoint_node.direction) in combined_set, True)

    def test_scan_can_proceed_diagonally_obstacle_at_c2_finds_forced_neighbour_at_b3(self):
        '''t3.map:
        7 . . . . G . . .
        6 . . . . . . . .
        5 T T T T T T . .
        4 . . . . . . . .
        3 T T . . . . . .
        2 T T . . . T T T
        1 . P F . T T T T
        0 S . . . T . . .
          0 1 2 3 4 5 6 7'''
        algorithm = JPS(self.t3)
        algorithm.find_shortest_path((0, 0), (4, 7))
        parent_node = Node((1, 1))
        combined_set = []
        combined_set.extend(algorithm.closed_set)
        combined_set.extend(algorithm.open_set)
        jumppoint_node = Node((2, 1), parent=parent_node, direction=(1, 0))

        self.assertEqual(jumppoint_node in combined_set or (
            jumppoint_node.position, jumppoint_node.direction) in combined_set, True)

    def test_scan_can_proceed_diagonally_obstacle_at_b3_finds_forced_neighbour_at_c3(self):
        '''t3_flipped.map:
        8 . . . . . . . .
        7 . . . . G . . .
        6 . . . . . . . .
        5 T T T T T T . .
        4 . . . . . . . .
        3 T . . . . . . .
        2 . . . . . T T T
        1 . . T T . T T T
        0 S . T T . . . .
          0 1 2 3 4 5 6 7'''
        algorithm = JPS(self.t3_flipped)
        algorithm.find_shortest_path((0, 0), (4, 7))
        parent_node = Node((1, 1))
        combined_set = []
        combined_set.extend(algorithm.closed_set)
        combined_set.extend(algorithm.open_set)
        jumppoint_node = Node((2, 2), parent=parent_node, direction=(1, 1))

        self.assertEqual(jumppoint_node in combined_set or (
            jumppoint_node.position, jumppoint_node.direction) in combined_set, True)

    def test_produce_neighbours_for_scan_diagonal_works_correctly_for_right_up(self):
        '''I imagine it as going right and up in this grid:
        c ■  	
        b ■  ↗          The black squares were already covered.
        a ■  ■	■       They are the so-called natural neigbours.
          1  2  3 
        '''
        parent_node = Node((0, 0), None, None)
        start_node = Node((1, 1), parent=parent_node, direction=(1, 1))
        neighbours = self.algorithm.produce_neighbours(start_node)
        # a1,a2,a3,b1,b2,b3,c1,c2,c3
        # a2,a3,b1,b2,b3,c1,c2,c3
        # a3,b2,b3,c1,c2,c3
        self.assertEqual(neighbours, ((0, 0), (1, 0), (2, 0),
                         (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)))

    def test_produce_neighbours_for_scan_diagonal_works_correctly_for_right_down(self):
        '''I imagine it as going right and up in this grid:
        c ■  	
        b ■  ↗          The black squares were already covered.
        a ■  ■	■       They are the so-called natural neigbours.
          1  2  3 
        '''
        parent_node = Node((0, 0), None, None)
        start_node = Node((1, 1), parent=parent_node, direction=(1, -1))
        neighbours = self.algorithm.produce_neighbours(start_node)

        # a2,a3,b1,b2,b3,c1,c2,c3
        # a3,b2,b3,c1,c2,c3
        # self.assertEqual(neighbours,((0, 0), (1, 1), (1, 0), (2, 2), (2, 1), (2, 0)))
        self.assertEqual(neighbours, ((0, 2), (0, 1), (0, 0),
                         (1, 2), (1, 1), (1, 0), (2, 2), (2, 1), (2, 0)))

    def test_produce_neighbours_for_scan_diagonal_works_correctly_for_left_down(self):
        '''I imagine it as going right and up in this grid:
        c ■  	
        b ■  ↗          The black squares were already covered.
        a ■  ■	■       They are the so-called natural neigbours.
          1  2  3 
        '''
        parent_node = Node((0, 0), None, None)
        start_node = Node((1, 1), parent=parent_node, direction=(-1, -1))
        neighbours = self.algorithm.produce_neighbours(start_node)

        # a3,b2,b3,c1,c2,c3
        self.assertEqual(neighbours, ((2, 2), (1, 2), (0, 2),
                         (2, 1), (1, 1), (0, 1), (2, 0), (1, 0), (0, 0)))

    def test_produce_neighbours_for_scan_diagonal_works_correctly_for_left_up(self):
        '''I imagine it as going right and up in this grid:
        c ■  	
        b ■  ↗          The black squares were already covered.
        a ■  ■	■       They are the so-called natural neigbours.
          1  2  3 
        '''
        parent_node = Node((0, 0), None, None)
        start_node = Node((1, 1), parent=parent_node, direction=(-1, 1))
        neighbours = self.algorithm.produce_neighbours(start_node)
        # a2,a3,b1,b2,b3,c1,c2,c3
        # a3,b2,b3,c1,c2,c3
        self.assertEqual(neighbours, ((2, 0), (2, 1), (2, 2),
                         (1, 0), (1, 1), (1, 2), (0, 0), (0, 1), (0, 2)))

    def test_find_shortest_path_returns_shortest_path(self):
        algorithm = JPS(self.wall_map)
        result = algorithm.find_shortest_path((0, 0), (0, 7))

        self.assertEqual(int(result), 7)

    def test_find_shortest_path_returns_shortest_path_2(self):
        algorithm = JPS(self.wall_map)
        result = algorithm.find_shortest_path((0, 0), (1, 7))

        self.assertEqual(float(result), 7.41)

    def test_find_shortest_path_returns_shortest_path_3(self):
        algorithm = JPS(self.arena_map)
        result = algorithm.find_shortest_path((5, 5), (20, 20))

        self.assertAlmostEqual(float(result), 23.5, places=1)

    def test_jps_finds_distance_on_arena_map(self):
        algorithm = JPS(self.arena_map)
        distance = algorithm.find_shortest_path((2, 2), (40, 40))
        self.assertAlmostEqual(float(distance), 55.9, places=1)

    def test_jps_finds_distance_on_arena_map_2(self):
        algorithm = JPS(self.arena2_map)
        distance = algorithm.find_shortest_path((1, 2), (5, 20))
        self.assertGreaterEqual(float(distance), 20)
        self.assertLessEqual(float(distance), 21)

    def test_jps_returns_minus_one_when_no_path_possible(self):
        algorithm = JPS(self.no_path_map)
        distance = algorithm.find_shortest_path((6, 6), (18, 30))
        self.assertGreaterEqual(distance, -1)
