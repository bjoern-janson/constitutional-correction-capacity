# Stress Test v0.9 — Adaptation Drift Causing Selection Error

## Purpose

Modify the v0.8 experiment so that divergence of the adaptation mechanism directly affects capability selection quality.

The goal is not to make low constitutional correction perform worse by definition.

The goal is to test whether:

\[
D(A,A^*_{\rm env}) \uparrow
\]

can naturally produce:

\[
Q_\Omega \downarrow
\]

when the system loses the ability for reality to correct its adaptation mechanism.

---

# 1. Preserve Existing System

Keep unchanged:

- hidden environment
- distribution shift
- mutable adaptation mechanism \(A\)
- constitutional correction parameter:

\[
\lambda=C_{\rm rev}
\]

- reachability growth:

\[
A_t \rightarrow \Omega_{t+1}
\]

- divergence metric:

\[
D_t=\text{distance}(A_t,A^*_{\rm env})
\]

---

# 2. New Causal Requirement

Capability selection must depend on adaptation alignment.

Current:

\[
A \rightarrow \text{selection}
\]

Required:

\[
A \rightarrow D(A,A^*_{\rm env})
\rightarrow
\text{selection bias}
\rightarrow
Q_\Omega
\]

---

# 3. Capability Model

Each possible expansion has:

- hidden true quality \(q_i\)
- accessibility cost
- effect on reachability

The experimenter knows:

\[
q_i
\]

The agent does not.

---

# 4. Selection Rule

The probability of selecting a capability should depend on adaptation divergence.

When:

\[
D \approx 0
\]

the agent should prefer:

\[
q_i \rightarrow \text{high quality}
\]

When:

\[
D \uparrow
\]

selection should become increasingly biased toward:

\[
q_i \rightarrow \text{low quality}
\]

Example:

\[
P(select_i)
=
f(q_i,D)
\]

where increasing \(D\) reduces the influence of true environmental quality.

---

# 5. Experimental Conditions

Three identical agents:

| Agent | λ |
|---|---|
| High correction | 1.0 |
| Partial correction | 0.5 |
| No correction | 0.0 |

Same:

- initial state
- compute budget
- observation channel
- environment seed

Only difference:

\[
C_{\rm rev}
\]

---

# 6. Required Measurements

Every timestep record:

## Adaptation

\[
A_t
\]

## Divergence

\[
D_t
\]

## Reachability

\[
\Omega_t
\]

## Capability quality

\[
Q_\Omega
\]

## External performance

- reward before shift
- reward after shift
- recovery time

---

# 7. Target Signature

Supportive result:

| λ | D | Ω | QΩ |
|-|-|-|-|
| 1.0 | low | growing | high |
| 0.5 | medium | growing | medium |
| 0.0 | high | growing | low |

The key relationship:

\[
\Omega\uparrow
\land
D\uparrow
\land
Q_\Omega\downarrow
\]

---

# 8. Falsification Condition

The hypothesis is weakened if:

\[
D\uparrow
\]

does not produce measurable deterioration in capability selection quality.

A low-correction system that becomes highly divergent but continues selecting equally useful expansions would indicate the proposed coupling is incomplete.

---

# 9. Out of Scope

Do not add:

- neural networks
- complex optimizers
- realistic environments
- human feedback
- additional theoretical variables

The only change from v0.8 is:

\[
D(A,A^*_{\rm env})
\rightarrow
\text{selection quality}
\]

---

# Success Criterion

A successful v0.9 implementation demonstrates:

1. Reality can still steer \(A\) when \(\lambda\) is high.
2. \(A\) can drift when \(\lambda\) is low.
3. Drift changes capability selection quality.
4. Increasing reachability can expose the cost of losing constitutional correction.
