# Fréchet

**Fréchet** is a tiny, dependency-free Python package for computing
[Fréchet bounds](https://en.wikipedia.org/wiki/Fr%C3%A9chet_inequalities) &mdash;
the tightest possible lower and upper bounds on the probability of an
intersection, union, or conditional event when all you know are the marginal
probabilities.

That constraint is the whole point. The usual tools of probability require a
joint distribution. Fréchet bounds require almost nothing, which makes them a
good fit for *zero-data* analytics: auditing numbers, sanity-checking a model,
or reasoning about a system whose raw data you cannot see.

??? question "How is "Fréchet" pronounced?"
    Click on the 🔊 icon to listen.
    <embed width='600' height='180' src='https://embed.howtopronounce.com/classic/en/french/frechet/7179413'>

## Install

Fréchet has no runtime dependencies and supports Python 3.7 and newer.

=== "From source"

    ```console
    git clone https://github.com/galenseilis/frechet.git
    cd frechet
    pip install -e .
    ```

=== "Directly from GitHub"

    ```console
    pip install "git+https://github.com/galenseilis/frechet.git"
    ```

## Quick start

Every public function returns a `(lower, upper)` tuple of Fréchet bounds.

```pycon
>>> from frechet.main import intersection, union
>>> intersection([0.5, 0.95])
(0.44999999999999996, 0.5)
>>> union([0.1, 0.05, 0.03333333333333333])
(0.1, 0.18333333333333335)
```

The intersection of two events is between `0.45` and `0.5`; their union is
between `0.1` and `0.18`. Those are the sharpest statements you can make from
the marginals alone.

## How these docs are organised

These pages follow the [Diátaxis](https://diataxis.fr/) framework, so each page
has one job and one audience.

<div class="grid cards" markdown>

-   :material-school:{ .lg .middle } **Tutorials**

    ---

    Learning-oriented lessons that take you from nothing to a working result.
    Start here if you are new to Fréchet.

    [:octicons-arrow-right-24: Getting started](tutorials/getting-started.md)

-   :material-clipboard-check:{ .lg .middle } **How-to guides**

    ---

    Task-oriented recipes for solving a specific problem, assuming you already
    know the basics.

    [:octicons-arrow-right-24: Compute intersections and unions](how-to/intersections-and-unions.md)

-   :material-book-open-variant:{ .lg .middle } **Reference**

    ---

    Information-oriented, exhaustive description of the public API.

    [:octicons-arrow-right-24: API reference](reference/api.md)

-   :material-lightbulb-on:{ .lg .middle } **Explanation**

    ---

    Understanding-oriented discussion of the mathematics and the design
    decisions behind the package.

    [:octicons-arrow-right-24: Mathematical background](explanation/mathematical-background.md)

</div>

## License

Fréchet is released under the [MIT License](https://github.com/galenseilis/frechet/blob/main/LICENSE).
