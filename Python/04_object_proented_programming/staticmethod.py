class Property:
    def __init__(self, x=None, square=None, cubic=None):
        self.x = x
        self.square = square
        self.cubic = cubic

    @staticmethod
    def prompt_init(x):
        square = x ** 2
        cubic = x ** 3
        return Property(x, square, cubic)

    def __repr__(self):
        return f"PROPERTY DETAILS:\n\tx: {self.x}, square: {self.square}, cubic: {self.cubic}"


if __name__ == "__main__":
    property = Property.prompt_init(2)
    print(property)
