import random

class EpsilonGreedySarsaAgent:
    def __init__(self, num_states, num_actions, epsilon, step_size):
        self.num_states = num_states
        self.num_actions = num_actions
        self.q_values = [[0]*self.num_actions]*self.num_states

        self.epsilon = epsilon     # epsilon-greedy
        self.step_size = step_size # alpha

    def select_action(self, state, verbose):
        if random.random() <= self.epsilon:
            if verbose:
                print("[INFO] explore")
            return random.randint(0, self.num_actions-1)
        else:
            if verbose:
                print("[INFO] exploit")
            return self.argmax(state)

    def update(self):
        raise NotImplementedError

    # helper
    def argmax(self, state):
        max_value = float("-inf")
        actions = []
        for action in range(self.num_actions):
            if self.q_values[state][action] > max_value:
                max_value = self.q_values[state][action]
                actions = [action]
            elif self.q_values[state][action] == max_value:
                actions.append(action)

        return random.choice(actions)
