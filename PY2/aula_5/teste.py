import unittest

class Teste(unittest.TestCase):
    def testeA(self):
        x = 1
        x2 = 1
        self.assertEqual(x,x2)

    def testeB(self):
        valor = True
        self.assertTrue(valor, 'Teste unitário retornou inválido!')