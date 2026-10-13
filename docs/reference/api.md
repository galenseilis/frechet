# API reference

All public functions live in the `frechet.main` module. The package root
(`frechet/__init__.py`) is intentionally empty, so always import from the
module:

```python
from frechet.main import intersection, union, conditional
```

Every function accepts any `Iterable` of marginal probabilities &mdash; lists,
tuples, and generators all work, because the input is converted to a list
internally. Every function returns a `(lower, upper)` tuple of floats.

## Summary

| Function | Returns bounds on |
| --- | --- |
| [`intersection`](#intersection) | `Pr[A_1 ∩ … ∩ A_n]` |
| [`union`](#union) | `Pr[A_1 ∪ … ∪ A_n]` |
| [`conditional`](#conditional) | `Pr[numerator \| denominator]` |
| [`jaccard_index`](#jaccard_index) | `Pr[A ∩ B] / Pr[A ∪ B]` |
| [`independence_gap`](#independence_gap) | `Pr[A ∩ B] - Pr[A] · Pr[B]` |
| [`almost_disjoint_gap`](#almost_disjoint_gap) | `Pr[A ∪ B] - (Pr[A] + Pr[B])` |

## Module `frechet.main`

::: frechet.main
    options:
      members: false

## intersection

::: frechet.main.intersection

## union

::: frechet.main.union

## conditional

::: frechet.main.conditional

## jaccard_index

::: frechet.main.jaccard_index

## independence_gap

::: frechet.main.independence_gap

## almost_disjoint_gap

::: frechet.main.almost_disjoint_gap
