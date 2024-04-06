from jps import JPS
from dijkstra import Dijkstra
from create_array import create_array


class AlgorithmService():
    def __init__(self):
        pass

    def run_algorithm(self,start_coordinates,goal_coordinates,map_path,slides,jps=False,dijkstra=False,visualization=False):
        lines = create_array(map_path)
        if jps:
            algorithm = JPS(lines)
            algorithm.find_shortest_path(start_coordinates, goal_coordinates, slides)

        else:
            algorithm = Dijkstra(lines)
            slides.append(algorithm.find_shortest_path(start_coordinates, goal_coordinates,slides))

algorithm_service = AlgorithmService()
