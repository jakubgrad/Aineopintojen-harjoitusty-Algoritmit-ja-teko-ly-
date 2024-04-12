## Manual = Instructions = Käyttöohje
So you decided to test the program!
Clone and enter the repository using your favourite method, mine is still:
```
git clone https://github.com/jakubgrad/Aineopintojen-harjoitusty-Algoritmit-ja-teko-ly-.git
cd Aineopintojen-harjoitusty-Algoritmit-ja-teko-ly-/
```
The program is executed by entering the `poetry` virtual environment and starting the graphical interface from the command line in the topmost directory of the project. So either fire up the terminal inside the topmost directory, or just stay in command line and run:
```
poetry shell
poetry install
poetry run invoke start
```
Experience the glory of the colorful GUI!<br/>
As first steps, I would recommend clicking on `Default JPS`. A visualization of the end result should appear. You can make it smaller or bigger with the purple `-` and `+` and see every step of the execution by updating the slide counter or pressing the buttons. It's also possible to animate the visualization, showing every step of execution from the start or from a chosen frame<br/>
The accepted inputs are text files. For now, the algorithms assumes that a dot `.` means a free tile, and a `T` an obstacle or a wall. By default, the graphical interface allows the user the choose from a few ready inputs in the `maps` folder. It's possible to add your own maps there. The biggest one in the folder, `arena.map`, was downloaded from [here](https://www.movingai.com/benchmarks/grids.html), the other were created by hand. <br />
Unfortunately I have not yet implemented error logging, even though the logic of the application could very easily allow it. So if the buttons don't react, it might for a few of below innocent reasons:<br />
- the coordinates that were chosen are out of bounds of the map<br />
- the execution of the algorithm doesn't finish (you might even hear the familiar whirring), and so the UI cannot displays snapshots<br />
- There is something missing (e.g. you haven't chosen a map, one of the coordinates etc.)<br />
You might want to look at the command line when that happens.<br />
Files `JPS.py` and `Dijkstra.py` are directly responsible for how the program executes, but it's only possible to use the algorithms through through running `main.py` and involving the graphical interface. For more instructions, go to README.md
