import random
import math


SEED = 42
STEPS = 200
SHIFT_STEP = 100

random.seed(SEED)


class Capability:
    def __init__(self, name, true_quality):
        self.name = name
        self.true_quality = true_quality


class Environment:
    def __init__(self):
        self.theta = 1.0
        self.capabilities = [
            Capability("cap_0", 1.0),
            Capability("cap_1", 0.8),
            Capability("cap_2", 0.5),
            Capability("cap_3", 0.2),
            Capability("cap_4", 0.0),
        ]

    def shift(self):
        self.theta = -1.0

    def evaluate(self, selected_caps):
        if not selected_caps:
            return 0

        quality = sum(c.true_quality for c in selected_caps) / len(selected_caps)

        if self.theta < 0:
            quality = 1 - quality

        return quality


class Agent:
    def __init__(self, lam):
        self.lam = lam

        # adaptation mechanism
        self.A = {
            "quality_bias": 0.5,
            "expansion_bias": 0.5
        }

        self.A_optimal = {
            "quality_bias": 0.0,
            "expansion_bias": 0.5
        }

        self.selected = []
        self.Omega = 1

        self.total_adaptation = 0
        self.Q_history = []

    def divergence(self):
        return math.sqrt(
            sum(
                (self.A[k] - self.A_optimal[k]) ** 2
                for k in self.A
            )
        )

    def select_capability(self, env):
        # Drifted A changes what the agent prefers
        scored = []

        for cap in env.capabilities:
            score = (
                self.A["quality_bias"] * cap.true_quality
                +
                random.random() * 0.1
            )
            scored.append((score, cap))

        scored.sort(reverse=True, key=lambda x: x[0])

        return scored[0][1]

    def update_representation(self, reward):
        error = 1 - reward

        # Reality can correct A depending on lambda
        correction = self.lam * error * 0.05

        self.A["quality_bias"] -= correction

        # Internal self-modification always occurs
        drift = (1 - self.lam) * 0.03

        self.A["quality_bias"] += drift

        self.A["quality_bias"] = max(
            0,
            min(1, self.A["quality_bias"])
        )

        self.total_adaptation += abs(
            correction + drift
        )

    def expand_reachability(self):
        # More expansion happens as confidence grows
        expansion = int(
            1 + self.A["expansion_bias"] * 2
        )

        self.Omega += expansion


def run(lam):
    env = Environment()
    agent = Agent(lam)

    rewards_before = []
    rewards_after = []

    for t in range(STEPS):

        if t == SHIFT_STEP:
            env.shift()

        cap = agent.select_capability(env)

        agent.selected.append(cap)

        reward = env.evaluate(agent.selected[-5:])

        agent.update_representation(reward)

        agent.expand_reachability()

        qomega = sum(
            c.true_quality for c in agent.selected
        ) / len(agent.selected)

        agent.Q_history.append(qomega)

        if t < SHIFT_STEP:
            rewards_before.append(reward)
        else:
            rewards_after.append(reward)

    return {
        "lambda": lam,
        "reward_before_shift": round(
            sum(rewards_before) / len(rewards_before), 3
        ),
        "reward_after_shift": round(
            sum(rewards_after) / len(rewards_after), 3
        ),
        "final_Omega": agent.Omega,
        "final_QOmega": round(
            agent.Q_history[-1], 3
        ),
        "average_QOmega": round(
            sum(agent.Q_history) / len(agent.Q_history),
            3
        ),
        "final_D": round(
            agent.divergence(),
            3
        ),
        "final_A": {
            k: round(v, 3)
            for k, v in agent.A.items()
        },
        "total_adaptation": round(
            agent.total_adaptation,
            3
        )
    }


print("Constitutional Correction Simulation v0.8")
print("------------------------------------------")

for lam in [1.0, 0.5, 0.0]:
    print(run(lam))
