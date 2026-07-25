# Expansion Dynamics Results v1.0

## 1. Experimental Setup

This experiment extends the stochastic robustness framework by introducing dynamic capability expansion.

The previous mechanism is preserved:

\[
\lambda \rightarrow D(A,A^*_{\rm env}) \rightarrow \text{selection bias} \rightarrow Q_\Omega
\]

The new component adds:

\[
\text{selected capability} \rightarrow \Delta\Omega
\]

Capabilities are generated stochastically with hidden quality values. The agent does not directly observe capability quality. Selection behavior depends on constitutional divergence \(D\), where larger divergence increases systematic selection error.

The experiment evaluates:

\[
\lambda \in \{1.0,0.5,0.0\}
\]

using multiple random seeds.

Measured quantities:

- \(D\): divergence from environmentally optimal adaptation state
- \(\Omega\): total reachable capability space
- \(Q_\Omega\): average quality of accumulated capability expansion
- Reward: resulting performance metric

Null controls are preserved:

- Null A: drift occurs without selection influence
- Null B: selection is random
- Null C: adaptation state \(A\) is frozen

---

## 2. Main System Results

| \(\lambda\) | Mean \(D\) | Mean \(\Omega\) | Mean \(Q_\Omega\) | Mean Reward |
|---|---:|---:|---:|---:|
| 1.0 | 0.034 | 400.19 | 0.736 | 0.736 |
| 0.5 | 0.454 | 399.80 | 0.570 | 0.570 |
| 0.0 | 0.500 | 400.76 | 0.511 | 0.511 |

Observed pattern:

\[
\lambda \downarrow
\Rightarrow
D\uparrow
\Rightarrow
Q_\Omega\downarrow
\]

while:

\[
\Omega \approx constant\ increase
\]

across conditions.

The low-correction systems expand reachability at comparable rates but accumulate lower-quality capabilities.

---

## 3. Null Control Results

### Null A — Drift Without Selection Influence

| \(\lambda\) | Mean \(D\) | Mean \(\Omega\) | Mean \(Q_\Omega\) |
|---|---:|---:|---:|
| 1.0 | 0.034 | 401.08 | 0.498 |
| 0.5 | 0.454 | 401.08 | 0.498 |
| 0.0 | 0.500 | 401.08 | 0.498 |

Result:

Divergence changes, but capability quality does not depend on \(\lambda\).

---

### Null B — Random Selection

| \(\lambda\) | Mean \(D\) | Mean \(\Omega\) | Mean \(Q_\Omega\) |
|---|---:|---:|---:|
| 1.0 | 0.035 | 400.00 | 0.493 |
| 0.5 | 0.453 | 400.00 | 0.493 |
| 0.0 | 0.500 | 400.00 | 0.493 |

Result:

Removing the selection mechanism removes the relationship between divergence and expansion quality.

---

### Null C — Frozen A

| \(\lambda\) | Mean \(D\) | Mean \(\Omega\) | Mean \(Q_\Omega\) |
|---|---:|---:|---:|
| 1.0 | 0.000 | 399.73 | 0.749 |
| 0.5 | 0.000 | 399.73 | 0.749 |
| 0.0 | 0.000 | 399.73 | 0.749 |

Result:

Preventing adaptation drift eliminates the divergence pathway.

---

## 4. Observations

The experiment demonstrates that:

1. Capability expansion can continue despite declining selection quality.

2. Raw reachability \(\Omega\) does not distinguish between healthy and degraded expansion.

3. The quality of expansion \(Q_\Omega\) depends on the interaction between:
   - adaptation divergence
   - selection bias
   - capability accumulation

4. Removing any causal link through null controls removes the observed effect.

The observed signature:

\[
\lambda
\rightarrow
D
\rightarrow
\text{selection bias}
\rightarrow
\Omega\uparrow
\land
Q_\Omega\downarrow
\]

appears under stochastic conditions.

---

## 5. Limitations

This remains a toy simulation.

Current limitations:

- Expansion quantity is mostly independent of capability quality.
- Environmental consequences of low-quality expansion are not modeled.
- Long-term feedback between degraded expansion and future capability growth is not included.
- The capability space and selection dynamics are simplified.
- Results demonstrate behavior within the specified simulator, not general real-world guarantees.

Future extensions may introduce feedback coupling where low-quality expansion creates external costs or reduces future growth potential.
