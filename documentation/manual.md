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
# Experience the glory of the colorful GUI!
As first steps, I would recommend clicking on `Default JPS`. A visualization of the end result should appear. You can make it smaller or bigger with the purple `-` and `+` and see every step of the execution by updating the slide counter or by pressing the buttons. It's also possible to animate the visualization, showing every step of execution from the start or from a chosen frame. The animation can only be stopped by clicking on *Stop animation*<br/>
# Input files
The accepted inputs are text files with `.map` extension, although you can also choose to load a file that has a different extension. If you want to create a file or download one from the internet for testing, make sure it resembles those that are in the `/map` directory. For now, the algorithms assume that a dot `.` means a free tile, and a `T` an obstacle or a wall. JPS and Dijkstra also expect the maps to be rectangular, although that might change in the future. <br>
Choosing a map takes place in the graphical interface. As mentioned, there are a few ready inputs in the `maps` folder. It's possible to add your own maps there. Major ones like `brc.map` and `arena.map` were downloadeded from [here](https://www.movingai.com/benchmarks/grids.html), the other were created by hand. <br />
# Structure
Files `JPS.py` and `Dijkstra.py` are directly responsible for how the program executes, but it's only possible to use the algorithms through through running `poetry run invoke start` and involving the graphical interface. For more instructions, go to [README.md](https://github.com/jakubgrad/Aineopintojen-harjoitusty-Algoritmit-ja-teko-ly-/blob/main/README.md).<br>
# Time testing
Because the program uses creates snapshots of execution (so-called *slides*) of the algorithms at runtime, the execution times that you will get inside the *Log* window will be inaccurate by default. It might also be, that for bigger maps the program freezes, because it tries to create lots and lots of snapshots of execution. To get accurate times and run the algorithms on bigger maps, click on 
![image](https://github.com/jakubgrad/Aineopintojen-harjoitusty-Algoritmit-ja-teko-ly-/assets/113715885/d40985ca-ef33-495e-800f-1c56ea7460a5)
And you should be good


# Troubleshooting
Unfortunately I have not yet implemented good error logging, even though the logic of the application could very easily allow it. So if the buttons don't react, it might for a few of below innocent reasons:<br />
- the coordinates that were chosen are out of bounds of the map<br />
- the execution of the algorithm doesn't finish (you might even hear the familiar whirring) because the computation takes too long, and so the UI cannot displays snapshots<br />
- There is something missing (e.g. you haven't chosen a map, one of the coordinates etc.)<br />
You might want to look at the command line when that happens.<br />

If you find that `Default Dijkstra` and `Default JPS` don't work, it might be because you have not run `poetry run invoke start` in the topmost directory
