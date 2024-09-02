import unittest
import rcipg

class TestRcipg(unittest.TestCase):

    def test_rollagain(self):
        result = rcipg.rollagain(4,[2,3])
        self.assertNotIn(result,[2,3])
        self.assertIn(result,[0,1])
        self.assertGreaterEqual(result,0)
        self.assertLess(result,4)

if __name__ == '__main__':
    unittest.main()
