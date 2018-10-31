

class Catalog():

    items_catalog = {}

    def add_item_catalog(self, name, price):
        self.name = name
        self.price = price
        self.items_catalog[self.name] = price

    def find_product(self, name):

        if name in self.items_catalog.keys():
            return name, self.items_catalog[name]
        else:
            return None

    def list_catalog(self):

        for product in self.items_catalog:
            print(product + ' : ' + str(self.items_catalog[product]))
        return self.items_catalog

    def clear_catalog(self):

        self.items_catalog.clear()

    def delete_element(self, name):

        del self.items_catalog[name]

    def modify_product(self, name, price):

        self.items_catalog[name] = price

    def find_price(self, product):
        return self.items_catalog[product]



class Carritus():

    items_carritus = {}

    def __init__(self, catalog):
        self.catalog = catalog

    def add_item(self, product, quantity=1):

        if self.catalog.find_product(product) is None:
            return None

        if not product in self.items_carritus:

            self.items_carritus[product] = quantity

        else:
            self.items_carritus[product] += quantity
        return "added"

    def list_items(self):

        if len(self.items_carritus) == 0:
            print ("No products in Carritus")

        for item in self.items_carritus:
            print("Product: " + item + " Quantity: " + str(self.items_carritus[item]))

        return self.items_carritus

    def clear(self):
        self.items_carritus.clear()

    def delete_item(self, product, quantity):

        if not product in self.items_carritus:
            return None

        else:
            self.items_carritus[product] -= quantity

        if self.items_carritus[product] < 0:
            self.items_carritus[product] = 0


    def calculate_total_price(self):
        total = 0
        for item in self.items_carritus:
            total += self.items_carritus[item] * self.catalog.find_price(item)

        return total
