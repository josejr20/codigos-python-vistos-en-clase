# Ejercicio practico: args y kwargs

## Instrucciones

Completa `exercise.py`.

El programa debe practicar funciones que reciben argumentos variables con `*args`
y argumentos por clave con `**kwargs`.

No necesitas mostrar cada resultado con `print()`. Despues de completar cada TODO,
revisa el valor de las variables para ver que hizo cada funcion u operacion.

Debes:

1. crear una funcion que reciba `*args`;
2. sumar numeros usando `*args`;
3. crear una funcion que reciba `**kwargs`;
4. leer valores desde un diccionario creado con `**kwargs`;
5. desempaquetar una lista con `*` al llamar una funcion;
6. desempaquetar un diccionario con `**` al llamar una funcion;
7. combinar un argumento fijo, `*args` y `**kwargs` en una misma funcion;
8. desempaquetar el resultado de una funcion en varias variables.

Debes utilizar:

- `*args`;
- `**kwargs`;
- desempaquetado con `*`;
- desempaquetado con `**`;
- funciones;
- `return`;
- `for`;
- diccionarios;
- `len()`.

## Valores esperados al revisar el resultado

```python
collected_args  # ('lapiz', 'cuaderno', 'regla')
total_sum  # 30
profile  # {'name': 'Ana', 'age': 20, 'course': 'Python'}
profile_name  # 'Ana'
profile_course  # 'Python'
items  # ['monitor', 'teclado', 'mouse']
unpacked_items  # ('monitor', 'teclado', 'mouse')
profile_data  # {'city': 'Lima', 'active': True}
unpacked_profile  # {'city': 'Lima', 'active': True}
order  # ('Luis', ('lapiz', 'cuaderno'), {'priority': True, 'paid': False})
order_customer  # 'Luis'
order_items  # ('lapiz', 'cuaderno')
order_details  # {'priority': True, 'paid': False}
item_count  # 2
is_paid  # False
```
