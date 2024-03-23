## Implementation document = Toteutusdokumentti<br />

The program is written in `Python`. It has the following structure at the moment:<br />
<br /> 
├── documentation           # documentation files <br />
├── maps                    # maps used to test the tool <br />
├── src                     # code files <br />
│   ├── __pychache_     
│   ├── tests               # test files <br />
│   ├── create_array.py     # turns a map into an array of rows <br />
│   ├── dijkstra.py         # turns an array of rows into a graph<br /> 
│   │                       # and executes dijkstrak<br /> 
│   └── main.py             # allows running the tool as a user<br /> 
└── ...<br /> 
<br /> 


# Targeted time and space requirements (e.g. O-analyses)**
   - [x] **JPS**:<br />
     - Time complexity: I found it hard to find time and space complexities for **JPS**. At the very least, it’s expected to work faster than A*, and A*’s time complexity of A* depends on the heuristic, in the worst case being [“O(b^d), where b is the branching factor (the average number of successors per state)”](https://en.wikipedia.org/wiki/A*_search_algorithm), and d the distance from start point to destination point. <br />
     - Space complexity: [O(b^d)](https://en.wikipedia.org/wiki/A*_search_algorithm)
   - [x] **Djikstra**:<br />
     - Time complexity of [O(V+E*log V)](https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/tutorial/#:~:text=Time%20Complexity%20of%20Dijkstra's%20Algorithm,E%20l%20o%20g%20V%20) when implemented with min-priority queue
     - Space complexity of [O(V)](https://www.geeksforgeeks.org/time-and-space-complexity-of-dijkstras-algorithm/)

# References
**JPS** http://users.cecs.anu.edu.au/~dharabor/data/papers/harabor-grastien-aaai11.pdf <br />
Space and time complexity of **JPS** https://en.wikipedia.org/wiki/A*_search_algorithm <br />
Time complexity of **Djikstra** https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/tutorial/#:~:text=Time%20Complexity%20of%20Dijkstra's%20Algorithm,E%20l%20o%20g%20V%20 <br />
Space complexity of **Djikstra** https://en.wikipedia.org/wiki/A*_search_algorithm <br />

