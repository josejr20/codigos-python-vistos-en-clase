# Ejercicio practico: secuencias con range

## Instrucciones

Completa `exercise.py`.

El programa debe crear y recorrer secuencias numericas usando `range()`.

No necesitas mostrar cada resultado con `print()`. Despues de completar cada TODO,
revisa el valor de las variables para ver que hizo cada operacion.

Debes:

1. crear una lista con numeros del 1 al 10;
2. crear una lista con numeros pares del 2 al 20;
3. crear una lista descendente del 10 al 1;
4. crear una lista con multiplos de 5 desde 5 hasta 50;
5. obtener el primer numero y el ultimo numero de la lista del 1 al 10;
6. obtener los primeros cinco numeros usando slicing;
7. sumar los numeros del 1 al 10 usando un ciclo `for`;
8. contar cuantos numeros pares hay entre 1 y 20 usando `range()`;
9. crear la tabla del 3 desde `3 x 1` hasta `3 x 10`.

Debes utilizar:

- `range()`;
- `list()`;
- indices;
- slicing;
- `for`;
- acumuladores;
- `len()`.

## Valores esperados al revisar el resultado

```python
numbers  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
countdown  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
multiples_of_five  # [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
first_number  # 1
last_number  # 10
first_five  # [1, 2, 3, 4, 5]
total  # 55
even_count  # 10
```

En el ultimo `for`, `multiplication_line` debe ir tomando valores como
`"3 x 1 = 3"`, `"3 x 2 = 6"`, `"3 x 3 = 9"`, etc.
