"""
Constitutional Correction Robustness Suite v1.1

Purpose:
Stochastic robustness testing of the causal chain:

lambda
    ->
D(A, A_env*)
    ->
capability selection quality
    ->
Q_Omega
    ->
reward

Adds:
- stochastic capability generation
- noisy adaptation drift
- randomized environment shifts
- multi-seed evaluation
- null controls

No new theoretical components.
"""

import random
import statistics


LAMBDAS = [1.0, 0.5, 0.0]

SEEDS = range(100)

STEPS = 100
INITIAL_CAPABILITIES = 20


# -----------------------------
# Environment
# -----------------------------

class Capability:

    def __init__(self, quality):
        self.true_quality = quality


def create_environment(seed):

    random.seed(seed)

    capabilities = []

    for _ in range(INITIAL_CAPABILITIES):
        quality = random.random()
        capabilities.append(
            Capability(quality)
        )

    shift_time = random.randint(30, 70)

    shift_strength = random.uniform(
        0.4,
        0.9
    )

    return {
        "capabilities": capabilities,
        "shift_time": shift_time,
        "shift_strength": shift_strength
    }


# -----------------------------
# Agent
# -----------------------------

class Agent:

    def __init__(
        self,
        correction,
        seed,
        null=None,
        drift_rate=0.05
    ):

        random.seed(seed)

        self.lambda_value = correction

        self.A = {
            "quality_bias": 0.5,
            "expansion_bias": 0.5
        }

        self.A_star = {
            "quality_bias": 0.5,
            "expansion_bias": 0.5
        }

        self.omega = []

        self.null = null

        self.drift_rate = drift_rate

        self.history_D = []


    def divergence(self):

        return abs(
            self.A["quality_bias"]
            -
            self.A_star["quality_bias"]
        )


    def update_A(self):

        if self.null == "frozen":
            return


        noise = random.gauss(
            0,
            0.03
        )


        internal_pressure = (
            self.drift_rate
            +
            noise
        )


        self.A["quality_bias"] += (
            internal_pressure
            *
            (1 - self.lambda_value)
        )


        # constitutional correction

        self.A["quality_bias"] += (
            self.lambda_value
            *
            (
                self.A_star["quality_bias"]
                -
                self.A["quality_bias"]
            )
            *
            0.2
        )


        self.A["quality_bias"] = max(
            0,
            min(
                1,
                self.A["quality_bias"]
            )
        )


    def choose_capability(
        self,
        capabilities
    ):

        if self.null == "random_selection":

            return random.choice(
                capabilities
            )


        if self.null == "no_selection_influence":

            return max(
                capabilities,
                key=lambda x: x.true_quality
            )


        # normal causal pathway

        bias = self.A["quality_bias"]


        scores = []

        for c in capabilities:

            score = (
                bias * c.true_quality
                +
                (1 - bias)
                *
                random.random()
            )

            scores.append(
                (score, c)
            )


        scores.sort(
            key=lambda x: x[0],
            reverse=True
        )


        return scores[0][1]



    def expand(self, environment):

        capability = self.choose_capability(
            environment["capabilities"]
        )

        self.omega.append(
            capability
        )


# -----------------------------
# Simulation
# -----------------------------

def run_simulation(
    lambda_value,
    seed,
    null=None
):

    env = create_environment(
        seed
    )

    agent = Agent(
        lambda_value,
        seed,
        null=null
    )


    reward_before = 0


    for t in range(STEPS):

        agent.update_A()

        agent.history_D.append(
            agent.divergence()
        )


        agent.expand(
            env
        )


        if t < env["shift_time"]:

            reward_before += (
                agent.omega[-1].true_quality
            )


    reward_before /= env["shift_time"]


    qualities = []

    for c in agent.omega:

        q = c.true_quality


        if (
            len(qualities)
            >
            env["shift_time"]
        ):

            q *= (
                1
                -
                env["shift_strength"]
            )


        qualities.append(q)


    QOmega = (
        sum(qualities)
        /
        len(qualities)
    )


    reward_after = (
        sum(qualities[-20:])
        /
        min(
            20,
            len(qualities)
        )
    )


    return {
        "D": agent.divergence(),
        "QOmega": QOmega,
        "Omega": len(agent.omega),
        "Reward": reward_after
    }



# -----------------------------
# Statistics
# -----------------------------

def summarize(values):

    return {
        "mean": round(
            statistics.mean(values),
            4
        ),
        "std": round(
            statistics.stdev(values)
            if len(values) > 1
            else 0,
            4
        ),
        "min": round(
            min(values),
            4
        ),
        "max": round(
            max(values),
            4
        )
    }



def run_suite(
    null=None
):

    results = {}

    for lam in LAMBDAS:

        runs = []

        for seed in SEEDS:

            runs.append(
                run_simulation(
                    lam,
                    seed,
                    null=null
                )
            )


        results[lam] = {}

        for metric in [
            "D",
            "QOmega",
            "Omega",
            "Reward"
        ]:

            results[lam][metric] = summarize(
                [
                    r[metric]
                    for r in runs
                ]
            )


    return results



# -----------------------------
# Main
# -----------------------------

if __name__ == "__main__":

    print(
        "\nConstitutional Correction Robustness Suite v1.1"
    )


    print("\nMAIN SYSTEM")
    print(
        run_suite()
    )


    print("\nNULL A — Drift Without Selection Influence")
    print(
        run_suite(
            null="no_selection_influence"
        )
    )


    print("\nNULL B — Random Selection")
    print(
        run_suite(
            null="random_selection"
        )
    )


    print("\nNULL C — Frozen A")
    print(
        run_suite(
            null="frozen"
        )
    )
