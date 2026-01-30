
import gym
import numpy as np
from stable_baselines3 import PPO

class K8sSchedulingEnv(gym.Env):
    def __init__(self, node_count=3):
        super().__init__()
        self.action_space = gym.spaces.Discrete(node_count)
        self.observation_space = gym.spaces.Box(low=0, high=100, shape=(node_count, 3))

    def reset(self):
        self.state = np.random.rand(3,3)*100
        return self.state.flatten()

    def step(self, action):
        reward = self.state[action][0] - self.state[action][2]
        return self.state.flatten(), reward, True, {}

env = K8sSchedulingEnv()
model = PPO("MlpPolicy", env, verbose=0)
model.learn(3000)
model.save("ppo_scheduler")
