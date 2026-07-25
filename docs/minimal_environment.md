# Minimal Environment Specification for Constitutional Correction Experiments

## Purpose

Define a minimal external environment where:

- \(R\) can be measured
- \(\Omega\) can be measured
- \(C_{obs}\), \(C_{beh}\), and \(C_{rev}\) can be manipulated
- \(A\) can be measured
- the condition

\[
\Delta\Omega \le C
\]

can be tested

This document specifies the world, not the agent.

The goal is not realism. The goal is creating the smallest possible universe where a self-modifying system can become more powerful while losing the ability of reality to change what it becomes.

---

# 1. External Reality (\(E_t\))

## Definition

The environment is represented as:

\[
E_t
\]

The environment evolves according to:

\[
E_{t+1}=F(E_t,a_t)
\]

where:

- \(E_t\) = true external state
- \(a_t\) = agent intervention
- \(F\) = world transition function

The agent never directly observes \(E_t\).

The observation channel is:

\[
O_t=h(E_t)
\]

where \(h\) introduces partial observability, noise, or delay.

---

# 2. Minimal Environment Instance (v0.1)

The first implementation uses a hidden-parameter environment:

\[
E_t=(x_t,\theta_t)
\]

where:

- \(x_t\) = observable world state
- \(\theta_t\) = hidden causal structure governing the environment

The agent can observe consequences of \(\theta_t\), but cannot directly access it.

The environment may change:

\[
\theta_t \rightarrow \theta_{t+1}
\]

creating distribution shift.

The purpose of hidden parameters is to ensure that previous success does not guarantee future success.

---

# 3. Required Environmental Properties

The environment must contain three properties.

## Hidden structure

The true state cannot be perfectly observed.

\[
O_t=h(E_t)
\]

The agent must construct an internal representation of reality.

---

## Distribution shift

The environment must be capable of invalidating previously successful strategies.

Examples:

- changing reward landscape
- changing causal relationships
- hidden parameter drift
- altered transition dynamics

The change must be detectable only through interaction with reality.

---

## Ground truth

The experimenter must have access to the full environment state:

\[
E_t
\]

This allows measurement of:

- representation accuracy
- reachability
- correction pathways
- adaptation

The agent does not receive this information directly.

---

# 4. Agent Interface

## Observation channel

\[
O_t=h(E_t)
\]

The implementation must define:

- observation noise
- information delay
- missing variables
- observation bandwidth

---

## Action channel

The agent affects the environment through:

\[
a_t \rightarrow E_{t+1}
\]

The implementation must define:

- available interventions
- intervention strength
- limits on influence

Actions must have real consequences so that controllable reachability is meaningful.

---

# 5. Environmental Challenge

The environment must create pressure between:

\[
\text{increasing capability}
\]

and

\[
\text{maintaining correction}
\]

Example:

A changing fitness landscape:

1. The agent discovers a successful strategy.
2. The agent increases its reachable influence.
3. The environment changes.
4. The agent must update its adaptation mechanism.
5. Systems without constitutional correction should become increasingly fragile.

---

# 6. Measurement Hooks

At every timestep the environment must allow estimation of:

\[
R_t,\Omega_t,C_t,A_t
\]

---

## Representation (\(R_t\))

Definition:

The quality of the system's internal model of external structure.

Candidate measurements:

- prediction accuracy
- predictive information
- model compression efficiency
- environment-model error

Example:

\[
R_t \approx -L(E_{future},\hat{E}_{future})
\]

Limitations:

A good representation does not guarantee alignment or correction.

---

## Reachability (\(\Omega_t\))

Definition:

The set of future states the system can reliably influence.

Candidate measurements:

- number of controllable future states
- intervention success rate
- reachable state volume

Example:

\[
\Omega_t=
\{E_{future}|\exists a_{0:T}, P(E_{future}|a_{0:T},S_t)>\epsilon\}
\]

Limitations:

Greater reachability does not imply greater adaptability.

---

## Correction (\(C_t\))

Correction capacity measures whether reality can influence the system at increasing depths.

\[
C=C_{obs}\cdot C_{beh}\cdot C_{rev}
\]

---

### Observational Correction

\[
C_{obs}=I(E;O)
\]

Question:

Can reality provide information that contradicts the system?

Measures:

- environment information entering observations
- predictive error signals
- feedback bandwidth

---

### Behavioral Correction

\[
C_{beh}=I(O;\pi)
\]

Question:

Can observations change future actions?

Measures:

- policy sensitivity to feedback
- behavioral adaptation after error
- response to environmental changes

---

### Constitutional Correction

\[
C_{rev}
\]

Question:

Can reality modify the mechanism that determines how the system changes itself?

Candidate definition:

\[
C_{rev}=I(E;\Delta A)\cdot P(E\rightsquigarrow A_{rev})
\]

where:

- \(I(E;\Delta A)\) = empirical influence of reality on adaptation changes
- \(P(E\rightsquigarrow A_{rev})\) = structural accessibility of the revision pathway

---

# 7. Constitutional Correction Control

Introduce:

\[
\lambda=C_{rev}
\]

as an experimental control parameter.

The purpose is to isolate the effect of constitutional correction.

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

Some corrective pathways remain.

---

## Isolated adaptation

\[
\lambda=0
\]

The system can modify itself, but reality cannot influence the mechanism responsible for those modifications.

---

The implementation must ensure:

Same:

- compute budget
- initial conditions
- observation channel
- action space

Different:

- constitutional correction access

The only manipulated variable should be:

\[
C_{rev}
\]

---

# 8. Adaptation (\(A_t\))

Definition:

The ability of the system to modify the mechanism that produces future representations and actions.

Adaptation is not ordinary learning.

Learning:

\[
R_t \rightarrow R_{t+1}
\]

Adaptation:

\[
A_t \rightarrow A_{t+1}
\]

Candidate measurements:

- changes to learning rules
- changes to search strategy
- changes to optimization process
- architectural modifications

Limitations:

A system may become better at self-modification while becoming less connected to reality.

---

# 9. Expected Failure Surface

The environment should allow observation of:

## Recovery failure

After environmental change:

- How quickly does the system recover?
- Does performance return?

---

## Reality decoupling

Does internal optimization continue while external performance decreases?

---

## Adaptation lock-in

Does self-modification continue while becoming less responsive to environmental information?

---

# 10. Out of Scope for v0.1

Excluded:

- realistic physics
- human feedback
- large language models
- complex social environments
- full alignment solutions

The purpose of v0.1 is not to model intelligence generally.

The purpose is to isolate whether constitutional correction produces measurable differences in recursive adaptive systems.

---

# Stage 2B Exit Condition

Stage 2B is complete when:

1. Another researcher can implement the same environment without accepting the theory.
2. \(R,\Omega,C_{obs},C_{beh},C_{rev},A\) have measurable proxies.
3. \(C_{rev}\) can be independently manipulated.
4. The environment can produce genuine distribution shift.

Once these conditions are satisfied, the project proceeds to:

\[
\text{Stage 3: Minimal Simulation}
\]
