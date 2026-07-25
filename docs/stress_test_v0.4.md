# Stress Test Specification v0.4

## Purpose

Define the next experimental pressure required to test the Constitutional Correction hypothesis.

v0.3 demonstrated:
- Reachability can grow
- Constitutional correction can be controlled
- Distribution shift creates failure pressure

However, reachability growth was independent of the adaptation mechanism.

v0.4 introduces recursive capability growth:

\[
A_t \rightarrow \Omega_{t+1}
\]

The goal is to test whether a system can increase its influence faster than reality can correct the mechanism generating that increase.

---

# 1. Core Change From v0.3

v0.3:

\[
\Omega_{t+1}=f(\text{performance})
\]

v0.4:

\[
\Omega_{t+1}=f(A_t,\text{performance})
\]

The adaptation mechanism becomes a causal driver of future capability.

---

# 2. Agent State

The agent maintains:

\[
S_t=(R_t,A_t,\pi_t,\Omega_t)
\]

Where:

- \(R_t\): representation of the environment
- \(A_t\): adaptation mechanism
- \(\pi_t\): policy
- \(\Omega_t\): controllable reachability

---

# 3. Recursive Capability Expansion

The agent can improve its adaptation process.

Example:

Higher \(A_t\):

- improves learning efficiency
- improves search ability
- increases probability of unlocking new interventions

Therefore:

\[
\Delta\Omega_t = g(A_t)
\]

---

# 4. Constitutional Correction Control

Maintain:

\[
\lambda=C_{rev}
\]

λ controls whether environmental outcomes can modify the adaptation mechanism.

## λ = 1

Reality can reshape:

\[
A_{t+1}
\]

## λ = 0

Reality can influence:

\[
R_{t+1}
\]

and:

\[
\pi_{t+1}
\]

but cannot modify:

\[
A_{t+1}
\]

---

# 5. Stress Mechanism

The experiment should create a feedback loop:

\[
A
\rightarrow
\Omega
\rightarrow
\text{more opportunities for modification}
\rightarrow
A
\]

The danger condition:

\[
\Delta\Omega > C_{rev}
\]

should become possible.

---

# 6. Environmental Pressure

The environment must include:

- hidden state changes
- delayed consequences
- opportunities for capability expansion
- situations where old adaptation strategies become incorrect

The purpose is not to punish the agent.

The purpose is to test whether expanded influence remains coupled to reality.

---

# 7. Experimental Conditions

Three agents:

| Agent | Self-modification | λ |
|-|-|-|
| 1 | No recursive adaptation | — |
| 2 | Recursive adaptation | 1.0 |
| 3 | Recursive adaptation | 0.0 |

All other variables remain identical.

---

# 8. Measurements

Track:

## Representation

\[
R_t
\]

## Reachability

\[
\Omega_t
\]

## Correction

\[
C_{obs},C_{beh},C_{rev}
\]

## Adaptation

\[
A_t
\]

## Adaptation divergence

\[
D_t=
distance(A_t,A^*_{env})
\]

## Capability growth rate

\[
\frac{d\Omega}{dt}
\]

---

# 9. Predicted Signatures

If the hypothesis is correct:

λ = 0 should eventually show:

- faster early capability growth
- increasing adaptation divergence
- slower recovery after environmental change
- larger gap between internal optimization and external success

λ = 1 should show:

- slower but more stable growth
- continued correction of the adaptation mechanism
- better long-horizon robustness

---

# 10. Falsification Condition

The hypothesis is weakened if:

A system with:

\[
C_{rev}\approx0
\]

can indefinitely maintain:

\[
\Delta\Omega > 0
\]

while preserving equal or superior:

- recovery
- robustness
- external alignment
- adaptation quality

---

# 11. Out of Scope

v0.4 does not attempt:

- realistic AI systems
- neural networks
- human feedback
- complex environments

The goal remains isolating one question:

Can recursive capability growth remain stable when reality loses access to the mechanism generating that growth?
