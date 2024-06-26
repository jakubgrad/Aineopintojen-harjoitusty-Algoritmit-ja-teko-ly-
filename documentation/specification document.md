## Specification document = Määrittelydokumentti<br />

I chose my programming language to be `Python`, because I have the most familiarity with it. Other languages I know reasonably well are `Javascript` and `React`, which are naturally not suitable for algorithm oriented applications. I occasionally learn `bash` and `C` though, so I can to a certain extent preview that sort of code, but I would prefer to peer review `Python` only.<br />

I choose my topic to be **route finding algorithms**, specifically **JPS**, i.e. [Jump Point Search vs Dijkstra](http://users.cecs.anu.edu.au/~dharabor/data/papers/harabor-grastien-aaai11.pdf), because I liked the paper on **JPS** and it seemed interesting to me that a new algorithm can be as much as an order of magnitude faster than it’s predecessor.  <br /><br />I like to relate what I learn to *real life* and because of that, I looked into where a grid like environment that **JPS** presupposes actually exists. I found that it can be used in video games (fair point), I imagine I could use digital maps to test out both of the algorithms. There is already a few suggestions in the [course page’s ideas section](https://moodle.helsinki.fi/mod/page/view.php?id=3527719), so I might just use those. <br /><br />
I belong to the Bachelor’s Programme in Science. I’ll document my work in English as I’m more proficient in it than in Finnish. <br /><br />
To answer the required questions:<br /><br />
1. What algorithms and data structures do you implement in your work?<br />
   - [x] I’m going to use **Jump Point Search** and **Djikstra** algorithms. Jump Point Search requires no memory overhead, and so no specific data structure apart from the returned path is needed to implement it to my understanding [Harabar et al., 2011, p. 1](http://users.cecs.anu.edu.au/~dharabor/data/papers/harabor-grastien-aaai11.pdf). Dijkstra's algorithm requires a priority queue data structure, which in the *final* version I hope to implement using `PriorityQueue` from Python’s `queue` library. <br />
2. What problem are you solving?
   - [x] 1. Finding whether **JPS** or **Djikstra** is better at finding optimal paths in a short time in a grid-like environment, 2. Whether this is always so or if there is cases in which the less optimal algorithm outperforms anyway (a mathematical proof would be required for that, so instead I’ll test various scenarios), 3. *Optionally* find which algorithm performs better at finding shortest paths in a hexagonal network mapped onto a globe.<br />
3. What inputs does the program receive and how are they used?<br />
   - [x] The program receives a **bitmap** *or a text file for the time being* showing which squares are traversable and which aren’t together with the size of the **bitmap** (e.g. 5x7, 50x50 or 25x100)
4. Targeted time and space requirements (e.g. O-analyses)
   - [x] **JPS**:<br />
     - Time complexity: I found it hard to find time and space complexities for **JPS**. At the very least, it’s expected to work faster than A*, and A*’s time complexity of A* depends on the heuristic, in the worst case being [“O(b^d), where b is the branching factor (the average number of successors per state)”](https://en.wikipedia.org/wiki/A*_search_algorithm), and d the distance from start point to destination point. <br />
     - Space complexity: [O(b^d)](https://en.wikipedia.org/wiki/A*_search_algorithm)
   - [x] **Djikstra**:<br />
     - In general, the time complexity of Dijkstra is [O(V+E*log V)](https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/tutorial/#:~:text=Time%20Complexity%20of%20Dijkstra's%20Algorithm,E%20l%20o%20g%20V%20) when implemented with min-priority queue. However, in a uniform (unweighted) grid-like environment Dijkstra acts more than less like Breadth-First Search and we can make the assumption that once the goal coordinates are reached, they were found with the shortest possible path. Thanks to [Wincewind](https://github.com/jakubgrad/Aineopintojen-harjoitusty-Algoritmit-ja-teko-ly-/issues/2) for pointing out that the search can stop there. Hence, the execution time is almost certainly smaller than O(V+E*log V) and actually depends on the distance to the goal coordinates, similarly to **JPS**. For **Dijkstra**, I would actually distinguish between:
       - **Worst-case time complexity** of [O(V + E)](https://techsauce.medium.com/time-complexity-and-space-complexity-of-dfs-and-bfs-algorithms-671217e43d58#), which arises when there is no path to the goal coordinates and the algorithm needs to visit all (or almost all) of the edges and vertices. However, this could be brought
       - **Average time complexity** of O(d²), where d is the distance between start and goal coordinates.I would argue this is the case for a map with few obstacle (which means that the search is expanding upwards, downwards, rightwards and leftwards). On such a map, the searched area grows in four directions and could be roughly approximated as a square. I got the insight from [geeks2geeks on BFS traversal on a 2d grid](https://www.geeksforgeeks.org/breadth-first-traversal-bfs-on-a-2d-array/) 
     - Space complexity of usual Dijkstra implementaiton is [O(V)](https://www.geeksforgeeks.org/time-and-space-complexity-of-dijkstras-algorithm/). Although perhaps this could be improved for my implementation to O(d²) since not all vertices need to be in memory to find the shortest path in a grid, the current implementation doesn't take advantage of that fact and intializes arrays for the entire size of the map.
        
## Achieved time complexity
View in the [implementation document](https://github.com/jakubgrad/Aineopintojen-harjoitusty-Algoritmit-ja-teko-ly-/blob/main/documentation/implementation%20document.md#achieved-time-and-space-requirements-eg-o-analyses-of-pseudocode)

## References
**JPS** http://users.cecs.anu.edu.au/~dharabor/data/papers/harabor-grastien-aaai11.pdf <br />
Space and time complexity of **JPS** https://en.wikipedia.org/wiki/A*_search_algorithm <br />
Time complexity of **Djikstra** https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/tutorial/#:~:text=Time%20Complexity%20of%20Dijkstra's%20Algorithm,E%20l%20o%20g%20V%20 <br />
Space complexity of **Djikstra** https://en.wikipedia.org/wiki/A*_search_algorithm <br />

