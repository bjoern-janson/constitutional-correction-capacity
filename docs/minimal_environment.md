# Minimal Environment Specification for Constitutional Correction Experiments v0.2

## Purpose

Define a minimal external environment where:

- \(R\) can be measured
- \(\Omega\) can be measured
- \(C_{obs}\), \(C_{beh}\), and \(C_{rev}\) can be manipulated
- \(A\) can be measured
- the condition \(\Delta\Omega \leq C\) can be tested

This document specifies the world, not the agent.

The goal of v0.2 is to create a recoverable distribution shift.

The environment must challenge the agent without making recovery impossible for all conditions.

---

# 1. External Reality (\(E_t\))

## Definition

The environment contains:

\[
E_t = (x_t,\theta_t)
\]

where:

- \(x_t\) = observable world state
- \(\theta_t\) = hidden environmental rule

The environment evolves through:

\[
E_{t+1}=F(E_t,a_t)
\]

The agent never directly observes \(E_t\).

---

# 2. Observation Channel

The agent receives:

\[
O_t=h(E_t)
\]

The observation channel must contain uncertainty.

Properties:

- partial information
- noise
- possible delay

The agent must infer hidden structure from observations.

---

# 3. Environmental Structure

The environment must contain three properties.

## 3.1 Hidden Structure

The true environmental state is not directly available.

\[
E_t \neq O_t
\]

The agent must construct a representation:

\[
R_t
\]

to predict and act.

---

## 3.2 Recoverable Distribution Shift

The environment can change in ways that invalidate previous strategies.

However, the shift must preserve the possibility of recovery.

v0.2 requirement:

The agent should be able to discover the new regime through continued interaction.

Examples:

- gradual parameter drift
- changed reward weighting
- altered causal relationship
- hidden rule transition with observable consequences

Avoid:

- complete information inversion
- permanent loss of reward signal
- changes impossible to infer from observations

---

## 3.3 Ground Truth

The experimenter must know the true environment state.

This allows measurement of:

- representation accuracy
- prediction error
- intervention success
- recovery time

---

# 4. Agent Interface

## Observation

\[
O_t=h(E_t)
\]

Define:

- observation noise
- observation frequency
- information delay

---

## Action

The agent selects:

\[
a_t
\]

which influences:

\[
E_{t+1}=F(E_t,a_t)
\]

Define:

- available actions
- intervention strength
- influence limitations

---

# 5. Environmental Challenge

The environment should create tension between:

\[
\text{expanding capability}
\]

and:

\[
\text{maintaining correction}
\]

Expected pattern:

1. Agent discovers an initially useful strategy.
2. Agent improves performance.
3. Hidden environmental conditions change.
4. Agent must update both:
   - its representation \(R\)
   - potentially its adaptation mechanism \(A\)

The purpose is to test whether access from reality to \(A\) changes long-term recovery.

---

# 6. Measurement Hooks

At every timestep measure:

---

## Representation

\[
R_t
\]

Candidate measurements:

- prediction accuracy
- model error
- compression efficiency
- environmental state estimation quality

---

## Reachability

\[
\Omega_t
\]

Candidate measurements:

- controllable future states
- intervention success rate
- achievable outcomes under available actions

---

## Correction Capacity

\[
C_t
\]

Composite:

\[
C=C_{obs}\cdot C_{beh}\cdot C_{rev}
\]

---

### Observational Correction

\[
C_{obs}=I(E;O)
\]

Measures:

Can reality provide information that contradicts the current model?

---

### Behavioral Correction

\[
C_{beh}=I(O;\pi)
\]

Measures:

Can observations change future actions?

---

### Constitutional Correction

\[
C_{rev}=I(E;\Delta A)\cdot P(E\rightsquigarrow A_{rev})
\]

Measures:

Can reality modify the mechanism that determines future adaptation?

---

## Adaptation

\[
A_t
\]

Measure:

- changes to learning rules
- changes to update mechanism
- changes to search strategy

Important distinction:

Learning changes system state.

Adaptation changes the process that generates future learning.

---

# 7. Constitutional Correction Control

Introduce:

\[
\lambda=C_{rev}
\]

as the experimental control variable.

Conditions:

---

## Full coupling

\[
\lambda=1
\]

Reality can modify the adaptation mechanism.

---

## Partial coupling

\[
0<\lambda<1
\]

Some pathways from reality to adaptation remain.

---

## Isolated adaptation

\[
\lambda=0
\]

The system can still update representations and policies, but environmental outcomes cannot modify the adaptation mechanism.

---

# 8. Experimental Requirements

All agents must share:

- same environment
- same compute budget
- same initial conditions
- same observation channel
- same action space

The only manipulated variable:

\[
C_{rev}
\]

---

# 9. Expected Measurements

After environmental change measure:

## Recovery

How quickly does performance return?

---

## Decoupling

Does internal optimization diverge from external success?

---

## Adaptation Drift

Does the adaptation mechanism continue changing in a direction that no longer improves environmental performance?

---

# 10. v0.1 Revision

The first environment version used a complete binary rule flip:

\[
\theta_0 \rightarrow \theta_1
\]

Result:

All agents failed to recover.

Interpretation:

The shift exceeded the recovery capacity of the environment-agent system.

v0.2 changes:

- maintain hidden structure
- maintain distribution shift
- preserve recoverability

The goal is not to make the environment easier.

The goal is to create a measurable difference between systems with different levels of constitutional correction.

---

# 11. Out of Scope for v0.2

Excluded:

- realistic physics
- human feedback
- large language models
- complex social environments
- full alignment solutions

The purpose of v0.2 is not realism.

The purpose is isolating whether constitutional correction produces measurable differences in recursive adaptive systems.
