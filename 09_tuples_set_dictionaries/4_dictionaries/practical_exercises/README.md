# Ejercicio practico: diccionarios

## Instrucciones

Completa `exercise.py`.

El programa debe practicar las operaciones principales con diccionarios: creacion,
acceso, modificacion, eliminacion, iteracion, metodos, comprehensions,
diccionarios anidados, combinacion, inversion, `zip()` y desempaquetado con `**`.

No necesitas mostrar cada resultado con `print()`. Despues de completar cada TODO,
revisa el valor de las variables para ver que hizo cada operacion.

Debes:

1. crear diccionarios literales, vacios y desde pares;
2. acceder a valores usando claves y `get()`;
3. agregar y actualizar claves;
4. eliminar elementos con `pop()`, `del`, `popitem()` y `clear()`;
5. comprobar si una clave existe con `in`;
6. usar `keys()`, `values()`, `items()` y `copy()`;
7. recorrer pares clave-valor con `for`;
8. crear diccionarios con comprehensions;
9. trabajar con diccionarios anidados;
10. combinar diccionarios con `**`;
11. invertir claves y valores;
12. crear un diccionario con `zip()`;
13. desempaquetar un diccionario con `**` al llamar una funcion.

Debes utilizar:

- diccionarios;
- claves y valores;
- `dict()`;
- `get()`;
- `update()`;
- `pop()`;
- `del`;
- `popitem()`;
- `clear()`;
- `in`;
- `keys()`;
- `values()`;
- `items()`;
- `copy()`;
- dict comprehensions;
- diccionarios anidados;
- `zip()`;
- `**`.

## Valores esperados al revisar el resultado

```python
product  # {'name': 'lapiz', 'price': 3.0, 'stock': 25}
sales_by_day  # {}
supplier  # {'brand': 'Faber', 'country': 'Peru'}
product_name  # 'lapiz'
product_category  # 'sin categoria'
removed_category  # 'utiles'
discontinued_product  # {}
removed_pair  # ('old_code', 'A1')
draft_product  # {}
has_stock  # True
product_keys  # ['name', 'price', 'stock']
product_values  # ['lapiz', 3.0, 25]
product_items  # [('name', 'lapiz'), ('price', 3.0), ('stock', 25)]
formatted_fields  # ['name: lapiz', 'price: 3.0', 'stock: 25']
product_copy  # {'name': 'lapiz', 'price': 3.0, 'stock': 25, 'status': 'activo'}
prices  # {'lapiz': 2.5, 'cuaderno': 8.0, 'regla': 3.0}
prices_with_tax  # {'lapiz': 2.95, 'cuaderno': 9.44, 'regla': 3.54}
affordable_prices  # {'lapiz': 2.5, 'regla': 3.0}
lapiz_stock  # 30
updated_lapiz_stock  # 40
base_product  # {'name': 'cuaderno', 'price': 8.0}
product_details  # {'stock': 12, 'category': 'papeleria'}
merged_product  # {'name': 'cuaderno', 'price': 8.0, 'stock': 12, 'category': 'papeleria'}
codes  # {'LPZ': 'lapiz', 'CDR': 'cuaderno'}
inverted_codes  # {'lapiz': 'LPZ', 'cuaderno': 'CDR'}
keys  # ['name', 'price', 'stock']
values  # ['mochila', 45.0, 5]
product_from_zip  # {'name': 'mochila', 'price': 45.0, 'stock': 5}
value_data  # {'price': 3.0, 'stock': 25}
inventory_value  # 75.0
```

En el `for`, `field_summary` debe ir tomando valores como `"name: lapiz"`,
`"price: 3.0"` y `"stock: 25"`.
