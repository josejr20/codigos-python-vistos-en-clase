# Ejercicio practico: clases y objetos

## Instrucciones

Completa `exercise.py`.

El programa debe practicar la creacion de clases, objetos, atributos, metodos y
comparacion de objetos.

No necesitas mostrar cada resultado con `print()`. Despues de completar cada TODO,
revisa el valor de las variables para ver que hizo cada operacion.

Debes:

1. crear una clase `Product`;
2. crear un metodo `__init__`;
3. guardar atributos en `self`;
4. crear objetos desde una clase;
5. acceder a atributos de un objeto;
6. modificar atributos;
7. crear y llamar metodos de instancia;
8. crear y llamar un metodo de clase con `@classmethod`;
9. crear y llamar un metodo estatico con `@staticmethod`;
10. comparar objetos con `__eq__`;
11. recorrer una lista de objetos.

Debes utilizar:

- `class`;
- `__init__`;
- `self`;
- atributos;
- objetos;
- metodos de instancia;
- `@classmethod`;
- `@staticmethod`;
- `__eq__`;
- `isinstance()`;
- `for`;
- listas.

## Valores esperados al revisar el resultado

```python
product_name  # 'lapiz'
product_price  # 2.5
product_stock  # 30
product_a.stock  # 25
subtotal_value  # 10.0
available  # True
product_b.name  # 'cuaderno'
product_b.price  # 8.0
product_b.stock  # 12
discounted_price  # 90.0
product_c.name  # 'lapiz'
product_c.price  # 3.0
product_c.stock  # 10
same_product  # True
product_summaries  # ['lapiz: 2.5 (25)', 'cuaderno: 8.0 (12)', 'lapiz: 3.0 (10)']
```

En el `for`, `product_summary` debe ir tomando valores como `"lapiz: 2.5 (25)"`,
`"cuaderno: 8.0 (12)"` y `"lapiz: 3.0 (10)"`.
