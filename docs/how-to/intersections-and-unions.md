# Compute bounds on intersections and unions

This guide shows you how to bound the probability that a collection of events
all occur (an intersection) or that at least one occurs (a union), given only
the marginal probabilities.

## Problem

You have marginal probabilities `Pr[A_1], …, Pr[A_n]` but not the joint
distribution, and you need the sharpest possible bounds on
`Pr[A_1 ∩ … ∩ A_n]` or `Pr[A_1 ∪ … ∪ A_n]`.

## Solution

Import `intersection` and `union` from `frechet.main` and pass any iterable of
probabilities. Each returns a `(lower, upper)` tuple.

```pycon
>>> from frechet.main import intersection, union
>>> intersection([0.5, 0.95])
(0.44999999999999996, 0.5)
>>> union([0.5, 0.95])
(0.95, 1.0)
```

The bounds are:

$$
\max\Bigl(0,\ \sum_k \Pr[A_k] - (n - 1)\Bigr)
\;\le\; \Pr\Bigl[\bigcap_k A_k\Bigr] \;\le\;
\min_k \bigl\{\Pr[A_k]\bigr\},
$$

$$
\max_k \bigl\{\Pr[A_k]\bigr\}
\;\le\; \Pr\Bigl[\bigcup_k A_k\Bigr] \;\le\;
\min\Bigl(1,\ \sum_k \Pr[A_k]\Bigr).
$$

## Variations

### More than two events

There is no limit on the number of events; the formulas generalise directly.

```pycon
>>> intersection([0.7, 0.8, 0.9])
(0.3999999999999999, 0.7)
>>> union([0.1, 0.05, 0.03333333333333333])
(0.1, 0.18333333333333335)
```

### Pass a generator or a tuple

The functions accept any `Iterable`, not just a list. Generators are consumed
safely because the input is converted to a list internally.

```pycon
>>> intersection(x / 10 for x in range(1, 6))
(0.0, 0.1)
>>> union((0.2, 0.3))
(0.3, 0.5)
```

### Bound the complement

To bound `Pr[¬A ∩ ¬B]` (neither event happens), apply the identity
`Pr[¬A] = 1 - Pr[A]` first, then take the intersection.

```pycon
>>> complement = [1 - p for p in [0.5, 0.95]]
>>> complement
[0.5, 0.050000000000000044]
>>> intersection(complement)
(0.0, 0.05)
```

## Watch out

- **Empty input raises `ValueError`.** `intersection([])` and `union([])` need
  at least one event because they call `min`/`max` on the probabilities.
- **Bounds are clamped to `[0, 1]`.** The lower intersection bound is never
  negative and the upper union bound never exceeds one.
- **Floating-point noise is expected.** Results such as `0.44999999999999996`
  are the closest double-precision value to `0.45`. Compare with a tolerance
  rather than `==` when writing tests.
- **The bounds can be wide.** That width is information: it is the price of
  knowing only the marginals. For two events the interval collapses only when
  one event is impossible or certain.
