from environment import Environment as Env


env = Env()
env.reset()

terminate = False
while terminate is False:
    env.render()
    action = input("action (w/s/a/d):")
    terminate = env.step(action)

env.render()
print("[INFO] you did it!!!")