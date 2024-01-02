# AI-Simulators

This repository contains AI algorithms that I implemented in Python to assist with assignments in my AI course.

## BFS/DFS Search
Performs DFS and BFS to get paths through a hard coded graph.  

#### To Run
- In terminal, use `cd search_algorithms` to get into the directory and use command `python search.py`

## Genetic Search
Genetic Search is a solution to a constraint satisfaction problem as a form of stochastic local search. Given a set of constraints C and a population containing a set of individuals X which contains properties \[x1...xn\], this algorithm seeks to mix-and-match individuals and mutating values until the properties satisfies every constraint. This proccess is similar to how sexual reproduction works. 

The starting individuals and constraints are hard-coded into the implementation. For this specific implementation, \[x1...xn\] is A-G.  The constraints are: 

- A > G, 
- |G - C| = 1, 
- D != C, G != F, 
- |E - F| is odd, 
- A <= H, 
- |H - C| is even, 
- E!= C, 
- H !=  F, 
- |F - B| = 1, 
- H != D, 
- E < D - 1, 
- C != F, 
- G < H, 
- D >= G, 
- E != H - 2, 
- D != F -1

#### To Run
- In terminal, use `cd genetic_search_algorithm` to get into the directory and use command `python genetic_algo.py`. It will print out things such as the probability of each individual to be chosen to match, how many constraints each individual satisfies, and which pair of individuals are chosen to reproduce.





