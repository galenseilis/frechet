# Mathematical background

This page explains *why* the package works the way it does. Read it if you want
to understand the mathematics, the notation, and the design decisions &mdash;
not if you just need to call a function (the
[how-to guides](../how-to/intersections-and-unions.md) are better for that).

## The problem: reasoning from marginals alone

Suppose you know the probability of each event in a family `A_1, …, A_n` but
you do not know how the events relate to one another. The events might overlap
heavily, be nearly disjoint, or anything in between. The **Fréchet
inequalities** give the tightest bounds on the probability of their
intersection and union that hold *for every* possible joint distribution
consistent with those marginals.

This is what makes the package useful for *zero-data* analytics: when a
summary statistic is available but the raw data is not, you can still make a
defensible statement rather than guessing.

## The two inequalities

There are two such inequalities. One bounds the intersection of events, and the
other bounds the union.

$$
\begin{align}
\max \left( 0, \sum_{k=1}^n \Pr[A_k] - (n-1) \right)
  \;\le\; & \Pr \left[ \bigcap_{k=1}^n A_k \right]
  \;\le\; \min_k \left\{ \Pr[A_k] \right\}, \\
\max \left\{ \Pr[A_k] \right\}
  \;\le\; & \Pr \left[ \bigcup_{k=1}^n A_k \right]
  \;\le\; \min \left( 1, \sum_{k=1}^n \Pr[A_k] \right).
\end{align}
$$

The lower intersection bound is the inclusion–exclusion principle pushed to its
limit: if the marginals sum to more than `1`, the excess must lie in the
overlap. The upper union bound is the complementary fact: the union can never
exceed one, nor the sum of the parts.

Here is a public domain portrait of Maurice Fréchet.

![](../assets/Frechet.jpeg)

## A note on notation

