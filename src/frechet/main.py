'''
https://en.wikipedia.org/wiki/Fr%C3%A9chet_inequalities
'''

from collections.abc import Iterable
from typing import Tuple


def intersection(probs: Iterable[float]) -> float:
    '''Compute Frechet bounds for an intersection of events.'''
    return max(0, sum(probs) - (len(probs) - 1), min(probs))

def union(probs) -> float:
    '''Compute Frechet bounds for a union of events.'''
    return max(probs), min(1, sum(probs))

def conditional(lprobs, rprobs, lop:str='intersection', rop:str='intersection') -> float:
    '''Frechet bounds for a conditional probability.

    PARAMETERS
    ----------
    lprobs: list[float]
        Left-hand-side probabilities.
    rprobs: list[float]
        Right-hand-side probabilities.
    lop: str
        Operator to be applied to left-hand-side probabilities.
    rop: str
        Operator to be applied to right-hand-side probabilities.
    '''
    if lop == 'intersection':
        left_prob = intersection(lprobs)
    elif lop == 'union':
        left_prob = union(lprobs)
    else:
        raise NotImplementedError(f'Operator {lop} not implemented.')

    if rop == 'intersection':
        right_prob = intersection(rprobs)
    elif rop == 'union':
        right_prob = union(rprobs)
    else:
        raise NotImplementedError(f'Operator {rop} not implemented.')



def jaccard_index(probs) -> Tuple[float, float]:
    '''Frechet bounds for a Jaccard index.
    '''
    _intersection = intersection(probs)
    _union = union(probs)
    lower = min(_intersection) / max(_union)
    upper = max(_intersection) / min(_union)
    return lower, upper

def independence_gap(probs):
    ...

def almost_disjoint_gap(probs):
    ...
