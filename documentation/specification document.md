## Specification document = Määrittelydokumentti<br />

I chose my programming language to be `Python`, because I have the most familiarity with it. Other languages I know reasonably well are `Javascript` and `React`, which are naturally not suitable for algorithm oriented applications. I occasionally learn `bash` and `C` though, so I can to a certain extent preview that sort of code, but I would prefer to peer review `Python` only.<br />

I choose my topic to be **route finding algorithms**, specifically **JPS**, i.e. [Jump Point Search vs Dijkstra](http://users.cecs.anu.edu.au/~dharabor/data/papers/harabor-grastien-aaai11.pdf), because I liked the paper on **JPS** and it seemed interesting to me that a new algorithm can be as much as an order of magnitude faster than it’s predecessor.  <br /><br />I like to relate what I learn to *real life* and because of that, I looked into where a grid like environment that **JPS** presupposes actually exists. I found that it can be used in video games (fair point), I imagine I could use digital maps to test out both of the algorithms. There is already a few suggestions in the [course page’s ideas section](https://moodle.helsinki.fi/mod/page/view.php?id=3527719), so I might just use those. <br /><br />
Video games are not *real real* life though, and I think it's possible to use the algorithm for a practical purpose in the physical world, for instant finding routes fo water transportation, since ocean and sea patches can be modelled as traversables vertices and land as intraversable vertices. Using the algorithms for finding a path on a map of Earth seems pretty straightforward, and I'll try to find **bitmaps** resembling Earth. Naturally, the accuracy would suffer since it's not possible to accurately represent Earth using squares. For an expansion idea, I think I could represent a globe using hexagons rather than squares, and to that extent I looked into representing the globe as hexagons and adjusting **JPS** and **Djikstra** to use hexagons to find the shortest route. It’s a pretty big addition that would also require a graphical view of the globe and the routes, so I’m thinking of it as being *optional* right now.<br /><br />
I belong to the Bachelor’s Programme in Science. I’ll document my work in English as I’m more proficient in it than in Finnish. <br /><br />
To answer the required questions:<br /><br />
1. What algorithms and data structures do you implement in your work?<br />
   - [x] I’m going to use **Jump Point Search** and **Djikstra** algorithms. Jump Point Search requires no memory overhead, and so no specific data structure apart from the returned path is needed to implement it to my understanding [Harabar et al., 2011, p. 1](http://users.cecs.anu.edu.au/~dharabor/data/papers/harabor-grastien-aaai11.pdf). Dijkstra's algorithm requires a priority queue data structure, which I hope to implement using `PriorityQueue` from Python’s `queue` library. <br />
2. What problem are you solving?
   - [x] 1. Finding whether **JPS** or **Djikstra** is better at finding optimal paths in a short time in a grid-like environment, 2. Whether this is always so or if there is cases in which the less optimal algorithm outperforms anyway (a mathematical proof would be required for that, so instead I’ll test various scenarios), 3. *Optionally* find which algorithm performs better at finding shortest paths in a hexagonal network mapped onto a globe.<br />
3. What inputs does the program receive and how are they used?<br />
   - [x] The program receives a **bitmap** showing which squares are traversable and which aren’t together with the size of the **bitmap** (e.g. 50x50 or 25x100)
4. Targeted time and space requirements (e.g. O-analyses)
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

