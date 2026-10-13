# AGENTS.md

Python package for computing Fréchet bounds on intersections/unions of events, with MkDocs documentation.

## Layout
- All code lives in `src/frechet/main.py`. `src/frechet/__init__.py` is empty: import as `from frechet.main import intersection`, **not** `from frechet import ...`.
- `docs/` holds MkDocs sources; `mkdocs.yml` is the doc build config. CI `.github/workflows/ci.yml` runs the test suite, then builds docs with `mkdocs build --strict` and publishes them with the GitHub Pages actions (`configure-pages`/`upload-pages-artifact`/`deploy-pages`) on every push to `main`/`master`. The repo's Pages build type is `workflow`, so `mkdocs gh-deploy` is **not** used. There is no lint/typecheck setup.

## Commands
- Editable install: `pip install -e .` (setuptools src-layout auto-discovery; no dependencies).
- Docs preview: `pip install mkdocs mkdocs-material mkdocstrings[python]` then `mkdocs serve` (same packages CI installs).
- Tests live in `tests/test_main.py` and use the stdlib `unittest` (no pytest dependency), runnable with `python -m unittest discover -s tests -v` (also runs in CI). They add `src/` to `sys.path`, so no install is needed.

## API
- Every public function returns a `(lower, upper)` `Tuple[float, float]` of Fréchet bounds: `intersection`, `union`, `conditional`, `jaccard_index`, `independence_gap`, `almost_disjoint_gap`.
- `conditional(lprobs, rprobs, lop='intersection', rop='intersection')` divides the bounds of the numerator by the bounds of the denominator; `lop`/`rop` accept `'intersection'` or `'union'`, anything else raises `NotImplementedError`. It may raise `ZeroDivisionError` when a denominator bound is `0`.
- All functions accept any `Iterable` (converted to `list` internally, so generators are safe).

## Docs conventions
- Docs follow the [Diátaxis](https://diataxis.fr/) framework: `docs/tutorials/` (learning-oriented), `docs/how-to/` (task-oriented), `docs/reference/` (information-oriented, generated with mkdocstrings), and `docs/explanation/` (understanding-oriented). Add new pages to the matching quadrant and register them in the `nav` in `mkdocs.yml`.
- `mkdocs.yml` sets `docstring_style: google` for mkdocstrings; keep docstrings Google style.
- mkdocstrings reads the package via `handlers.python.paths: [src]`, so the reference builds without installing the package.
- The math-heavy docs rely on MathJax via `pymdownx.arithmatex`; the config lives in `docs/javascripts/mathjax.js`. Grid cards and icon shortcodes need `attr_list`, `md_in_html`, and `pymdownx.emoji`.
