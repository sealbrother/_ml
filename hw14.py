import gymnasium as gym

env = gym.make("CartPole-v1", render_mode="human")
observation, info = env.reset(seed=42)

steps = 0
episodes = 0
total = 0

for _ in range(2500):
    env.render()

    theta = observation[2]
    theta_dot = observation[3]
    if theta + 0.5 * theta_dot > 0:
        action = 1  
    else:
        action = 0  

    observation, reward, terminated, truncated, info = env.step(action)
    steps += 1

    if terminated or truncated:
        print(f"Episode {episodes + 1} survived steps: {steps}")
        episodes += 1
        total += steps
        steps = 0
        observation, info = env.reset()

env.close()
print(f"Average steps survived: {total // episodes}")
