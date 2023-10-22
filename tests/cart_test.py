import unittest

from src.discount import DiscountOption, SequelDiscount
from src.cart import ShoppingCart
from src.movie import Movie


class TestSequenceDiscount(unittest.TestCase):
    """
    A class that contains test cases for the ShoppingCart class.
    """

    def setUp(self):
        """
        A method that sets up the test case.
        """
        self.cart = ShoppingCart()
        self.movies = [Movie("Back to the Future 1", 15,
                            sequel_name="Back to the Future"),
                       Movie("Back to the Future 2", 15,
                             sequel_name="Back to the Future"),
                       Movie("Back to the Future 3", 15,
                             sequel_name="Back to the Future"),
                       Movie("La chèvre", 20)]
        self.discount = [
            SequelDiscount("Back to the Future",[DiscountOption(2, 15), DiscountOption(3, 20)]),
            SequelDiscount("The Lord of the Rings",[DiscountOption(2, 15), DiscountOption(3, 30)]),
        ]
        self.cart.add_discount(self.discount[0])
        self.cart.add_movie(self.movies[0])
        self.cart.add_movie(self.movies[1])
        self.cart.add_movie(self.movies[2])
        self.cart.add_movie(self.movies[3])

    def tearDown(self):
        """
        A method that tears down the test case.
        """
        pass

    def test_calculate_total_price(self):
        """
        A method that tests the calculate_total_price() method of the ShoppingCart class.
        """
        self.assertEqual(self.cart.calculate_total_price(), 56.0)
        self.cart.add_movie(self.movies[0]) # adding the same movie of the same sequel to test discount
        self.assertEqual(self.cart.calculate_total_price(), 68.0)
        self.cart.add_movie(Movie('Star trek', 30)) # adding extra movie to test discount
        self.assertEqual(self.cart.calculate_total_price(), 98.0)
    
    def test_get_discount(self):
        """
        A method that tests the get_discount() method of the ShoppingCart class.
        """
        self.assertEqual(self.cart.get_discount('Back to the Future'), self.discount[0])
        self.assertIsNone(self.cart.get_discount('The Lord of the Rings'))
        self.cart.add_discount(self.discount[1])
        self.assertEqual(self.cart.get_discount('The Lord of the Rings'), self.discount[1])
        self.assertEqual(self.cart.get_discount('Back to the Future'), self.discount[0])
        
    

if __name__ == '__main__':
    unittest.main()
