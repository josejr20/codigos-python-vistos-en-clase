# TODO 1: crea una lista con numeros del 1 al 10 usando range().
numbers = list(range(1, 11))

# TODO 2: crea una lista con numeros pares del 2 al 20 usando range().
even_numbers = list(range(2, 21, 2))

# TODO 3: crea una lista descendente del 10 al 1 usando range().
countdown = list(range(10, 0, -1))

# TODO 4: crea una lista con multiplos de 5 desde 5 hasta 50 usando range().
multiples_of_five = list(range(5, 51, 5))

# TODO 5: obtiene el primer numero de numbers usando indice positivo.
first_number = numbers[0]

# TODO 6: obtiene el ultimo numero de numbers usando indice negativo.
last_number = numbers[-1]

# TODO 7: obtiene los primeros cinco numeros usando slicing.
first_five = numbers[:5]

# TODO 8: suma los numeros del 1 al 10 usando un ciclo for y un acumulador.
total = 0
for num in range(1, 11):
    total += num

# TODO 9: cuenta cuantos numeros pares hay entre 1 y 20 usando range() y len().
even_count = len(even_numbers)

# TODO 10: muestra numbers.
print("Números del 1 al 10:", numbers)

# TODO 11: muestra even_numbers.
print("Números pares del 2 al 20:", even_numbers)

# TODO 12: muestra countdown.
print("Cuenta regresiva:", countdown)

# TODO 13: muestra multiples_of_five.
print("Multiplos de 5:", multiples_of_five)

# TODO 14: muestra first_number.
print("Primer numero:", first_number)

# TODO 15: muestra last_number.
print("Ultimo numero:", last_number)

# TODO 16: muestra first_five.
print("Primeros cinco numeros:", first_five)

# TODO 17: muestra total.
print("Suma total:", total)

# TODO 18: muestra el titulo "Tabla del 3:".
print("Tabla del 3:")

# TODO 19: muestra la tabla del 3 desde 3 x 1 hasta 3 x 10 usando range().
for i in range(1, 11):
    print(f"3 x {i} = {3 * i}")

# TODO 20: muestra even_count.
print("Cantidad de números pares:", even_count)