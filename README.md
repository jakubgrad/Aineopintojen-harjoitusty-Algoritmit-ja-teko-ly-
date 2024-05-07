# JPS vs Dijkstra
A repository for the course Aineopintojen harjoitustyö: Algoritmit ja tekoäly (period 4) Laboratoriotyöskentely<br /><br />
[Specification document = Määrittelydokumentti](https://github.com/jakubgrad/Aineopintojen-harjoitusty-Algoritmit-ja-teko-ly-/blob/main/documentation/specification%20document.md) <br>
[Testing document = Testausdokumentti](https://github.com/jakubgrad/Aineopintojen-harjoitusty-Algoritmit-ja-teko-ly-/blob/main/documentation/testing%20document.md) <br>
[Implementation document = Toteutusdokumentti](https://github.com/jakubgrad/Aineopintojen-harjoitusty-Algoritmit-ja-teko-ly-/blob/main/documentation/implementation%20document.md) <br>
[Manual = Käyttöohje](https://github.com/jakubgrad/Aineopintojen-harjoitusty-Algoritmit-ja-teko-ly-/blob/main/documentation/manual.md) <br>

To understand `JPS` better I recommend reading [this article](https://zerowidth.com/2013/a-visual-explanation-of-jump-point-search/) and [this blogpost](https://www.gamedev.net/tutorials/programming/artificial-intelligence/jump-point-search-fast-a-pathfinding-for-uniform-cost-grids-r4220/).
To test out the app simply download the repository, then <br />
```
cd Aineopintojen-harjoitusty-Algoritmit-ja-teko-ly-/ 
poetry shell
poetry install
poetry run invoke start
```
Doing that should open a GUI tool with a welcoming interface. <br />

<p align="center">
    <img src="/documentation/pictures/program.png" width="30%" alt="UI image">
</p>
Now that the tool is open you can try it. I recommend first trying out `Default JPS` and `Default Dijkstra`, since these examples have predefined start and goal coordinates and maps that I know to work well.<br/>
Once you run a regular or a default algorithm, using the UI you can change the size of the display, see every step of execution by updating the counter and even animate the execution from any point.<br/><br/>
Other useful commands are:
```
poetry run invoke test #runs pytest on the code
poetry run invoke coverage-report #creates a branch testing report and opens it online
```
If after running `coverage-report` task you get an error similar to this one:
```
[13289:13289:0403/183659.749216:ERROR:process_singleton_posix.cc(353)] The profile appears to be in use by
 another Google Chrome process (44970) on another computer (vdi-cubic-025.ad.helsinki.fi).
Chrome has locked the profile so that it doesn't get corrupted.
If you are sure no other processes are using this profile,
you can unlock the profile and relaunch Chrome.
```
You can run  `rm -rf ~/.config/google-chrome/Singleton*` and then try to generate the report again. It should open in your browser. If it doesn't, there is still the possibility of opening it with a browser application directly from the file in html-cov in the topmost directory of the project, or executing `poetry run invoke coverage` and finding the result file yourself.<br/>
Note: the above `poetry` commands can be run in any project directory thanks to using absolute path of the project in `tasks.py`<br/>

If you are experiencing any issues with the command line or graphical tool, you might want to run:
```
poetry shell
poetry install
```
If there are import problems with python, which is unlikely to occur in the first place, the following might help:
```
export PYTHONPATH=~/Documents/Algorithms\ and\ AI/Aineopintojen-harjoitusty-Algoritmit-ja-teko-ly-/src/
export PYTHONPATH=~/home/x/Documents/Algorithms\ and\ AI/Aineopintojen-harjoitusty-Algoritmit-ja-teko-ly-/src/services
```
Currently the code isn't the nicest and needs a lot of refactoring and linting, but feel free to take a look at any of it!<br><br>
[Peer review 1](https://github.com/Wincewind/tiralabra/issues/1)<br>
[Peer review 2](https://github.com/levitesuo/algoritmit-harjoitusty-/issues/2)

