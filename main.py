from maze import Maze
from player import Player
from mocked_mazes import test_maze_1

labirinto = Maze.create_from_dict(test_maze_1)
jogador = Player("Renan", "♫")

labirinto.spawn_player(jogador, 3, 3)
labirinto.show()

print(jogador)
jogador.set_goal(9,5)
print("")
jogador.show_goal(str_mode=True)
print(labirinto)