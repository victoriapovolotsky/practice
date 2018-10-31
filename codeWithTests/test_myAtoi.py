import unittest
from myAtoi import MyAtoi

class MyAtoiTestCase(unittest.TestCase):

    def test_myAtoi_posNum(self):
        a = MyAtoi()
        self.assertEqual(a.my_atoi('123'),123)
        self.assertEqual(a.my_atoi('    123'),123)
        self.assertEqual(a.my_atoi('    123dfajdlask'),123)
        self.assertEqual(a.my_atoi('    123  dfajdlask'),123)
        self.assertEqual(a.my_atoi('123dfajdlask'),123)
        self.assertEqual(a.my_atoi('1'),1)
        self.assertEqual(a.my_atoi('  1'),1)
        self.assertEqual(a.my_atoi('  1shdakjhsdk'),1)
        self.assertEqual(a.my_atoi('1shdakjhsdk'),1)
        self.assertEqual(a.my_atoi('123+123'),123)
        self.assertEqual(a.my_atoi('1230123'),1230123)



    def test_myAtoi_negNum(self):
        a = MyAtoi()
        self.assertEqual(a.my_atoi('-123'),-123)
        self.assertEqual(a.my_atoi('    -123'),-123)
        self.assertEqual(a.my_atoi('    -123dfajdlask'),-123)
        self.assertEqual(a.my_atoi('    -123  dfajdlask'),-123)
        self.assertEqual(a.my_atoi('-123dfajdlask'),-123)
        self.assertEqual(a.my_atoi('-1'),-1)
        self.assertEqual(a.my_atoi('  -1'),-1)
        self.assertEqual(a.my_atoi('  -1shdakjhsdk'),-1)
        self.assertEqual(a.my_atoi('-1shdakjhsdk'),-1)

    def test_myAtoi_posNumWSign(self):
        a = MyAtoi()
        self.assertEqual(a.my_atoi('+123'),123)
        self.assertEqual(a.my_atoi('    +123'),123)
        self.assertEqual(a.my_atoi('    +123dfajdlask'),123)
        self.assertEqual(a.my_atoi('    +123  dfajdlask'),123)
        self.assertEqual(a.my_atoi('+123dfajdlask'),123)
        self.assertEqual(a.my_atoi('+1'),1)
        self.assertEqual(a.my_atoi('  +1'),1)
        self.assertEqual(a.my_atoi('  +1shdakjhsdk'),1)
        self.assertEqual(a.my_atoi('+1shdakjhsdk'),1)

    def test_myAtoi_noConversion(self):
        a = MyAtoi()
        self.assertEqual(a.my_atoi('dklsfja+123'),0)
        self.assertEqual(a.my_atoi('sakdjSL    +123'),0)
        self.assertEqual(a.my_atoi('KALKSD    123dfajdlask'),0)
        self.assertEqual(a.my_atoi(''),0)
        self.assertEqual(a.my_atoi('SADJKSKLA'),0)
        self.assertEqual(a.my_atoi(' +'),0)
        self.assertEqual(a.my_atoi('-'),0)
        self.assertEqual(a.my_atoi('0'),0)
        self.assertEqual(a.my_atoi('. D123'),0)

    def test_myAtoi_tooBig(self):
        a = MyAtoi()
        self.assertEqual(a.my_atoi('123456789101'),2147483647)
        self.assertEqual(a.my_atoi('2147483647'),2147483647)
        self.assertEqual(a.my_atoi('9147483647'),2147483647)
        self.assertEqual(a.my_atoi('  9147483647fdjls'),2147483647)

    def test_myAtoi_tooSmall(self):
        a = MyAtoi()
        self.assertEqual(a.my_atoi('-123456789101'),-2147483648)
        self.assertEqual(a.my_atoi('-2147483648'),-2147483648)
        self.assertEqual(a.my_atoi('-9147483647'),-2147483648)
        self.assertEqual(a.my_atoi('  -9147483647fdjls'),-2147483648)


if __name__ == '__main__':
    unittest.main()