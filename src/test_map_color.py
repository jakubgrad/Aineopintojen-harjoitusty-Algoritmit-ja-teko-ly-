class ColoredMap:
    def __init__(self, map):
        self.map = map

    def print_map(self):
        transposed_map = [list(column) for column in zip(*self.map)]
        for i, row in enumerate(reversed(transposed_map)):
            print(' '.join(row))
        print('  ' + ' '.join(str(i) for i in range(len(self.map[0]))))


# Example usage
map = [
    ['\033[92mS\033[0m', '.', '.', '.'],
    ['2', '\033[94mT\033[0m', '.', '.'],
    ['.', '.', '.', '.'],
    ['.', '.', '.', '\033[91mG\033[0m']
]

colored_map = ColoredMap(map)
colored_map.print_map()
