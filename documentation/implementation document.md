## Implementation document = Toteutusdokumentti<br />

# Structure

├── maps                    &emsp;&emsp;&emsp; maps used to test the tool <br />
├── src                     &emsp;&emsp;&emsp; code files <br />
│   ├── tests               &emsp;&emsp;&emsp;test files <br />
│   ├── create_map.py       &emsp;&emsp;&emsp; turns a map into an array of rows <br />
│   ├── dijkstra.py         &emsp;&emsp;&emsp; implementation of Dijkstra<br /> 
│   ├── jps.py              &emsp;&emsp;&emsp; implementation of JPS<br /> 
│   ├── config.py           &emsp;&emsp;&emsp; provides useful variables like<br /> 
│   │                       &emsp;&emsp;&emsp; path to root directory<br /> 
│   ├── main.py             &emsp;&emsp;&emsp; allows running the tool as a user<br />
│   └── services            &emsp;&emsp;&emsp;  
│       └── algorithm_service.py &emsp;&emsp;&emsp; responsible <br />
│                           &emsp;&emsp;&emsp; for interaction between UI and algorithms <br />
├── ui                      &emsp;&emsp;&emsp; ui files <br />
│   └── ui.py               &emsp;&emsp;&emsp; main and only ui file<br />
└── ...<br /> 

<br> <br> 
The program is written in `Python`. Upon `poetry run invoke start`, `main.py` is called. `main.py` starts the UI, which contains references to algorith_service. Initially no algorithm is run, and the user needs to choose their own start/goal coordinates, map and JPS or Dijkstra or choose a default run of either of the two. I created the default option to simplify testing the program, but it's probably easiest to test the functioning of the program with these default options.<br />
# Important functions
<br /> `algorithm_service.py` handles things like converting the string input of the user and the proper conversion of the map as well as directly calling the algorithms with appropriate algorithms. Because there is a lot of buttons in the UI it might seem like `algorithm_service.py` is pretty short, and in fact I would like to see feedback on how to improve it. (The UI could probably use some refactoring as well). <br />
`algorithm_service.py` calls the appropriate algorithm with user-chosen start/goal coordinates and map. Both algorithms are first fed the map, and only then called with `find_shortest_path`. It allows the user to choose different coordinates and run them on the same map.<br />

# Achieved time and space requirements (e.g. O-analyses of pseudocode)
I did the following tests following the [instructions in the manual](https://github.com/jakubgrad/Aineopintojen-harjoitusty-Algoritmit-ja-teko-ly-/blob/main/documentation/manual.md#time-testing):<br>

`arena.map` 49x49 <br>
Distance is 56.7 from (2,2) to (33,46) <br>
JPS executes in `0.00684 s` <br>
Dijkstra executes in `0.0636 s` <br><br>

`smaller_brc.map` 130x54 <br>
Distance is 116 from (9,12) to (9,128) <br>
Dijkstra executes in `0.551 s`<br>
JPS executes in `0.00193 s`, since the first scan goes straight from start coordinates to goal coordinates. Over 200 times faster than Dijkstra for these settings.<br><br>

`smaller_brc.map` 130x54<br>
Distance is 133 from (1,11) to (40,128)<br>
Dijkstra executes in `0.540 s`<br>
JPS executes in `0.0695 s`, still tenfold faster than Dijkstra<br><br>

`medium_brc.map` 182x124<br>
Distance is 184.8 from (10,10) to (100,100)<br>
JPS executes in `1.76811 s`<br>
Dijkstra executes in `6.734957218170166 s`, very likely due to the fact that my implementation initializes an array for all squares on the map. <br><br>
Based on these it seems that the time complexities in the [specification document](https://github.com/jakubgrad/Aineopintojen-harjoitusty-Algoritmit-ja-teko-ly-/blob/main/documentation/specification%20document.md) match the tests and the algorithms behave predictably.


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



