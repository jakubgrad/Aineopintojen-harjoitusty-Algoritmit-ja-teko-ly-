# Testing document = Testatusdokumentti

1. Unit testing coverage report.<br />
   - [x] [Week 4](http://jakubgrad.ddns.net:2231/htmlcov4/), also [Week 3](http://jakubgrad.ddns.net:2231/htmlcov/), [Week 2](http://jakubgrad.ddns.net:2231/HTML%20coverage/)<br />
   - [x] [Week 4](http://http://87.92.126.250:2231/htmlcov4/), also [Week 3](http://http://87.92.126.250:2231/htmlcov/), [Week 2](http://http://87.92.126.250:2231/HTML%20coverage/)<br />
2. What has been tested, how was this done?<br />
   - [x] There is a lot of tests for **JPS** and much less for **Dijkstra**. For **JPS**: <br />
     - I created a few maps like `t1.map`, `t2.map` to test different situations. Specifically, I want to see if **JPS** notices *forced neighbours* and adds them to the open set for further expansion. At the end of week 4 it seems that it can find all *forced neighbours* and hence all the *jumpoints*. The tests also include neat commented out pictures of the map with marked start and goal coordinates and the desired *forced neighbour*, which makes it super easy to understand the purpose of each of this type of tests.<br />
     - The tests find if correct nodes are added initially to the open set <br />
     - The tests find if producing neighbours works in all orientations. I don't know how other implementations of **JPS** handle this, but I decided to include just two scanning functions: diagonal and straight, that are in a way oblivious to the direction of the scan. Thanks to that, for instance, the code doesn't know if it's moving up or left, or if it's goin right-up or left-down.<br />
     - There is a lot of small unit tests testing the functionality of simple elemenets of the core solution, e.g. tests for adding and subtracting tuples, finding distance between a pair of coordinates etc. <br />
   - [ ] There is no time, space, or correctness tests. All correctness tests were visual testing of the algorithms in UI, and anything more complicated would require some precalculated values and bigger maps.<br />
3. What kind of inputs was the testing done with? <br />
   - [x] I tested **Dijkstra** with the use of a map file `arena.map`. **JPS** was tested more comprehensively with 4 or 5 different maps and slightly different start and goal coordinates. *It would be a good idea to make very hard tests now to see if the inputs so far were too easy to spot mistakes*.  <br />
   - Most of the tests were designed to test **JPS** since I found it much more complicated to work out. Also, visually confirming that **JPS** works is much harder, since it requires recreating a path in the visualization. The **Dijkstra** code that I've written simply marks some nodes as visited until all of the available ones are. As unit testing goes, the inputs target mostly specific parts of the code, so there is no such thing as a performance or correctness tests yet. The tests include checking if:
     - The node class works correctly, e.g. nodes are possible to compare and and arrange in a min heap.
     - The algorithm doesn't proceed if start coordinates and goal coordinates are the same
     - The algorithm doesn't proceed if start coordinates or goal coordinates are outside of the map
     - **JPS** can check and add to open set if possible the the neighbouring squares of the start coordinates
     - **JPS** notices *forced neighbours* during straight and diagonal scans and adds them to the open list
     - **JPS** doesn't go in circles, at least not very big ones (there is a closed set which the JPS check before adding a new jump point)
     - During a scan, **JPS** correctly assigns coordinates to the squares around it, regardles of the direction of the scan
     - **JPS** correctly assigns coordinates to the squares around it, regardles of the direction of the scan
     - **JPS** correctly recognizes *jumppoints*
- [ ] The inputs weren't very representative and overall they are very small
4. How can the tests be repeated?<br />
   - [x] Go to the root directory, and execute: `poetry run invoke coverage-report`. The results should appear in the browser. If you get an error similar to this one:
```
[13289:13289:0403/183659.749216:ERROR:process_singleton_posix.cc(353)] The profile appears to be in use by
 another Google Chrome process (44970) on another computer (vdi-cubic-025.ad.helsinki.fi).
Chrome has locked the profile so that it doesn't get corrupted.
If you are sure no other processes are using this profile,
you can unlock the profile and relaunch Chrome.
```
You can run  `rm -rf ~/.config/google-chrome/Singleton*` and then try to generate the report again. <br />
   
   - I would like to expand the tests to include randomized data sets or different maps, but first I need to implemenet a visualization for **Dijkstra** and make the GUI more user-friendly.
   - [x] Go to the root directory, and execute: `poetry run invoke coverage-report`<br />
5. Presentation of the results of possible empirical testing of the program's operation in graphic form. (If it fits the topic)<br /><br />
# Default JPS visualization
![Default JPS](/documentation/pictures/default_jps.png)
<br/>`S` shows the starting place, `G` the goal. `¤` denotes the path taken by the algorithm in execution. Log puts the distance taken at 7.82.
# Default Dijkstra visualization
![Default Dijkstra](/documentation/pictures/default_dijkstra.png)
<br/>The starting place can be seen by going to slide 0 or clicking on "Animate from start!". Algorithm found the distance to be 4.23, shown is the 1000th slide. <br/>
   - [X] Looking at the graphical interface and the command line simulation of the **JPS**, I can see that it covers the whole map, doesn't get stuck and finds the goal node when possible. I haven't tested yet if the algorithm will cease to execute because it found a suboptimal route yet, although if I remember correctly, according to the paper on **JPS** that isn't probable. <br />
   - I would like to expand the tests to include randomized data sets or different maps, but first I need to implemenet a better visualization for Dijkstra and include a better choice for maps.





