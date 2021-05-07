# RandomWalk
Simulation on Python, using the bokeh library

The objective of this little project is to understand and implement sophisticated tools and complex concepts on a python file, and deagregate the relevant information for answer my curiosity about some behaviours and fundamentals concepts on simulation.

## Output Examples
![randomWalk](https://github.com/PabloTabilo/randomWalk/blob/main/resources/example.png?raw=true)
* This graph is an example using the bokeh library
* The objective is visualize the behaviours of two drunk guys, both with different parameters of move.
* What's the difference between them?
* The First guy is subject to this behaviour: ```return random.choice([(0,1),(0,-1),(1,0),(-1,0)])```
* Meanwhile the second guy:
```
pos_x = 1 if random.random()<=.5 else 0
pos_y = 1 if random.random()<=.5 else 0
pos_x = -1 if random.random()<=.5 else pos_x
pos_y = -1 if random.random()<=.5 else pos_y
return (pos_x, pos_y)
```
![distances](https://github.com/PabloTabilo/randomWalk/blob/main/resources/means_dists.png?raw=true)
* The Purpose of this image is represent the behaviour of the mean distance for each epoch (experiments) on each number of different steps.

## Prerequisites
* Python
* We need a ```venv``` for install bokeh package and not interfer with the local enviroment.
* Only package ```pip install bokeh```

## Build with ...
* [Python vanilla](https://www.python.org/)
