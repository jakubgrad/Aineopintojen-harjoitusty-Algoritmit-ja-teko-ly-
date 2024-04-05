from heapq import *
from dijkstra import Dijkstra
from jps import JPS
from create_array import create_array
import argparse


if __name__ == "__main__":
    """Main part of the program, that takes parameters such as user-chosen algorithm, map, starting and terminating coordinates.

    Prints the shortest path calculated by the chosen algorithm
    """

    parser = argparse.ArgumentParser(
        description='JPS vs Djikstra \nFor an example on Dijkstra (no visualization yet), run:\n python3 main.py --dijkstra --map arena.map 5 5 20 30\nFor a good example on JPS, run:\n python3 main.py --jps --map wall.map 0 0 4 7 ', formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--map', type=str, default="arena.map",
                        help='Name of the file inside map folder, e.g. arena.map')
    parser.add_argument('--dijkstra', action='store_true',
                        help='You want to try dijkstra')
    parser.add_argument('--jps', action='store_true',
                        help='You want to try JPS')
    parser.add_argument('integers', metavar='start_x start_y goal_x goal_y',
                        type=int, nargs='+', help="Start and goal nodes' coordinates, e.g. 0 0 4 7")

    args = parser.parse_args()
    start_coordinates = (args.integers[0], args.integers[1])
    goal_coordinates = (args.integers[2], args.integers[3])
    map_path = "../maps/"+args.map
    lines = create_array(map_path)
    if args.jps:
        algorithm = JPS(lines)
        algorithm.find_shortest_path(start_coordinates, goal_coordinates)

    elif args.dijkstra:
        algorithm = Dijkstra(lines)
        print(algorithm.find_shortest_path(
            start_coordinates, goal_coordinates))