You may notice that these docs use the set-theoretic symbols `∩` and `∪` rather
than the logical connectives `∧` and `∨`. In many settings they can be used
interchangeably, but formal [probability theory](https://en.wikipedia.org/wiki/Probability_space)
is defined on sets, so we prefer the set-theoretic notation.

## The independence gap

??? abstract "What it measures"
    The independence gap quantifies statistical dependence. The Fréchet
    inequalities put lower and upper bounds on how much dependence there could
    be, given only the marginal probabilities.

The independence gap was conceived of sometime between asking [*A formal
definition of a "measure of association"*](https://stats.stackexchange.com/q/534454/69508)
and posting [this answer](https://stats.stackexchange.com/a/589235/69508) to
that question. It was originally defined in terms of cumulative distribution
functions, but [Sextus Empiricus](https://stats.stackexchange.com/users/164061/sextus-empiricus)
readily generalised it to events from any probability space in
[their answer](https://stats.stackexchange.com/a/623001/69508) to
[*Is the pairwise independence gap bounded to $[-1/4, 1/4]$? What about for n variables?*](https://stats.stackexchange.com/q/622983/69508).

For events `E_1, …, E_n` from a suitable probability space
`(Ω, 𝓕, P)`, the independence gap is

$$
\phi[E_1, \ldots, E_n] \triangleq
\Pr\left[ \bigcap_{k=1}^n E_k \right] - \prod_{k=1}^n \Pr[E_k].
$$

Statistical independence of the collection is exactly the equality

$$
\Pr\left[ \bigcap_{k=1}^n E_k \right] = \prod_{k=1}^n \Pr[E_k],
$$

so the gap measures independence directly from its definition:

- a value of **zero** means the events are statistically independent,
- a **positive** value means the joint probability is larger than independence
  would predict,
- a **negative** value means the joint probability is smaller.

Because the Fréchet bounds on the intersection always contain the product
`∏ Pr[E_k]`, the resulting bounds on the gap **always cover zero**. That is why
you cannot use it to rule out independence.

??? failure "Ruling out independence is impossible"
    One might naïvely hope that the bounds could rule out statistical
    independence, but they cannot. The bounds will always cover zero.

## The almost-disjoint gap

??? abstract "What it measures"
    The almost-disjoint gap quantifies how close a collection of events is to
    being disjoint (mutually exclusive). The Fréchet inequalities provide bounds
    that can be normalised into a score.

In [*Can we obtain a probability interpretation on these bounds obtained from
the ADG and Frechet inequalities?*](https://stats.stackexchange.com/q/623136/69508),
the almost-disjoint gap (ADG) is defined as

!!! quote
    The **almost-disjoint gap** is given by

    $$
    \mathcal{D}_{\mu} \left( E_1, \ldots, E_n \right)
    \triangleq
    \mu \left( \bigcup_{k=1}^{n} E_k \right)
    - \sum_{k=1}^n \mu \left( E_k \right),
    $$

    where `μ` is a measure and `{E_k}` are elements of a suitable
    σ-algebra. When the ADG equals zero, the events are
    [almost everywhere](https://en.wikipedia.org/wiki/Almost_everywhere)
    [pairwise disjoint](https://en.wikipedia.org/wiki/Disjoint_sets).

The [inclusion–exclusion principle](https://en.wikipedia.org/wiki/Inclusion%E2%80%93exclusion_principle)
states that

$$
P\left( \bigcup_{k=1}^n E_k \right)
= \underbrace{\sum_{k=1}^n P(E_k)}_{\text{marginal terms}}
+ \underbrace{\sum_{k=2}^n \left((-1)^{k-1} \sum_{\substack{I \subseteq \{1, \ldots, n \} \\ |I| = k}} P\left(\bigcap_{i \in I} E_i \right) \right)}_{\text{joint terms}}.
$$

This shows directly what the ADG means: it is exactly the sum of the joint
terms.

$$
\mathcal{D}_{P} \left( E_1, \ldots, E_n \right)
= \underbrace{\sum_{k=2}^n \left((-1)^{k-1} \sum_{\substack{I \subseteq \{1, \ldots, n \} \\ |I| = k}} P\left(\bigcap_{i \in I} E_i \right) \right)}_{\text{joint terms}}.
$$

Combining the ADG with the Fréchet union inequality bounds the ADG in terms of
the marginals:

$$
\max \{ P(E_k) \} - \sum_{k=1}^n P ( E_k )
\;\le\; \mathcal{D}_{P} \left( E_1, \ldots, E_n \right) \;\le\;
\min \left(1, \sum_{k=1}^n P(E_k) \right) - \sum_{k=1}^n P ( E_k ).
$$

Not knowing the marginals, the most extreme bounds depend only on the number of
events:

$$
1 - n \;\le\; \mathcal{D}_{P} \left( E_1, \ldots, E_n \right) \;\le\; 0.
$$

### Normalising the almost-disjoint gap

Since `1 - n ≤ 0`, we can flip the bounds by multiplying by `-1`:

$$
0 \;\le\; -\mathcal{D}_{P} \left( E_1, \ldots, E_n \right) \;\le\; n-1.
$$

Because `n - 1` can exceed one, divide through by `n - 1` to normalise onto the
unit interval:

$$
0 \;\le\; \frac{-\mathcal{D}_{P} \left( E_1, \ldots, E_n \right)}{n-1} \;\le\; 1.
$$

## Where this is useful

The primary applications are in data analysis where the appropriate summary
statistics are available but the raw data is not. Typical situations include
auditing reported figures, sanity-checking a model against partial information,
or reasoning about a system you cannot access directly.

## Design philosophy

Fréchet is designed to work with minimal dependencies. Because the primary use
case is to work with summary statistics, dealing with truly "big data" is out of
scope. The package therefore uses no special packages or language extensions
&mdash; only the Python standard library.

??? question "Is Fréchet compatible with PyPy?"
    Fréchet appears to work with PyPy, but this is not a supported compatibility
    guarantee.
