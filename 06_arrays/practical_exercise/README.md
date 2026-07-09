# Ejercicio practico: inventario con listas

## Instrucciones

Completa `exercise.py`.

El programa debe representar un inventario de productos usando una lista.

No necesitas mostrar cada resultado con `print()`. Despues de completar cada TODO,
revisa el valor de las variables y de `inventory` para ver que hizo cada operacion.

Debes:

1. crear una lista inicial con `"lapiz"`, `"cuaderno"`, `"borrador"` y `"regla"`;
2. revisar el inventario inicial;
3. obtener el primer producto usando indice positivo;
4. obtener el ultimo producto usando indice negativo;
5. obtener los productos centrales usando slicing;
6. modificar `"cuaderno"` por `"agenda"`;
7. agregar `"mochila"` al final con `append()`;
8. insertar `"plumon"` en la posicion 2 con `insert()`;
9. agregar `"colores"` y `"tijera"` con `extend()`;
10. eliminar `"borrador"` con `remove()`;
11. revisar el inventario actualizado;
12. vender el primer producto usando `pop(0)`;
13. comprobar si `"regla"` existe en el inventario;
14. obtener el indice de `"regla"`;
15. obtener la cantidad de productos con `len()`;
16. obtener los primeros tres productos y los ultimos dos usando slicing;
17. recorrer los productos finales usando `for` y `enumerate()`.

Debes utilizar:

- una lista;
- indices positivos y negativos;
- slicing;
- `append()`;
- `insert()`;
- `extend()`;
- `remove()`;
- `pop()`;
- `in`;
- `index()`;
- `len()`;
- `for`;
- `enumerate()`.

## Valores esperados al revisar el resultado

```python
inventory  # ['agenda', 'plumon', 'regla', 'mochila', 'colores', 'tijera']
first_product  # 'lapiz'
last_product  # 'regla'
middle_products  # ['cuaderno', 'borrador']
sold_product  # 'lapiz'
has_rule  # True
rule_index  # 2
product_count  # 6
first_three  # ['agenda', 'plumon', 'regla']
last_two  # ['colores', 'tijera']
```

En el `for`, `numbered_product` debe ir tomando valores como `"1. agenda"`,
`"2. plumon"`, `"3. regla"`, etc.
