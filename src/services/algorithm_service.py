from jps import JPS
from dijkstra import Dijkstra
from create_map import create_map


class AlgorithmService():
    def __init__(self):
        pass

    def run_algorithm(self, start_coordinates, goal_coordinates, map_path, slides, jps=False, dijkstra=False, visualization=False):
        start_coordinates = self.coordinates_extract(start_coordinates)
        goal_coordinates = self.coordinates_extract(goal_coordinates)
        lines = create_map(map_path)

        algorithm = JPS(lines) if jps else Dijkstra(lines)
        distance = algorithm.find_shortest_path(
            start_coordinates, goal_coordinates, slides, visual=True)
        return distance

    def coordinates_ok(self, start, goal):
        start = self.coordinates_extract(start)
        goal = self.coordinates_extract(goal)
        if start == False or goal == False:
            return False
        return True

    def coordinates_extract(self, input_text):
        try:
            coordinates = input_text.split(',')
            if len(coordinates) != 2:
                raise ValueError("Invalid input format")
            x = int(coordinates[0])
            y = int(coordinates[1])
            if not (isinstance(x, int) and isinstance(y, int)):
                raise ValueError("Both coordinates must be integers")
            return (x, y)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return False


algorithm_service = AlgorithmService()
