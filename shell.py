
class ShellSort:
    @staticmethod
    def sort(arr):
        n = len(arr)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            gap //= 2

import unittest
import random
import csv

class TestShellSort(unittest.TestCase):
    def test_shell_sort(self):
        # Generar números aleatorios entre 0 y 10000
        cantidad_numeros = 3000
        numeros_originales = [random.randint(0, 10000) for _ in range(cantidad_numeros)]

        # Hacer una copia para ordenarla y comparar con la original
        numeros_ordenados = numeros_originales.copy()

        # Ordenar la copia utilizando ShellSort
        ShellSort.sort(numeros_ordenados)

        # Verificar que la lista ordenada es igual a la lista original ordenada
        self.assertEqual(sorted(numeros_originales), numeros_ordenados)

        # Guardar los números generados y ordenados en un archivo CSV
        with open('numeros.csv', 'w', newline='') as csvfile:
            fieldnames = ['Original', 'Ordenado']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for original, ordenado in zip(numeros_originales, numeros_ordenados):
                writer.writerow({'Original': original, 'Ordenado': ordenado})

if __name__ == '__main__':
    unittest.main()
