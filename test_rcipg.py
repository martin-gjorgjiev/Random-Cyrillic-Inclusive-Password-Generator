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
        pass

if __name__ == '__main__':
    unittest.main()
