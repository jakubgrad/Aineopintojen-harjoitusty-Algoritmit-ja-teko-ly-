from heapq import * 
from dijkstra import Dijkstra 
from create_array import create_array
import argparse


if __name__ == "__main__":
    """Main part of the program, that takes parameters such as user-chosen algorithm, map, starting and terminating nodes.

    Prints the shortest path calculated by the chosen algorithm
    """

    parser = argparse.ArgumentParser(description='JPS vs Djikstra.')
    parser.add_argument('-m', '--file', type=str, default="arena.map",help='Name of the file inside map folder, e.g. arena.map')
    parser.add_argument('-a', '--start_node', type=int, default=47, help='Start node, e.g. 47')
    parser.add_argument('-b', '--end_node', type=int, default=93, help='End node, e.g. 93')
    parser.add_argument('-d', '--dijkstra',action='store_true', help='You want to try dijkstra')
    args = parser.parse_args()
    path = "../maps/"+args.file
    lines = create_array(path)
    a = args.start_node
    b = args.end_node
    if args.dijkstra:
        algorithm = Dijkstra(lines)
        print(algorithm.find_shortest_path(a,b))

