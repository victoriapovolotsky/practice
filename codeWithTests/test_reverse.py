import unittest
from reverse import Solution

class ReverseTestCase(unittest.TestCase):

    def test_reverse_posNum(self):
        sol = Solution()
        self.assertEqual(sol.reverse(123),321)

    def test_reverse_negNum(self):
        sol = Solution()
        self.assertEqual(sol.reverse(-654),-456)

    def test_reverse_posNumWZero(self):
        sol = Solution()
        self.assertEqual(sol.reverse(120),21)

    def test_reverse_negNumWZero(self):
        sol = Solution()
        self.assertEqual(sol.reverse(-3210),-123)

    def test_reverse_Zero(self):
        sol = Solution()
        self.assertEqual(sol.reverse(0),0)

    def test_reverse_largeNum(self):
        sol = Solution()
        self.assertEqual(sol.reverse(1234560709),0)

    def test_types(self):
        sol = Solution()
        self.assertRaises(TypeError, sol.reverse, '123')
        self.assertRaises(TypeError, sol.reverse, [123])


if __name__ == '__main__':
    unittest.main()