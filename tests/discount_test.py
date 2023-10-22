import unittest

from src.discount import DiscountOption, SequelDiscount


class TestSequenceDiscount(unittest.TestCase):
    """
    A class that contains test cases for the SequelDiscount class.
    """

    def setUp(self):
        """
        A method that sets up the test case.
        """
        pass

    def tearDown(self):
        """
        A method that tears down the test case.
        """
        pass

    def test_get_discount(self):
        """
        A method that tests the get_discount() method of the SequelDiscount class.
        """
        s = SequelDiscount("Back to the Future", [
                       DiscountOption(2, 15), DiscountOption(3, 20)])
        self.assertEqual(s.get_discount(1), 0)
        self.assertEqual(s.get_discount(2), 15)
        self.assertEqual(s.get_discount(3), 20)
        self.assertEqual(s.get_discount(4), 20)
    
if __name__ == '__main__':
    unittest.main()
