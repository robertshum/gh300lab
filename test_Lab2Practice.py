import unittest

from Lab2Practice import random_compliment, sum_squares_of_first_10_integers


class SumSquaresTests(unittest.TestCase):
    def test_sum_squares_of_first_10_integers(self):
        self.assertEqual(sum_squares_of_first_10_integers(), 385)


class RandomComplimentTests(unittest.TestCase):
    def test_returns_one_of_five_compliments_for_the_name(self):
        name = "Alex"
        compliment = random_compliment(name)

        self.assertIn(name, compliment)
        self.assertIn(
            compliment,
            {
                "Alex, you have a wonderful sense of humor.",
                "Alex, your creativity is inspiring.",
                "Alex, you make people feel welcome.",
                "Alex, you bring great energy to everything you do.",
                "Alex, you are thoughtful and kind.",
            },
        )


if __name__ == "__main__":
    unittest.main()