from maze import Maze

class Player:
    def __init__(self, name: str, alias: str):
        self.name: str = name
        self.alias: str= alias
        self.spawned: bool = False
        self.maze: Maze = None
        self.pos_x: int = None
        self.pos_y: int = None
        self.goal = None

    def __str__(self):
        return f'''
==============================================================================
Player "{self.name}" [{self.alias}]:
-- Current Maze: {self.maze.name}
-- Current Position: x={self.pos_x}, y={self.pos_y} 
==============================================================================
        '''

    def set_maze(self, maze: Maze, x: int, y: int):
        self.maze = maze
        self.pos_x = x
        self.pos_y = y

    def set_goal(self, x: int, y: int):
        print(f"Trying to set {self.name}'s goal to to x: {x}, y: {y}...")

        if self.maze == None:
            return print("This player isn't spawned in any maze.")
        checked_position = self.maze.check_position(x, y)
        if not checked_position == "valid":
            return print("This position is " + checked_position + "...")
        
        self.goal = { "x": x, "y": y }
        return print(f"{self.name}'s goal was changed with success!")
    
    def show_goal(self, str_mode: bool=False):
        if self.goal  == None:
            return print("This player don't have a goal.")
        
        self.maze.show_position(self.goal["x"], self.goal["y"], str_mode)

