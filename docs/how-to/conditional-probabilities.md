# Compute bounds on a conditional probability

This guide shows you how to bound `Pr[numerator | denominator]` from marginal
probabilities, choosing the set operator used on each side.

## Problem

You need bounds on a conditional probability such as `Pr[A ∩ B | C ∪ D]`, but
you only have the marginal probabilities of `A`, `B`, `C`, and `D`.

## Solution

Call `conditional` with the numerator probabilities, the denominator
probabilities, and the operator to apply on each side. Operators are named
`'intersection'` (the default) or `'union'`.

```pycon
>>> from frechet.main import conditional
>>> conditional([0.2, 0.3], [0.5], lop='union', rop='intersection')
(0.6, 1.0)
```

The bounds are computed by bounding the numerator and the denominator
separately and then dividing:

$$
\frac{\text{numerator}_{\text{lower}}}{\text{denominator}_{\text{upper}}}
\;\le\; \Pr[\text{numerator} \mid \text{denominator}] \;\le\;
\frac{\text{numerator}_{\text{upper}}}{\text{denominator}_{\text{lower}}}.
$$

## Choosing operators

| Desired quantity | Call |
| --- | --- |
| `Pr[A ∩ B | C ∩ D]` | `conditional([a, b], [c, d])` |
| `Pr[A ∪ B | C ∩ D]` | `conditional([a, b], [c, d], lop='union')` |
| `Pr[A ∩ B | C ∪ D]` | `conditional([a, b], [c, d], rop='union')` |
| `Pr[A ∪ B | C ∪ D]` | `conditional([a, b], [c, d], lop='union', rop='union')` |

Passing any other operator name raises `NotImplementedError`:

```pycon
>>> conditional([0.5], [0.5], lop='xor')
Traceback (most recent call last):
    ...
NotImplementedError: Operator xor not implemented.
```

## Watch out

### A zero lower denominator bound raises

The upper bound divides by the denominator's *lower* bound. When that bound is
`0`, Python raises `ZeroDivisionError`.

```pycon
>>> conditional([0.1], [0.1, 0.2])
Traceback (most recent call last):
    ...
ZeroDivisionError: float division by zero
```

The denominator here is `Pr[C ∩ D]`, whose lower bound is `0`, so no finite
upper bound on the ratio can be derived this way. Guard against it by checking
`intersection(...)` before calling, or by choosing `rop='union'` when the
denominator is a union.

### The interval may extend past `[0, 1]`

Because the package divides interval endpoints independently, the resulting
interval is a conservative over-approximation and can spill outside `[0, 1]`:

```pycon
>>> conditional([0.6], [0.8, 0.7])
(0.8571428571428572, 1.2)
```

A probability cannot exceed `1`, so you may clamp the bounds yourself if your
application requires it. The over-approximation is intentional: it stays valid
without assuming dependence between the numerator and denominator.

## Related

- Review the exact signature in the [API reference](../reference/api.md#conditional).
- Learn the reasoning in the [mathematical background](../explanation/mathematical-background.md).
