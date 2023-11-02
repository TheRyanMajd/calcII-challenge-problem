# calcII-challenge-problem

- [Harmonic Series](#the-harmonic-series)
- [Alternating Harmonic Series](#alternating-harmonic-series)
- [Contributions](#Contributions)

## The Harmonic Series:

$$(\sum_{n=1}^{\infty} \frac{1}{n})$$

$$ (\frac{1}{1} + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \frac{1}{5} + \frac{1}{6} + \frac{1}{7} + \frac{1}{8} + \ldots + \frac{1}{n-1} + \frac{1}{n}...)$$

Remember that the harmonic series DIVERGES to infinity.
This is because
$$(\sum_{n=1}^{\infty} \frac{1}{n}) => \sum_{n=1}^{\infty} \frac{1}{n^P}$$ where $P = 1$

<span></span> $P \ge 1$ : Diverge

$P < 1$ : Converge

![Harmonic Series to n = 100 by Jim Voss](image.png)

## Alternating Harmonic Series:

$$(\sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n}) $$

$$ (\frac{1}{1} - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \frac{1}{5} - \frac{1}{6} + \frac{1}{7} - \frac{1}{8} + \ldots +-\ldots)$$

### Splitting Apart the Series into Two Groups

1. $\frac{1}{1} + \frac{1}{3} + \frac{1}{5} + \frac{1}{7} + \ldots + \frac{1}{2n-1}$
2. $-\frac{1}{2} - \frac{1}{4} - \frac{1}{6} - \ldots - \frac{1}{2n}$

<span></span>$\frac{1}{n} > \frac{1}{n+1} > 0 $, and the $\lim_{n \to \infty} \frac{1}{n}$ is $0$. Therefore, $0 > \lim_{n \to \infty} \frac{1}{n+1}$. This indicates that the series converges at $\ln(2)$.

The Alternating Series Test supports the convergence.

![Alternating Series to n = 50 by Jim Voss](image-1.png)

## Contributions

Contributions by:

- Ryan Majd
- Abigail Clark
- Jim Voss

https://www.geogebra.org/m/fGKxsUp4
https://www.geogebra.org/m/FBaEmDy7
