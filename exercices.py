class Item:
    def __init__(self, price, weight):
        """Initializes a new item with a given price and weight."""
        self.price = price
        self.weight = weight

# Example of code using the class
i = Item(10, 20)

# Accessing the price and weight of the item
print(f"Price: {i.price}, Weight: {i.weight}")
