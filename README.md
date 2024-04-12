# JPS vs Dijkstra
A repository for the course Aineopintojen harjoitustyö: Algoritmit ja tekoäly (period 4) Laboratoriotyöskentely<br /><br />

Currently the tool is still under production 🛠. The goal is to have a tool that can show to the user the functioning of the algorithms and that can compare the two algorithms in terms of time complexity. For details, make sure to look into the [specification document](https://github.com/jakubgrad/Aineopintojen-harjoitusty-Algoritmit-ja-teko-ly-/blob/main/documentation/specification%20document.md) 📎<br /><br />
To understand `JPS` better I recommend reading [this article](https://zerowidth.com/2013/a-visual-explanation-of-jump-point-search/) and [this blogpost](https://www.gamedev.net/tutorials/programming/artificial-intelligence/jump-point-search-fast-a-pathfinding-for-uniform-cost-grids-r4220/)
To test out the app simply download the repository, then <br />
```
cd Aineopintojen-harjoitusty-Algoritmit-ja-teko-ly-/ 
poetry shell
poetry install
poetry run invoke start
```
You can also look into the [manual](/documentation/manual.md) for tips.<br />
Doing that should open a GUI tool with a welcoming interface. <br />

A window like the one below should open <br/>![image](/documentation/pictures/program.png)
Now that the tool is open you can test it. If you run the command in the topmost directory, when you click on "Choose map" a few options should appear. I would recommend first testing JPS. For that, the best choice would be to pick `wall.map`, start coordinates 0,0 and goal coordinates 4,7. After you clikc on `Run JPS` you should see a short visualization of the algorithm.
If you want to see Dijkstra, there's unfortunately no visualization for that yet, and running the algorithm on any chosen map will only produce the length of the shortest path found using Dijkstra algorithm. You can see it if you choose e.g. the `arena.map`, start coordinates 4,3 and goal coordinates 5,11.
<br/>
The command line too also exists because I started working on the algorithms using command line simulations. To test them out, you can e.g. run:
```
poetry run invoke jps
```
which is a shortcut for `python3 cli.py --jps --visual --map wall.map 0 0 4 7` and has the advantage over the graphical interface that it uses colors and logs comments on what's happenning. It also produces the final path as a series of coordinates at the end unlike the graphical interface. <br />
It's also possible to test dijkstra in command line with:
```
poetry run invoke dijktra
```
Although the output being just the length of the path isn't too exciting. To learn more about the command line type:
```
python3 src/cli.py --help
```
The command line tool also allows you to pass start and goal coordinates as arguments.<br/>
Other useful commands are:
```
poetry run invoke test
```
To run `pytest` on the code and 

```
poetry run invoke coverage-report
```
To create and open in a browser the branch coverage. If you get an error similar to this one:
```
[13289:13289:0403/183659.749216:ERROR:process_singleton_posix.cc(353)] The profile appears to be in use by
 another Google Chrome process (44970) on another computer (vdi-cubic-025.ad.helsinki.fi).
Chrome has locked the profile so that it doesn't get corrupted.
If you are sure no other processes are using this profile,
you can unlock the profile and relaunch Chrome.
```
You can run  `rm -rf ~/.config/google-chrome/Singleton*` and then try to generate the report again. It should open in your browser. If it doesn't, there is still the possibility of opening it with a browser application directly from the file in html-cov in the topmost directory of the project.<br/>
Note: the above `poetry` commands can be run in any project directory thanks to using absolute path of the project in `tasks.py`<br/>

If you are experiencing any issues with the command line or graphical tool, you might want to run:
```
poetry shell
poetry install
```
If there are import problems with python, the following might help:
```
export PYTHONPATH=~/Documents/Algorithms\ and\ AI/Aineopintojen-harjoitusty-Algoritmit-ja-teko-ly-/src/
export PYTHONPATH=~/home/x/Documents/Algorithms\ and\ AI/Aineopintojen-harjoitusty-Algoritmit-ja-teko-ly-/src/services
```
Currently the code isn't the nicest and needs a lot of refactoring, but feel free to take a look at JPS code! It was very challenging to write it from ground-up.

