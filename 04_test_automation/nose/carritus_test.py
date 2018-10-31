from carritus import Catalog
from carritus import Carritus

catalog = Catalog()

catalog.add_item_catalog('potatoes', 2.5)

catalog.add_item_catalog('tralara', 1.5)

catalog.list_catalog()

carrito = Carritus(catalog)

carrito.add_item('potatoes', 2)
carrito.list_items()

carrito.add_item('potatoes', 3)
carrito.list_items()


carrito.delete_item('potatoes', 1)
carrito.list_items()


carrito.delete_item('potatoes', 5)
carrito.list_items()

carrito.clear()
carrito.list_items()

carrito.add_item('potatoes', 2)
carrito.add_item('tralara', 3)

total = carrito.calculate_total_price()
print(total)


