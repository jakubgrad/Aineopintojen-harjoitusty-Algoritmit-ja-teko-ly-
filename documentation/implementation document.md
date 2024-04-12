## Implementation document = Toteutusdokumentti<br />

The program is written in `Python`. It has the following structure at the moment:<br />
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

# Notes
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


# Targeted time and space requirements (e.g. O-analyses)
   - [x] **JPS**:<br />
     - Time complexity: I found it hard to find time and space complexities for **JPS**. At the very least, it’s expected to work faster than A*, and A*’s time complexity of A* depends on the heuristic, in the worst case being [“O(b^d), where b is the branching factor (the average number of successors per state)”](https://en.wikipedia.org/wiki/A*_search_algorithm), and d the distance from start point to destination point. <br />
     - Space complexity: [O(b^d)](https://en.wikipedia.org/wiki/A*_search_algorithm)
   - [x] **Djikstra**:<br />
     - Time complexity of [O(V+E*log V)](https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/tutorial/#:~:text=Time%20Complexity%20of%20Dijkstra's%20Algorithm,E%20l%20o%20g%20V%20) when implemented with min-priority queue
     - Space complexity of [O(V)](https://www.geeksforgeeks.org/time-and-space-complexity-of-dijkstras-algorithm/)

# Use of large language models 
The only LLM I've used was Chatgpt 3.5. I used it a lot to interpret the bugs in the console, e.g. "cannot import module". It was especially useful when dealing with GUI, because I have close to zero experience on it and the error messages just don't tell me anything understandable. This way it was so much faster to debug, because often it's just something that I didn't notice and ChatGPT almost always picks it up. I also found ChatGPT great for suggesting different programming tricks, like e.g. the ANSI color codes and reminding how lambda, list comprehension etc. work. In other cases it was utterly useless, maybe because it cannot even conceptualize folder structure or how my algorithm would actually be used (it's not started by just calling the class for instance.). Also, with larger and multiple files, ChatGPT was too confused about what's what and couldn't help at all.

# References
**JPS** http://users.cecs.anu.edu.au/~dharabor/data/papers/harabor-grastien-aaai11.pdf <br />
Space and time complexity of **JPS** https://en.wikipedia.org/wiki/A*_search_algorithm <br />
Time complexity of **Djikstra** https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/tutorial/#:~:text=Time%20Complexity%20of%20Dijkstra's%20Algorithm,E%20l%20o%20g%20V%20 <br />
Space complexity of **Djikstra** https://en.wikipedia.org/wiki/A*_search_algorithm <br />



