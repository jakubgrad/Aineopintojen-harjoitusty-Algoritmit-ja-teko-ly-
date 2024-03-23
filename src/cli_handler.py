import argparse

from create_array import create_array

parser = argparse.ArgumentParser(description='JPS vs Djikstra.')
parser.add_argument('-m', '--file', type=str, default="arena.map",help='Name of the file inside map folder, e.g. arena.map')
parser.add_argument('-a', '--start_node', type=int, default=47, help='Start node, e.g. 47')
parser.add_argument('-b', '--end_node', type=int, default=93, help='End node, e.g. 93')
parser.add_argument('-d', '--dijkstra',action='store_true', help='You want to try dijkstra')
args = parser.parse_args()
#if args.dijkstra:
#    print("Dijkstra flag -d is provided.")

path = "../maps/"+args.file
lines = create_array(path)
a = args.start_node
b = args.end_node

