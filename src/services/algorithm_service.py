from jps import JPS
from dijkstra import Dijkstra
from create_map import create_map
import time


class AlgorithmService():
    def __init__(self):
        pass

    def run_algorithm(self, start_coordinates, goal_coordinates, map_path, slides, jps=False, dijkstra=False, visual=False):
        start_coordinates = self.coordinates_extract(start_coordinates)
        goal_coordinates = self.coordinates_extract(goal_coordinates)
        map = create_map(map_path)
        
        init_start_time = time.time()
        algorithm = JPS(map) if jps else Dijkstra(map)
        distance = algorithm.find_shortest_path(
            start_coordinates, goal_coordinates, slides, visual=visual)

        init_end_time = time.time()


        init_time = init_end_time - init_start_time

        running_start_time = time.time()

        _ = algorithm.find_shortest_path(
                    start_coordinates, goal_coordinates, slides, visual=False)

        running_end_time = time.time()
        running_time = running_end_time - running_start_time

        execution_time = init_time + running_time

        return distance, execution_time

    def count_edges(self,map_path):
        map = create_map(map_path)
        algorithm = Dijkstra(map)
        return algorithm.edge_counter

    def count_vertices(self,map_path):
        map = create_map(map_path)
        algorithm = Dijkstra(map)
        return len(algorithm.vertices)



    def coordinates_ok(self, start, goal):
        start = self.coordinates_extract(start)
        goal = self.coordinates_extract(goal)
        if start == False or goal == False:
            return False
        return True

    def view_map(self, map_path):
        map = create_map(map_path)
        num_rows = len(map)
        len_row = len(map[0])

        rotated_regular_map = [
            [''] * num_rows for _ in range(len_row)]

        for i in range(num_rows):
            for j in range(len_row):
                rotated_regular_map[len_row - j - 1][i] = map[i][j]
        
        rmap = ""
        for i, row in enumerate(rotated_regular_map):
            row_with_numbers = [str(len_row-i - 1)] + row
            rmap += " ".join(row_with_numbers) + "\n"
        last_row = " ".join(str(i) for i in range(num_rows))
        rmap += "  "+last_row + "\n"
        return rmap

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
