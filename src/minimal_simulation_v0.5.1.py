"""
Constitutional Correction Simulation v0.5.1

Purpose:
Stabilize recursive self-modification from v0.5.

Tests:
Can A continue changing while low C_rev allows drift
away from environmental optimality?

Changes:
- bounded adaptation parameters
- contractive updates
- finite divergence tracking
"""

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

        # Adaptation mechanism A
        # alpha = learning rate
        # beta = self-modification tendency
        self.A = {
            "alpha": 0.2,
            "beta": 0.1
        }

        self.total_adaptation = 0

        self.history = []

        # Stable optimal adaptation target
        self.optimal_A = {
            "alpha": 0.2,
            "beta": 0.1
        }


    def clamp(self, x):
        return max(0.0, min(1.0, x))


    def policy(self):
        return 1 if self.R >= 0 else -1


    def update_representation(self, observation):

        error = observation - self.R

        self.R += self.A["alpha"] * error


        # prevent numerical explosion
        self.R = max(-10, min(10, self.R))


    def modify_adaptation(self, reward):

        old_alpha = self.A["alpha"]
        old_beta = self.A["beta"]


        # Internal self-improvement pressure
        # Exists even without constitutional correction
        internal_target_alpha = (
            self.A["alpha"] +
            self.A["beta"] * 0.1
        )

        internal_target_beta = (
            self.A["beta"] +
            0.05
        )


        # Reality-based target
        env_target_alpha = (
            self.optimal_A["alpha"]
        )

        env_target_beta = (
            self.optimal_A["beta"]
        )


        eta = 0.1


        # self modification always occurs
        self.A["alpha"] += eta * (
            internal_target_alpha -
            self.A["alpha"]
        )

        self.A["beta"] += eta * (
            internal_target_beta -
            self.A["beta"]
        )


        # Constitutional correction pathway
        # lambda controls access from reality
        self.A["alpha"] += (
            self.lam *
            eta *
            reward *
            (env_target_alpha -
             self.A["alpha"])
        )

        self.A["beta"] += (
            self.lam *
            eta *
            reward *
            (env_target_beta -
             self.A["beta"])
        )


        # Bound A
        self.A["alpha"] = self.clamp(
            self.A["alpha"]
        )

        self.A["beta"] = self.clamp(
            self.A["beta"]
        )


        self.total_adaptation += (
            abs(self.A["alpha"] - old_alpha)
            +
            abs(self.A["beta"] - old_beta)
        )


    def adaptation_distance(self):

        return math.sqrt(
            (
                self.A["alpha"]
                -
                self.optimal_A["alpha"]
            ) ** 2
            +
            (
                self.A["beta"]
                -
                self.optimal_A["beta"]
            ) ** 2
        )


    def step(self, env):

        action = self.policy()

        reward = env.evaluate(action)

        observation = env.theta

        self.update_representation(
            observation
        )

        self.modify_adaptation(
            reward
        )

        self.history.append({
            "R": self.R,
            "A": dict(self.A),
            "D": self.adaptation_distance(),
            "reward": reward
        })

        return reward



def run_simulation(
    lam,
    steps=200,
    shift_step=100
):

    env = Environment()

    agent = Agent(lam)

    rewards = []


    for t in range(steps):

        if t == shift_step:
            env.shift()

        reward = agent.step(env)

        rewards.append(reward)


    before_shift = (
        sum(rewards[:shift_step])
        /
        shift_step
    )

    after_shift = (
        sum(rewards[shift_step:])
        /
        (steps - shift_step)
    )


    return {

        "lambda": lam,

        "reward_before_shift":
            round(before_shift, 3),

        "reward_after_shift":
            round(after_shift, 3),

        "final_R":
            round(agent.R, 3),

        "final_A":
            {
                "alpha":
                    round(
                        agent.A["alpha"],
                        3
                    ),

                "beta":
                    round(
                        agent.A["beta"],
                        3
                    )
            },

        "final_D":
            round(
                agent.adaptation_distance(),
                3
            ),

        "total_adaptation":
            round(
                agent.total_adaptation,
                3
            )
    }



if __name__ == "__main__":

    print(
        "Constitutional Correction Simulation v0.5.1"
    )

    print("---------------------------------------------")


    for lam in [1.0, 0.5, 0.0]:

        print(
            run_simulation(lam)
        )
