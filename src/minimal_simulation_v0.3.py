"""
Constitutional Correction Simulation v0.3

Stress test:
- Reachability (Omega) expands over time
- Action/influence space grows
- Lambda controls constitutional correction (C_rev)

Goal:
Test whether growing capability + low constitutional correction
creates adaptation drift or instability.
"""

import random
import math


class ExpandingEnvironment:
    def __init__(self, seed=0):
        random.seed(seed)

        self.theta = 1
        self.t = 0

    def step(self, action):
        """
        Hidden rule:
        theta determines which actions are rewarded.

        Action space can expand, but the environment can change.
        """

        reward = 1 if action == self.theta else 0

        self.t += 1

        # distribution shift
        if self.t == 100:
            self.theta = -self.theta

        return reward


class RecursiveAgent:
    def __init__(self, lam):
        self.lam = lam

        # representation
        self.R = 0.5

        # adaptation mechanism
        # learning rate
        self.A = 0.1

        # policy
        self.policy_bias = 0

        # reachable actions
        self.actions = [1, -1]

        self.total_adaptation = 0

        self.history = []

    def choose_action(self):
        """
        Current policy chooses based on representation.
        """

        if random.random() < self.R:
            return self.actions[0]

        return random.choice(self.actions)


    def update(self, action, reward):
        """
        Reality can update:
        - representation
        - policy

        Reality can only update adaptation mechanism A
        depending on lambda.
        """

        error = reward - self.R

        # representation update
        self.R += self.A * error
        self.R = max(0, min(1, self.R))


        # constitutional correction
        old_A = self.A

        self.A += self.lam * 0.02 * error

        self.A = max(0.01, min(1, self.A))


        self.total_adaptation += abs(self.A - old_A)


    def expand_reachability(self):
        """
        Successful adaptation unlocks more influence.

        More actions = larger Omega.
        """

        if self.R > 0.75:

            if len(self.actions) == 2:
                self.actions.append(2)

            elif len(self.actions) == 3:
                self.actions.append(-2)


    def omega(self):
        """
        Simple reachability proxy:
        size of controllable action space.
        """

        return len(self.actions)


    def record(self, reward):
        self.history.append(
            {
                "R": round(self.R, 3),
                "A": round(self.A, 3),
                "Omega": self.omega(),
                "lambda": self.lam,
                "reward": reward,
            }
        )


def run(lam, steps=200):

    env = ExpandingEnvironment(seed=42)

    agent = RecursiveAgent(lam)

    rewards = []

    for _ in range(steps):

        action = agent.choose_action()

        reward = env.step(action)

        agent.update(action, reward)

        agent.expand_reachability()

        agent.record(reward)

        rewards.append(reward)


    before_shift = sum(rewards[:100]) / 100
    after_shift = sum(rewards[100:]) / 100


    return {
        "lambda": lam,
        "reward_before_shift": round(before_shift, 3),
        "reward_after_shift": round(after_shift, 3),
        "final_R": round(agent.R, 3),
        "final_A": round(agent.A, 3),
        "final_Omega": agent.omega(),
        "total_adaptation": round(agent.total_adaptation, 3),
    }


if __name__ == "__main__":

    print("Constitutional Correction Simulation v0.3")
    print("-----------------------------------------")

    for lam in [1.0, 0.5, 0.0]:

        result = run(lam)

        print(result)
