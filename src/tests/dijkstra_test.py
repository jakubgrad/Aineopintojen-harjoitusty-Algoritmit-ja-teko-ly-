import unittest
from dijkstra import Dijkstra
from create_map import create_map


class TestDijkstra(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")
        # path = "../../maps/arena.map"
        self.arena_map = create_map("maps/arena.map")
        self.arena2_map = create_map("maps/arena2.map")

        slides = []
        self.algorithm = Dijkstra(self.arena_map)
        # a = args.start_node
        # b = args.end_node

    def test_dijkstra_initializes_properly(self):
        self.assertEqual(str(self.algorithm), 'Number of nodes: 2401')

    def test_dijkstra_finds_distances_on_arena_map(self):
        slides = []
        distance = self.algorithm.find_shortest_path(
            (4, 3), (5, 11), slides, visual=False)
        self.assertEqual(distance, 8.41)

    def test_dijkstra_finds_straight_distance_on_arena_map(self):
        slides = []
        distance = self.algorithm.find_shortest_path(
            (3, 43), (27, 43), slides, visual=False)
        self.assertEqual(distance, 24)

    def test_dijkstra_finds_distance_on_arena_map_1(self):
        slides = []
        distance = self.algorithm.find_shortest_path(
            (5, 5), (20, 20), slides, visual=False)
        self.assertAlmostEqual(float(distance), 23.5, places=1)

    def test_dijkstra_finds_distance_on_arena_map_2(self):
        slides = []
        distance = self.algorithm.find_shortest_path(
            (2, 2), (40, 40), slides, visual=False)
        self.assertAlmostEqual(float(distance), 55.9, places=1)

    def test_dijkstra_finds_distance_on_arena_map_2(self):
        algorithm = Dijkstra(self.arena2_map)
        distance = algorithm.find_shortest_path((1, 2), (5, 20))
        self.assertGreaterEqual(float(distance), 21)
        self.assertLessEqual(float(distance), 22)


'''
    def test_dijkstra_works_for_small_graphs_out_of_maps(self):
        self.algorithm.add_edge(1,2,2)
        self.assertEqual(self.algorithm.find_shortest_path(1,3), -1)
        self.algorithm.add_edge(1,3,5)
        self.assertEqual(self.algorithm.find_shortest_path(1,3), 5)
        self.algorithm.add_edge(2,3,1)
        self.assertEqual(self.algorithm.find_shortest_path(2,3), 1)
'''
