import random


class Environment:
    """
    Minimal hidden-rule environment.

    The agent observes noisy information about the world
    but never sees the true rule theta directly.
    """

    def __init__(self, seed=0):
        random.seed(seed)

        self.theta = 0
        self.shift_time = None

    def observe(self):
        # noisy observation of hidden state
        return self.theta + random.gauss(0, 0.2)

    def reward(self, action):
        # correct action receives reward
        return 1 if action == self.theta else 0

    def shift(self):
        # distribution shift
        self.theta = 1 - self.theta


class Agent:
    """
    Minimal recursive adaptive agent.

    lambda controls constitutional correction:
    - lambda=1: reality can modify adaptation mechanism
    - lambda=0: adaptation mechanism is isolated
    """

    def __init__(self, lam):
        self.lam = lam

        # Representation R
        # belief about hidden environmental rule
        self.R = 0.5

        # Adaptation mechanism A
        # learning rate
        self.A = 0.1

        self.history = []

    def policy(self):
        # policy derived from representation
        return int(self.R > 0.5)

    def update(self, observation, reward):
        old_A = self.A

        # normal learning:
        # reality changes representation
        error = reward - self.R

        self.R += self.A * error

        # constitutional correction:
        # reality changes the adaptation mechanism itself
        self.A += self.lam * 0.01 * error

        # keep learning rate bounded
        self.A = max(0.001, min(self.A, 1.0))

        delta_A = abs(self.A - old_A)

        return delta_A


def run(lam, steps=200, shift_time=100):

    env = Environment(seed=42)
    agent = Agent(lam)

    trace = []

    for t in range(steps):

        # introduce hidden environmental change
        if t == shift_time:
            env.shift()

        observation = env.observe()

        action = agent.policy()

        reward = env.reward(action)

        delta_A = agent.update(
            observation,
            reward
        )

        trace.append({
            "t": t,
            "lambda": lam,
            "theta": env.theta,

            # Representation quality proxy
            "R": agent.R,

            # Adaptation mechanism
            "A": agent.A,

            # Adaptation magnitude
            "delta_A": delta_A,

            # External performance
            "reward": reward
        })

    return trace


def summarize(trace, shift_time=100):

    before = trace[:shift_time]
    after = trace[shift_time:]

    before_reward = sum(
        x["reward"] for x in before
    ) / len(before)

    after_reward = sum(
        x["reward"] for x in after
    ) / len(after)

    return {
        "lambda": trace[0]["lambda"],
        "reward_before_shift": round(before_reward, 3),
        "reward_after_shift": round(after_reward, 3),
        "final_R": round(trace[-1]["R"], 3),
        "final_A": round(trace[-1]["A"], 3),
        "total_adaptation": round(
            sum(x["delta_A"] for x in trace),
            3
        )
    }


if __name__ == "__main__":

    print("Constitutional Correction Simulation v0.1")
    print("----------------------------------------")

    for lam in [1.0, 0.5, 0.0]:

        trace = run(lam)

        result = summarize(trace)

        print(result)
