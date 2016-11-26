import unittest
import knightschool

class KnightSchoolTest(unittest.TestCase):
    def test_brute_schedule(self):
        courses = [['C1', 9, 10, 'b'], ['C2', 10, 14, 'g'], ['C3', 12, 15, 'a']]
        self.assertEqual(knightschool.brute_schedule(courses), [['C1', 9, 10, 'b'], ['C2', 10, 14, 'g']])

    def test_fast_schedule(self):
        courses = [['C1', 9, 10, 'b'], ['C2', 10, 14, 'g'], ['C3', 10, 15, 'a']]
        self.assertEqual(knightschool.fast_schedule(courses), [['C1', 9, 10, 'b'], ['C2', 10, 14, 'g']])
        courses = [['C1', 9, 10, 'b'], ['C2', 10, 14, 'g'], ['C3', 10, 15, 'a']]


if __name__ == "__main__":
    unittest.main()
