## Implementation document = Toteutusdokumentti<br />

The program is written in `Python`. It has the following directory structure at the moment:<br />
<br /> 
├── maps                    &emsp;&emsp;&emsp;# maps used to test the tool <br />
├── src                     &emsp;&emsp;&emsp;# code files <br />
│   ├── tests               &emsp;&emsp;&emsp;#test files <br />
│   ├── create_map.py       &emsp;&emsp;&emsp;# turns a map into an array of rows <br />
│   ├── dijkstra.py         &emsp;&emsp;&emsp;# implementation of Dijkstra<br /> 
│   ├── jps.py              &emsp;&emsp;&emsp;# implementation of JPS<br /> 
│   ├── config.py           &emsp;&emsp;&emsp;# provides useful variables like<br /> 
│   │                       &emsp;&emsp;&emsp;# path to root directory<br /> 
│   ├── main.py             &emsp;&emsp;&emsp;# allows running the tool as a user<br />
│   └── services            &emsp;&emsp;&emsp;#  
│       └── algorithm_service.py &emsp;&emsp;&emsp;# responsible <br />
│                           &emsp;&emsp;&emsp;# for interaction between UI and algorithms <br />
├── ui                      &emsp;&emsp;&emsp;# ui files <br />
│   └── ui.py               &emsp;&emsp;&emsp;# main and only ui file<br />
└── ...<br /> 
<br /> 
# Structure
Upon `poetry run invoke start`, `main.py` is called. `main.py` starts the UI, which contains references to algorith_service. Initially no algorithm is run, and the user needs to choose their own start/goal coordinates, map and JPS or Dijkstra or choose a default run of either of the two. I created the default option to simplify testing the program, but it's probably easiest to test the functioning of the program with these default options.<br />
<br /> `algorithm_service.py` handles things like converting the string input of the user and the proper conversion of the map as well as directly calling the algorithms with appropriate algorithms. Because there is a lot of buttons in the UI it might seem like `algorithm_service.py` is pretty short, and in fact I would like to see feedback on how to improve it. (The UI could probably use some refactoring as well). <br />
`algorithm_service.py` calls the appropriate algorithm with user-chosen start/goal coordinates and map. Both algorithms are first fed the map, and only then called with `find_shortest_path`. It allows the user to choose different coordinates and run them on the same map.<br />

