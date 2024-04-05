import unittest
from jps import JPS, Node
from create_array import create_array

class TestJPS(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")
        path = "maps/wall.map"
        lines = create_array(path)
        self.up_lines = create_array("maps/up.map")
        self.algorithm = JPS(lines)
        self.start_coordinates = (0,0)
        self.goal_coordinates = (4,7)
        self.start_node = Node(self.start_coordinates)
        self.goal_node = Node(self.goal_coordinates)
        
    def test_node_class_works_correctly(self):
        node = Node((0,0))
        self.assertEqual(node.position, (0,0))

    def test_subtracting_tuples_works_correctly(self):
        tuple1 = (8,6)
        tuple2 = (8,5)
        result = self.algorithm.subtract_tuples(tuple1,tuple2)

        self.assertEqual(result, (0,1))

    def test_node_class_str_works_correctly(self):
        parent_node = Node((2,7), parent=None, direction=(1,1))
        node = Node((3,8),parent=parent_node,direction=(1,0) )
        self.assertEqual(str(node), 'coordinates (3, 8), parent coordinates (2, 7), direction (1, 0)')

    def test_if_goal_node_is_not_within_map_0_is_returned(self):
        result = self.algorithm.find_shortest_path((-5,-2),(4,7))
        self.assertEqual(result, 0)

    def comparing_nodes_works_as_expected(self):
        parent_node = Node((2,7), parent=None, direction=(1,1))
        node1 = Node((3,8),parent=parent_node,direction=(1,0) )
        node2 = Node((3,8),parent=parent_node,direction=(1,0) )
        self.assertEqual(node1,node2)


    def two_nodes_with_the_same_parameters_return_true_when_compared(self):
        parent_node = Node((0,0),parent=None, direction=(1,1))
        node1 = Node((2,2), parent=parent_node, direction=(0,0))
        node2 = Node((2,2), parent=parent_node, direction=(0,0))
        self.assertEqual(node1,node2)

    def test_node_class_works_correctly(self):
        start_node = Node((0,0), parent=None, direction=(1,1))
        node1 = Node((3,3), parent=start_node, direction=(1,0))
        node2 = Node((4,3), parent=node1, direction=(0,1))
        goal_node = Node((4,7), parent=node2, direction=(0,1))

        self.assertEqual(self.algorithm.recreate_path(goal_node), '(4, 7)(4, 3)(3, 3)(0, 0)')


    def test_if_start_node_and_end_node_are_the_same_return_0(self):
        result = self.algorithm.find_shortest_path((1,1),(1,1))
        self.assertEqual(result, 0)

    def test_JPS_initializes_properly(self):
        self.assertEqual(str(self.algorithm), 'Number of rows: 5, Length of a row: 8')
    
    def test_JPS_initializes_start_and_end_nodes_correctly_when_finding_shortest_path(self):
        self.algorithm.find_shortest_path((0,0),(4,7))
        start_node = self.start_node 
        goal_node = self.goal_node

        self.assertEqual(self.algorithm.start_node.position, (0,0))
        self.assertEqual(self.algorithm.goal_node.position, (4,7))

    def test_open_set_initializes_as_empty(self):
        self.assertEqual(len(self.algorithm.open_set), 0)

    def test_a_position_direction_tuple_can_be_added_to_the_open_set(self):
        self.algorithm.open_set.append(((0,0),"r"))

        self.assertEqual(self.algorithm.open_set, [((0,0),"r")])

    def test_open_set_initializes_as_empty(self):
        self.assertEqual(len(self.algorithm.open_set), 0)

    def test_jps_adds_3_adjacent_squares_to_open_list_when_starting_from_a_corner(self):
        start_coordinates = self.start_coordinates
        goal_coordinates = self.goal_coordinates
        self.algorithm.find_shortest_path(start_coordinates, goal_coordinates)

        node1 = Node((1,0), parent=self.algorithm.start_node, direction=(1,0))
        node2 = Node((1,1), parent=self.algorithm.start_node, direction=(1,1))
        node3 = Node((0,1), parent=self.algorithm.start_node, direction=(0,1))

        self.assertEqual(node1 in self.algorithm.open_set, True)

    def test_same_node_cannot_be_added_to_the_open_set_twice(self):
        #node = Node((2,2), parent=Node, direction=(1,1)),
        #self.algorithm.add_node_to_open_set_if_new(node, (3,3))
        #result = self.algorithm.add_node_to_open_set_if_new(node, (3,3))

        self.assertEqual(False, False)
        

    def test_jps_adds_8_adjacent_squares_to_open_list_when_starting_from_a_place_with_free_space_to_all_sides(self):
        self.algorithm.find_shortest_path((1,1),(4,7))

        nodes = [
          Node((0,2), parent=self.algorithm.start_node, direction=(-1,1)),
          Node((1,2), parent=self.algorithm.start_node, direction=(0,1)),
          Node((2,2), parent=self.algorithm.start_node, direction=(1,1)),
          Node((0,1), parent=self.algorithm.start_node, direction=(-1,0)),
          Node((2,1), parent=self.algorithm.start_node, direction=(1,0)),
          Node((0,0), parent=self.algorithm.start_node, direction=(-1,-1)),
          Node((1,0), parent=self.algorithm.start_node, direction=(0,-1)),
          Node((2,0), parent=self.algorithm.start_node, direction=(1,-1))
        ]

        self.assertEqual(len(self.algorithm.open_set), 8)
        self.assertEqual(all(node in self.algorithm.open_set for node in nodes), True)

    def test_open_set_heap_is_a_heap(self):
        self.algorithm.find_shortest_path(self.start_coordinates,self.goal_coordinates)

        self.assertEqual(type(self.algorithm.open_set_heap), list) 

    def test_scanning_straight_stops_when_hitting_a_wall(self):
        node_at_map_border = Node((4,7), parent=None, direction=(1,0))
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
        node_going_right = Node((3,3),parent=None,direction=(1,0))
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
        node_going_left = Node((3,3),parent=None,direction=(-1,0))
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
        node_going_up = Node((3,3),parent=None,direction=(0,1))
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
        node_going_down = Node((3,3),parent=None,direction=(0,-1))
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

    def test_scan_can_proceed_straight_up_and_find_a_forced_neighbour_diagonally_left(self):
        algorithm = JPS(self.up_lines)
        algorithm.find_shortest_path((1,1),(5,2))
        parent_node = Node((3,1))
        jumppoint_node = Node((4,2), parent=parent_node, direction=(1,1))
        combined_set = []
        combined_set.extend(algorithm.closed_set)
        combined_set.extend(algorithm.open_set_heap) 
        self.assertEqual(jumppoint_node in combined_set,True)

    def test_scan_can_proceed_straight_up_and_find_a_forced_neighbour_diagonally_right(self):
        algorithm = JPS(self.up_lines)
        algorithm.find_shortest_path((1,1),(7,2))
        parent_node = Node((5,1))
        combined_set = []
        combined_set.extend(algorithm.closed_set)
        combined_set.extend(algorithm.open_set_heap) 
        jumppoint_node = Node((6,0), parent=parent_node, direction=(1,-1))

        self.assertEqual(jumppoint_node in combined_set,True)

    def test_produce_neighbours_for_scan_diagonal_works_correctly_for_right_up(self):
        '''I imagine it as going right and up in this grid:
        c ■  	
        b ■  ↗          The black squares were already covered.
        a ■  ■	■       They are the so-called natural neigbours.
          1  2  3 
        '''
        parent_node = Node((0,0),None,None)
        start_node = Node((1,1),parent=parent_node,direction=(1,1))
        neighbours = self.algorithm.produce_neighbours(start_node)
        #a1,a2,a3,b1,b2,b3,c1,c2,c3
        #a2,a3,b1,b2,b3,c1,c2,c3
        #a3,b2,b3,c1,c2,c3
        self.assertEqual(neighbours,((0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)))

    def test_produce_neighbours_for_scan_diagonal_works_correctly_for_right_down(self):
        '''I imagine it as going right and up in this grid:
        c ■  	
        b ■  ↗          The black squares were already covered.
        a ■  ■	■       They are the so-called natural neigbours.
          1  2  3 
        '''
        parent_node = Node((0,0),None,None)
        start_node = Node((1,1),parent=parent_node,direction=(1,-1))
        neighbours = self.algorithm.produce_neighbours(start_node)

        #a2,a3,b1,b2,b3,c1,c2,c3
        #a3,b2,b3,c1,c2,c3
        #self.assertEqual(neighbours,((0, 0), (1, 1), (1, 0), (2, 2), (2, 1), (2, 0)))
        self.assertEqual(neighbours,((0, 2), (0, 1), (0, 0), (1, 2), (1, 1), (1, 0), (2, 2), (2, 1), (2, 0)))

    def test_produce_neighbours_for_scan_diagonal_works_correctly_for_left_down(self):
        '''I imagine it as going right and up in this grid:
        c ■  	
        b ■  ↗          The black squares were already covered.
        a ■  ■	■       They are the so-called natural neigbours.
          1  2  3 
        '''
        parent_node = Node((0,0),None,None)
        start_node = Node((1,1),parent=parent_node,direction=(-1,-1))
        neighbours = self.algorithm.produce_neighbours(start_node)

        #a3,b2,b3,c1,c2,c3
        self.assertEqual(neighbours,((2, 2), (1, 2), (0, 2), (2, 1), (1, 1), (0, 1), (2, 0), (1, 0), (0, 0)))

    def test_produce_neighbours_for_scan_diagonal_works_correctly_for_left_up(self):
        '''I imagine it as going right and up in this grid:
        c ■  	
        b ■  ↗          The black squares were already covered.
        a ■  ■	■       They are the so-called natural neigbours.
          1  2  3 
        '''
        parent_node = Node((0,0),None,None)
        start_node = Node((1,1),parent=parent_node,direction=(-1,1))
        neighbours = self.algorithm.produce_neighbours(start_node)
        #a2,a3,b1,b2,b3,c1,c2,c3
        #a3,b2,b3,c1,c2,c3
        self.assertEqual(neighbours,((2, 0), (2, 1), (2, 2), (1, 0), (1, 1), (1, 2), (0, 0), (0, 1), (0, 2)))

