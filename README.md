# Computational Analysis of the Mobius Randomness Principle and Mertens Asymptotic Bounds

## Abstract

This research platform provides a high-performance numerical framework to evaluate the statistical properties of the **Mobius function ($\mu(n)$)** and the trajectory of its cumulative sum, the **Mertens function ($M(n)$)**, up to $N = 10^7$.

The project investigates the empirical validity of the **Mobius Randomness Law**, quantifies absolute local extrema, and performs advanced time-series diagnostics, including Autocorrelation Functions (ACF) and Ljung-Box formal tests, to rigorously isolate stochastic noise from underlying deterministic arithmetic structures.

---

# Theoretical Framework & Foundations

## 1. The Mobius Function and Square-Free Density

The Mobius function

$$
\mu: \mathbb{Z}^{+} \rightarrow \{-1,0,1\}
$$

is defined as:

$$
\mu(n)=
\begin{cases}
1, & \text{if } n=1,\\
(-1)^k, & \text{if } n \text{ is a product of } k \text{ distinct primes},\\
0, & \text{if } p^2|n \text{ for some prime } p.
\end{cases}
$$

The asymptotic density of square-free numbers, i.e. numbers satisfying:

$$
\mu(n)\neq0
$$

is determined by the value of the Riemann zeta function:

$$
\lim_{x\to\infty}
\frac{1}{x}
\sum_{n\le x}|\mu(n)|
=
\frac{1}{\zeta(2)}
=
\frac{6}{\pi^2}
\approx0.6079271
$$

By symmetry, the asymptotic probabilities are:

$$
P(\mu(n)=1)=P(\mu(n)=-1)
=
\frac{3}{\pi^2}
\approx0.3039635
$$

---

## 2. Asymptotic Bounds and the Riemann Hypothesis

The Mertens function is defined as:

$$
M(x)=\sum_{n\le x}\mu(n)
$$

It is connected to the reciprocal of the Riemann zeta function through the Dirichlet series:

$$
\frac{1}{\zeta(s)}
=
\sum_{n=1}^{\infty}\frac{\mu(n)}{n^s},
\qquad
\Re(s)>1
$$

The growth rate of $M(x)$ is closely related to the distribution of non-trivial zeros of $\zeta(s)$.

The Riemann Hypothesis is equivalent to:

$$
M(x)=O(x^{1/2+\epsilon}),
\qquad
\forall \epsilon>0
$$

The classical Mertens Conjecture:

$$
|M(x)|<\sqrt{x}
$$

was disproved by Odlyzko and te Riele (1985) using LLL lattice reduction techniques.

This project investigates the empirical behavior and boundary conditions of $M(x)$ within the computational domain:

$$
1\le x\le10^7
$$

---

# Computational Methodology

## 1. High-Performance Linear Sieve Implementation

The C++ core (`mertens.cpp`) avoids the computational overhead of classical prime sieves by using a strict **Linear Sieve** algorithm.

Complexity:

- Time complexity: **O(N)**
- Space complexity: **O(N)**

Every composite integer is processed uniquely through its least prime factor:

$$
lp[n]
$$

The Mobius function is computed using the following rules:

- If:

$$
p < lp[i]
$$

then:

$$
lp[p\cdot i]=p,
\qquad
\mu(p\cdot i)=-\mu(i)
$$


- If:

$$
p=lp[i]
$$

then:

$$
p^2|(p\cdot i),
\qquad
\mu(p\cdot i)=0
$$

---

## 2. Statistical Analysis Pipeline

The Python module (`analysis_final.py`) treats the deterministic sequence:

$$
\mu(n)
$$

as a pseudo-stochastic process.

The analysis includes:

- Autocorrelation Function analysis (ACF)
- Long-range dependence evaluation
- Ljung-Box Q-test for independence testing

The null hypothesis:

$$
H_0
$$

assumes independence up to lag $k$.

The statistic:

$$
Q=
n(n+2)
\sum_{j=1}^{k}
\frac{\hat{\rho}_j^2}{n-j}
\sim
\chi^2(k)
$$

---

# Empirical Results ($N=10^7$)

## 1. Frequency Distribution and Convergence

The numerical experiment confirms strong agreement with the theoretical densities derived from:

$$
\frac{1}{\zeta(2)}
$$

| Value ($\mu(n)$) | Empirical Count | Empirical Density | Theoretical Density | Delta |
|---|---:|---:|---:|---:|
| -1 | 3,039,127 | 0.303913 | 0.303964 | -0.000051 |
| 0 | 3,920,709 | 0.392071 | 0.392073 | -0.000002 |
| +1 | 3,040,164 | 0.304016 | 0.303964 | +0.000052 |

---

## 2. Extremal Boundary Conditions

For:

$$
1\le n\le10^7
$$

the detected extrema are:

- **Global Maximum:**

$$
M(n)=1143
$$

at:

$$
n=9,993,034
$$


- **Global Minimum:**

$$
M(n)=-1078
$$

at:

$$
n=7,109,110
$$


- **Maximum Absolute Deviation:**

$$
|M(n)|=1143
$$

at:

$$
n=9,993,034
$$


The normalized value:

$$
\frac{|M(n)|}{\sqrt n}
\approx
\frac{1143}{3161.17}
\approx0.3616
$$

shows that the trajectory remains well inside the classical square-root growth envelope.

---

# Repository Architecture

```text
mertens.cpp              - Optimized linear sieve implementation
analysis_final.py        - Statistical analysis engine (ACF and Ljung-Box tests)
distribution.txt         - Mobius distribution data
extremes.txt             - Computed extrema coordinates
mertens_plot.csv         - Downsampled Mertens trajectory data (1:1000)
mertens.png              - Visualization of M(n) trajectory
mertens_normalized.png   - Normalized asymptotic behavior plot
autocorr_mu.png          - Autocorrelation plot of the Mobius sequence
autocorr_M.png           - Autocorrelation plot of the Mertens function