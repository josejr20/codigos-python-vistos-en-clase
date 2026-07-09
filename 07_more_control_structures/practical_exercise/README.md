# Ejercicio practico: revision de productos

## Instrucciones

Completa `exercise.py`.

El programa debe revisar productos de una tienda usando estructuras de control con `for`.

No necesitas mostrar cada resultado con `print()`. Despues de completar cada TODO,
revisa el valor de las variables para ver que hizo cada ciclo u operacion.

Debes:

1. crear una lista de productos;
2. crear una lista de precios;
3. crear una lista de productos agotados;
4. recorrer los productos y saltar los agotados usando `continue`;
5. guardar los productos disponibles en una nueva lista;
6. buscar un producto usando `for...else`;
7. encontrar el primer producto caro usando `break`;
8. crear combinaciones de colores y tallas usando ciclos `for` anidados;
9. crear saludos para clientes usando `for in`;
10. recorrer los saludos creados.

Debes utilizar:

- `for`;
- `for...else`;
- `break`;
- `continue`;
- ciclos anidados;
- listas;
- `append()`;
- `enumerate()`.

## Valores esperados al revisar el resultado

```python
products  # ['laptop', 'tablet', 'smartphone', 'monitor', 'teclado']
prices  # [1200, 800, 1500, 650, 120]
out_of_stock  # ['tablet', 'monitor']
available_products  # ['laptop', 'smartphone', 'teclado']
search_product  # 'impresora'
search_result  # 'impresora no encontrado'
first_expensive_product  # 'laptop'
colors  # ['negro', 'blanco']
sizes  # ['S', 'M', 'L']
variants  # ['negro - S', 'negro - M', 'negro - L', 'blanco - S', 'blanco - M', 'blanco - L']
customers  # ['Ana', 'Luis', 'Marta']
greetings  # ['Hola, Ana', 'Hola, Luis', 'Hola, Marta']
```

En el ultimo `for`, `greeting` debe ir tomando valores como `"Hola, Ana"`,
`"Hola, Luis"` y `"Hola, Marta"`.
