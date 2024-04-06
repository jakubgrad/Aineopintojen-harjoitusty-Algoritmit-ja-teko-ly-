from jps import JPS

class AlgorithmService():
    def __init__(self):
        pass
    def run_algorithm(self,start_coordinates,goal_coordinates,map_path,jps=False,dijkstra=False):
        print("success")
    '''
        algorithm = JPS(lines)
        algorithm.find_shortest_path(start_coordinates, goal_coordinates)

    elif args.dijkstra:
        algorithm = Dijkstra(lines)
        print(algorithm.find_shortest_path(
            start_coordinates, goal_coordinates))

    '''
    def login(self, username, password):

        #For now:
        if username == "m":
            if password == "m":
                return True
        return False
               
    def registration(self, username, password):
        #For now:
        if username == "m":
            if password == "m":
                return True
        return False


algorithm_service = AlgorithmService()
