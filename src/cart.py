from discount import SequelDiscount, DiscountOption
from movie import Movie


class ShoppingCart:
    """
    A class representing a shopping cart that can hold movies and discounts.

    Attributes:
    movies (list[Movie]): A list of Movie objects representing the movies in the cart.
    discounts (list[SequelDiscount]): A list of SequelDiscount objects representing the discounts in the cart.
    """

    def __init__(self):
        """
        Initializes a new instance of the ShoppingCart class.
        """
        self.movies: list[Movie] = []
        self.discounts: list[SequelDiscount] = []

    def add_movie(self, movie: Movie):
        """
        Adds a movie to the cart.

        Args:
        movie (Movie): A Movie object representing the movie to add to the cart.
        """
        self.movies.append(movie)

    def add_discount(self, discount: SequelDiscount):
        """
        Adds a discount to the cart.

        Args:
        discount (SequelDiscount): A SequelDiscount object representing the discount to add to the cart.
        """
        self.discounts.append(discount)

    def get_discount(self, name: str) -> SequelDiscount or None:
        """
        Gets a discount from the cart by name.

        Args:
        name (str): A string representing the name of the discount to get.

        Returns:
        SequelDiscount: A SequelDiscount object representing the discount with the specified name, or None if not found.
        """
        for discount in self.discounts:
            if discount.sequel_name == name:
                return discount
        return None

    def calculate_total_price(self) -> float:
        """
        Calculates the total price of the movies in the cart, taking into account any discounts.

        Returns:
        float: A float representing the total price of the movies in the cart.
        """
        movie_counts = {}
        sequel_counts = {}
        total_price = 0

        # Count the number of each movie in the cart
        for movie in self.movies:
            movie_counts[movie.title] = movie_counts.get(movie.title, 0) + 1
            if movie.is_sequel:
                sequel_counts[movie.sequel_name] = sequel_counts.get(
                    movie.sequel_name, 0) + 1

        for movie in self.movies:
            if movie.is_sequel:
                discount = self.get_discount(movie.sequel_name)
                if discount:
                    price = (
                        movie.price * (100-discount.get_discount(sequel_counts[movie.sequel_name])) / 100)
                    # print(f"Price for {movie.title} after discount is {price}")
                    total_price += price
                else:
                    total_price += movie.price
            else:
                total_price += movie.price

        return round(total_price, 2)  # Convert total price to an integer
