import unittest

from src.logica.Operaciones import Operaciones


class Pruebas(unittest.TestCase):
    def test_media_listaVacia_lanzaExcepcion(self):
        # Arrange
        numeros = []
        operacion = Operaciones(numeros)

        # Assert
        with self.assertRaises(ValueError):
            operacion.calcularMedia()

    def test_media_unNumero_retornaElNumero(self):
        # Arrange
        numeros = [3.5]
        resultadoEsperado = 3.5
        operacion = Operaciones(numeros)

        # Act
        resultadoActual = operacion.calcularMedia()

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)
