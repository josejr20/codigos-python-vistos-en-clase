# TODO 1: crea una lambda sin parametros que devuelva "Reporte de productos".
get_title = lambda : "Reporte de productos"

# TODO 2: crea una lambda que calcule el cuadrado de un numero.
square = lambda x: x * x

# TODO 3: crea una lambda que calcule el subtotal usando precio y cantidad.
calculate_subtotal = lambda precio, cantidad: precio * cantidad

# TODO 4: crea una lambda que aplique 10% de descuento a un precio.
apply_discount = lambda precio: precio * 0.90

# TODO 5: crea una lambda que devuelva "Caro" si el precio es mayor o igual a 100.
# Si no, debe devolver "Economico".
classify_price = lambda precio: "Caro" if precio >= 100 else "Economico"

# TODO 6: crea una lista de precios.
prices = [55, 120.5, 88.8, 204.3, 39]

# TODO 7: crea una lambda que reciba una lista y devuelva solo precios mayores o iguales a 100.
get_high_prices = lambda lista: [precio for precio in lista if precio >= 100]

# TODO 8: crea una lambda que reciba una lista y devuelva todos los precios con 10% de descuento.
get_discounted_prices = lambda lista: [precio * 0.90 for precio in lista]

# TODO 9: crea una lista de productos como tuplas (nombre, precio).
products = [
    ("Chocolate", 12.50),
    ("Perfume", 210.00),
    ("Audífonos", 150.00),
    ("Planta", 35.00)
]

# TODO 10: ordena products por precio usando sorted() y key=lambda.
sorted_products = sorted(products, key=lambda producto: producto[1])

# TODO 11: obtiene el producto mas caro usando max() y key=lambda.
most_expensive_product = max(products, key=lambda producto: producto[1])

# TODO 12: muestra el titulo.
print(get_title())

# TODO 13: muestra el cuadrado de 5.
print(square(5))

# TODO 14: muestra el subtotal de precio 20 y cantidad 3.
print(calculate_subtotal(20, 3))

# TODO 15: muestra el precio 100 con descuento.
print(apply_discount(100))

# TODO 16: muestra la categoria del precio 120.
print(classify_price(120))

# TODO 17: muestra los precios altos.
print(get_high_prices(prices))

# TODO 18: muestra los precios con descuento.
print(get_discounted_prices(prices))

# TODO 19: muestra los productos ordenados.
print(sorted_products)

# TODO 20: muestra el producto mas caro.
print(most_expensive_product)

