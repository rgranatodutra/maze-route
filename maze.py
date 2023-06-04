class Maze:
    def __init__(self, width: int, height: int):
        self.table = [[" " for _ in range(width)] for _ in range(height)]
        self.table_height = height
        self.table_width = width

    def __str__(self):
        maze_str = ""
        for row in self.table:
            maze_str += ' '.join(row) + '\n'
        return maze_str

    def add_wall(self, start_pos_x: int, start_pos_y: int, wall_width: int, wall_height: int, alias: str="W"):
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

        for x in range(wall_width):
            current_pos_y = start_pos_y
            for y in range(wall_height):
                self.table[current_pos_y][current_pos_x] = alias
                current_pos_y += 1 
            current_pos_x +=1
    
    def show(self):
        for row in self.table:
            print(row)
    
    @staticmethod
    def create_from_dict(maze_dict: dict):
        new_maze = Maze(maze_dict["width"], maze_dict["height"])
        for wall in maze_dict["walls"]:
            new_maze.add_wall(wall["sx"], wall["sy"], wall["w"], wall["h"], wall["a"])
        return new_maze
