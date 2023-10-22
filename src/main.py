from movie import Movie
from discount import SequelDiscount, DiscountOption
from cart import ShoppingCart


# Sample movies and discounts
default_db = {
    'Back to the Future 1': Movie("Back to the Future 1", 15,
                                  sequel_name="Back to the Future"),  # Marking as sequel
    'Back to the Future 2': Movie("Back to the Future 2", 15,
                                  sequel_name="Back to the Future"),  # Marking as sequel
    'Back to the Future 3': Movie("Back to the Future 3", 15,
                                  sequel_name="Back to the Future")  # Marking as sequel
}

default_discounts = [
    SequelDiscount("Back to the Future", 
                   [DiscountOption(2, 15), DiscountOption(3, 20)]),
    SequelDiscount("Star trek", 
                   [DiscountOption(2, 15), DiscountOption(3, 20), DiscountOption(4, 25)])
    ]  # Sequel-specific discounts

# Sample shopping cart
cart = ShoppingCart()

# Applying discounts
for discount in default_discounts:
    cart.add_discount(discount)


if __name__ == "__main__":
    # Adding movies to the cart
    input_movie_names = []
    print("Enter the list of movies to calculate the total price\nEach of the movie name in a new line, press enter(empty line) to stop")
    print('Input:')
    while True:
        line = input()
        if line:
            input_movie_names.append(line)
        else:
            break
    for movie_name in input_movie_names:
        if movie_name in default_db:
            cart.add_movie(default_db[movie_name])
        else:
            cart.add_movie(Movie(movie_name, 20))    
    total_price = cart.calculate_total_price()
    print("Output:")
    print(total_price)
