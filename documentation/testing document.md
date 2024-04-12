# Testing document = Testatusdokumentti

1. Unit testing coverage report.<br />
   - [x] [Here!](http://jakubgrad.ddns.net:2231/htmlcov/) . Also [the old coverage report](http://jakubgrad.ddns.net:2231/HTML%20coverage/)<br />
2. What has been tested, how was this done?<br />
   - [x] First Dijkstra, JPS and create_array were tested. `Test_map_color.py` was also somehow tested, although it's mostly a file for me to learn how colours in the command line work. `cli.py` was not tested because it's not supposed to be the final product, but only a helpful tool for development. <br />
3. What kind of inputs was the testing done with? <br />
   - [x] In `test_dijkstra_works_for_small_graphs_out_of_maps` I tested Dijkstra by creating a graph through add_edge directly and testing the shortest paths without the use of a map file. In `test_dijkstra_finds_distances_on_arena_map` I tested Dijkstra using an actual map with free spaces and obstacles. This also tests the script create_array.py, which turns the map file into an array of rows e.g. `[[.....T....TTT..], [..T.. ...` where `T` is an obstacle, `.` a free space. <br />
   - Most of the tests were designed to test JPS since I found it much more complicated to work out. As unit testing goes, the inputs target mostly specific parts of the code, so there is no such thing as a performance or correctness tests yet. The tests include checking if:
     - The node class works correctly, e.g. nodes are possible to compare and and arrange in a min heap.
     - The algorithm doesn't proceed if start coordinates and goal coordinates are the same
     - The algorithm doesn't proceed if start coordinates or goal coordinates are outside of the map
     - JPS can check and add to open set if possible the the neighbouring squares of the start coordinates
     - JPS notices forced neighbours during straight scan and adds them to the open list
     - JPS doesn't go in circles (there is a closed set which the JPS check before adding a new jump point)
     - During a scan, JPS correctly assigns coordinates to the squares around it, regardles of the direction of the scan
     - 
   - 
4. How can the tests be repeated?<br />
   - [x] Go to the root directory, and execute: `poetry run invoke coverage-report`<br />
5. Presentation of the results of possible empirical testing of the program's operation in graphic form. (If it fits the topic)<br />
![Default JPS](/documentation/pictures/default_jps.png)
![Default Dijkstra](/documentation/pictures/default_dijkstra.png)
   - [X] Looking at the graphical interface and the command line simulation of the algorithm, I can see that it covers the whole map, doesn't get stuck and finds the goal node when possible. I haven't tested yet if the algorithm will cease to execute because it found a suboptimal route yet, although if I remember correctly, according to the paper on JPS that isn't probable. <br />
   - I would like to expand the tests to include randomized data sets or different maps, but first I need to implemenet a visualization for Dijkstra and make the GUI more user-friendly.





