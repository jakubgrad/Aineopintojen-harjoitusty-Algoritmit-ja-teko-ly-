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

## Week 6 
- Thought that some checks can be perform already in the `algorithm_service`, e.g. checking if the start and goal coordinates are the same. So i implemented e.g. checking that the coordinates lie within the map already in `algorithm_service`. But because there is tests e.g. for returning 0 when coordinates are the same for JPS and Dijkstra, I didn't remove checking for this situation inside `JPS` and `Dijkstra`
- Added message to the log when a map is not selected
- Deleted all debugging printouts and code comments
