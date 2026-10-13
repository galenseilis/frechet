# Worked examples

These examples show the Fréchet bounds applied end to end. They are
understanding-oriented: the point is to build intuition for what the bounds
mean, not to teach the API. Every number below is produced by the package.

!!! warning
    The numbers on this page **are made up** and should *not* be used for any
    real-world decision.

## The Linda problem

A [conjunction fallacy](https://en.wikipedia.org/wiki/Conjunction_fallacy) is
an inference that the intersection of two or more events is more probable than
any event alone. Amos Tversky and Daniel Kahneman raised awareness of this in
the form of the Linda problem:

!!! quote
    Linda is 31 years old, single, outspoken, and very bright. She majored in
    philosophy. As a student, she was deeply concerned with issues of
    discrimination and social justice, and also participated in anti-nuclear
    demonstrations.

    Which is more probable?

    1. Linda is a bank teller.
    2. Linda is a bank teller and is active in the feminist movement.

A non-trivial fraction of participants pick option `2`, even though it is
logically impossible: an intersection is a subset of each of its parts, so

$$
\Pr[A \cap B] \le \min\bigl(\Pr[A],\, \Pr[B]\bigr).
$$

Suppose `Pr[A] = 1/2` and `Pr[B] = 19/20`. The upper bound is

$$
\Pr[A \cap B] \le \min\left(\tfrac{1}{2}, \tfrac{19}{20}\right) = \tfrac{1}{2}.
$$

The lower bound comes from the inclusion–exclusion squeeze:

$$
\max\left(0,\ \Pr[A] + \Pr[B] - 1\right) = \tfrac{9}{20}.
$$

So `Pr[A ∩ B] ∈ [9/20, 1/2]`. The package agrees:

```pycon
>>> from frechet.main import intersection
>>> intersection([1/2, 19/20])
(0.44999999999999996, 0.5)
```

## Bad weather at the picnic

You are planning a picnic and define "bad weather" as precipitation (`PPT`),
high winds (`HW`), or temperatures outside `[20, 30]` °C (`ET`). You only have
marginals:

$$
\Pr[\text{PPT}] = \tfrac{1}{10}, \quad
\Pr[\text{HW}] = \tfrac{1}{20}, \quad
\Pr[\text{ET}] = \tfrac{1}{30}.
$$

The Fréchet union bounds give

$$
\max\left\{ \Pr[\text{PPT}], \Pr[\text{HW}], \Pr[\text{ET}] \right\}
= \tfrac{1}{10}
\;\le\; \Pr[\text{PPT} \cup \text{HW} \cup \text{ET}],
$$

$$
\Pr[\text{PPT} \cup \text{HW} \cup \text{ET}]
\;\le\; \min\left(1, \tfrac{1}{10} + \tfrac{1}{20} + \tfrac{1}{30}\right)
= \tfrac{11}{60}.
$$

So the chance of bad weather is somewhere in `[1/10, 11/60]`, roughly `10%` to
`18%`:

```pycon
>>> from frechet.main import union
>>> union([1/10, 1/20, 1/30])
(0.1, 0.18333333333333335)
```

## Diagnostic screening

A screening test is meant to detect a condition `D` from a symptom `S`. You
know that `40%` of a population has the condition and `70%` has the symptom, but
the joint occurrence `Pr[D ∩ S]` is not recorded. What can you say about
`Pr[D | S]`?

First bound the numerator, the joint probability:

```pycon
>>> from frechet.main import intersection
>>> intersection([0.4, 0.7])
(0.10000000000000009, 0.4)
```

At least `10%` of people must have both, and at most `40%`. Now divide by
`Pr[S] = 0.7`:

```pycon
>>> from frechet.main import conditional
>>> conditional([0.4, 0.7], [0.7])
(0.142857142857143, 0.5714285714285715)
```

So `Pr[D | S]` lies between about `14%` and `57%`. The interval is wide, and
that width is the honest answer: without the joint distribution, no sharper
claim is possible.

This is also a caution. If the symptom is common and the condition is not
strongly associated with it, the conditional probability can be far from the
`100%` that a "positive screen" might suggest.

??? tip "Why the lower bound is not zero here"
    The lower bound is positive only because the marginals sum to more than one
    (`0.4 + 0.7 = 1.1`). When they do not, the overlap could be empty and the
    lower bound collapses to zero.
