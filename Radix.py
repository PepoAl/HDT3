import unittest
import random
import csv

def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]

def radixSort(array):
    max_element = max(array)

    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10

class TestRadixSort(unittest.TestCase):
    def test_radix_sort(self):
        # Generar números aleatorios entre 0 y 10000
        cantidad_numeros = 3000
        numeros_originales = [random.randint(0, 10000) for _ in range(cantidad_numeros)]

        # Hacer una copia para ordenarla y comparar con la original
        numeros_ordenados = numeros_originales.copy()

        # Ordenar la copia utilizando Radix Sort
        radixSort(numeros_ordenados)

        # Verificar que la lista ordenada es igual a la lista original ordenada
        self.assertEqual(sorted(numeros_originales), numeros_ordenados)

        # Guardar los números generados y ordenados en un archivo CSV
        with open('numeros_radix_sort.csv', 'w', newline='') as csvfile:
            fieldnames = ['Original', 'Ordenado']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for original, ordenado in zip(numeros_originales, numeros_ordenados):
                writer.writerow({'Original': original, 'Ordenado': ordenado})

if __name__ == '__main__':
    unittest.main()
