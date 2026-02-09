import time

from environment import Environment as Env
from agent import RandomAgent


env = Env()
random_agent = RandomAgent()

for episode in range(1):
    env.reset()
    step_counter = 0

    terminate = False
    while terminate is False:
        env.render()

        action = random_agent.select_action()
        terminate = env.step(action)

        print(f"[INFO] step_counter: {step_counter}")
        step_counter += 1

        time.sleep(0.1)

    env.render()
    print("[INFO] finish!!!")

# terminate = False
# while terminate is False:
#     env.render()

#     action = input("action (w/s/a/d):")

#     terminate = env.step(action)

# env.render()
# print("[INFO] finish!!!")
