import unittest

class FibonacciGenerator:
    def generate_sequence(self, n):
        """
        Gera os primeiros n números da sequência de Fibonacci.
        :param n: Número de elementos na sequência.
        :return: Lista contendo a sequência de Fibonacci.
        """
        if n <= 0:
            return []  # OK: Sequência vazia para entrada inválida.
        
        sequence = [0, 1]
        #for _ in range(n):
            #next_number = sequence[-1] + sequence[-1]  # BUG: Deve ser sequence[-1] + sequence[-2].
        for _ in range(n - 2): #loop ajustado
            next_number = sequence[-1] + sequence[-2] #loop corrigido
            sequence.append(next_number)
        return sequence[:n]  # OK: Retorna apenas os primeiros n números.

    def get_nth_number(self, n):
        """
        Retorna o enésimo número da sequência de Fibonacci (baseado em índice 1).
        :param n: Posição do número na sequência (1-indexed).
        :return: Número correspondente na sequência.
        """
        if n <= 0:
            return None  # OK: Entrada inválida retorna None.
        elif n == 1:
            return 0  # OK: Primeiro número da sequência é 0.
        elif n == 2:
            return 1  # OK: Segundo número da sequência é 1.
        
        a, b = 0, 1
        for _ in range(n - 2):  # BUG: Deve ser range(n - 1).
            a, b = b, a+b #ajuste do loop para calcular de forma correta
        return b

class TestFibonacciGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = FibonacciGenerator()

    def test_generate_sequence(self):
        self.assertEqual(self.generator.generate_sequence(5), [0, 1, 1, 2, 3])
        self.assertEqual(self.generator.generate_sequence(1), [0])
        self.assertEqual(self.generator.generate_sequence(0), [])
        self.assertEqual(self.generator.generate_sequence(-1), [])

    def test_get_nth_number(self):
        self.assertEqual(self.generator.get_nth_number(1), 0)
        self.assertEqual(self.generator.get_nth_number(2), 1)
        self.assertEqual(self.generator.get_nth_number(6), 5)
        self.assertIsNone(self.generator.get_nth_number(0))
        self.assertIsNone(self.generator.get_nth_number(-1))

if __name__ == "__main__":
    unittest.main()
