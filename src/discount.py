
class DiscountOption:
    """
    A class representing a discount option for a movie rental service.

    Attributes:
    - num_sequels (int): the number of sequels required to be rented to be eligible for the discount
    - discount_percent (float): the percentage discount offered for the rental if the customer is eligible

    Methods:
    - __str__(): returns a string representation of the DiscountOption object
    - __repr__(): returns a string representation of the DiscountOption object
    """
    def __init__(self, num_sequels: int, discount_percent: float):
        self.num_sequels = num_sequels
        self.discount_percent = discount_percent

    def __str__(self):
        return f"DiscountOption({self.num_sequels}, {self.discount_percent})"

    def __repr__(self):
        return self.__str__()


class SequelDiscount:
    """
    A class representing a discount for a series of sequels.

    Attributes:
    - sequel_name (str): The name of the sequel series.
    - discount_options (list[DiscountOption]): A list of DiscountOption objects representing the available discount options.
    """

    def __init__(self, sequel_name: str, discount_options: list[DiscountOption]):
        self.sequel_name = sequel_name
        self.discount_options = discount_options
        self.discount_options.sort(key=lambda x: x.num_sequels, reverse=True)

    def get_discount(self, num_sequels: int) -> float:
        """
        Returns the discount percentage for a given number of sequels.

        Args:
        - num_sequels (int): The number of sequels to calculate the discount for.

        Returns:
        - float: The discount percentage for the given number of sequels.
        """
        for option in self.discount_options:
            if num_sequels >= option.num_sequels:
                return option.discount_percent
        return 0

    def __str__(self):
        return f"SequelDiscount({self.sequel_name}, {self.discount_options})"
