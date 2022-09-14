import unittest
from coding_problems.arrays_two_sum_l1 import try_two_sum

class PairSumTests(unittest.TestCase):
    """check False result"""
    def test_false_result(self):
        self.assertFalse(
            try_two_sum([1, 2, 3, 9], 8),
            "we should get False, because we don't have needed pair"
        )

    def test_true_result(self):
        """check True result"""
        self.assertIn(
            try_two_sum([1, 2, 4, 4], 8),
            ([2, 3], [3, 2])
        )

    def test_wrong_types(self):
        """check wrong inputs"""
        self.assertEqual(
            try_two_sum([None], 2),
            "Exactly array and number required"
        )


if __name__ == "__main__":
    unittest.main()
