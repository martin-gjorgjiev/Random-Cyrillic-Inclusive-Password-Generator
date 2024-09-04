import unittest
import rcipg

class TestRcipg (unittest.TestCase):

    def test_rollAgain (self):
        result = rcipg.rollAgain(4, [2,3])
        self.assertNotIn(result, [2,3])
        self.assertIn(result, [0,1])
        self.assertGreaterEqual(result, 0)
        self.assertLess(result, 4)

    def test_buildPassword (self):
        result = rcipg.buildPassword(8, '12')
        self.assertIs(len(result), 8)
        self.assertIn(result[0], '12')

    def test_checkSize (self):
        self.assertTrue(rcipg.checkSize(8))
        self.assertRaises(ValueError,rcipg.checkSize,'6')
        self.assertRaises(ValueError,rcipg.checkSize,-1)
        self.assertRaises(ValueError,rcipg.checkSize,True)

    def test_checkNumeric(self):
        self.assertTrue(rcipg.checkNumeric(u'ч*8A'))
        self.assertFalse(rcipg.checkNumeric(u'ч*aA'))

    def test_checkUpper(self):
        self.assertTrue(rcipg.checkUpper('aA'))
        self.assertFalse(rcipg.checkUpper('aa'))

    def test_checkSpecial(self):
        self.assertTrue(rcipg.checkSpecial(u'ч*8A'))
        self.assertFalse(rcipg.checkSpecial(u'ч8A'))

    def test_checkCyrillic(self):
        self.assertTrue(rcipg.checkCyrillic(u'ч*8A'))
        self.assertFalse(rcipg.checkCyrillic(u'*aA'))

    def test_generate (self):
        # strSize, uppercaseChar, specialChar, cyrillicChar
        allResult = rcipg.generate(8,True,True,True)
        cyrillicResult = rcipg.generate(8,False,False,True)
        specialResult = rcipg.generate(8,False,True,False)
        upperResult = rcipg.generate(8,True,False,False)

        self.assertTrue(rcipg.checkUpper(upperResult))
        self.assertTrue(rcipg.checkSpecial(specialResult))
        self.assertTrue(rcipg.checkCyrillic(cyrillicResult))
        self.assertTrue(rcipg.checkNumeric(allResult))

        self.assertFalse(rcipg.checkUpper(specialResult))
        self.assertFalse(rcipg.checkSpecial(cyrillicResult))
        self.assertFalse(rcipg.checkCyrillic(upperResult))

if __name__ == '__main__':
    unittest.main()
