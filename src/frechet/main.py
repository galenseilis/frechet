'''Fréchet bounds on intersections, unions, and conditional probabilities.

Every public function accepts any iterable of marginal probabilities and
returns a ``(lower, upper)`` tuple of Fréchet bounds. The package has no
runtime dependencies.

The bounds are described at
https://en.wikipedia.org/wiki/Fr%C3%A9chet_inequalities.
'''

from collections.abc import Iterable
from typing import Tuple


def intersection(probs: Iterable[float]) -> Tuple[float, float]:
    '''Compute Fréchet bounds for the probability of an intersection of events.

    Args:
        probs: Probabilities of the individual events.

    Returns:
        The lower and upper bounds on ``Pr[A_1 ∩ ... ∩ A_n]`` as a
        ``(lower, upper)`` tuple.
    '''
    probs = list(probs)
    lower = max(0.0, sum(probs) - (len(probs) - 1))
    upper = min(probs)
    return lower, upper


def union(probs: Iterable[float]) -> Tuple[float, float]:
    '''Compute Fréchet bounds for the probability of a union of events.

    Args:
        probs: Probabilities of the individual events.

    Returns:
        The lower and upper bounds on ``Pr[A_1 ∪ ... ∪ A_n]`` as a
        ``(lower, upper)`` tuple.
    '''
    probs = list(probs)
    lower = max(probs)
    upper = min(1.0, sum(probs))
    return lower, upper


def conditional(
    lprobs: Iterable[float],
    rprobs: Iterable[float],
    lop: str = 'intersection',
    rop: str = 'intersection',
) -> Tuple[float, float]:
    '''Compute Fréchet bounds for a conditional probability.

    The conditional probability is bounded by taking the ratio of the bounds
    on the numerator and the denominator, i.e. ``left / right``.

    Args:
        lprobs: Probabilities of the events in the numerator.
        rprobs: Probabilities of the events in the denominator.
        lop: Operator applied to ``lprobs``; either ``'intersection'`` or
            ``'union'``.
        rop: Operator applied to ``rprobs``; either ``'intersection'`` or
            ``'union'``.

    Returns:
        The lower and upper bounds on the conditional probability as a
        ``(lower, upper)`` tuple.

    Raises:
        NotImplementedError: If ``lop`` or ``rop`` is not a supported operator.
    '''
    if lop == 'intersection':
        left_lower, left_upper = intersection(lprobs)
    elif lop == 'union':
        left_lower, left_upper = union(lprobs)
    else:
        raise NotImplementedError(f'Operator {lop} not implemented.')

    if rop == 'intersection':
        right_lower, right_upper = intersection(rprobs)
    elif rop == 'union':
        right_lower, right_upper = union(rprobs)
    else:
        raise NotImplementedError(f'Operator {rop} not implemented.')

    lower = left_lower / right_upper
    upper = left_upper / right_lower
    return lower, upper


def jaccard_index(probs: Iterable[float]) -> Tuple[float, float]:
    '''Compute Fréchet bounds for the Jaccard index.

    The Jaccard index is the ratio of the intersection to the union, so its
    bounds are obtained by dividing the intersection bounds by the union
    bounds.

    Args:
        probs: Probabilities of the individual events.

    Returns:
        The lower and upper bounds on the Jaccard index as a ``(lower, upper)``
        tuple.
    '''
    probs = list(probs)
    intersection_lower, intersection_upper = intersection(probs)
    union_lower, union_upper = union(probs)
    return intersection_lower / union_upper, intersection_upper / union_lower


def independence_gap(probs: Iterable[float]) -> Tuple[float, float]:
    '''Compute Fréchet bounds for the independence gap.

    The independence gap is the joint probability of the events minus the
    product of their marginal probabilities. Its bounds are obtained by
    subtracting the product of the marginal probabilities from the bounds on
    the intersection.

    Args:
        probs: Probabilities of the individual events.

    Returns:
        The lower and upper bounds on the independence gap as a
        ``(lower, upper)`` tuple.
    '''
    probs = list(probs)
    intersection_lower, intersection_upper = intersection(probs)
    product = 1.0
    for prob in probs:
        product *= prob
    return intersection_lower - product, intersection_upper - product


def almost_disjoint_gap(probs: Iterable[float]) -> Tuple[float, float]:
    '''Compute Fréchet bounds for the almost-disjoint gap.

    The almost-disjoint gap is the probability of the union of the events
    minus the sum of their marginal probabilities. Its bounds are obtained by
    subtracting the sum of the marginal probabilities from the bounds on the
    union.

    Args:
        probs: Probabilities of the individual events.

    Returns:
        The lower and upper bounds on the almost-disjoint gap as a
        ``(lower, upper)`` tuple.
    '''
    probs = list(probs)
    union_lower, union_upper = union(probs)
    total = sum(probs)
    return union_lower - total, union_upper - total
