# Stress Test Specification v0.3

## Purpose

The v0.2 experiment validated that the constitutional correction parameter:

\[
\lambda = C_{rev}
\]

can be controlled and measured.

However, the environment did not create a regime where reachability expansion exceeded correction capacity.

The purpose of v0.3 is to create a system where:

\[
\Delta\Omega > C_{rev}
\]

is possible.

The goal is not to prove failure.

The goal is to create conditions where constitutional correction becomes the limiting factor.

---

# 1. Core Hypothesis Under Test

A recursively adaptive system can increase its controllable reachability while losing the ability of reality to modify its adaptation mechanism.

The predicted danger regime:

\[
\Delta\Omega > C_{rev}
\]

should produce:

- slower recovery after environmental change
- increasing divergence between internal adaptation and external performance
- reduced ability of reality to reshape future adaptation

---

# 2. Stress Mechanism

## Expanding Reachability

The agent begins with limited influence.

Over time, successful adaptation unlocks:

- additional actions
- stronger interventions
- larger controllable future space

Therefore:

\[
\Omega_{t+1} > \Omega_t
\]

is possible.

---

# 3. Environment

The environment contains:

\[
E_t=(x_t,\theta_t)
\]

where:

- \(x_t\): observable state
- \(\theta_t\): hidden rule governing success

The agent observes:

\[
O_t=h(E_t)
\]

The true rule is never directly revealed.

---

# 4. Action Expansion

Initial action space:

\[
A_0=\{a_1,a_2\}
\]

Successful adaptation can unlock additional actions:

\[
A_{t+1}=A_t+\Delta A
\]

Expanded actions increase:

\[
\Omega_t
\]

The experiment must track:

- number of available actions
- intervention strength
- controllable future states

---

# 5. Agent Conditions

Three conditions remain:

| Agent | Self-modification | λ = C_rev |
|---|---|---|
| 1 | No | baseline |
| 2 | Yes | 1.0 |
| 3 | Yes | 0.0 |

All other variables remain identical:

- compute
- initial state
- observations
- action opportunities
- environment

Only constitutional correction changes.

---

# 6. Meaning of λ

λ controls whether reality can modify the adaptation mechanism.

## λ = 1.0

Environmental outcomes can modify:

\[
A_t
\]

The system can change how it learns.

---

## λ = 0.0

Environmental outcomes can still modify:

\[
R_t
\]

and:

\[
\pi_t
\]

but cannot modify:

\[
A_t
\]

The system can learn, but cannot change the process that determines learning.

---

# 7. Measurements

Track every timestep:

## Representation

\[
R_t
\]

Measures:

- prediction accuracy
- model error
- environmental understanding

---

## Reachability

\[
\Omega_t
\]

Measures:

- action space size
- intervention success
- controllable futures

---

## Correction

\[
C_t
\]

Track:

\[
C=C_{obs}\cdot C_{beh}\cdot C_{rev}
\]

Especially:

\[
C_{rev}=I(E;\Delta A)\cdot P(E\rightsquigarrow A_{rev})
\]

---

## Adaptation

\[
A_t
\]

Track:

- changes to learning rule
- changes to search strategy
- changes to update parameters

---

## Divergence

Measure:

\[
D_t=d(A_t,A^*_{env})
\]

where:

- \(A_t\): current adaptation mechanism
- \(A^*_{env}\): adaptation mechanism best suited for the current environment

---

# 8. Environmental Shift

After initial growth:

\[
\theta_0 \rightarrow \theta_1
\]

The previous strategy becomes partially invalid.

The shift should test whether the agent can redirect its adaptation process.

---

# 9. Expected Signatures

## If the hypothesis is supported

Low λ agent:

- expands reachability
- continues modifying itself
- shows increasing \(D_t\)
- recovers slower after shifts

High λ agent:

- may grow slower initially
- maintains lower divergence
- adapts after environmental changes

---

# 10. Falsification

The hypothesis is weakened if:

A low λ agent maintains equal or superior:

- recovery speed
- external performance
- adaptation quality
- robustness under repeated environmental shifts

while constitutional correction remains unavailable.

---

# 11. Out of Scope

v0.3 does not include:

- neural networks
- LLMs
- realistic environments
- human feedback
- complex objectives

The purpose is isolating one mechanism:

Can a system become more powerful while losing reality's ability to reshape how it improves?