# Achieved time and space requirements (e.g. O-analyses of pseudocode)
In week 5 I finally got around to measuring the execution time of the algorithms and I found a challenge.<br/> 
*Time complexity formula* for Dijkstra is O(V+E*log V) where *E* is number of edges and *v* is number of nodes.<br/>
This means that execution time of Dijkstra depends both on the number of nodes and the number of edges. <br/>
What I could do is create separate graphs that aren't grids and have a specific number of edges and vertices. I haven't gotten around to doing that since the implementation of **Dijkstra** and **JPS** that I created uses maps in the format *.map* that you can see in the [dedicated folder](https://github.com/jakubgrad/Aineopintojen-harjoitusty-Algoritmit-ja-teko-ly-/tree/main/maps).<br/>
Instead what I did so far was measure Dijkstra on maps of different sizes and use the *time complexity formula* O(V+E*log V) to *predict* how long it should take to run Dijkstra on a given map. This gives me pairs of *achieved time* and *predicted time*, e.g. for `arena.map` time found is 1.16 seconds and time predicted is 3829 (without any units). This alone doesn't tell us anything, but having a few tuples of data like that I was able to create this graph:
![image](/documentation/pictures/Figure_achieved_vs_predicted_for_dijkstra.png)
The orange line shows the time it would take if my implementation had *exactly* the time complexity of O(V+E*log V), and the blue line the actual achieved time.
So we can see that the algorithm performs within the time complexity for smaller maps, and 
dijkstra on brc.map:
10, 10, 100, 100
Distance is 186.57
Execution time is 0.06116676330566406

JPS:
worst case being [O(b^d), where b is the branching factor (the average number of successors per state)

# Notes
-**"Achieved time and space requirements (e.g. O-analyses of pseudocode)". In the works!**<br />
-**"Performance and O analysis comparison (if suitable for the topic of the work)". Same!**<br />
-would be nice to you notation e.g. read_map(map_name: str) -> list: to make clearer what inputs and outputs are for a given function
- After loading a file to the user interface, it shows up in the naked form of a *.map file, and worse even, it is not rotated correctly. It can be very confusing to the user, and because there is no error log for choosing coordinates out of the map, it might seem like the UI doesn't work!
- I realized that in a uniform graph such as one constructed from a grid, Dijkstra works essentially like a Breadth-First Search. I could have implemented it as such but I already coded Dijkstra.
- It would be nice to create a datastructure for JPS that encapsulated the neighbour nodes. 
- It would be a good place to introduce the a-c 1-3 notation
- The input maps are assumed to be rectangular
- I want to add colors to the visualization. It used to exist in command line, but Tkinter doesn't support the methods I've been using
- There used to be a color map for JPS, but I removed it bc Tkinter doesn't support fonts?
- Arrows are not marked as free. It's nice that algorithm won't run into the same area again, but it also means it will hallucinate forced neighbours (and it does)
- Need to run more different types of tests for Dijkstra
- Need to run tests for efficiency / results of the algorithms
- Add_neighbours_of_start_coordinates_to_open_set could use the function produce_neighbours
- Need to move print_for_cli away from JPS
- Add debug mode?
- Add different types of tests
- The maps are flipped vertically and horizontally so that coordinates feel natural (i.e. they resemble cartesian coordinate system in the 1st quarter)


# Targeted time and space requirements (e.g. O-analyses)
   - [x] **JPS**:<br />
     - Time complexity: I found it hard to find time and space complexities for **JPS**. At the very least, it’s expected to work faster than A*, and A*’s time complexity of A* depends on the heuristic, in the worst case being [“O(b^d), where b is the branching factor (the average number of successors per state)”](https://en.wikipedia.org/wiki/A*_search_algorithm), and d the distance from start point to destination point. **I need to conduct time complexity testing myself still**<br />
     - Space complexity: [O(b^d)](https://en.wikipedia.org/wiki/A*_search_algorithm)
   - [x] **Djikstra**:<br />
     - Time complexity of [O(V+E*log V)](https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/tutorial/#:~:text=Time%20Complexity%20of%20Dijkstra's%20Algorithm,E%20l%20o%20g%20V%20) when implemented with min-priority queue
     - Space complexity of [O(V)](https://www.geeksforgeeks.org/time-and-space-complexity-of-dijkstras-algorithm/)

# Use of large language models 
The only LLM I've used was Chatgpt 3.5. I used it a lot to interpret the bugs in the console, e.g. "cannot import module". It was especially useful when dealing with GUI, because I have close to zero experience on it and the error messages just don't tell me anything understandable. This way it was so much faster to debug, because often it's just something that I didn't notice and ChatGPT almost always picks it up. I also found ChatGPT great for suggesting different programming tricks, like e.g. the ANSI color codes and reminding how lambda, list comprehension etc. work. In other cases it was utterly useless, maybe because it cannot even conceptualize folder structure or how my algorithm would actually be used (it's not started by just calling the class for instance.). Also, with larger and multiple files, ChatGPT was too confused about what's what and couldn't help at all. With well formulated questions there is significant benefit. E.g., it's suggested me to use exceptions when I asked what can end a deep recursion. 

# References
**JPS** http://users.cecs.anu.edu.au/~dharabor/data/papers/harabor-grastien-aaai11.pdf <br />
Space and time complexity of **JPS** https://en.wikipedia.org/wiki/A*_search_algorithm <br />
Time complexity of **Djikstra** https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/tutorial/#:~:text=Time%20Complexity%20of%20Dijkstra's%20Algorithm,E%20l%20o%20g%20V%20 <br />
Space complexity of **Djikstra** https://en.wikipedia.org/wiki/A*_search_algorithm <br />
<br />
Recommend for understanding JPS:
- [Visual explanation of JPS](https://zerowidth.com/2013/a-visual-explanation-of-jump-point-search/)
- [Jump Point Search: Fast A* Pathfinding for Uniform Cost Grids](https://www.gamedev.net/tutorials/programming/artificial-intelligence/jump-point-search-fast-a-pathfinding-for-uniform-cost-grids-r4220/)



