# TODO 1: crea una lista de productos.
products = ['alfajor', 'galleta', 'chocoteja', 'chizito', 'yogurt']

# TODO 2: crea una lista de precios.
prices = [1.50, 0.80, 2.50, 0.50, 3.50]

# TODO 3: crea una lista de productos agotados.
out_of_stock = ['alfajor', 'chocoteja']

# TODO 4: crea una lista vacia para guardar productos disponibles.
available_products = []

# TODO 5: recorre products. Si el producto esta en out_of_stock, usa continue.
# Si esta disponible, agregalo a available_products.
for product in products:
    if product in out_of_stock:
        continue
    available_products.append(product)

# TODO 6: crea search_product con el valor "impresora".
search_product = "galleta"

# TODO 7: busca search_product dentro de products usando for...else.
# Si lo encuentras, guarda "<producto> encontrado" en search_result y usa break.
# Si el ciclo termina sin break, guarda "<producto> no encontrado" en search_result.
for product in products:
    if product == search_product:
        search_result = f"{product} encontrado"
        break
else:
    search_result = f"{search_product} no encontrado"

# TODO 8: busca el primer producto con precio mayor que 1000 usando enumerate() y break.
# Guarda el producto en first_expensive_product.
first_expensive_product = None
for index, price in enumerate(prices):
    if price > 1000:
        first_expensive_product = products[index]
        break

# TODO 9: crea una lista de colores y una lista de tallas.
colors = ["rojo", "azul", "morado", "negro"]
sizes = ["S", "M", "L"]

# TODO 10: crea una lista vacia para guardar variantes.
variants = []

# TODO 11: usa ciclos for anidados para crear variantes con el formato "color - talla".
for color in colors:
    for size in sizes:
        variants.append(f"{color} - {size}")


# TODO 12: crea una lista de clientes.
customers = ["Jose", "Jorge", "Angela"]

# TODO 13: crea una lista vacia para guardar saludos.
greetings = []

# TODO 14: recorre customers y agrega saludos con el formato "Hola, <cliente>".
for customer in customers:
    greetings.append(f"Hola, {customer}")

# TODO 15: muestra available_products.
print("Productos disponibles:", available_products)

# TODO 16: muestra search_result.
print("Resultado de busqueda:", search_result)

# TODO 17: muestra first_expensive_product.
print("Primer producto caro:", first_expensive_product)

# TODO 18: muestra variants.
print("Variantes:", variants)

# TODO 19: muestra el titulo "Saludos:".
print("Saludos:")

# TODO 20: recorre greetings y muestra cada saludo.
for greeting in greetings:
    print(greeting)

