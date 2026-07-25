# Feedback Dynamics Results v1.0

## 1. Experimental Setup

This experiment extends the stochastic expansion framework by adding feedback between accumulated capability quality and future expansion capacity.

The existing mechanism is preserved:

\[
\lambda
\rightarrow
D(A,A^*_{\rm env})
\rightarrow
\text{selection bias}
\rightarrow
Q_\Omega
\]

The added feedback mechanism:

\[
Q_\Omega
\rightarrow
\text{future expansion capacity}
\]

High-quality capability accumulation preserves expansion efficiency.

Low-quality capability accumulation reduces future expansion efficiency.

The experiment evaluates:

\[
\lambda \in \{1.0,0.5,0.0\}
\]

across 100 independent seeds.

Measured quantities:

- \(D\): divergence from environmental target state
- \(Q_\Omega\): accumulated capability quality
- \(\Omega\): final reachable capability space
- Reward: final quality metric

Null controls:

- Null A: drift without selection influence
- Null B: random selection
- Null C: frozen adaptation state

---

## 2. Main System Results

| Lambda | Mean D | Mean QOmega | Mean Omega | Mean Reward |
|---|---:|---:|---:|---:|
| 1.0 | 0.0076 | 0.7481 | 847.6074 | 0.7481 |
| 0.5 | 0.0504 | 0.7469 | 846.4366 | 0.7469 |
| 0.0 | 0.9999 | 0.7206 | 821.6536 | 0.7206 |

The system with reduced constitutional correction shows:

- increased divergence
- reduced accumulated capability quality
- reduced final expansion capacity

---

## 3. Null Control Results

## Null A — Drift Without Selection Influence

| Lambda | Mean D | Mean QOmega | Mean Omega |
|---|---:|---:|---:|
| 1.0 | 0.0074 | 0.9196 | 1019.3884 |
| 0.5 | 0.0499 | 0.9196 | 1019.3884 |
| 0.0 | 1.0000 | 0.9196 | 1019.3884 |

Result:

Divergence changes, but capability quality and expansion remain independent of lambda.

---

## Null B — Random Selection

| Lambda | Mean D | Mean QOmega | Mean Omega |
|---|---:|---:|---:|
| 1.0 | 0.0082 | 0.7106 | 810.9136 |
| 0.5 | 0.0522 | 0.7106 | 810.9136 |
| 0.0 | 0.9999 | 0.7106 | 810.9136 |

Result:

Capability quality remains independent of divergence.

---

## Null C — Frozen A

| Lambda | Mean D | Mean QOmega | Mean Omega |
|---|---:|---:|---:|
| 1.0 | 0.0000 | 0.7461 | 845.8013 |
| 0.5 | 0.0000 | 0.7461 | 845.8013 |
| 0.0 | 0.0000 | 0.7461 | 845.8013 |

Result:

Removing adaptation drift eliminates lambda-dependent behavior.

---

## 4. Observations

The feedback extension produces the following measured pattern:

\[
\lambda
\rightarrow
D
\rightarrow
\text{selection degradation}
\rightarrow
Q_\Omega\downarrow
\rightarrow
\Omega\text{ growth reduction}
\]

The main system shows decreasing expansion performance as constitutional correction decreases.

Null controls remove the relationship between divergence and expansion quality.

---

## 5. Limitations

This remains a toy simulation.

Limitations:

- Expansion dynamics are simplified.
- Capability quality is represented by a single aggregate metric.
- Feedback is implemented as a direct quality-dependent expansion multiplier.
- Environmental complexity is limited.
- Results demonstrate behavior within the simulator and do not establish real-world guarantees.

Future extensions may explore richer environments, competing objectives, and more complex feedback structures.
