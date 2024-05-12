import time
from jps import JPS
from dijkstra import Dijkstra
from create_map import create_map


class AlgorithmService():
    def __init__(self):
        pass

    def run_algorithm(self, start_coordinates, goal_coordinates,
            map_path, slides, jps=False, visual=False):
        """Initializes and runs selected algorithm to find shortest path 
        between the start and goal coordinates on specified map.

        Args:
            start_coordinates (str): The coordinates of the starting point in the format "x,y".
            goal_coordinates (str): The coordinates of the goal point in the format "x,y".
            map_path (str): The path to the map file.
            slides (list): a list that collects snapshots of execution 
            jps (bool): whther JPS should be used. Default is False.
            dijkstra (bool): whther Dijkstra should be used. Default is False.
            visual (bool): Whether to save slides for animation in UI. Default is False.

        Returns:
            distance (float): The shortest distance between the start and goal points.
            execution_time (float): The initialization and running time of the algorithm in seconds.
            message (str): A message containing information about the algorithm's results
                and performance.
        """

        start_coordinates = self.coordinates_extract(start_coordinates)
        goal_coordinates = self.coordinates_extract(goal_coordinates)
        grid = create_map(map_path)

        start_time = time.time()

        algorithm = JPS(grid) if jps else Dijkstra(grid)

        distance = algorithm.find_shortest_path(
            start_coordinates, goal_coordinates, slides, visual=visual)

        end_time = time.time()

        execution_time = end_time - start_time

        #jps_time_complexity = jps_branching_factor**distance

        message = (f"Distance is {distance}\n"
                   f"Execution time is {execution_time}\n")

        return distance, execution_time, message

    def coordinates_ok(self, start, goal, map_path):
        """Check if start and goal coordinates are in a valid format.

        Args:
            start (str): The coordinates of the starting point in the format "x,y".
            goal (str): The coordinates of the goal point in the format "x,y".
            map (str): a filepath that contains the map

        Returns:
            True if both coordinates are in a valid format and within the map,
            False otherwise.
        """

        grid = create_map(map_path)

        start = self.coordinates_extract(start)
        goal = self.coordinates_extract(goal)
        if start is False or goal is False:
            return False

        rows = len(grid)
        cols = len(grid[0])

        x, y = start
        if not (0 <= x < rows and 0 <= y < cols):
            return False

        x, y = goal
        if not (0 <= x < rows and 0 <= y < cols):
            return False

        return True

    def view_map(self, map_path):
        """Generate preview of the map

        Args:
            map_path (str): The path to the map file.

        Returns:
            A string representing the map with vertical and horizontal coordinates,
            flipped so that users can use cartesian coordinates.
        """

        grid = create_map(map_path)
        num_rows = len(grid)
        len_row = len(grid[0])

        rotated_grid = [[''] * num_rows for _ in range(len_row)]

        for i in range(num_rows):
            for j in range(len_row):
                rotated_grid[len_row - j - 1][i] = grid[i][j]

        preview = ""
        for i, row in enumerate(rotated_grid):
            row_with_numbers = [str(len_row - i - 1)] + row
            preview += " ".join(row_with_numbers) + "\n"
        last_row = " ".join(str(i) for i in range(num_rows))
        preview += "  " + last_row + "\n"
        return preview

    def coordinates_extract(self, input_text):
        """Extract coordinates from the input text

        Args:
            input_text (str): The input text containing coordinates in the format "x,y".

        Returns:
            A tuple containing the extracted coordinates (x, y) if input is valid, 
            False if the input format is invalid.
        """

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
            print(f"Error: {e}")
            return False


algorithm_service = AlgorithmService()
