# Weekly Report 6 
1. What have I been up to this week? <br />
   - [x] Most of the week I was writing reviews for this and actually other courses too. I like writing reviews so I took my time to familiarize myself with other repositories and write pretty long responses. In terms of my repository, I read the review from another student and course instructor on Labtool and tried to improve my code based on the feedback. I was glad to find that the performance tests that I need to do are quite minor. I'm glad the instructor pointed out that the time complexity in my specification document is inaccurate, since in a uniform grid-like environment a Dijkstra search should end once a goal node has been found. My time complexity was in contrast a time complexity of finding the path to all nodes in a graph, which is greater than or equal to that time.
   - [x] I read the peer review of another student on my repository and it was super useful. I haven't grasped JPS fully but Wincewind has read my code very closely and pointed out very important things. Namely, that Dijkstra didn't actually stop once it found the goal node, that the priority queue for JPS was not like it was supposed to be (the heuristic should be A*-like). They also pointed out that if the heuristic is like in A* search, once the goal node is found the search is complete. After implemented Wincewind's suggestions my code got about a 100x times faster :))
   - I linted some of the code, I'm planninng to continue polishing the code next week too
   - I found that while optimizing my code many functions like e.g. turn_45_degrees became obsolete. In total there were perhaps 40-50 lines of obsolete code that I found and deleted.
   - I deleted printouts and comments that I didn't find useful
   - I wrote some docstrings
2. How has the program progressed? <br />
   - JPS is finally faster than Dijkstra and possible to run on bigger maps
   - I have more confidence that my program implemented JPS correctly
   - The code is cleaner and easier to understand
   - JPS returns -1 when path cannot be found
3. What did I learn this week / today? <br />
   - By reviewing levitesuo's repository I found an interesting way of visualizing the algorithms. Actually, I found both of the repositories that I reviewed quite interesting in that respect. 
   - I understood JPS and Dijkstra a bit better
4. What was unclear or caused difficulties? Answer this section honestly, as you will receive help based on this section if needed.  <br />
   - I was a bit lost on how I improve JPS so that it's closer to the description in the paper, since I wasn't so sure about JPS itself. Fortunately the code review helped me write the most important changes 
5. What do I do next? <br />
   - Test time complexity a bit more, lint, improve coverage of the tests
**Other considerations:** <br />
I spent around **10** hours this week working on the project **5** of it was spent on giving reviews<br />
 
