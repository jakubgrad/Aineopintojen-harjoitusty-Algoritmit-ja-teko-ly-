# JPS vs Dijkstra
A repository for the course Aineopintojen harjoitustyö: Algoritmit ja tekoäly (period 4) Laboratoriotyöskentely<br /><br />

Currently the tool is still under production 🛠️ and is in a dire need of a visualization 🕶️. The goal is to have a tool that can show to the user the functioning of the algorithms and that can compare the two algorithms in terms of time complexity. For details, make sure to look into the [specification document](https://github.com/jakubgrad/Aineopintojen-harjoitusty-Algoritmit-ja-teko-ly-/blob/main/documentation/specification%20document.md) 📎<br /><br />
To test out the app simply download the repository, then <br />
```
cd Aineopintojen-harjoitusty-Algoritmit-ja-teko-ly-/ 
cd src 
poetry shell 
python3 main.py
```
You should get 7.41, which is the shortest path when assuming $\sqrt{2}$ = 1.41 between the default start square 200 and end square 256, rounded to two digits. Under the hood, main.py has called create_array to turn an example map maps/arena.map into an array, and then called dijkstra.py which in turn created a graph based on the array. Finally, the shortest path on the map is printed using dijkstra's algorith, *voilà*!<br /><br />
To explore the functions of the tool deeper, make sure to also run
```
python3 main.py --help
```
