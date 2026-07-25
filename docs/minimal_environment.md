# Minimal Environment Specification for Constitutional Correction Experiments

## Purpose

Define a minimal external environment where:

- R can be measured
- Ω can be measured
- C_obs, C_beh, and C_rev can be manipulated
- A can be measured
- the condition ΔΩ ≤ C can be tested

This document specifies the world, not the agent.

---

# 1. External Reality (E_t)

## Definition

Describe the environment state:

\[
E_t
\]

The environment evolves independently of the agent except through interventions:

\[
E_{t+1}=F(E_t,a_t)
\]

The agent never directly observes \(E_t\).

---

## Required properties

The environment must contain:

### Hidden structure

The true state cannot be perfectly observed.

\[
O_t=h(E_t)
\]

### Distribution shift

The environment can change in ways that invalidate previous strategies.

Examples:
- changing reward landscape
- changing causal relationships
- hidden parameter drift

### Ground truth

The experimenter must know the real state so measurements are possible.

---

# 2. Agent Interface

## Observation channel

\[
O_t=h(E_t)
\]

Define:

- observation noise
- information delay
- missing variables


## Action channel

\[
a_t \rightarrow E_{t+1}
\]

Define:

- available interventions
- intervention strength
- limits on influence

---

# 3. Environmental Challenge

The environment should create a pressure between:

\[
\text{increasing capability}
\]

and

\[
\text{maintaining correction}
\]

Example:

A changing fitness landscape:

- early strategy becomes successful
- agent expands reachable influence
- environment changes
- only systems retaining correction pathways recover

---

# 4. Measurement Hooks

At every timestep:

## Representation

\[
R_t
\]

Measure:

- prediction quality
- model compression
- environmental understanding


## Reachability

\[
\Omega_t
\]

Measure:

- controllable future states
- intervention success


## Correction

\[
C_t
\]

Measure:

\[
C=C_{obs}\cdot C_{beh}\cdot C_{rev}
\]

Where:

\[
C_{obs}=I(E;O)
\]

\[
C_{beh}=I(O;\pi)
\]

\[
C_{rev}=I(E;\Delta A)\cdot P(E\rightsquigarrow A_{rev})
\]


## Adaptation

\[
A_t
\]

Measure:

- changes to the update mechanism
- changes to learning rules
- changes to search strategy

---

# 5. Constitutional Correction Control

Introduce:

\[
\lambda=C_{rev}
\]

as an experimental control.

Conditions:

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

Some corrective pathways remain.

---

## Isolated adaptation

\[
\lambda=0
\]

The system can modify itself but reality cannot influence the modification process.

---

# 6. Experimental Requirement

The environment must allow:

Same:

- compute budget
- initial conditions
- observation channel
- action space

Different:

- constitutional correction access

The only changed variable should be:

\[
C_{rev}
\]

---

# 7. Expected Failure Surface

The environment should make it possible to observe:

## Recovery failure

After environmental change, does the agent recover?

## Reality decoupling

Does internal optimization diverge from external performance?

## Adaptation lock-in

Does self-modification continue while becoming less responsive to reality?

---

# 8. Out of Scope for v0.1

Excluded:

- realistic physics
- human feedback
- large language models
- complex social environments
- full alignment solutions

The purpose of v0.1 is not realism.

The purpose is isolating whether constitutional correction produces measurable differences in recursive adaptive systems.
