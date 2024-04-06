# JPS vs Dijkstra
A repository for the course Aineopintojen harjoitustyö: Algoritmit ja tekoäly (period 4) Laboratoriotyöskentely<br /><br />

Currently the tool is still under production 🛠. The goal is to have a tool that can show to the user the functioning of the algorithms and that can compare the two algorithms in terms of time complexity. For details, make sure to look into the [specification document](https://github.com/jakubgrad/Aineopintojen-harjoitusty-Algoritmit-ja-teko-ly-/blob/main/documentation/specification%20document.md) 📎<br /><br />
To understand `JPS` better I recommend reading [this article](https://zerowidth.com/2013/a-visual-explanation-of-jump-point-search/) and [this blogpost](https://www.gamedev.net/tutorials/programming/artificial-intelligence/jump-point-search-fast-a-pathfinding-for-uniform-cost-grids-r4220/)
To test out the app simply download the repository, then <br />
```
cd Aineopintojen-harjoitusty-Algoritmit-ja-teko-ly-/ 
poetry shell 
```
After doing that, you have plenty of choices for testing out the application. Currently there is both a graphical interface tool and a command line tool.
To use the graphical tool, run in the topmost directory of the project:
```
poetry run invoke start
```
A window like the one below should open <br/>![image](https://github.com/jakubgrad/Aineopintojen-harjoitusty-Algoritmit-ja-teko-ly-/assets/113715885/cd760ad4-5d2c-400e-b259-cc8831fb1d97)
Now that the tool is open you can test it. If you run the command in the topmost directory, when you click on "Choose map" a few options should appear. I would recommend first testing JPS. For that, the best choice would be to pick `wall.map`, start coordinates 0,0 and goal coordinates 4,7. After you clikc on `Run JPS` you should see a short visualization of the algorithm.
If you want to see Dijkstra, there's unfortunately no visualization for that yet, and running the algorithm on any chosen map will only produce the length of the shortest path found using Dijkstra algorithm. You can see it if you choose e.g. the `arena.map`, start coordinates 4,3 and goal coordinates 5,11.
<br/>
The command line too also exists because I started working on the algorithms using command line simulations. To test them out, you can e.g. run:
```
poetry run invoke jps
```
which is a shortcut for `python3 cli.py --jps --map wall.map 0 0 4 7`.
You should get 7.41, which is the shortest path when assuming $\sqrt{2}$ = 1.41 between the default start square 200 and end square 256, rounded to two digits. Under the hood, main.py has called create_array to turn an example map maps/arena.map into an array, and then called dijkstra.py which in turn created a graph based on the array. Finally, the shortest path on the map is printed using dijkstra's algorith, *voilà*!<br /><br />
To explore the functions of the tool deeper, make sure to also run
```
python3 main.py --help
```

run poetry run invoke start in topmost directory, otherwise the suggested map directory won't be there
