# TODO 1: crea una lista de numeros del 1 al 10.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# TODO 2: crea una lista con los cuadrados de numbers usando list comprehension.
squares = [x*x for x in numbers]

# TODO 3: crea una lista solo con los numeros pares.
evens = [x for x in numbers if x % 2 == 0]

# TODO 4: crea una lista solo con los numeros mayores que 5.
greater_than_five = [x for x in numbers if x > 5]

# TODO 5: crea una lista de etiquetas "Par" o "Impar".
labels = ["Par" if x % 2 == 0 else "Impar" for x in numbers]

# TODO 6: crea una lista donde los pares se dupliquen y los impares se conviertan en 0.
modified_numbers = [x*2 if x % 2 == 0 else 0 for x in numbers]

# TODO 7: crea una lista de nombres.
names = ["Carlos", "Antonio", "Jorge", "Jose", "Miguel"]

# TODO 8: crea una lista con los nombres en mayusculas.
uppercase_names = [name.upper() for name in names]

# TODO 9: crea una lista solo con los nombres que tengan mas de 4 caracteres.
long_names = [name for name in names if len(name) > 4]

# TODO 10: crea una lista de numeros pequeños y una lista de letras.
small_numbers = [6, 4, 9, 7, 5]
letters = ['g', 'k', 'l', 'a', 'd']

# TODO 11: crea pares (numero, letra) combinando small_numbers y letters con varios for.
number_letter_pairs = [(num, letter) for num in small_numbers for letter in letters]

# TODO 12: crea una lista de numeros y una lista de vocales.
more_numbers = [1, 2, 3, 4, 5, 6]
vowels = ['a', 'e', 'i', 'o', 'u']

# TODO 13: crea pares solo con numeros pares y vocales "a" y "e".
filtered_pairs = [(num, vowel) for num in more_numbers if num % 2 == 0 for vowel in vowels if vowel in ['a', 'e']]

# TODO 14: muestra numbers.
print(numbers)

# TODO 15: muestra squares.
print("Cuadrados:", squares)

# TODO 16: muestra evens.
print("Pares:", evens)

# TODO 17: muestra greater_than_five.
print("Mayores que 5:", greater_than_five)

# TODO 18: muestra labels.
print("Etiquetas:", labels)

# TODO 19: muestra modified_numbers.
print("Números modificados:", modified_numbers)

# TODO 20: muestra uppercase_names.
print("Nombres en mayúsculas:", uppercase_names)

# TODO 21: muestra long_names.
print("Nombres largos:", long_names)

# TODO 22: muestra number_letter_pairs.
print("Pares número-letra:", number_letter_pairs)

# TODO 23: muestra filtered_pairs.
print("Pares filtrados:", filtered_pairs)