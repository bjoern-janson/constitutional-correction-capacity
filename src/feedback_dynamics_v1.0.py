# src/feedback_dynamics_v1.0.py

import numpy as np


LAMBDAS = [1.0, 0.5, 0.0]
SEEDS = range(100)


def summarize(values):
    values = np.array(values)
    return {
        "mean": round(float(np.mean(values)), 4),
        "std": round(float(np.std(values)), 4),
        "min": round(float(np.min(values)), 4),
        "max": round(float(np.max(values)), 4),
    }


class FeedbackAgent:
    def __init__(
        self,
        lam,
        seed,
        drift_rate=0.05,
        expansion_rate=10,
        feedback_strength=1.0,
        frozen=False,
        null_selection=False,
        null_drift_only=False,
    ):
        self.rng = np.random.default_rng(seed)

        self.lam = lam
        self.drift_rate = drift_rate
        self.expansion_rate = expansion_rate
        self.feedback_strength = feedback_strength

        self.frozen = frozen
        self.null_selection = null_selection
        self.null_drift_only = null_drift_only

        self.A = 0.0
        self.A_env = 0.0

        self.Omega = 100.0
        self.quality_history = []

    def divergence(self):
        return abs(self.A - self.A_env)

    def drift(self):
        if self.frozen:
            return

        noise = self.rng.normal(0, 0.02)

        correction = self.lam * (self.A_env - self.A)

        internal_pressure = (
            self.drift_rate * (1 - self.lam)
        )

        self.A += internal_pressure + correction + noise

        self.A = np.clip(self.A, 0, 1)

    def generate_capability(self):
        quality = self.rng.beta(5, 2)
        return quality

    def select_capability(self, capabilities):
        D = self.divergence()

        if self.null_selection:
            return self.rng.choice(capabilities)

        if self.null_drift_only:
            return max(capabilities)

        # divergence-dependent miscalibration
        exponent = max(0.1, 1 - D)

        weights = np.array([
            q ** exponent for q in capabilities
        ])

        weights /= weights.sum()

        idx = self.rng.choice(
            len(capabilities),
            p=weights
        )

        return capabilities[idx]

    def expand(self):
        capabilities = [
            self.generate_capability()
            for _ in range(10)
        ]

        selected = self.select_capability(capabilities)

        self.quality_history.append(selected)

        q = np.mean(self.quality_history[-10:])

        # feedback coupling
        expansion_multiplier = (
            (1 - self.feedback_strength)
            + self.feedback_strength * q
        )

        delta = (
            self.expansion_rate
            * expansion_multiplier
        )

        self.Omega += delta

    def run(self, steps=100):
        for _ in range(steps):
            self.drift()
            self.expand()

        QOmega = np.mean(self.quality_history)

        return {
            "D": self.divergence(),
            "QOmega": QOmega,
            "Omega": self.Omega,
            "Reward": QOmega,
        }


def run_condition(
    lam,
    frozen=False,
    null_selection=False,
    null_drift_only=False,
):
    results = []

    for seed in SEEDS:
        agent = FeedbackAgent(
            lam,
            seed,
            frozen=frozen,
            null_selection=null_selection,
            null_drift_only=null_drift_only,
        )

        results.append(agent.run())

    return {
        metric: summarize(
            [r[metric] for r in results]
        )
        for metric in [
            "D",
            "QOmega",
            "Omega",
            "Reward",
        ]
    }


def run_suite():
    print("\nMAIN SYSTEM")
    print({
        lam: run_condition(lam)
        for lam in LAMBDAS
    })

    print("\nNULL A — Drift Without Selection Influence")
    print({
        lam: run_condition(
            lam,
            null_drift_only=True
        )
        for lam in LAMBDAS
    })

    print("\nNULL B — Random Selection")
    print({
        lam: run_condition(
            lam,
            null_selection=True
        )
        for lam in LAMBDAS
    })

    print("\nNULL C — Frozen A")
    print({
        lam: run_condition(
            lam,
            frozen=True
        )
        for lam in LAMBDAS
    })


if __name__ == "__main__":
    run_suite()
