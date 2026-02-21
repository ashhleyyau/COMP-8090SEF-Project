from abc import ABC, abstractmethod

class Item(ABC):
    @abstractmethod
    def get_cost(self):  # Return the cost of the item
        pass

# Product inherits from Item
class Product(Item):
    total_products = 0  # Class attribute: total number of products created
    _product_no = 1  # Class attribute: counter for auto‑generating product numbers

    # Magic method: constructor
    def __init__(self, supplier, description, cost, quantity, unit):
        # Private attributes: for encapsulation
        self.__product_no = f"A{Product._product_no:03d}"
        Product._product_no += 1
        self.__supplier = supplier
        self.__description = description
        self.__cost = cost
        self.__quantity = quantity
        self.__unit = unit
        Product.total_products += 1

    # Getters: Encapsulation
    def get_product_no(self):
        return self.__product_no

    def get_supplier(self):
        return self.__supplier

    def get_description(self):
        return self.__description

    def get_cost(self):
        return self.__cost

    @staticmethod
    def is_valid_cost(cost):  # Static method: check if the cost is positive
        return cost > 0

    def get_quantity(self):
        return self.__quantity

    def get_unit(self):
        return self.__unit

    def set_quantity(self, value):  # Setter: check if the quantity is positive
        if value >= 0:
            self.__quantity = value
        else:
            raise ValueError("Quantity must be a valid integer")

    # Polymorphism base method
    def get_selling_price(self):
        return self.__cost

    # Class method: access the class attribute total_products
    @classmethod
    def get_total_products(cls):  
        return cls.total_products

    # Magic method: compare the products by product no for sorting
    def __lt__(self, other): 
        return self.__product_no < other.__product_no

# Inherits from Product
class FreshFood(Product):
    def get_selling_price(self):  # Polymorphism: override with 20% markup
        return super().get_selling_price() * 1.2

class Groceries(Product):
    def get_selling_price(self):  # Polymorphism: override with 50% markup
        return super().get_selling_price() * 1.5

class Household(Product):
    def get_selling_price(self):  # Polymorphism: override with 40% markup
        return super().get_selling_price() * 1.4
