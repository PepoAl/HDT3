import unittest
import random
import csv

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

class TestQuickSort(unittest.TestCase):
    def test_quick_sort(self):
        # Generar números aleatorios entre 0 y 10000
        cantidad_numeros = 3000
        numeros_originales = [random.randint(0, 10000) for _ in range(cantidad_numeros)]

        # Hacer una copia para ordenarla y comparar con la original
        numeros_ordenados = numeros_originales.copy()

        # Ordenar la copia utilizando Quicksort
        quicksort(numeros_ordenados, 0, len(numeros_ordenados) - 1)

        # Verificar que la lista ordenada es igual a la lista original ordenada
        self.assertEqual(sorted(numeros_originales), numeros_ordenados)

        # Guardar los números generados y ordenados en un archivo CSV
        with open('numeros_quicksort.csv', 'w', newline='') as csvfile:
            fieldnames = ['Original', 'Ordenado']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for original, ordenado in zip(numeros_originales, numeros_ordenados):
                writer.writerow({'Original': original, 'Ordenado': ordenado})

if __name__ == '__main__':
    unittest.main()
