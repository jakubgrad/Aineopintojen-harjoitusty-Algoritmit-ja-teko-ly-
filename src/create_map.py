def create_map(path):
    """A handy function that takes a map from the folder maps in the root directory and returns it as a list of list 

    Args:
        Path to the map, e.g. map/arena.map in the form ...TTT..T etc.

    Returns:
        A list of lists such as [[["."],["T"]...["T"]],[["."],["T"]...["T"],....]]] 
        ....where T is an obstacle, . is a free square
    """

    with open(path, "r") as file:
        lines = []
        file.readline()
        height_line = file.readline().strip()
        height = height_line.split(" ")[1]
        width_line = file.readline().strip()
        width = width_line.split(" ")[1]
        file.readline()
        for l in file:
            line = l.strip()
            # print(line)
            lines.append(line)
    map = [list(row) for row in lines]
    return map
