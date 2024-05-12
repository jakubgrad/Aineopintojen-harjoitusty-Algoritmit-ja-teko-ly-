import unittest
from dijkstra import Dijkstra
from create_map import create_map


class TestDijkstra(unittest.TestCase):
    def setUp(self):
        self.arena_map = create_map("maps/arena.map")
        self.arena2_map = create_map("maps/arena2.map")
        self.no_path_map = create_map("maps/no_path.map")

        slides = []
        self.algorithm = Dijkstra(self.arena_map)

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

    def test_dijkstra_returns_minus_one_when_no_path_possible(self):
        algorithm = Dijkstra(self.no_path_map)
        distance = algorithm.find_shortest_path((6, 6), (18, 30))
        self.assertGreaterEqual(distance, -1)

    def test_dijkstra_returns_None_when_start_and_goal_nodes_are_the_same(self):
        algorithm = Dijkstra(self.arena_map)
        distance = algorithm.find_shortest_path((6, 6), (6, 6))
        self.assertEqual(distance, None)
