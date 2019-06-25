from unittest import TestCase
import task6


class TestTest6(TestCase):

    def setUp(self):
        """Init"""

    def test_identity(self):
        """Test for is task6"""
        self.assertIsNone(task6.identity(mystring="1+1=3"))

    def test_foperp(self):
        self.assertTrue(task6.foperp('+', 1, 2, 3))
        self.assertFalse(task6.foperp('+', 1, 2, 4))
        self.assertTrue(task6.foperp('-', 3, 2, 1))
        self.assertFalse(task6.foperp('-', 1, 2, 4))
        self.assertTrue(task6.foperp('*', 1, 2, 2))
        self.assertFalse(task6.foperp('*', 1, 2, 4))
        self.assertTrue(task6.foperp('/', 6, 2, 3))
        self.assertFalse(task6.foperp('/', 1, 2, 4))

    def tearDown(self):
        """Finish"""
