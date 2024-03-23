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
    parser.add_argument('-a', '--start_node', type=int, default=200, help='Start node, e.g. 200')
    parser.add_argument('-b', '--end_node', type=int, default=256, help='End node, e.g. 256')
    parser.add_argument('-d', '--dijkstra',action='store_true', help='You want to try dijkstra')
    parser.add_argument('-j', '--jps',action='store_true', help='You want to try JPS (not working yet)')
    args = parser.parse_args()
    path = "../maps/"+args.file
    lines = create_array(path)
    a = args.start_node
    b = args.end_node
    if args.dijkstra or True:
        algorithm = Dijkstra(lines)
        print(algorithm.find_shortest_path(a,b))

