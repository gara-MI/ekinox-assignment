class Movie:
    def __init__(self, title: str, price: float = 20.0, sequel_name: str = None):
        self.title = title
        self.price = price
        self.sequel_name = sequel_name
        self.is_sequel = sequel_name is not None
