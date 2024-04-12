from jps import JPS
from dijkstra import Dijkstra
from dijkstra import Presentation
from create_array import create_array


class AlgorithmService():
    def __init__(self):
        pass

    def run_algorithm(self, start_coordinates, goal_coordinates, map_path, slides, jps=False, dijkstra=False, visualization=False):
        start_coordinates = self.coordinates_extract(start_coordinates)
        goal_coordinates = self.coordinates_extract(goal_coordinates)
        lines = create_array(map_path)
        if jps:
            algorithm = JPS(lines)
            distance = algorithm.find_shortest_path(
                start_coordinates, goal_coordinates, slides, visual=True)
            return distance
        else:
            presentation = Presentation(lines)
            algorithm = Dijkstra(lines, presentation)
            distance = algorithm.find_shortest_path(
                start_coordinates, goal_coordinates)
            slides.extend(presentation.slides)
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
