# frechet

**Fréchet** is a tiny, dependency-free Python package for computing
[Fréchet bounds](https://en.wikipedia.org/wiki/Fr%C3%A9chet_inequalities) on the
probability of intersections, unions, and conditional events, given only the
marginal probabilities.

```pycon
>>> from frechet.main import intersection, union
>>> intersection([0.5, 0.95])
(0.44999999999999996, 0.5)
>>> union([0.1, 0.05, 0.03333333333333333])
(0.1, 0.18333333333333335)
```

## Install

```console
pip install -e .
```

## Documentation

Full documentation follows the [Diátaxis](https://diataxis.fr/) framework and
is published at **<https://galenseilis.github.io/frechet/>**:

- [Tutorials](https://galenseilis.github.io/frechet/tutorials/getting-started/) &mdash; learn by doing.
- [How-to guides](https://galenseilis.github.io/frechet/how-to/intersections-and-unions/) &mdash; solve a specific task.
- [Reference](https://galenseilis.github.io/frechet/reference/api/) &mdash; the complete public API.
- [Explanation](https://galenseilis.github.io/frechet/explanation/mathematical-background/) &mdash; the mathematics and design.

To preview the docs locally:

```console
pip install mkdocs-material "mkdocstrings[python]"
mkdocs serve
```

## Tests

```console
python -m unittest discover -s tests -v
```

## License

[MIT](LICENSE)
