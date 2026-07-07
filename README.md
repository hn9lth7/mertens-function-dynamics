# Computational Analysis of the Mobius Randomness Principle and Mertens Asymptotic Bounds

## Abstract

This research platform provides a high-performance numerical framework to evaluate the statistical properties of the **Mobius function** and the trajectory of its cumulative sum, the **Mertens function**, up to:

```math
N = 10^7
```

The project investigates the empirical validity of the **Mobius Randomness Law**, quantifies absolute local extrema, and performs advanced time-series diagnostics, including Autocorrelation Functions (ACF) and Ljung-Box formal tests, to distinguish stochastic behavior from deterministic arithmetic structures.

---

# Theoretical Framework and Foundations

## 1. The Mobius Function and Square-Free Density

The Mobius function is defined as:

```math
\mu(n)=
\begin{cases}
1, & n=1,\\
(-1)^k, & n \text{ is a product of } k \text{ distinct primes},\\
0, & p^2|n \text{ for some prime } p.
\end{cases}
```

The density of square-free numbers is given by:

```math
\lim_{x\to\infty}
\frac{1}{x}
\sum_{n\le x}|\mu(n)|
=
\frac{1}{\zeta(2)}
=
\frac{6}{\pi^2}
\approx 0.6079271
```

Therefore:

```math
P(\mu(n)=1)=P(\mu(n)=-1)
=
\frac{3}{\pi^2}
\approx 0.3039635
```

---

# 2. Asymptotic Bounds and the Riemann Hypothesis

The Mertens function is defined as:

```math
M(x)=\sum_{n\le x}\mu(n)
```

It is connected to the reciprocal Riemann zeta function through:

```math
\frac{1}{\zeta(s)}
=
\sum_{n=1}^{\infty}
\frac{\mu(n)}{n^s},
\qquad
Re(s)>1
```

The growth rate of the Mertens function is related to the distribution of non-trivial zeros of the Riemann zeta function.

The Riemann Hypothesis is equivalent to:

```math
M(x)=O(x^{1/2+\epsilon}),
\qquad
\epsilon>0
```

The classical Mertens Conjecture:

```math
|M(x)|<\sqrt{x}
```

was disproved by Odlyzko and te Riele in 1985 using LLL lattice reduction techniques.

This project investigates the empirical behavior and boundary conditions of:

```math
1 \le x \le 10^7
```

---

# Computational Methodology

## 1. High-Performance Linear Sieve Implementation

The C++ core:

```
mertens.cpp
```

implements a strict **Linear Sieve** algorithm.

Complexity:

```
Time complexity:  O(N)
Space complexity: O(N)
```

The sieve uses the least prime factor:

```math
lp[n]
```

to calculate the Mobius function in a single pass.

Rules:

If:

```math
p < lp[i]
```

then:

```math
lp[p\cdot i]=p,
\qquad
\mu(p\cdot i)=-\mu(i)
```

If:

```math
p=lp[i]
```

then:

```math
p^2|(p\cdot i),
\qquad
\mu(p\cdot i)=0
```

---

# 2. Statistical Analysis Pipeline

The Python module:

```
analysis_final.py
```

treats the deterministic sequence:

```math
\mu(n)
```

as a pseudo-stochastic process.

The analysis includes:

- Autocorrelation Function analysis
- Long-range dependence analysis
- Ljung-Box statistical testing

The Ljung-Box statistic:

```math
Q=
n(n+2)
\sum_{j=1}^{k}
\frac{\hat{\rho}_j^2}{n-j}
\sim
\chi^2(k)
```

tests the null hypothesis:

```math
H_0
```

of independence up to lag:

```math
k
```

---

# Empirical Results

## Experiment Domain

```math
N=10^7
```

---

# 1. Frequency Distribution and Convergence

The measured distribution agrees with the theoretical density:

```math
\frac{1}{\zeta(2)}
```

| Value | Empirical Count | Empirical Density | Theoretical Density | Delta |
|---|---:|---:|---:|---:|
| -1 | 3,039,127 | 0.303913 | 0.303964 | -0.000051 |
| 0 | 3,920,709 | 0.392071 | 0.392073 | -0.000002 |
| +1 | 3,040,164 | 0.304016 | 0.303964 | +0.000052 |

---

# 2. Extremal Boundary Conditions

Within:

```math
1 \le n \le 10^7
```

the detected extrema are:

### Global Maximum

```
M(n) = 1143
n = 9,993,034
```

### Global Minimum

```
M(n) = -1078
n = 7,109,110
```

### Maximum Absolute Deviation

```
|M(n)| = 1143
n = 9,993,034
```

The normalized value:

```math
\frac{|M(n)|}{\sqrt n}
=
\frac{1143}{3161.17}
\approx0.3616
```

shows that the trajectory remains well inside classical square-root growth bounds.

---

# Repository Architecture

```text
mertens.cpp
    Optimized linear sieve implementation

analysis_final.py
    Statistical analysis engine with ACF and Ljung-Box tests

distribution.txt
    Mobius distribution data

extremes.txt
    Computed extrema coordinates

mertens_plot.csv
    Downsampled Mertens trajectory dataset

mertens.png
    Visualization of M(n) trajectory

mertens_normalized.png
    Normalized asymptotic behavior plot

autocorr_mu.png
    Autocorrelation plot of the Mobius sequence

autocorr_M.png
    Autocorrelation plot of the Mertens function
```

---

# Conclusion

This computational study demonstrates that the Mobius function exhibits strong statistical properties consistent with probabilistic randomness while preserving deep deterministic arithmetic structure.

The numerical investigation up to:

```math
N=10^7
```

confirms:

- convergence of Mobius value frequencies;
- bounded growth of the Mertens function;
- weak autocorrelation behavior;
- compatibility with theoretical predictions from analytic number theory.

The project provides a reproducible computational framework for further investigation of Mobius randomness and Mertens asymptotic behavior.