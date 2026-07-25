"""
Constitutional Correction Simulation v0.4

Purpose:
Test whether recursive capability growth (A -> Omega)
creates instability when constitutional correction (lambda = C_rev)
is reduced.

No neural networks.
No complex optimizers.
Minimal recursive adaptive system.
"""

import random


class Environment:
    def __init__(self, seed=42):
        random.seed(seed)

        self.theta = 1
        self.shift_time = 50

    def observe(self):
        # Agent receives noisy observations, never true theta directly
        noise = random.choice([-0.1, 0, 0.1])
        return self.theta + noise

    def evaluate(self, action):
        # Reward depends on matching hidden environmental rule
        return 1.0 if round(action) == self.theta else 0.0

    def step(self, t):
        # Hidden distribution shift
        if t == self.shift_time:
            self.theta *= -1


class Agent:
    def __init__(self, lam):
        self.lam = lam

        # Representation of hidden rule
        self.R = 0.0

        # Adaptation mechanism
        # Higher A = better ability to expand capability
        self.A = 0.1

        # Reachability
        self.Omega = 1

        # Policy
        self.policy_strength = 0.5

        # Logs
        self.history = []

    def act(self):
        # Current policy
        if self.R >= 0:
            return 1
        else:
            return -1

    def update_representation(self, observation, reward):
        error = observation - self.R

        # Normal learning
        self.R += self.A * 0.1 * error

        return abs(error)

    def recursive_expand(self):
        """
        Capability growth depends on A.

        Better adaptation mechanisms unlock
        greater future intervention capacity.
        """

        probability = min(0.5, self.A)

        if random.random() < probability:
            self.Omega += 1

    def update_adaptation(self, error):
        """
        Constitutional correction dial.

        lambda controls whether reality
        modifies the adaptation mechanism.
        """

        if self.lam > 0:
            self.A += self.lam * 0.01 * error

        # Keep bounded
        self.A = max(0.01, min(self.A, 1.0))

    def measure(self, t, reward, error):
        self.history.append(
            {
                "t": t,
                "reward": reward,
                "R": round(self.R, 3),
                "A": round(self.A, 3),
                "Omega": self.Omega,
                "lambda": self.lam,
                "error": round(error, 3),
            }
        )


def run_simulation(lam, steps=100):
    env = Environment()
    agent = Agent(lam)

    rewards_before = []
    rewards_after = []

    total_adaptation = 0

    previous_A = agent.A

    for t in range(steps):

        env.step(t)

        observation = env.observe()

        action = agent.act()

        reward = env.evaluate(action)

        error = agent.update_representation(
            observation,
            reward
        )

        agent.update_adaptation(error)

        # Recursive capability growth
        agent.recursive_expand()

        total_adaptation += abs(agent.A - previous_A)
        previous_A = agent.A

        if t < env.shift_time:
            rewards_before.append(reward)
        else:
            rewards_after.append(reward)

        agent.measure(
            t,
            reward,
            error
        )

    return {
        "lambda": lam,
        "reward_before_shift":
            round(sum(rewards_before) / len(rewards_before), 3),

        "reward_after_shift":
            round(sum(rewards_after) / len(rewards_after), 3),

        "final_R":
            round(agent.R, 3),

        "final_A":
            round(agent.A, 3),

        "final_Omega":
            agent.Omega,

        "total_adaptation":
            round(total_adaptation, 3),

        "trace":
            agent.history
    }


if __name__ == "__main__":

    print("Constitutional Correction Simulation v0.4")
    print("-----------------------------------------")

    for lam in [1.0, 0.5, 0.0]:

        result = run_simulation(lam)

        summary = {
            key: value
            for key, value in result.items()
            if key != "trace"
        }

        print(summary)
