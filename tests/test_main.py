import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from frechet.main import (  # noqa: E402
    almost_disjoint_gap,
    conditional,
    independence_gap,
    intersection,
    jaccard_index,
    union,
)


class IntersectionTests(unittest.TestCase):
    def test_two_events(self):
        lower, upper = intersection([0.5, 0.95])
        self.assertAlmostEqual(lower, 0.45)
        self.assertAlmostEqual(upper, 0.5)

    def test_lower_bound_clamped_at_zero(self):
        self.assertEqual(intersection([0.1, 0.2]), (0.0, 0.1))

    def test_single_event(self):
        self.assertEqual(intersection([0.3]), (0.3, 0.3))

    def test_certain_events(self):
        self.assertEqual(intersection([1.0, 1.0, 1.0]), (1.0, 1.0))

    def test_accepts_generator(self):
        lower, upper = intersection(p for p in [0.5, 0.95])
        self.assertAlmostEqual(lower, 0.45)
        self.assertAlmostEqual(upper, 0.5)

    def test_accepts_tuple(self):
        lower, upper = intersection((0.5, 0.95))
        self.assertAlmostEqual(lower, 0.45)
        self.assertAlmostEqual(upper, 0.5)

    def test_lower_not_greater_than_upper(self):
        lower, upper = intersection([0.7, 0.8, 0.2, 0.6])
        self.assertLessEqual(lower, upper)

    def test_empty_raises(self):
        with self.assertRaises(ValueError):
            intersection([])


class UnionTests(unittest.TestCase):
    def test_three_events(self):
        lower, upper = union([1 / 10, 1 / 20, 1 / 30])
        self.assertAlmostEqual(lower, 1 / 10)
        self.assertAlmostEqual(upper, 11 / 60)

    def test_upper_bound_clamped_at_one(self):
        self.assertEqual(union([0.5, 0.6]), (0.6, 1.0))

    def test_single_event(self):
        self.assertEqual(union([0.3]), (0.3, 0.3))

    def test_accepts_generator(self):
        lower, upper = union(p for p in [0.5, 0.6])
        self.assertEqual((lower, upper), (0.6, 1.0))

    def test_lower_not_greater_than_upper(self):
        lower, upper = union([0.1, 0.2, 0.3])
        self.assertLessEqual(lower, upper)

    def test_empty_raises(self):
        with self.assertRaises(ValueError):
            union([])


class ConditionalTests(unittest.TestCase):
    def test_defaults_use_intersection(self):
        lower, upper = conditional([0.4], [0.8])
        self.assertAlmostEqual(lower, 0.4 / 0.8)
        self.assertAlmostEqual(upper, 0.4 / 0.8)

    def test_union_numerator_intersection_denominator(self):
        lower, upper = conditional([0.2, 0.3], [0.5], 'union', 'intersection')
        self.assertAlmostEqual(lower, 0.6)
        self.assertAlmostEqual(upper, 1.0)

    def test_union_denominator(self):
        lower, upper = conditional([0.5], [0.2, 0.3], 'intersection', 'union')
        self.assertAlmostEqual(lower, 0.5 / 0.5)
        self.assertAlmostEqual(upper, 0.5 / 0.3)

    def test_invalid_left_operator(self):
        with self.assertRaises(NotImplementedError):
            conditional([0.5], [0.5], lop='xor')

    def test_invalid_right_operator(self):
        with self.assertRaises(NotImplementedError):
            conditional([0.5], [0.5], rop='xor')

    def test_zero_lower_denominator_raises(self):
        with self.assertRaises(ZeroDivisionError):
            conditional([0.1], [0.1, 0.2])


class JaccardIndexTests(unittest.TestCase):
    def test_two_events(self):
        lower, upper = jaccard_index([0.2, 0.3])
        self.assertAlmostEqual(lower, 0.0 / 0.5)
        self.assertAlmostEqual(upper, 0.2 / 0.3)

    def test_certain_events(self):
        self.assertEqual(jaccard_index([1.0, 1.0]), (1.0, 1.0))

    def test_single_event(self):
        self.assertEqual(jaccard_index([0.4]), (1.0, 1.0))

    def test_lower_not_greater_than_upper(self):
        lower, upper = jaccard_index([0.2, 0.9, 0.4])
        self.assertLessEqual(lower, upper)


class IndependenceGapTests(unittest.TestCase):
    def test_bounds_centered_on_product(self):
        lower, upper = independence_gap([0.5, 0.2])
        self.assertAlmostEqual(lower, -0.1)
        self.assertAlmostEqual(upper, 0.1)

    def test_pairwise_extreme_case(self):
        lower, upper = independence_gap([0.5, 0.5])
        self.assertAlmostEqual(lower, -0.25)
        self.assertAlmostEqual(upper, 0.25)

    def test_always_covers_zero(self):
        lower, upper = independence_gap([0.3, 0.7, 0.9])
        self.assertLessEqual(lower, 0.0)
        self.assertGreaterEqual(upper, 0.0)

    def test_independent_events_give_zero_gap(self):
        self.assertEqual(independence_gap([1.0, 1.0]), (0.0, 0.0))


class AlmostDisjointGapTests(unittest.TestCase):
    def test_docs_example(self):
        lower, upper = almost_disjoint_gap([1 / 10, 1 / 20, 1 / 30])
        self.assertAlmostEqual(lower, -1 / 12)
        self.assertAlmostEqual(upper, 0.0)

    def test_bounds_are_non_positive(self):
        lower, upper = almost_disjoint_gap([0.1, 0.2, 0.3])
        self.assertLessEqual(lower, 0.0)
        self.assertLessEqual(upper, 0.0)

    def test_disjoint_events_lower_bound(self):
        lower, upper = almost_disjoint_gap([0.2, 0.3])
        self.assertAlmostEqual(lower, -0.2)
        self.assertAlmostEqual(upper, 0.0)


class ReturnTypeTests(unittest.TestCase):
    def test_all_functions_return_float_pairs(self):
        results = [
            intersection([0.2, 0.3]),
            union([0.2, 0.3]),
            conditional([0.2], [0.5]),
            jaccard_index([0.2, 0.3]),
            independence_gap([0.2, 0.3]),
            almost_disjoint_gap([0.2, 0.3]),
        ]
        for result in results:
            self.assertIsInstance(result, tuple)
            self.assertEqual(len(result), 2)
            self.assertTrue(all(isinstance(value, float) for value in result))


if __name__ == '__main__':
    unittest.main()
