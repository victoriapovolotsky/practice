import unittest
from MaxArea import MaxArea

class MaxAreaTestCase(unittest.TestCase):

    def test_max_area(self):
            a = MaxArea()
            self.assertEqual(a.max_area([1,8,6,2,5,4,8,3,7]),49)

if __name__ == '__main__':
    unittest.main()