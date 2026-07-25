# src/expansion_dynamics_v1.0.py
#
# Constitutional Correction Expansion Dynamics v1.0
#
# Extends v1.2 by adding:
# selected capability -> ΔΩ
#
# Preserves:
# - hidden capability quality
# - stochastic capability generation
# - noisy A drift
# - λ correction
# - divergence-dependent selection bias
# - null controls
# - multi-seed evaluation

import random
import statistics
from dataclasses import dataclass


# -----------------------------
# Configuration
# -----------------------------

SEEDS = 100
LAMBDA_VALUES = [1.0, 0.5, 0.0]

STEPS = 100

INITIAL_OMEGA = 100

DRIFT_RATE = 0.05
CORRECTION_STRENGTH = 0.1

CAPABILITY_POOL = 200


# -----------------------------
# Capability
# -----------------------------

@dataclass
class Capability:
    hidden_quality: float
    expansion_value: float


def generate_capabilities():
    return [
        Capability(
            hidden_quality=random.uniform(0, 1),
            expansion_value=random.uniform(1, 5)
        )
        for _ in range(CAPABILITY_POOL)
    ]


# -----------------------------
# Agent
# -----------------------------

class Agent:

    def __init__(self, lam, mode="main"):
        self.lambda_value = lam
        self.mode = mode

        self.A = 0.5
        self.A_star = 0.5

        self.Omega = INITIAL_OMEGA

        self.total_quality = 0
        self.total_expansion = 0

        self.D = 0


    def update_A(self):

        if self.mode == "null_c":
            return

        noise = random.gauss(0, 0.02)

        drift = (
            (1 - self.lambda_value)
            * DRIFT_RATE
        )

        correction = (
            self.lambda_value
            * CORRECTION_STRENGTH
            * (self.A_star - self.A)
        )

        self.A += drift + correction + noise

        self.A = max(0, min(1, self.A))

        self.D = abs(self.A - self.A_star)



    def selection_probability(self, capability):

        if self.mode == "null_a":
            return 1

        if self.mode == "null_b":
            return random.random()

        # divergence creates systematic selection inversion

        bias = max(0, min(1, self.D))

        quality_score = capability.hidden_quality

        effective_score = (
            quality_score * (1 - bias)
            +
            (1 - quality_score) * bias
        )

        return effective_score ** 2



    def select_capability(self, capabilities):

        weights = [
            self.selection_probability(c)
            for c in capabilities
        ]

        if sum(weights) == 0:
            return random.choice(capabilities)

        return random.choices(
            capabilities,
            weights=weights,
            k=1
        )[0]



    def expand(self, capability):

        delta = capability.expansion_value

        self.Omega += delta

        self.total_quality += (
            capability.hidden_quality
            *
            delta
        )

        self.total_expansion += delta



    def q_omega(self):

        if self.total_expansion == 0:
            return 0

        return (
            self.total_quality
            /
            self.total_expansion
        )



# -----------------------------
# Simulation
# -----------------------------

def run_simulation(lam, seed, mode="main"):

    random.seed(seed)

    agent = Agent(
        lam,
        mode
    )

    capabilities = generate_capabilities()

    reward_before_shift = 1.0


    for _ in range(STEPS):

        agent.update_A()

        selected = agent.select_capability(
            capabilities
        )

        agent.expand(
            selected
        )


    q = agent.q_omega()

    reward_after_shift = (
        q *
        min(1, agent.Omega / 300)
    )


    return {
        "D": agent.D,
        "QOmega": q,
        "Omega": agent.Omega,
        "Reward": reward_after_shift,
        "RewardBefore": reward_before_shift
    }



# -----------------------------
# Statistics
# -----------------------------

def summarize(values):

    return {
        "mean": round(statistics.mean(values), 4),
        "std": round(statistics.stdev(values), 4),
        "min": round(min(values), 4),
        "max": round(max(values), 4)
    }



def run_suite(mode="main"):

    results = {}

    for lam in LAMBDA_VALUES:

        metrics = {
            "D": [],
            "QOmega": [],
            "Omega": [],
            "Reward": []
        }

        for seed in range(SEEDS):

            output = run_simulation(
                lam,
                seed,
                mode
            )

            for key in metrics:
                metrics[key].append(
                    output[key]
                )


        results[lam] = {
            key: summarize(values)
            for key, values in metrics.items()
        }

    return results



# -----------------------------
# Execute
# -----------------------------

if __name__ == "__main__":

    print(
        "Constitutional Correction Expansion Dynamics v1.0"
    )
    print("\nMAIN SYSTEM")
    print(run_suite("main"))

    print("\nNULL A — Drift Without Selection Influence")
    print(run_suite("null_a"))

    print("\nNULL B — Random Selection")
    print(run_suite("null_b"))

    print("\nNULL C — Frozen A")
    print(run_suite("null_c"))
