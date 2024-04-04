import unittest
from jps import JPS, Node
from create_array import create_array

class TestJPS(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")
        path = "maps/wall.map"
        lines = create_array(path)
        self.algorithm = JPS(lines)
        self.start_node = Node((0,0))
        self.goal_node = Node((4,7))
        
    def test_node_class_works_correctly(self):
        node = Node((0,0))
        self.assertEqual(node.position(), (0,0))

    def test_if_start_node_and_end_node_are_the_same_return_0(self):
        result = self.algorithm.find_shortest_path((1,1),(1,1))
        self.assertEqual(result, 0)

    def test_JPS_initializes_properly(self):
        self.assertEqual(str(self.algorithm), 'Number of rows: 5, Length of a row: 8')
    
    def test_JPS_initializes_start_and_end_nodes_correctly_when_finding_shortest_path(self):
        self.algorithm.find_shortest_path((0,0),(4,7))
        start_node = self.start_node 
        goal_node = self.goal_node

        self.assertEqual(self.algorithm.start_node.i, 0)
        self.assertEqual(self.algorithm.start_node.j, 0)
        self.assertEqual(self.algorithm.goal_node.i, 4)
        self.assertEqual(self.algorithm.goal_node.j, 7)

    def test_open_set_initializes_as_empty(self):
        self.assertEqual(len(self.algorithm.open_set), 0)

    def test_a_position_direction_tuple_can_be_added_to_the_open_set(self):
        self.algorithm.open_set.append(((0,0),"r"))

        self.assertEqual(self.algorithm.open_set, [((0,0),"r")])

    def test_open_set_initializes_as_empty(self):
        self.assertEqual(len(self.algorithm.open_set), 0)

    def test_jps_adds_3_adjacent_squares_to_open_list_when_starting_from_a_corner(self):
        result = self.algorithm.find_shortest_path((0,0),(4,7))

        self.assertEqual(len(result), 3)
        self.assertEqual((1,1) in [node.position() for node in result], True)


    #def test_JPS_correctly_initializes_open_set_when_finding_shortest_path(self):
    #    self.algorithm.find_shortest_path(0,0,4,7)
#
 #       self.assertEqual(self.algorithm.open_set.i, 0)
  #      self.assertEqual(self.algorithm.start_node.j, 0)
   #     self.assertEqual(self.algorithm.goal_node.i, 4)
    #    self.assertEqual(self.algorithm.goal_node.j, 7)


