import os

current_directory = os.getcwd()
root_directory = current_directory  # os.path.dirname(current_directory)
maps_directory = os.path.join(root_directory, "maps")
default_dijkstra = os.path.join(maps_directory, "arena.map")
default_jps = os.path.join(maps_directory, "wall.map")

if __name__ == "__main__":
    print("Current Directory:", current_directory)
