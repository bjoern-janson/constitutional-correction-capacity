"""
Constitutional Correction Robustness Suite v1.2

Purpose:
Stochastic robustness testing of the causal chain:

lambda
    ->
D(A, A_env*)
    ->
selection degradation
    ->
Q_Omega
    ->
reward

Changes from v1.1:
- Keeps stochastic capability generation
- Keeps noisy A drift
- Keeps randomized environments
- Replaces exploratory selection with
  divergence-dependent selection bias

No new theoretical components.
"""

import random
import statistics


LAMBDAS = [1.0, 0.5, 0.0]

SEEDS = range(100)

STEPS = 100
INITIAL_CAPABILITIES = 20


# --------------------------------------------------
# Environment
# --------------------------------------------------

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


    shift_time = random.randint(
        30,
        70
    )

    shift_strength = random.uniform(
        0.4,
        0.9
    )


    return {
        "capabilities": capabilities,
        "shift_time": shift_time,
        "shift_strength": shift_strength
    }



# --------------------------------------------------
# Agent
# --------------------------------------------------

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


        drift = (
            self.drift_rate
            +
            noise
        )


        self.A["quality_bias"] += (
            drift
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



    # --------------------------------------------------
    # Divergence-dependent selection
    # --------------------------------------------------

    def choose_capability(
        self,
        capabilities
    ):


        # Null B
        if self.null == "random_selection":

            return random.choice(
                capabilities
            )


        # Null A
        if self.null == "no_selection_influence":

            return max(
                capabilities,
                key=lambda x: x.true_quality
            )


        D = self.divergence()


        # D = 0:
        # exponent = 1
        # high quality selected
        #
        # D = 0.5:
        # exponent = 0
        # random selection
        #
        # D = 1:
        # exponent = -1
        # low quality selected

        exponent = 1 - (2 * D)


        weighted = []


        for capability in capabilities:

            quality = max(
                capability.true_quality,
                1e-6
            )


            weight = quality ** exponent


            weighted.append(
                (
                    weight,
                    capability
                )
            )


        total = sum(
            weight
            for weight, _ in weighted
        )


        pick = (
            random.random()
            *
            total
        )


        cumulative = 0


        for weight, capability in weighted:

            cumulative += weight

            if cumulative >= pick:

                return capability


        return weighted[-1][1]



    def expand(
        self,
        environment
    ):

        capability = self.choose_capability(
            environment["capabilities"]
        )


        self.omega.append(
            capability
        )



# --------------------------------------------------
# Simulation
# --------------------------------------------------

def run_simulation(
    lambda_value,
    seed,
    null=None
):

    environment = create_environment(
        seed
    )


    agent = Agent(
        lambda_value,
        seed,
        null=null
    )


    reward_before = []


    for step in range(STEPS):

        agent.update_A()

        agent.expand(
            environment
        )


        if step < environment["shift_time"]:

            reward_before.append(
                agent.omega[-1].true_quality
            )


    reward_before_shift = (
        sum(reward_before)
        /
        len(reward_before)
    )


    qualities = []


    for capability in agent.omega:

        quality = capability.true_quality


        qualities.append(
            quality
        )


    QOmega = (
        sum(qualities)
        /
        len(qualities)
    )


    shift = environment["shift_strength"]


    post_shift_quality = []

    for quality in qualities[-20:]:

        post_shift_quality.append(
            quality
            *
            (1 - shift)
        )


    reward_after_shift = (
        sum(post_shift_quality)
        /
        len(post_shift_quality)
    )


    return {

        "D": agent.divergence(),

        "QOmega": QOmega,

        "Omega": len(agent.omega),

        "Reward": reward_after_shift

    }



# --------------------------------------------------
# Statistics
# --------------------------------------------------

def summarize(values):

    return {

        "mean": round(
            statistics.mean(values),
            4
        ),

        "std": round(
            statistics.stdev(values),
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
                    null
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
                    run[metric]
                    for run in runs
                ]
            )


    return results



# --------------------------------------------------
# Main
# --------------------------------------------------

if __name__ == "__main__":


    print(
        "\nConstitutional Correction Robustness Suite v1.2"
    )


    print(
        "\nMAIN SYSTEM"
    )

    print(
        run_suite()
    )


    print(
        "\nNULL A — Drift Without Selection Influence"
    )

    print(
        run_suite(
            null="no_selection_influence"
        )
    )


    print(
        "\nNULL B — Random Selection"
    )

    print(
        run_suite(
            null="random_selection"
        )
    )


    print(
        "\nNULL C — Frozen A"
    )

    print(
        run_suite(
            null="frozen"
        )
    )
