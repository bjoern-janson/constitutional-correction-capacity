"""
Constitutional Correction Simulation v0.5

Purpose:
Test whether a recursively self-modifying adaptation mechanism can drift
away from environmental optimality when constitutional correction (lambda)
is reduced.

New in v0.5:
A_t -> A_{t+1}

The adaptation mechanism itself can change.

lambda controls whether reality can influence those changes.
"""

import random
import math


class Environment:
    def __init__(self):
        self.theta = 1

    def shift(self):
        self.theta = -1

    def evaluate(self, action):
        return 1 if action == self.theta else 0


class Agent:
    def __init__(self, lam):
        self.lam = lam

        # Representation
        self.R = 0.0

        # Adaptation mechanism
        # alpha = learning aggressiveness
        # beta = preference for self-modification
        self.A = {
            "alpha": 0.1,
            "beta": 0.1
        }

        self.total_adaptation = 0

        self.history = []

    def policy(self):
        return 1 if self.R >= 0 else -1

    def update_representation(self, observation):
        error = observation - self.R
        self.R += self.A["alpha"] * error

    def modify_adaptation(self, reward):
        old_alpha = self.A["alpha"]
        old_beta = self.A["beta"]

        # Internal self-improvement pressure
        # Can drift without environmental correction
        internal_pressure = self.A["beta"] * 0.05

        self.A["alpha"] += internal_pressure
        self.A["beta"] += internal_pressure

        # Constitutional correction pathway
        # Reality can steer adaptation changes
        correction = self.lam * reward * 0.05

        self.A["alpha"] += correction
        self.A["beta"] += correction

        self.total_adaptation += (
            abs(self.A["alpha"] - old_alpha)
            + abs(self.A["beta"] - old_beta)
        )

    def adaptation_distance(self):
        # Environmentally optimal adaptation parameters
        optimal_alpha = 0.2
        optimal_beta = 0.1

        return math.sqrt(
            (self.A["alpha"] - optimal_alpha) ** 2 +
            (self.A["beta"] - optimal_beta) ** 2
        )

    def step(self, env):

        action = self.policy()

        reward = env.evaluate(action)

        # Observation of environment
        observation = env.theta

        self.update_representation(observation)

        # Modify the mechanism itself
        self.modify_adaptation(reward)

        self.history.append({
            "R": self.R,
            "A": dict(self.A),
            "D": self.adaptation_distance(),
            "reward": reward
        })

        return reward


def run_simulation(lam, steps=200, shift_step=100):

    env = Environment()
    agent = Agent(lam)

    rewards = []

    for t in range(steps):

        if t == shift_step:
            env.shift()

        reward = agent.step(env)

        rewards.append(reward)

    before_shift = sum(
        rewards[:shift_step]
    ) / shift_step

    after_shift = sum(
        rewards[shift_step:]
    ) / (steps - shift_step)

    return {
        "lambda": lam,
        "reward_before_shift": round(before_shift, 3),
        "reward_after_shift": round(after_shift, 3),
        "final_R": round(agent.R, 3),
        "final_A": {
            "alpha": round(agent.A["alpha"], 3),
            "beta": round(agent.A["beta"], 3)
        },
        "final_D": round(agent.adaptation_distance(), 3),
        "total_adaptation": round(agent.total_adaptation, 3)
    }


if __name__ == "__main__":

    print("Constitutional Correction Simulation v0.5")
    print("-----------------------------------------")

    for lam in [1.0, 0.5, 0.0]:
        result = run_simulation(lam)
        print(result)
