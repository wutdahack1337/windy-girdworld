import time

from environment import Environment as Env
from agent_random import RandomAgent
from agent_sarsa import EpsilonGreedySarsaAgent


env = Env()

def run():
    mode = input("mode (human/random/sarsa): ")

    if mode == "human":
        terminate = False
        while terminate is False:
            env.render()
            action = input("action (w/s/a/d): ")
            terminate = env.step(action)

    elif mode == "random":
        agent = RandomAgent()
        for episode in range(1):
            env.reset()
            step_counter = 0

            terminate = False
            while terminate is False:
                env.render()

                action = agent.select_action()
                terminate = env.step(action)

                print(f"[INFO] step_counter: {step_counter}")
                step_counter += 1

                time.sleep(0.025)

    elif mode == "sarsa":
        agent = EpsilonGreedySarsaAgent(7*10, 4, 0.1, 0.5)

        raise NotImplementedError
    else:
        print("[WARN] only human/random/sarsa")
        return

    env.render()
    print("[INFO] finish!!!")

if __name__ == "__main__":
    run()
