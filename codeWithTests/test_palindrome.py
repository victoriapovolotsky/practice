import unittest
from palindrome import Palindrome

class PalindromeTestCase(unittest.TestCase):

    def test_palindrome_palindromeTrue(self):
        p = Palindrome()
        self.assertTrue(p.is_palindrome(121))
        self.assertTrue(p.is_palindrome(11))        
        self.assertTrue(p.is_palindrome(12521))
        self.assertTrue(p.is_palindrome(1))

    def test_palindrome_palindromeFalse(self):
        p=Palindrome()
        self.assertFalse(p.is_palindrome(12))
        self.assertFalse(p.is_palindrome(11222))

    def test_palindrome_notPalindromeNeg(self):
        p=Palindrome()
        self.assertFalse(p.is_palindrome(-121))

    def test_palindrome_Zero(self):
        p=Palindrome()
        self.assertTrue(p.is_palindrome(0))

    def test_types(self):
        p=Palindrome()
        self.assertRaises(TypeError, p.is_palindrome, '121')
        self.assertRaises(TypeError, p.is_palindrome, [123])
        self.assertRaises(TypeError, p.is_palindrome, 12.21)


if __name__ == '__main__':
    unittest.main()