import unittest
import random
import csv

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

class TestMergeSort(unittest.TestCase):
    def test_merge_sort(self):
        # Generar números aleatorios entre 0 y 10000
        cantidad_numeros = 3000
        numeros_originales = [random.randint(0, 10000) for _ in range(cantidad_numeros)]

        # Hacer una copia para ordenarla y comparar con la original
        numeros_ordenados = numeros_originales.copy()

        # Ordenar la copia utilizando Merge Sort
        merge_sort(numeros_ordenados)

        # Verificar que la lista ordenada es igual a la lista original ordenada
        self.assertEqual(sorted(numeros_originales), numeros_ordenados)

        # Guardar los números generados y ordenados en un archivo CSV
        with open('numeros_merge_sort.csv', 'w', newline='') as csvfile:
            fieldnames = ['Original', 'Ordenado']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for original, ordenado in zip(numeros_originales, numeros_ordenados):
                writer.writerow({'Original': original, 'Ordenado': ordenado})

if __name__ == '__main__':
    unittest.main()
