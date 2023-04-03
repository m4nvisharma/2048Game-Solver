# 2048 Game-Solver

##2048 Generator
The 2048 generator starts off by designing the board as an array of 0’s. Once the game is in motion, the game inputs two random numbers, either a 2 or a 4, to begin the game. The player is able to move in any direction; left, right, up, or down using the related keys. After every move, the board adds another tile at random, with a 90% chance of placing a 2 and a 10% chance of placing a 4, until the game board is full or the player reaches 2048.

##2048 Solver
The solver uses a heuristic algorithm to find the best route to win the game; to reach 2048. The game solver measures the situation of the board, and considers what the situation of the board if it moved left, right, up or down. For each possible move, it considers where the next random tile could be placed and displays a list of possible outcomes. It finds the heuristic value, in comparison to a set ‘ideal’ board, for each situation of each move, and averages them out to create a heuristic value for every move. The board decides to play the 'best move', the move with the highest heuristic value, until the board is full or reaches 2048. 
