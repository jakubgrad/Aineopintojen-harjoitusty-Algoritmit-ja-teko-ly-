import unittest
from dijkstra import Dijkstra
from create_array import create_array

class TestDijkstra(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")
        #path = "../../maps/arena.map"
        path = "maps/arena.map"
        lines = create_array(path)
        self.algorithm = Dijkstra(lines)
        #a = args.start_node
        #b = args.end_node


    def test_dijkstra_initializes_properly(self):
        self.assertEqual(str(self.algorithm), 'Number of nodes: 2401')

    def test_dijkstra_finds_distances_on_arena_map(self):
        self.assertEqual(self.algorithm.find_shortest_path((4,3),(5,11)), 8.41)

'''
    def test_dijkstra_works_for_small_graphs_out_of_maps(self):
        self.algorithm.add_edge(1,2,2)
        self.assertEqual(self.algorithm.find_shortest_path(1,3), -1)
        self.algorithm.add_edge(1,3,5)
        self.assertEqual(self.algorithm.find_shortest_path(1,3), 5)
        self.algorithm.add_edge(2,3,1)
        self.assertEqual(self.algorithm.find_shortest_path(2,3), 1)
'''

