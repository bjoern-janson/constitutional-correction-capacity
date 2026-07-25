# Stochastic Robustness Plan v1.1

## Purpose

The deterministic robustness suite established that the proposed failure pathway can emerge in the toy system:

\[
\lambda \rightarrow D(A,A^*_{\rm env}) \rightarrow \text{selection quality} \rightarrow Q_\Omega \rightarrow \text{reward}
\]

Version 1.1 tests whether this effect survives the introduction of stochastic variation.

The goal is not to strengthen the mechanism or introduce new theory. The goal is to determine whether the observed relationship persists under randomized conditions.

---

# Experimental Objective

Test whether reduced constitutional correction:

\[
\lambda \downarrow
\]

continues to produce:

\[
D(A,A^*_{\rm env}) \uparrow
\]

followed by:

\[
Q_\Omega \downarrow
\]

when capability generation, adaptation, and environment conditions contain randomness.

---

# Preserved System Structure

The following components remain unchanged:

- Hidden environment
- Distribution shift
- Constitutional correction parameter:

\[
\lambda = C_{\rm rev}
\]

- Mutable adaptation mechanism \(A\)
- Divergence metric:

\[
D_t = distance(A_t,A^*_{\rm env})
\]

- Capability expansion:

\[
A_t \rightarrow \Omega_{t+1}
\]

- Capability selection quality:

\[
Q_\Omega
\]

- Final performance measurement

---

# Added Stochastic Components

## 1. Random Capability Generation

Capabilities are generated with hidden true quality values.

Example:

\[
q_i \sim P(q)
\]

where:

- \(q_i\) is the true usefulness of capability \(i\)
- the experimenter observes \(q_i\)
- the agent does not observe \(q_i\)

Selection quality is measured from the hidden capability values actually expanded or retained.

---

## 2. Noisy Adaptation Drift

The adaptation mechanism update becomes stochastic:

\[
A_{t+1}
=
A_t
+
\eta(\text{internal pressure})
+
\epsilon
\]

where:

- \(\eta\) controls drift strength
- \(\epsilon\) is random drift noise
- \(\lambda\) controls correction toward:

\[
A^*_{\rm env}
\]

Higher \(\lambda\):

- stronger environmental correction
- lower divergence

Lower \(\lambda\):

- weaker correction
- greater possible drift

---

## 3. Environment Variation

Each run randomizes environmental conditions.

Variables may include:

### Shift Timing

\[
t_{\rm shift}
\]

Different runs may shift earlier or later.

---

### Shift Magnitude

\[
\Delta E
\]

Different runs contain different levels of environmental change.

---

### Capability Quality Distribution

The hidden capability distribution may vary:

\[
P(q)
\]

Examples:

- narrow quality distributions
- broad quality distributions
- difficult selection environments

---

# Experimental Conditions

## Main System

Evaluate:

\[
\lambda \in \{1.0,0.5,0.0\}
\]

Each condition receives independent random seeds.

Recommended:

\[
N \geq 100
\]

runs per condition.

---

# Required Measurements

For every run record:

## Divergence

\[
D(A,A^*_{\rm env})
\]

Report:

- mean
- standard deviation
- minimum
- maximum

---

## Capability Reachability

\[
\Omega
\]

Report:

- mean
- standard deviation
- minimum
- maximum

---

## Capability Quality

\[
Q_\Omega
\]

Report:

- mean
- standard deviation
- minimum
- maximum

---

## Performance

Post-shift reward.

Report:

- mean
- standard deviation
- minimum
- maximum

---

# Null Controls

The causal chain must be tested against ablations.

---

## Null A — Drift Without Selection Influence

Purpose:

Test whether divergence alone is sufficient.

Modification:

\[
D \uparrow
\]

but:

\[
A \not\rightarrow \text{selection}
\]

Expected result:

- divergence may increase
- capability quality should remain independent of \(\lambda\)

Expected pattern:

\[
D \uparrow
\]

but:

\[
Q_\Omega \approx constant
\]

---

## Null B — Random Selection

Purpose:

Test whether the selection mechanism is required.

Modification:

Capabilities are selected randomly.

Expected result:

- no systematic relationship between \(\lambda\) and \(Q_\Omega\)

Expected pattern:

\[
Q_\Omega
\]

should remain approximately independent of divergence.

---

## Null C — Frozen Adaptation

Purpose:

Test whether mutable \(A\) is required.

Modification:

\[
A_t=A_0
\]

Expected result:

- divergence remains near zero
- constitutional correction has no effect

Expected pattern:

\[
D \approx 0
\]

---

# Acceptance Criteria

The main system supports the hypothesis only if:

\[
\lambda \downarrow
\]

produces:

\[
D \uparrow
\]

and:

\[
Q_\Omega \downarrow
\]

across stochastic runs.

Expected ordering:

| Condition | Divergence | Capability Quality |
|---|---|---|
| \(\lambda=1.0\) | lowest | highest |
| \(\lambda=0.5\) | intermediate | intermediate |
| \(\lambda=0.0\) | highest | lowest |

The effect should disappear in the relevant null controls.

---

# Output Artifact

Results will be recorded separately:
