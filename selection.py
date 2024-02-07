import unittest
import random
import csv

def selection_sort(arr, ascending=True):
    n = len(arr)

    for i in range(n):
        extreme_index = i
        for j in range(i + 1, n):
            if ascending:
                condition = arr[j] < arr[extreme_index]
            else:
                condition = arr[j] > arr[extreme_index]

            if condition:
                extreme_index = j

        arr[i], arr[extreme_index] = arr[extreme_index], arr[i]

class TestSelectionSort(unittest.TestCase):
    def test_selection_sort_ascending(self):
        # Generar números aleatorios entre 0 y 10000
        cantidad_numeros = 3000
        numeros_originales = [random.randint(0, 10000) for _ in range(cantidad_numeros)]

        # Hacer una copia para ordenarla y comparar con la original
        numeros_ordenados = numeros_originales.copy()

        # Ordenar la copia utilizando Selection Sort en orden ascendente
        selection_sort(numeros_ordenados, ascending=True)

        # Verificar que la lista ordenada es igual a la lista original ordenada
        self.assertEqual(sorted(numeros_originales), numeros_ordenados)

        # Guardar los números generados y ordenados en un archivo CSV
        with open('numeros_selection_sort_ascending.csv', 'w', newline='') as csvfile:
            fieldnames = ['Original', 'Ordenado']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for original, ordenado in zip(numeros_originales, numeros_ordenados):
                writer.writerow({'Original': original, 'Ordenado': ordenado})

    def test_selection_sort_descending(self):
        # Generar números aleatorios entre 0 y 10000
        cantidad_numeros = 3000
        numeros_originales = [random.randint(0, 10000) for _ in range(cantidad_numeros)]

        # Hacer una copia para ordenarla y comparar con la original
        numeros_ordenados = numeros_originales.copy()

        # Ordenar la copia utilizando Selection Sort en orden descendente
        selection_sort(numeros_ordenados, ascending=False)

        # Verificar que la lista ordenada es igual a la lista original ordenada en orden descendente
        self.assertEqual(sorted(numeros_originales, reverse=True), numeros_ordenados)

        # Guardar los números generados y ordenados en un archivo CSV
        with open('numeros_selection_sort_descending.csv', 'w', newline='') as csvfile:
            fieldnames = ['Original', 'Ordenado']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for original, ordenado in zip(numeros_originales, numeros_ordenados):
                writer.writerow({'Original': original, 'Ordenado': ordenado})

if __name__ == '__main__':
    unittest.main()
