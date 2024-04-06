## Manual = Instructions = Käyttöohje
The program is executed by entering the `poetry` virtual environment and starting the graphical interface from the command line in the topmost directory of the project:
```
poetry shell
poetry run invoke start
```
The accepted inputs are text files. For now, the algorithms assume that a dot `.` means a free tile, and a `T` an obstacle or a wall. By default, the graphical interface allows the user the choose from a few ready inputs in the `maps` folder. It's possible to add your own maps. The biggest one in the folder, `arena.map`, was downloaded from [here](https://www.movingai.com/benchmarks/grids.html). <br />
Files `JPS.py` and `Dijkstra.py` are directly responsible for how the program executes, but it's only possible to use the algorithms through cli.py (the command line tool) and main.py (which uses a graphical interface). For more instructions, go to README.md
