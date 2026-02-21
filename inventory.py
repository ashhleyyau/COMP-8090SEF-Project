from datetime import datetime
from product import Product

class Record:
    # Records restock or sell operation
    def __init__(self, description, operation, quantity, new_quantity):
        self.__timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__description = description
        self.__operation = operation
        self.__quantity = quantity
        self.__new_quantity = new_quantity

    # Getters: Encapsulation
    def get_timestamp(self):
        return self.__timestamp

    def get_description(self):
        return self.__description

    def get_operation(self):
        return self.__operation

    def get_quantity(self):
        return self.__quantity

    # Magic method: string representation
    def __str__(self):
        return f"[{self.__timestamp}] {self.__operation}: {self.__description} {self.__quantity} quantity"

# Manages products and records
class Inventory:
    def __init__(self):
        self.__products = []
        self.__records = []

    # Core operations
    def add_product(self, product):
        self.__products.append(product)

    def restock_product(self, description, quantity):
        product = self.find_product(description)
        if product:
            product.set_quantity(product.get_quantity() + quantity)
            self.__records.append(Record(description, "Restock", quantity, product.get_quantity()))
            return True
        return False

    def sell_product(self, description, quantity):
        product = self.find_product(description)
        if product and product.get_quantity() >= quantity:
            product.set_quantity(product.get_quantity() - quantity)
            self.__records.append(Record(description, "Sell", quantity, product.get_quantity()))
            return True
        return False

    def delete_product(self, description):
        for product in self.__products:
            if product.get_description() == description:
                self.__products.remove(product)
                return True
        return False

    # Helper methods
    def find_product(self, description):
        for product in self.__products:
            if product.get_description() == description:
                return product
        return None

    def get_products(self):
        return self.__products.copy()

    def get_records(self):
        return self.__records.copy()

    def get_last_record(self, description):
        product_records = [r for r in self.__records if r.get_description() == description]
        if product_records:
            return product_records[-1]
        return None