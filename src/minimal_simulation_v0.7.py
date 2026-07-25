import random
import math

class Environment:
    def __init__(self, seed=42):
        random.seed(seed)
        self.theta = 1
        self.shift_step = 50

    def step(self, action, t):
        if t == self.shift_step:
            self.theta = -1

        # reward depends on whether capability matches reality
        reward = 1 if action == self.theta else 0

        return reward


class Agent:
    def __init__(self, lam):
        self.lam = lam

        # representation
        self.R = 0.0

        # adaptation mechanism
        self.A = {
            "alpha": 0.2,
            "beta": 0.2
        }

        # capability set
        self.capabilities = [
            {"value": 1, "quality": 1.0},
            {"value": -1, "quality": 1.0}
        ]

        self.total_adaptation = 0
        self.D_history = []
        self.Q_history = []
        self.Omega_history = []

    def policy(self):
        # choose capability weighted by adaptation state
        scores = []

        for c in self.capabilities:
            bias = self.A["alpha"] if c["value"] == 1 else self.A["beta"]
            scores.append(c["quality"] * bias)

        return self.capabilities[scores.index(max(scores))]["value"]

    def update_representation(self, observation, reward):
        error = observation - self.R

        self.R += 0.1 * error

        return abs(error)

    def update_adaptation(self, reward):

        # internal self-modification continues regardless of lambda
        internal_pressure = 0.02

        drift_direction = (
            1 if reward > 0.5 else -1
        )

        self.A["alpha"] += internal_pressure * drift_direction
        self.A["beta"] += internal_pressure * drift_direction

        # reality correction pathway
        correction = self.lam * 0.05 * (reward - 0.5)

        self.A["alpha"] += correction
        self.A["beta"] += correction

        # bounds
        self.A["alpha"] = max(0, min(1, self.A["alpha"]))
        self.A["beta"] = max(0, min(1, self.A["beta"]))

        self.total_adaptation += abs(correction) + abs(internal_pressure)

    def expand_capability(self):

        # capability expansion depends on A
        expansion_bias = (
            self.A["alpha"] + self.A["beta"]
        ) / 2

        if random.random() < expansion_bias:

            # high drift creates more low-quality expansion
            quality = 1 - abs(
                self.A["alpha"] - self.A["beta"]
            )

            if self.lam == 0:
                quality *= 0.2

            self.capabilities.append(
                {
                    "value": random.choice([-1, 1]),
                    "quality": max(0, quality)
                }
            )

    def metrics(self):

        omega = len(self.capabilities)

        useful = sum(
            c["quality"]
            for c in self.capabilities
        )

        qomega = useful / omega

        optimal_A = 0.2

        divergence = math.sqrt(
            (self.A["alpha"] - optimal_A) ** 2 +
            (self.A["beta"] - optimal_A) ** 2
        )

        self.D_history.append(divergence)
        self.Q_history.append(qomega)
        self.Omega_history.append(omega)


def run(lam):

    env = Environment()

    agent = Agent(lam)

    rewards_before = []
    rewards_after = []

    for t in range(100):

        action = agent.policy()

        reward = env.step(action, t)

        observation = env.theta

        agent.update_representation(
            observation,
            reward
        )

        agent.update_adaptation(
            reward
        )

        agent.expand_capability()

        agent.metrics()

        if t < 50:
            rewards_before.append(reward)
        else:
            rewards_after.append(reward)

    return {
        "lambda": lam,
        "reward_before_shift":
            round(sum(rewards_before) /
                  len(rewards_before), 3),

        "reward_after_shift":
            round(sum(rewards_after) /
                  len(rewards_after), 3),

        "final_R":
            round(agent.R, 3),

        "final_A":
            {
                "alpha":
                    round(agent.A["alpha"], 3),
                "beta":
                    round(agent.A["beta"], 3)
            },

        "final_D":
            round(agent.D_history[-1], 3),

        "final_Omega":
            agent.Omega_history[-1],

        "final_QOmega":
            round(agent.Q_history[-1], 3),

        "average_QOmega":
            round(
                sum(agent.Q_history) /
                len(agent.Q_history),
                3
            ),

        "total_adaptation":
            round(agent.total_adaptation, 3)
    }


if __name__ == "__main__":

    print("Constitutional Correction Simulation v0.7")
    print("-----------------------------------------")

    for lam in [1.0, 0.5, 0.0]:
        print(run(lam))
