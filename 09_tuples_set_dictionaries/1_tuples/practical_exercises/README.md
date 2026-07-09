# Ejercicio practico: tuplas y desempaquetado

## Instrucciones

Completa `exercise.py`.

El programa debe practicar creacion de tuplas, acceso por indice, slicing y desempaquetado.

No necesitas mostrar cada resultado con `print()`. Despues de completar cada TODO,
revisa el valor de las variables para ver que hizo cada operacion.

Debes:

1. crear tuplas simples;
2. desempaquetar una tupla en variables;
3. acceder a elementos usando indices positivos y negativos;
4. obtener partes de una tupla usando slicing;
5. usar desempaquetado extendido con `*`;
6. desempaquetar tuplas anidadas;
7. recorrer una tupla de pares desempaquetando cada par;
8. retornar multiples valores desde una funcion;
9. intercambiar variables usando desempaquetado de tuplas.

Debes utilizar:

- tuplas;
- indices;
- slicing;
- desempaquetado;
- desempaquetado extendido;
- tuplas anidadas;
- `for`;
- funciones;
- retorno multiple.

## Valores esperados al revisar el resultado

```python
student  # ('Ana', 18, 'Python')
student_name  # 'Ana'
student_age  # 18
student_course  # 'Python'
scores  # (15, 18, 20, 17, 19)
first_score  # 15
last_score  # 19
middle_scores  # (18, 20, 17)
first_grade  # 15
other_grades  # [18, 20, 17]
final_grade  # 19
points  # ((10, 20), (30, 40))
first_x  # 10
first_y  # 20
second_x  # 30
second_y  # 40
products  # (('lapiz', 2.5), ('cuaderno', 8.0), ('regla', 3.0))
formatted_products  # ['lapiz cuesta 2.5', 'cuaderno cuesta 8.0', 'regla cuesta 3.0']
min_score  # 15
max_score  # 20
left  # 'azul'
right  # 'rojo'
```

En el `for`, `product_summary` debe ir tomando valores como `"lapiz cuesta 2.5"`,
`"cuaderno cuesta 8.0"` y `"regla cuesta 3.0"`.
