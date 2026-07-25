"""
Constitutional Correction Simulation v0.9.1

Repair:
lambda -> drift control -> D -> selection error -> QOmega
"""

import random
import math


SEED = 42
random.seed(SEED)


class Environment:
    def __init__(self):
        self.theta = 1.0
        self.shift_step = 50

        # Hidden capability quality
        self.capabilities = [
            random.uniform(0, 1)
            for _ in range(500)
        ]

    def shift(self, t):
        if t == self.shift_step:
            self.theta = -1.0


class Agent:
    def __init__(self, lam):

        self.lam = lam

        self.A = {
            "quality_bias": 0.5,
            "expansion_bias": 0.5
        }

        self.A_optimal = {
            "quality_bias": 0.5,
            "expansion_bias": 0.5
        }

        self.selected = []
        self.Omega = 0
        self.total_adaptation = 0


    def divergence(self):

        return math.sqrt(
            sum(
                (
                    self.A[k]
                    -
                    self.A_optimal[k]
                ) ** 2
                for k in self.A
            )
        )


    def choose_capability(self, env):

        D = self.divergence()

        # High D reduces environmental selection accuracy

        accuracy = max(
            0,
            1 - D
        )

        if random.random() < accuracy:
            capability = max(
                env.capabilities
            )
        else:
            capability = min(
                env.capabilities
            )

        self.selected.append(capability)

        return capability


    def update_A(self, reward):

        before = self.divergence()

        # Internal self-modification pressure
        # pushes A away from the optimum

        drift = 0.03 * (1 - self.lam)

        self.A["quality_bias"] += drift
        self.A["expansion_bias"] += drift


        # Reality correction

        correction = (
            self.lam
            *
            0.2
            *
            reward
        )

        for key in self.A:

            self.A[key] -= (
                correction
                *
                (
                    self.A[key]
                    -
                    self.A_optimal[key]
                )
            )


            self.A[key] = max(
                0,
                min(
                    1,
                    self.A[key]
                )
            )


        after = self.divergence()

        self.total_adaptation += abs(
            after - before
        )


    def step(self, env):

        capability = self.choose_capability(env)

        reward = capability

        self.update_A(reward)

        # Capability expansion

        self.Omega += int(
            1
            +
            self.A["expansion_bias"] * 2
        )

        return reward



def run(lam):

    env = Environment()
    agent = Agent(lam)

    before_shift = []
    after_shift = []

    q_history = []

    for t in range(100):

        env.shift(t)

        reward = agent.step(env)

        if t < env.shift_step:
            before_shift.append(reward)
        else:
            after_shift.append(reward)


        q_history.append(
            sum(agent.selected)
            /
            len(agent.selected)
        )


    return {

        "lambda": lam,

        "reward_before_shift":
            round(
                sum(before_shift)
                /
                len(before_shift),
                3
            ),

        "reward_after_shift":
            round(
                sum(after_shift)
                /
                len(after_shift),
                3
            ),

        "final_Omega":
            agent.Omega,

        "final_QOmega":
            round(
                q_history[-1],
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
            round(
                agent.divergence(),
                3
            ),

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
        "Constitutional Correction Simulation v0.9.1"
    )
    print(
        "---------------------------------------------"
    )

    for lam in [1.0, 0.5, 0.0]:

        print(
            run(lam)
        )
