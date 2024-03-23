# Testing document = Testatusdokumentti

1. Unit testing coverage report.<br />
   - [x] [Here!](http://jakubgrad.ddns.net:2231/HTML%20coverage/) <br />
2. What has been tested, how was this done?<br />
   - [x] The algorithm dijkstra and create_array were tested, create_array somewhat indirectly. 
<br />
3. What kind of inputs was the testing done with?
<br />
   - [x] In `test_dijkstra_works_for_small_graphs_out_of_maps` I tested Dijkstra by creating a graph through add_edge directly and testing the shortest paths without the use of a map file. In `test_dijkstra_finds_distances_on_arena_map` I tested Dijkstra using an actual map with free spaces and obstacles. This also tests the script create_array.py, which turns the map file into an array of rows e.g. `[[.....T....TTT..], [..T.. ...` where `T` is an obstacle, `.` a free space. <br />
4. How can the tests be repeated?
<br />
   - [x] Go to the root directory, and execute:
<br />
`coverage run --branch -m pytest src && coverage report -m`
<br /><br />
5. Presentation of the results of possible empirical testing of the program's operation in graphic form. (If it fits the topic)
<br />
   - [ ] Coming out next week
<br />





