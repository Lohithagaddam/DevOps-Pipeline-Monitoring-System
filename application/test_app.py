import unittest
from app import get_grade


class TestApplication(unittest.TestCase):

    def test_grade_A(self):
        self.assertEqual(get_grade(95), "A")

    def test_grade_fail(self):
        self.assertEqual(get_grade(0), "Fail")

    def test_grade_B(self):
        self.assertEqual(get_grade(80), "B")

    def test_grade_C(self):
        self.assertEqual(get_grade(60), "C")


if __name__ == "__main__":
    unittest.main()
