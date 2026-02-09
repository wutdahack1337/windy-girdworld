import random

class Environment:
    def __init__(self):
        self.n = 7
        self.m = 10
        self.agent_position = (3, 0)
        self.goal_position = (3, 7)

        self.windy_columns = [3, 4, 5, 6, 7, 8]


    def reset(self):
        # start position
        self.agent_position = (3, 0)
        return self.agent_position


    def step(self, action):
        windy = 0
        if self.agent_position[1] in self.windy_columns:
            windy = 1

        terminate = False

        if action == 'w':
            self.agent_position = ( max(0,        self.agent_position[0] - 1 - windy) , self.agent_position[1] )
        elif action == 's':
            self.agent_position = ( min(self.n-1, self.agent_position[0] + 1 - windy) , self.agent_position[1] )
        elif action == 'a':
            self.agent_position = ( max(0,        self.agent_position[0] - windy), max(0,        self.agent_position[1] - 1) )
        elif action == 'd':
            self.agent_position = ( max(0,        self.agent_position[0] - windy), min(self.m-1, self.agent_position[1] + 1) )
        else:
            print("[WARN] just w, s, a, d")
            return terminate

        if self.agent_position == self.goal_position:
            terminate = True

        return terminate
        

    def render(self):
        for i in range(self.n):
            for j in range(self.m):
                if (i, j) == self.agent_position:
                    print('A',end='')
                    continue

                if (i, j) == self.goal_position:
                    print('G', end='')
                    continue

                if j in self.windy_columns:
                    print('^',end='')
                    continue

                print('.', end='')

            print()

        

