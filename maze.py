class Maze:
    def __init__(self, name: str, width: int, height: int):
        self.name = name
        self.table = [[" " for _ in range(width)] for _ in range(height)]
        self.table_height = height
        self.table_width = width

    def add_wall(self, start_pos_x: int, start_pos_y: int, wall_width: int, wall_height: int, alias: str="W"):
        """ Função que adiciona uma parede ao labirinto """
        possible_width = (self.table_width - start_pos_x - wall_width) >= 0

        if not possible_width:
            return print(f'''Wall is too large...
            Width: {wall_width}, starting in position x: {start_pos_x}.
            Maximum width in this position: {self.table_width - start_pos_x}
            ''')
        possible_height = (self.table_height - start_pos_y - wall_height) >= 0

        if not possible_height:
            return print(f'''Wall is too tall...
            Height: {wall_height}, starting in position y: {start_pos_y}.
            Maximum height in this position: {self.table_height - start_pos_y}
            ''')
        
        current_pos_x = start_pos_x 

        for _ in range(wall_width):
            current_pos_y = start_pos_y
            for _ in range(wall_height):
                self.table[current_pos_y][current_pos_x] = alias
                current_pos_y += 1 
            current_pos_x +=1
    
    def spawn_player(self, player, pos_x: int, pos_y: int):
        """ Função que spawna um player dentro do labirinto """
        if (pos_x + 1) > self.table_width or (pos_y + 1) > self.table_height:
            return print('Invalid position.')
        if self.table[pos_y][pos_x] != " ":
            return print('This position is already occupied by something.')
        self.table[pos_y][pos_x] = player.alias

        player.set_maze(self, pos_x, pos_y)

        return print(f'Player spawned on x: {pos_x}, y: {pos_y}')
    
    def check_position(self, x: int, y: int):
        """ Função que checa se uma posição do labirinto está ocupada """
        if x > self.table_width or y > self.table_height:
            return "invalid"
        if self.table[y][x] != " ":
            return "blocked"
        return "valid"
    
    
    def show_position(self, x: int, y: int, str_mode):
        """ Função que exibe com uma marcação, uma posição do labirinto se a mesma estiver livre """
        checked_position = self.check_position(x, y)

        if not checked_position == "valid":
            return print("This position is " + checked_position + "...")
        
        table_copy = [row[:] for row in self.table]
        table_copy[y][x] = "✪"

        if not str_mode:
            for row in table_copy:
                print(row)
        else:
            maze_str = ""
            for row in table_copy:
                maze_str += ' '.join(row) + '\n'
            return print(maze_str)

    def show(self, str_mode: bool):
        """ Função que mostra labirinto em formato de array """
        print(" ")
        if str_mode:
            maze_str = ""
            for row in self.table:
                maze_str += ' '.join(row) + '\n'
            return print(maze_str)
        else:
            for row in self.table:
                print(row)
        return print(" ")
    
    @staticmethod
    def create_from_dict(maze_dict: dict):
        """ Função que cria labirinto a partir de um dicionário (mocked_mazes) """
        new_maze = Maze(maze_dict["name"], maze_dict["width"], maze_dict["height"])
        for wall in maze_dict["walls"]:
            new_maze.add_wall(wall["sx"], wall["sy"], wall["w"], wall["h"], wall["a"])
        return new_maze
