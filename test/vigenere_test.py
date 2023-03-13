import unittest
import random
import string
import sys

sys.path.append('../src')

from vigenere import Vigenere


class TestVigenere(unittest.TestCase):
    def test_convert_string_to_list(self):
        vigenere = Vigenere()
        self.assertEqual(['A', 'Z', 'x', 'D', 'l', 'p'], vigenere.convert_string_to_list("AZxDlp"))

    def test_make_key_list_from_keyword(self):
        vigenere = Vigenere()
        self.assertEqual(['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C'],
                         vigenere.make_key_list_from_keyword(["A", "B", "C"],
                                                             ['1', '2', '3', '4', '5', '6', '7', '8', '9']))

    def test_write_read_file(self):
        vigenere = Vigenere()
        random_string1 = ''.join(random.choices(string.ascii_lowercase, k=5))
        random_string2 = ''.join(random.choices(string.ascii_lowercase, k=5))
        random_content = "{}\n{}".format(random_string1, random_string2)
        vigenere.write_file("test.txt", random_content)
        self.assertEqual(random_content, vigenere.read_file("test.txt"))

    def test_encrypt_string(self):
        vigenere = Vigenere()
        self.assertEqual("¥§a", vigenere.encrypt_string("abc", ['D', 'E', chr(254)]))

    def test_decrypt_string(self):
        vigenere = Vigenere()
        self.assertEqual("abc", vigenere.decrypt_string("¥§a", ['D', 'E', chr(254)]))


if __name__ == '__main__':
    unittest.main()
