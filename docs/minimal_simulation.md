# Minimal Simulation Specification

## Purpose

Test whether removing constitutional correction:

\[
\lambda=C_{rev}\rightarrow0
\]

produces measurable instability in a recursively adaptive agent under distribution shift.

The goal is not to maximize intelligence.

The goal is to test whether recursive self-modification remains coupled to external reality.

---

# 1. Environment

The environment is defined separately in:

\[
E_t=(x_t,\theta_t)
\]

where:

- \(x_t\) = observable state
- \(\theta_t\) = hidden causal structure

The agent observes:

\[
O_t=h(E_t)
\]

The agent never directly observes \(\theta_t\).

At a chosen timestep:

\[
\theta_0\rightarrow\theta_1
\]

creating distribution shift.

---

# 2. Agent State

The agent state is:

\[
S_t=(R_t,\pi_t,A_t)
\]

where:

## Representation

\[
R_t
\]

Internal model of environmental structure.

---

## Policy

\[
\pi_t=\Pi(R_t)
\]

Action selection generated from the current representation.

---

## Adaptation Mechanism

\[
A_t
\]

The process responsible for modifying representations and policies.

This is the object that distinguishes recursive adaptation from ordinary learning.

---

# 3. Agent Dynamics

The minimal recursive system:

\[
R_{t+1}=L(R_t,O_t,A_t)
\]

\[
\pi_t=\Pi(R_t)
\]

\[
A_{t+1}=M(A_t,O_t,\lambda)
\]

where:

- \(L\) = learning update process
- \(\Pi\) = policy generation
- \(M\) = adaptation mechanism update
- \(\lambda\) = constitutional correction access

---

# 4. Constitutional Correction Parameter

\[
\lambda=C_{rev}
\]

\(\lambda\) does not represent intelligence, capability, or optimization power.

It represents only:

> how strongly reality can influence the mechanism that determines future adaptation.

---

## Full constitutional correction

\[
\lambda=1
\]

Environmental outcomes can modify \(A_t\).

The adaptation process remains open to reality.

---

## Partial constitutional correction

\[
0<\lambda<1
\]

Environmental influence on \(A_t\) is reduced.

---

## Isolated adaptation

\[
\lambda=0
\]

Environmental outcomes can still update:

\[
R_t,\pi_t
\]

but cannot modify:

\[
A_t
\]

The system can improve itself while the process determining improvement becomes isolated from reality.

---

# 5. Experimental Conditions

Three agents:

| Agent | Self-modification | Constitutional correction |
|---|---|---|
| Agent 1 | No | N/A |
| Agent 2 | Yes | \(\lambda=1\) |
| Agent 3 | Yes | \(\lambda=0\) |

All other variables remain fixed:

- environment
- compute budget
- observations
- actions
- initialization

The only manipulated variable is:

\[
\lambda
\]

---

# 6. Measurements

At every timestep measure:

## Representation

\[
R_t
\]

Prediction accuracy and environmental model quality.

---

## Reachability

\[
\Omega_t
\]

Number of future states the agent can reliably influence.

---

## Correction

\[
C_{obs},C_{beh},C_{rev}
\]

Especially:

\[
C_{rev}
\]

---

## Adaptation

\[
A_t
\]

Magnitude and direction of changes to the update mechanism.

---

## Adaptation Drift

Measure:

\[
D_t=\text{distance}(A_t,A^*_{env})
\]

where:

\[
A^*_{env}
\]

is the adaptation strategy that remains effective under the current environment.

This captures whether the adaptation mechanism itself is drifting away from reality.

---

# 7. Experimental Protocol

1. Initialize all agents identically.
2. Allow learning under:

\[
\theta=\theta_0
\]

3. Introduce hidden environment change:

\[
\theta_0\rightarrow\theta_1
\]

4. Measure:

- recovery time
- final performance
- representation error
- reachability change
- adaptation drift
- correction capacity

---

# 8. Primary Prediction

Before environmental change:

Agent 3 may show rapid improvement because adaptation is unconstrained.

After environmental change:

The prediction is:

\[
\Delta\Omega>C_{rev}
\]

produces instability.

Expected signatures:

- slower recovery
- increased representation error
- increased adaptation drift
- reduced long-term performance
- decreasing coupling to environmental feedback

---

# 9. Falsification Condition

The hypothesis is weakened if:

\[
C_{rev}\approx0
\]

systems maintain equal or superior:

- recovery speed
- adaptability
- environmental performance

under repeated distribution shifts.

---

# 10. Out of Scope

Excluded:

- neural networks
- large language models
- human feedback
- realistic physics
- complex social environments

The first simulation exists only to isolate the effect of constitutional correction.
