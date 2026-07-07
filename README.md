# Computational Analysis of the M?bius Randomness Principle and Mertens Asymptotic Bounds

## Abstract
This research platform provides a high-performance numerical framework to evaluate the statistical properties of the **M?bius function ($\mu(n)$)** and the trajectory of its cumulative sum, the **Mertens function ($M(n)$)**, up to $N = 10^7$. The project investigates the empirical validity of the **M?bius Randomness Law**, quantifies absolute local extrema, and performs advanced time-series diagnostics (including Autocorrelation Functions and Ljung-Box formal tests) to rigorously isolate stochastic noise from underlying deterministic arithmetic structures.

---

## Theoretical Framework & Foundations

### 1. The M?bius Function and Square-Free Density
The M?bius function $\mu: \mathbb{Z}^+ \to \{-1, 0, 1\}$ is defined as:
$$
\mu(n) = \begin{cases} 
1, & \text{if } n = 1, \\ 
(-1)^k, & \text{if } n \text{ is a product of } k \text{ distinct primes}, \\ 
0, & \text{if } n \text{ is divisible by a prime square } (p^2 \mid n). 
\end{cases}
$$
Analytically, the asymptotic density of square-free numbers ($n$ such that $\mu(n) \neq 0$) is determined by the value of the Riemann zeta function at $s=2$:
$$
\lim_{x \to \infty} \frac{1}{x} \sum_{n \le x} |\mu(n)| = \frac{1}{\zeta(2)} = \frac{6}{\pi^2} \approx 0.6079271
$$
By symmetry, the theoretical asymptotic probabilities for non-zero values split equally:
$$
P(\mu(n) = 1) = P(\mu(n) = -1) = \frac{3}{\pi^2} \approx 0.3039635
$$

### 2. Asymptotic Bounds and the Riemann Hypothesis
The Mertens function $M(x) = \sum_{n \le x} \mu(n)$ governs the analytic behavior of the reciprocal of the Riemann zeta function via the Dirichlet series:
$$
\frac{1}{\zeta(s)} = \sum_{n=1}^{\infty} \frac{\mu(n)}{n^s} \quad \text{for } \Re(s) > 1
$$
The rate of growth of $M(x)$ is intrinsically connected to the distribution of non-trivial zeroes of $\zeta(s)$. The **Riemann Hypothesis (RH)** is mathematically equivalent to the statement that:
$$
M(x) = \mathcal{O}(x^{\frac{1}{2} + \epsilon}) \quad \forall \epsilon > 0
$$
The strict **Mertens Conjecture** ($|M(x)| < \sqrt{x}$), proposed by Franz Mertens in 1897, was formally disproved by Odlyzko and te Riele (1985) via the LLL lattice basis reduction algorithm. This project maps the exact empirical boundary conditions within the $10^7$ domain.

---

## Computational Methodology

### 1. High-Performance Linear Sieve Implementation
The C++ core (`mertens.cpp`) avoids the computational redundancy of standard $O(N \log \log N)$ prime sieves by utilizing a strict **Linear Sieve** architecture achieving **$O(N)$ time complexity** and **$O(N)$ space complexity**. 

Every composite integer $n$ is isolated uniquely via its *least prime factor* ($lp[n]$), enabling precise single-pass updates of the multiplicative M?bius function:
- If $p < lp[i]$, then $lp[p \cdot i] = p \implies \mu(p \cdot i) = -\mu(i)$
- If $p = lp[i]$, then $p^2 \mid (p \cdot i) \implies \mu(p \cdot i) = 0$

### 2. Statistical Analysis Pipeline
The Python suite (`analysis_final.py`) treats the deterministic sequence $\mu(n)$ as a pseudo-stochastic process. It evaluates long-range dependence structures and uses the **Ljung-Box Q-test** to test the null hypothesis $H_0$ of independence up to lag $k$:
$$
Q = n(n+2) \sum_{j=1}^k \frac{\hat{\rho}_j^2}{n-j} \sim \chi^2(k)
$$

---

## Empirical Results ($N = 10^7$)

### 1. Frequency Distribution & Convergence
Numerical validation shows excellent agreement with the theoretical densities derived from $1/\zeta(2)$:

| Value ($\mu(n)$) | Empirical Count | Empirical Density | Theoretical Asymptotic Density | Delta ($\Delta$) |
|:---|:---|:---|:---|:---|
| **$-1$** | $3,039,127$ | $0.303913$ | $0.303964$ | $-0.000051$ |
| **$0$** | $3,920,709$ | $0.392071$ | $0.392073$ | $-0.000002$ |
| **$+1$** | $3,040,164$ | $0.304016$ | $0.303964$ | $+0.000052$ |

### 2. Extremal Boundary Conditions
Local extrema within the interval $[1, 10^7]$ were localized precisely at the following coordinates:
- **Global Maximum ($M(n)$):** $+1143$ at $n = 9,993,034$
- **Global Minimum ($M(n)$):** $-1078$ at $n = 7,109,110$
- **Maximum Absolute Deviation ($|M(n)|$):** $1143$ at $n = 9,993,034$

At the maximal point, the ratio $\frac{|M(n)|}{\sqrt{n}} \approx \frac{1143}{3161.17} \approx 0.3616$, reinforcing that the sequence operates deep within the classical $\mathcal{O}(\sqrt{n})$ envelope.

---

## Repository Architecture

```text
??? mertens.cpp           # Optimized linear sieve executing O(N) evaluation and text serialization
??? analysis_final.py     # Statistics engine computing ACF and Ljung-Box formal inference
??? distribution.txt      # Serialized density distribution matrix for ?(n)
??? extremes.txt          # Computed coordinates for absolute boundary conditions
??? mertens_plot.csv      # Systematically downsampled dataset (1:1000) for scalable visualization
??? mertens.png           # Dynamic path visualization of M(n) against an unconstrained Gaussian walk
??? mertens_normalized.png# Scaled asymptotic behavior under the law of the iterated logarithm bounds
??? autocorr_mu.png       # High-resolution ACF diagram for the underlying arithmetic sequence
??? autocorr_M.png       # High-resolution ACF diagram for the integrated Mertens trajectory