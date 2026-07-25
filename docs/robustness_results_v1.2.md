# Constitutional Correction Robustness Results v1.2

## 1. Experimental Setup

- Purpose
- Preserved causal chain
- Stochastic additions:
  - hidden capability quality sampling
  - drift noise
  - randomized environments
  - multi-seed evaluation

Conditions:
- λ ∈ {1.0, 0.5, 0.0}
- Main system
- Null A
- Null B
- Null C

---

## 2. Main System Results

| λ | D mean | D std | QΩ mean | QΩ std | Reward mean | Reward std |
|---|---|---|---|---|---|---|

Observations:
- D increases as λ decreases
- QΩ decreases as D increases
- Reward follows QΩ degradation

---

## 3. Null Control Results

### Null A — Drift Without Selection Influence

Table.

Observation:
- Divergence changes but selection quality does not.

### Null B — Random Selection

Table.

Observation:
- Selection quality is independent of λ.

### Null C — Frozen A

Table.

Observation:
- Divergence pathway is removed.

---

## 4. Observations

- The stochastic selection pathway reproduces the predicted direction.
- The result depends on the coupling between A divergence and capability selection.
- Removing either drift or selection dependence eliminates the effect.

---

## 5. Limitations

- Toy environment only.
- Ω remains fixed.
- Does not test dynamic capability expansion.
- Does not establish behavior outside the simulated assumptions.
- Further work required for stochastic expansion dynamics.
