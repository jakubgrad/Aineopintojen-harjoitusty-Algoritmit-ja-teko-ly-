## Week 3 

export PYTHONPATH=/home/x/Documents/Algorithms\ and\ AI/Aineopintojen-harjoitusty-Algoritmit-ja-teko-ly-/src/
export PYTHONPATH=/home/x/Documents/Algorithms\ and\ AI/Aineopintojen-harjoitusty-Algoritmit-ja-teko-ly-/src/services
imports failed without these 
might not be necessary anymore

## Week 4 
- GUI is functional
- Removed most printouts in JPS algorithm for clarity of code

## Week 5
- changed JPS to not finish once a goal coordinate is reached, but instead to keep looking for shorter paths.
- Changed the method which JPS used to output the distance from a `try except` block and recursion-breaking `raise error` to having `self.min_distance` and updating it whenever the goal coordinate is reached in a new way
- Wrote tests for correctness for Dijkstra and JPS with a +-1 margin of error
- Added logging of time, predicted time complexities, number of edges and vertices to the UI
- refactored creating log messages to `algorithm_service`

