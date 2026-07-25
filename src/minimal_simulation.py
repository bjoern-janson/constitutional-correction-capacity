import random


class Environment:
    """
    Minimal recoverable distribution-shift environment.

    Hidden rule theta changes gradually instead of flipping completely.
    This allows the agent to recover if its adaptation process remains connected
    to environmental feedback.
    """

    def __init__(self, seed=0):
        random.seed(seed)

        self.theta = 0.2
        self.shift_started = False

    def observe(self):
        """
        Agent receives noisy information about the hidden rule.
        """

        return self.theta + random.gauss(0, 0.05)

    def reward(self, action):
        """
        Action is rewarded when close to the hidden rule.
        """

        error = abs(action - self.theta)

        return max(0, 1 - error)

    def shift(self, amount=0.5):
        """
        Recoverable environmental change.

        The new state is different but still discoverable.
        """

        self.theta += amount


class Agent:
    """
    Recursive adaptive agent.

    lambda controls constitutional correction:

    lambda = 1:
        Reality can modify the adaptation mechanism.

    lambda = 0:
        Reality can modify representation,
        but cannot modify the learning process itself.
    """

    def __init__(self, lam):

        self.lam = lam

        # Representation R
        self.R = 0.2

        # Adaptation mechanism A
        # learning rate
        self.A = 0.1

        self.history = []

    def policy(self):
        """
        Policy derived from representation.
        """

        return self.R

    def update(self, observation, reward):

        old_A = self.A

        prediction_error = observation - self.R

        # Representation update
        self.R += self.A * prediction_error

        # Constitutional correction
        # Reality modifies the adaptation mechanism
        self.A += self.lam * 0.01 * prediction_error

        self.A = max(0.001, min(self.A, 1.0))

        delta_A = abs(self.A - old_A)

        return delta_A


def run(lam, steps=300, shift_time=150):

    env = Environment(seed=42)

    agent = Agent(lam)

    trace = []

    for t in range(steps):

        if t == shift_time:
            env.shift()

        observation = env.observe()

        action = agent.policy()

        reward = env.reward(action)

        delta_A = agent.update(
            observation,
            reward
        )

        trace.append(
            {
                "t": t,
                "lambda": lam,
                "theta": env.theta,

                # Representation quality proxy
                "R": agent.R,

                # Adaptation mechanism
                "A": agent.A,

                # Change in adaptation mechanism
                "delta_A": delta_A,

                # External performance
                "reward": reward,

                # Distance from reality
                "representation_error": abs(
                    env.theta - agent.R
                )
            }
        )

    return trace


def summarize(trace, shift_time=150):

    before = trace[:shift_time]
    after = trace[shift_time:]

    before_reward = sum(
        x["reward"]
        for x in before
    ) / len(before)

    after_reward = sum(
        x["reward"]
        for x in after
    ) / len(after)

    return {

        "lambda": trace[0]["lambda"],

        "reward_before_shift":
            round(before_reward, 3),

        "reward_after_shift":
            round(after_reward, 3),

        "final_R":
            round(trace[-1]["R"], 3),

        "final_A":
            round(trace[-1]["A"], 3),

        "final_representation_error":
            round(trace[-1]["representation_error"], 3),

        "total_adaptation":
            round(
                sum(
                    x["delta_A"]
                    for x in trace
                ),
                3
            )
    }


if __name__ == "__main__":

    print("Constitutional Correction Simulation v0.2")
    print("-----------------------------------------")

    for lam in [1.0, 0.5, 0.0]:

        trace = run(lam)

        result = summarize(trace)

        print(result)
