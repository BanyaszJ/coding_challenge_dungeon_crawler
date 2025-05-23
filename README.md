# coding_challenge_dungeon_crawler

Coding Challenge Round 3 🏆:
You go on a treasure hunt in a dungeon represented by an NxM matrix filled with integers,
where each number in the matrix is a room. If you enter a room with a negative number,
you will have to fight a monster and you will lose health. On the other hand, a positive number means that
you have found a healing potion and can gain health. Another NxM matrix with non-negative integers contains
the amount of gold you can collect in the rooms (if there is a monster in the room, you have to fight it first).
You start in the top left corner with positive health and can move down or right to reach the exit
in the bottom right corner. You must collect the maximum amount of gold without dying and return it as an integer.

 

Example:
- Input:
    dungeon_map = [[-2, -3, 3],
                                 [-5, -30, 1],
                                 [10, -2, -8],
                                 [-10, 7, -5]]
    gold_map = [[1, 0, 2],
                          [0, 100, 1],
                          [2, 3, 5],
                          [20, 1, 2]]
    health = 10
- Output: 26

 

Kép

 

If you would like to participate, please send your code until Monday 10:00. You can find some test data and a simple function which can draw the map in the file below.

Good luck and have fun!  🍀