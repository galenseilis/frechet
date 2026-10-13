# Getting started

This tutorial walks you through the Fréchet package from an empty Python
session to every function it offers. You will compute bounds by hand first, then
verify the package agrees.

No probability background is assumed beyond the idea that probabilities are
numbers between `0` and `1`.

## What you will build

By the end of this tutorial you will have computed, for the same collection of
events:

- the bounds on the probability that **all** of them happen (an intersection),
- the bounds on the probability that **at least one** happens (a union),
- the bounds on a **conditional** probability,
- scores that describe how **dependent** and how **almost disjoint** the events
  are.

## Before you start

Install the package from a checkout of the repository:

```console
git clone https://github.com/galenseilis/frechet.git
cd frechet
pip install -e .
```

You can confirm it worked by importing the library. In a fresh Python session:

```pycon
>>> from frechet.main import intersection
```

If that line runs without error, you are ready.

## Step 1: Bounds on an intersection

Imagine a weather service tells you two marginal probabilities for next
Saturday: a `50%` chance of rain and a `95%` chance of wind. It does not tell
you the chance of rain *and* wind. What can you say anyway?

Write down what you know. Let `A` be "it rains" and `B` be "it is windy", with
`Pr[A] = 0.5` and `Pr[B] = 0.95`. The Fréchet inequalities say the joint
probability `Pr[A ∩ B]` is squeezed between two values:

$$
\max\bigl(0,\ \Pr[A] + \Pr[B] - 1\bigr)
\;\le\; \Pr[A \cap B] \;\le\;
\min\bigl(\Pr[A], \Pr[B]\bigr).
$$

By hand, the lower bound is `0.5 + 0.95 - 1 = 0.45`, and the upper bound is
`min(0.5, 0.95) = 0.5`. Now let the package do it:

```pycon
>>> from frechet.main import intersection
>>> intersection([0.5, 0.95])
(0.44999999999999996, 0.5)
```

The first number is the lower bound, the second is the upper bound. So there is
between a `45%` and a `50%` chance of rain *and* wind. The lone floating-point
digit is just how `0.45` is stored internally; treat the result as `(0.45, 0.5)`.

The same idea works for any number of events:

```pycon
>>> intersection([0.7, 0.8, 0.9])
(0.3999999999999999, 0.7)
```

## Step 2: Bounds on a union

Now ask the other question: what is the chance of rain **or** wind **or** both?
The bounds are

$$
\max_k \bigl\{\Pr[A_k]\bigr\}
\;\le\; \Pr\Bigl[\bigcup_k A_k\Bigr] \;\le\;
\min\Bigl(1,\ \sum_k \Pr[A_k]\Bigr).
$$

```pycon
>>> from frechet.main import union
>>> union([0.5, 0.95])
(0.95, 1.0)
```

The union is almost certain, somewhere between `95%` and `100%`. Notice the
upper bound was capped at `1`. Add a third event and the cap still applies:

```pycon
>>> union([0.6, 0.7])
(0.7, 1.0)
```

## Step 3: Conditional probability bounds

Conditional probability is a ratio, `Pr[A | B] = Pr[A ∩ B] / Pr[B]`. To bound
it, the package bounds the numerator and denominator and divides.

By default both sides are treated as intersections:

```pycon
>>> from frechet.main import conditional
>>> conditional([0.4], [0.8])
(0.5, 0.5)
```

Here `Pr[A | B]` is exactly `0.5` because both pieces were single events.

Real problems mix operators. Suppose you want `Pr[A ∩ B | C ∪ D]`. Pass the
operator names `'intersection'` or `'union'` for each side:

```pycon
>>> conditional([0.2, 0.3], [0.5], lop='union', rop='intersection')
(0.6, 1.0)
```

The numerator is a union `(0.2 ∪ 0.3)`, and the denominator is the single event
`0.5`. You will learn more about the operator arguments in the
[conditional probability how-to](../how-to/conditional-probabilities.md).

## Step 4: Measuring dependence

Two events are independent when `Pr[A ∩ B] = Pr[A] · Pr[B]`. The **independence
gap** is the difference between the joint probability and that product, and the
package bounds it for you:

```pycon
>>> from frechet.main import independence_gap
>>> independence_gap([0.5, 0.5])
(-0.25, 0.25)
```

The bounds always straddle zero, so marginals alone can never prove that events
depend on one another. They only tell you how far dependence *could* go.

## Step 5: Measuring near-disjointness

Finally, the **almost-disjoint gap** measures how far a collection is from
being mutually exclusive. It is the union minus the sum of the marginals:

```pycon
>>> from frechet.main import almost_disjoint_gap
>>> almost_disjoint_gap([0.2, 0.3])
(-0.2, 0.0)
```

A value of `0` would mean the events never overlap. Read more about both scores
in the [independence and disjointness how-to](../how-to/independence-and-disjointness.md).

## Next steps

You have now used every function in the package. From here:

- Solve a concrete task with the [how-to guides](../how-to/intersections-and-unions.md).
- Look up exact signatures in the [API reference](../reference/api.md).
- Learn *why* the formulas look the way they do in the
  [mathematical background](../explanation/mathematical-background.md).
