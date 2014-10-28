Rankings Table Generator
========================

Python-based command line application that calculates the rankings table for a soccer league.

Usage
-----
Given a text input file with game results in the following format:

Lions 3, Snakes 3  
Tarantulas 1, FC Awesome 0  
Lions 1, FC Awesome 1  
Tarantulas 3, Snakes 1  
Lions 4, Grouches 0  

the application will output ranked teams in order, as follows:

1. Tarantulas, 6 pts
2. Lions, 5 pts
3. FC Awesome, 1 pt
3. Snakes, 1 pt
5. Grouches, 0 pts

The rules
---------
In this league, a draw (tie) is worth 1 point and a win is worth 3 points. A loss is worth 0 points. If two or more teams have the same number of points, they should have the same rank and be printed in alphabetical order (as in the tie for 3rd place in the sample data).
