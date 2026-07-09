# Ejercicio practico: list comprehensions

## Instrucciones

Completa `exercise.py`.

El programa debe crear nuevas listas usando list comprehensions.

No necesitas mostrar cada resultado con `print()`. Despues de completar cada TODO,
revisa el valor de las variables para ver que hizo cada comprehension.

Debes:

1. crear una lista de numeros del 1 al 10;
2. crear una lista con los cuadrados de esos numeros;
3. crear una lista solo con los numeros pares;
4. crear una lista solo con los numeros mayores que 5;
5. crear una lista de etiquetas `"Par"` o `"Impar"`;
6. crear una lista donde los pares se dupliquen y los impares se conviertan en `0`;
7. crear una lista de nombres en mayusculas;
8. crear una lista de nombres que tengan mas de 4 caracteres;
9. crear pares `(numero, letra)` combinando numeros y letras con varios `for`;
10. crear pares solo con numeros pares y vocales `"a"` y `"e"`.

Debes utilizar:

- list comprehensions simples;
- list comprehensions con `if`;
- list comprehensions con `if/else`;
- metodos de strings dentro de una comprehension;
- multiples `for` dentro de una comprehension.

## Valores esperados al revisar el resultado

```python
numbers  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
evens  # [2, 4, 6, 8, 10]
greater_than_five  # [6, 7, 8, 9, 10]
labels  # ['Impar', 'Par', 'Impar', 'Par', 'Impar', 'Par', 'Impar', 'Par', 'Impar', 'Par']
modified_numbers  # [0, 4, 0, 8, 0, 12, 0, 16, 0, 20]
names  # ['Ana', 'Luis', 'Marcela', 'Jose']
uppercase_names  # ['ANA', 'LUIS', 'MARCELA', 'JOSE']
long_names  # ['Marcela']
small_numbers  # [1, 2, 3]
letters  # ['a', 'b']
number_letter_pairs  # [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b'), (3, 'a'), (3, 'b')]
more_numbers  # [1, 2, 3, 4]
vowels  # ['a', 'e', 'i']
filtered_pairs  # [(2, 'a'), (2, 'e'), (4, 'a'), (4, 'e')]
```
