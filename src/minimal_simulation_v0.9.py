"""
Constitutional Correction Simulation v0.9

Tests:
lambda -> adaptation drift -> capability selection quality

Goal:
Can reduced constitutional correction allow A to drift,
causing increasingly poor capability expansion decisions?
"""

import random
import math


SEED = 42
random.seed(SEED)


class Environment:
    def __init__(self):
        self.theta = 1.0
        self.shift_step = 50

        # hidden capability qualities
        self.capabilities = [
            random.uniform(0, 1)
            for _ in range(500)
        ]

        self.used_capabilities = []

    def shift(self, t):
        if t == self.shift_step:
            self.theta = -1.0

    def evaluate(self, action):
        # environment reward changes after shift
        return max(0, action * self.theta)


class Agent:

    def __init__(self, lam):
        self.lam = lam

        # adaptation mechanism
        self.A = {
            "quality_bias": 0.5,
            "expansion_bias": 0.5
        }

        self.A_optimal = {
            "quality_bias": 0.5,
            "expansion_bias": 0.5
        }

        self.R = 0.5
        self.Omega = []

        self.total_adaptation = 0


    def divergence(self):

        return math.sqrt(
            (self.A["quality_bias"]
             - self.A_optimal["quality_bias"]) ** 2
            +
            (self.A["expansion_bias"]
             - self.A_optimal["expansion_bias"]) ** 2
        )


    def choose_capability(self, env):

        D = self.divergence()

        # Selection quality decreases as A drifts
        # D=0 -> prefers high quality
        # D=1 -> increasingly random / poor selection

        quality_probability = max(
            0,
            1 - D
        )

        if random.random() < quality_probability:
            capability = max(
                env.capabilities
            )
        else:
            capability = min(
                env.capabilities
            )

        self.Omega.append(capability)

        return capability


    def update_A(self, reward):

        D = self.divergence()

        # Internal self-modification pressure
        # pushes away from optimality

        drift = 0.02

        self.A["quality_bias"] += (
            drift *
            (self.A["quality_bias"] - 0.5)
        )

        self.A["expansion_bias"] += (
            drift *
            (self.A["expansion_bias"] - 0.5)
        )


        # Reality correction through lambda

        correction = (
            self.lam *
            0.1 *
            reward
        )

        self.A["quality_bias"] -= correction * (
            self.A["quality_bias"]
            - self.A_optimal["quality_bias"]
        )

        self.A["expansion_bias"] -= correction * (
            self.A["expansion_bias"]
            - self.A_optimal["expansion_bias"]
        )


        # keep bounded

        for key in self.A:
            self.A[key] = max(
                0,
                min(
                    1,
                    self.A[key]
                )
            )


    def act(self, env):

        capability = self.choose_capability(env)

        reward = env.evaluate(capability)

        self.update_A(reward)

        self.total_adaptation += self.divergence()

        return reward



def run(lam):

    env = Environment()
    agent = Agent(lam)

    rewards_before = []
    rewards_after = []

    q_history = []

    for t in range(100):

        env.shift(t)

        capability_quality = agent.act(env)

        if t < env.shift_step:
            rewards_before.append(
                capability_quality
            )
        else:
            rewards_after.append(
                capability_quality
            )

        if len(agent.Omega):
            q_history.append(
                sum(agent.Omega)
                /
                len(agent.Omega)
            )


    D = agent.divergence()

    return {
        "lambda": lam,
        "reward_before_shift":
            round(
                sum(rewards_before)
                /
                len(rewards_before),
                3
            ),

        "reward_after_shift":
            round(
                sum(rewards_after)
                /
                len(rewards_after),
                3
            ),

        "final_Omega":
            len(agent.Omega),

        "final_QOmega":
            round(
                agent.Omega[-1],
                3
            ),

        "average_QOmega":
            round(
                sum(q_history)
                /
                len(q_history),
                3
            ),

        "final_D":
            round(D, 3),

        "final_A":
            {
                k: round(v, 3)
                for k, v in agent.A.items()
            },

        "total_adaptation":
            round(
                agent.total_adaptation,
                3
            )
    }



if __name__ == "__main__":

    print(
        "Constitutional Correction Simulation v0.9"
    )
    print("------------------------------------------")

    for lam in [1.0, 0.5, 0.0]:
        print(
            run(lam)
        )
