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

    def get_goal_route(self):
        if self.goal  == None:
            return print("This player don't have a goal.")
        
        table_copy = [row[:] for row in self.maze.table]
        reached_player = False
        
        current_distance = 0
        table_copy[self.goal["y"]][self.goal["x"]] = 0
        possibilities = [[{ "x": self.goal["x"], "y": self.goal["y"] }]]

        while not reached_player:
            new_possibilities = []

            for coords in possibilities[current_distance]:
                check_pos_1 = self.maze.check_position(coords["x"] - 1, coords["y"])
                already_passed_pos_1 = any(v["x"] == (coords["x"] - 1) and v["y"] == (coords["y"]) for v in possibilities[current_distance - 1])

                check_pos_2 = self.maze.check_position(coords["x"] + 1, coords["y"])
                already_passed_pos_2 = any(v["x"] == (coords["x"] + 1) and v["y"] == (coords["y"]) for v in possibilities[current_distance - 1])

                check_pos_3 = self.maze.check_position(coords["x"], coords["y"] + 1)
                already_passed_pos_3 = any(v["x"] == (coords["x"]) and v["y"] == (coords["y"] + 1) for v in possibilities[current_distance - 1])

                check_pos_4 = self.maze.check_position(coords["x"], coords["y"] - 1)
                already_passed_pos_4 = any(v["x"] == (coords["x"]) and v["y"] == (coords["y"] - 1) for v in possibilities[current_distance - 1])

                # Adicione esta verificação antes de adicionar as coordenadas possíveis
                if coords["x"] == self.pos_x and coords["y"] == self.pos_y:
                    reached_player = True
                    break

                if check_pos_1 == "valid" and not already_passed_pos_1:
                    new_possibilities.append({ "x": coords["x"] - 1, "y": coords["y"]})
                if check_pos_2 == "valid" and not already_passed_pos_2:
                    new_possibilities.append({ "x": coords["x"] + 1, "y": coords["y"] })
                if check_pos_3 == "valid" and not already_passed_pos_3:
                    new_possibilities.append({ "x": coords["x"], "y": coords["y"] + 1 })
                if check_pos_4 == "valid" and not already_passed_pos_4:
                    new_possibilities.append({ "x": coords["x"], "y": coords["y"] - 1 })

                table_copy[coords["y"]][coords["x"]] = f'{current_distance}'

            possibilities.append(new_possibilities)
            current_distance += 1
            
            if not possibilities[current_distance] or reached_player:
                break

        print(possibilities)
        maze_str = ""
        for row in table_copy:
            maze_str += ' '.join(row) + '\n'
        print(maze_str)
            
            


