from maze import Maze
from mocked_mazes import test_maze_1

labirinto = Maze.create_from_dict(test_maze_1)
print(labirinto)