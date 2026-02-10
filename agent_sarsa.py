

class EpsilonGreedySarsaAgent:
    def __init__(self, num_states, num_actions, epsilon, step_size):
        self.num_states = num_states
        self.num_actions = num_actions
        self.q = [[0]*self.num_actions]*self.num_states

        self.epsilon = epsilon     # epsilon-greedy
        self.step_size = step_size # alpha

    def select_action(self):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError