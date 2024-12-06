import unittest


class StringUtils:
    def reverse_string(self, s):
        #return s   Nenhuma operação em string
        return s[:: -1]  # Retorna a string invertida

    def is_palindrome(self, s):
        return s == s[::-1]  # OK

class TestStringUtils(unittest.TestCase):
    def setUp(self):
        self.utils = StringUtils()

    def test_reverse_string(self):
        self.assertEqual(self.utils.reverse_string("daniel"), "leinad")
        self.assertEqual(self.utils.reverse_string("oi"), "io")
        self.assertEqual(self.utils.reverse_string(""), "")

    def test_is_palindrome(self):
        self.assertTrue(self.utils.is_palindrome("hannah"))
        self.assertTrue(self.utils.is_palindrome("natan"))
        self.assertFalse(self.utils.is_palindrome("daniel"))
        self.assertTrue(self.utils.is_palindrome(""))

if __name__ == "__main__":
    unittest.main()
