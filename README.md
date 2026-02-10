# windy-girdworld
Windy Gridworld   

<img width="502" height="258" alt="image" src="https://github.com/user-attachments/assets/e715b079-a89a-4310-a73c-2cc27b9d34e6" />


> This is a standard gridwolrd, with start and goal states, but with one difference: there is a crosswind running upward through the middle of the grid.   
> The actions are the standard four - up, down, right, and left.   
> But in the middle region the resultant next states are shifted upward by a "wind", the strength of which varies from column to column. The strength of the wind is given below each column, in number of cells shifted upward.  
> This is an undiscounted episodic task, with constant rewards of -1 until the goal state is reached.   

```
  0123456789
0 ...^^^??^.
1 ...^^^??^.
2 ...^^^??^.
3 A..^^^?G^.
4 ...^^^??^.
5 ...^^^??^.
6 ...^^^??^.
```

```
python main.py
```
