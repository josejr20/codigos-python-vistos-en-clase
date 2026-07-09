# Ejercicio practico: lambdas para productos

## Instrucciones

Completa `exercise.py`.

El programa debe usar funciones lambda para trabajar con productos y precios.

No necesitas mostrar cada resultado con `print()`. Despues de completar cada TODO,
revisa el valor de las variables para ver que hizo cada lambda.

Debes:

1. crear una lambda sin parametros que devuelva `"Reporte de productos"`;
2. llamar la lambda del titulo y guardar el resultado;
3. crear una lambda que calcule el cuadrado de un numero;
4. llamar la lambda del cuadrado con `5`;
5. crear una lambda que calcule el subtotal de un producto usando precio y cantidad;
6. llamar la lambda del subtotal con precio `20` y cantidad `3`;
7. crear una lambda que aplique 10% de descuento a un precio;
8. llamar la lambda del descuento con `100`;
9. crear una lambda que diga si un precio es `"Caro"` o `"Economico"`;
10. llamar la lambda de clasificacion con `120`;
11. crear una lista de precios;
12. crear una lambda que reciba una lista y devuelva solo los precios mayores o iguales a 100;
13. llamar la lambda de precios altos con la lista de precios;
14. crear una lambda que reciba una lista y devuelva los precios con descuento;
15. llamar la lambda de descuentos con la lista de precios;
16. crear una lista de productos como tuplas `(nombre, precio)`;
17. ordenar los productos por precio usando `sorted()` y `key=lambda`;
18. obtener el producto mas caro usando `max()` y `key=lambda`.

Debes utilizar:

- `lambda`;
- lambdas con cero, uno y varios parametros;
- condicional dentro de una lambda;
- list comprehension dentro de una lambda;
- `sorted()` con `key=lambda`;
- `max()` con `key=lambda`.

## Valores esperados al revisar el resultado

```python
title  # 'Reporte de productos'
square_result  # 25
subtotal  # 60
discounted_price  # 90.0
price_category  # 'Caro'
prices  # [50, 120, 250, 80, 100]
high_prices  # [120, 250, 100]
discounted_prices  # [45.0, 108.0, 225.0, 72.0, 90.0]
products  # [('laptop', 2500), ('mouse', 50), ('monitor', 650), ('teclado', 80)]
sorted_products  # [('mouse', 50), ('teclado', 80), ('monitor', 650), ('laptop', 2500)]
most_expensive_product  # ('laptop', 2500)
```
