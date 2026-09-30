import unittest
from add_numbers import add


class TestAddNumbers(unittest.TestCase):
    def test_add_integers(self):
        self.assertEqual(add(5, 10), 15)

    def test_add_floats(self):
        self.assertAlmostEqual(add(5.5, 4.3), 9.8)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-5, -10), -15)
        self.assertEqual(add(-5, 10), 5)


if __name__ == "__main__":
    unittest.main()
