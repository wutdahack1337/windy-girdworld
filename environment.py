import random

class Environment:
    def __init__(self):
        self.n = 7
        self.m = 10
        self.agent_position = (3, 0)
        self.goal_position = (3, 7)

        self.windy_1_columns = [3, 4, 5, 8]
        self.windy_2_columns = [6, 7]

    def reset(self):
        # start position
        self.agent_position = (3, 0)
        return self.agent_position

    def step(self, action):
        windy = 0
        if self.agent_position[1] in self.windy_1_columns:
            windy = 1
        elif self.agent_position[1] in self.windy_2_columns:
            windy = 2

        terminate = False

        if   action == 'w' or action == 0:
            self.agent_position = ( max(0,        self.agent_position[0] - 1 - windy) , self.agent_position[1] )
        elif action == 's' or action == 1:
            self.agent_position = ( min(self.n-1, self.agent_position[0] + 1 - windy) , self.agent_position[1] )
        elif action == 'a' or action == 2:
            self.agent_position = ( max(0,        self.agent_position[0] - windy), max(0,        self.agent_position[1] - 1) )
        elif action == 'd' or action == 3:
            self.agent_position = ( max(0,        self.agent_position[0] - windy), min(self.m-1, self.agent_position[1] + 1) )
        else:
            print("[WARN] only w/s/a/d or 0/1/2/3")
            return terminate

        if self.agent_position == self.goal_position:
            terminate = True

        return terminate

    # helper
    def render(self):
        for i in range(self.n):
            for j in range(self.m):
                if (i, j) == self.agent_position:
                    print('A',end='')
                elif (i, j) == self.goal_position:
                    print('G', end='')
                elif j in self.windy_1_columns:
                    print("^",end='')
                elif j in self.windy_2_columns:
                    print('?',end='')
                else:
                    print('.', end='')
            print()

    def state(self, location):
        return location[0]*self.m + location[1]
