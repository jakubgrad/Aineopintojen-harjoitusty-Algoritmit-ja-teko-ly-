def create_map(path):
    """A handy function that takes a map from the folder maps
       in the root directory and returns it as a list of list 

    Args:
        Path to the map, e.g. map/arena.map in the form ...TTT..T etc.

    Returns:
        A list of lists such as [[["."],["T"]...["T"]],[["."],["T"]...["T"],....]]] 
        ....where T is an obstacle, . is a free square
    """

    with open(path, "r", encoding='utf-8') as file:
        lines = []
        file.readline()
        _ = file.readline().strip()
        _ = file.readline().strip()
        file.readline()
        for l in file:
            line = l.strip()
            lines.append(line)
    grid = [list(row) for row in lines]
    return grid
