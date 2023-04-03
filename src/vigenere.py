import getopt
import sys


def print_usage():
    print('vigenere.py -k <keyword> [--encrypt] [--decrypt] -p <plaintextfile> -c <ciphertextfile>')
    sys.exit()


class Vigenere:
    def __init__(self, argv=None):
        self.ciphertextfile = None
        self.plaintextfile = None
        self.is_decrypt = None
        self.is_encrypt = None
        self.keyword = None

        if argv is not None:
            self.parse_arguments(argv)

    def parse_arguments(self, argv):
        try:
            opts, args = getopt.getopt(argv, "hedk:p:c:", ["encrypt", "decrypt",
                                                           "keyword=", "plaintextfile=",
                                                           "ciphertextfile=", ])
            for opt, arg in opts:
                if opt == '-h':
                    print_usage()
                elif opt in ("-k", "--keyword"):
                    self.keyword = arg
                elif opt in ("-e", "--encrypt"):
                    self.is_encrypt = True
                    self.is_decrypt = False
                elif opt in ("-d", "--decrypt"):
                    self.is_encrypt = False
                    self.is_decrypt = True
                elif opt in ("-p", "--plaintextfile"):
                    self.plaintextfile = arg
                elif opt in ("-c", "--ciphertextfile"):
                    self.ciphertextfile = arg
        except getopt.GetoptError:
            print_usage()

        if self.keyword is None or self.plaintextfile is None or self.ciphertextfile is None:
            print_usage()

    def perform_operation(self):
        keyword_list = self.convert_string_to_list(self.keyword)

        if self.is_encrypt:
            print("Encrypting contents of {} into {}".format(self.plaintextfile, self.ciphertextfile))
            plaintext = self.read_file(self.plaintextfile)
            plaintext_list = self.convert_string_to_list(plaintext)
            key_list = self.make_key_list_from_keyword(keyword_list, plaintext_list)
            ciphertext = self.encrypt_string(plaintext_list, key_list)
            self.write_file(self.ciphertextfile, ciphertext)
        else:
            print("Decrypting contents of {} into {}".format(self.ciphertextfile, self.plaintextfile))
            ciphertext = self.read_file(self.ciphertextfile)
            ciphertext_list = self.convert_string_to_list(ciphertext)
            key_list = self.make_key_list_from_keyword(keyword_list, ciphertext_list)
            plaintext = self.decrypt_string(ciphertext_list, key_list)
            self.write_file(self.plaintextfile, plaintext)

    def convert_string_to_list(self, string_to_convert):

        char_list = []
        for char in string_to_convert:
            char_list.append(char)
        return char_list

    def make_key_list_from_keyword(self, keyword_list, text_list):
        key_list = []
        i = 0
        for character in text_list:
            if character.isalnum():
                key_list.append(keyword_list[i % len(keyword_list)])
                i += 1
            else:
                key_list.append('')
        return key_list

    def read_file(self, filename):
        with open(filename, 'r') as file:
            contents = file.read()
        return contents

    def write_file(self, filename, contents):
        with open(filename, 'w') as file:
            file.write(contents)

    def encrypt_string(self, plaintext_list, key_list):
        ciphertext_list = []
        for i in range(len(plaintext_list)):
            if plaintext_list[i].isalpha():
                ciphertext_list.append(chr((ord(plaintext_list[i]) + ord(key_list[i])) % 256))
            else:
                ciphertext_list.append('')
        ciphertext = ''.join(ciphertext_list)
        return ciphertext

    def decrypt_string(self, ciphertext_list, key_list):
        decrypted_list = []
        for i, char in enumerate(ciphertext_list):
            key_char = key_list[i % len(key_list)]
            decrypted_char = chr((ord(char) - ord(key_char)) % 256)
            decrypted_list.append(decrypted_char)
        return ''.join(decrypted_list)


if __name__ == '__main__':
    Vigenere(sys.argv[1:]).perform_operation()
