# Measure independence and disjointness

This guide shows you how to quantify statistical dependence and how close a
collection of events is to being mutually exclusive, using only marginal
probabilities.

## Problem

You want a single number describing whether events are independent
(`Pr[A ∩ B] = Pr[A] · Pr[B]`) or almost disjoint
(`Pr[A ∪ B] = Pr[A] + Pr[B]`), but you only have the marginals.

## Solution: independence gap

The **independence gap** is `Pr[A ∩ B] - Pr[A] · Pr[B]`. Bounding the
intersection and subtracting the product gives bounds on the gap.

```pycon
>>> from frechet.main import independence_gap
>>> independence_gap([0.5, 0.2])
(-0.1, 0.1)
>>> independence_gap([0.5, 0.5])
(-0.25, 0.25)
```

Interpretation:

- `0` inside the interval is unavoidable &mdash; **marginals can never rule out
  independence**, because the interval always contains `0`.
- A positive value means the joint probability is *larger* than independence
  would predict (positively associated).
- A negative value means it is *smaller* (negatively associated).
- For two events the gap always lies within `[-1/4, 1/4]`; the package returns
  the tighter bounds implied by the marginals you supply.

## Solution: almost-disjoint gap

The **almost-disjoint gap** is `Pr[A ∪ B] - (Pr[A] + Pr[B])`. It is `0` exactly
when the events are disjoint, and negative when they overlap.

```pycon
>>> from frechet.main import almost_disjoint_gap
>>> almost_disjoint_gap([0.2, 0.3])
(-0.2, 0.0)
>>> almost_disjoint_gap([0.1, 0.05, 0.03333333333333333])
(-0.08333333333333334, 0.0)
```

The upper bound is always `0` (the union can never exceed the sum of the
marginals), so a value *near* `0` means the events are nearly disjoint.

## Normalise to the unit interval

The theoretical ranges are known, so you can rescale the raw gaps. For the
almost-disjoint gap of `n` events, `-(Pr[union] - sum)` lies in `[0, n - 1]`:

```pycon
>>> from frechet.main import almost_disjoint_gap
>>> lower, upper = almost_disjoint_gap([0.2, 0.3])
>>> n = 2
>>> (-upper / (n - 1), -lower / (n - 1))
(-0.0, 0.2)
```

A similar normalisation applies to the independence gap; see the
[mathematical background](../explanation/mathematical-background.md) for the
derivation.

## Watch out

- **The gaps are signed.** Negative values are meaningful, not errors.
- **The independence gap always covers zero.** Do not treat a lower bound
  greater than zero as evidence of dependence; it cannot occur from marginals.
- **The almost-disjoint gap never has a positive upper bound.** If you see one
  for `n ≥ 2`, check your inputs.
