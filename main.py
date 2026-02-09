import time

from environment import Environment as Env
from agent import RandomAgent


env = Env()
random_agent = RandomAgent()

for episode in range(1):
    env.reset()

    timestep = 0

    terminate = False
    while terminate is False:
        env.render()

        action = random_agent.select_action()
        print(f"[INFO] timestep {timestep}")

        terminate = env.step(action)

        time.sleep(0.1)

        timestep += 1

    env.render()
    print("[INFO] finish!!!")