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
        character_list = []
        # TODO this method should convert a given string
        # into a list of given characters and return that list
        return character_list

    def make_key_list_from_keyword(self, keyword_list, text_list):
        key_list = []
        # TODO adds the user entered keyword into a list character by character
        # The resulting key needs to be the same length as the text being encrypted / decrypted
        # This means the letters in the keyword have to be repeated until the key_list is populated!
        # Use the modulo operator to make sure your current position in the text stays within
        # the bounds of the keyword_list
        return key_list

    def read_file(self, filename):
        # TODO read contents of filename and return as string
        return ''

    def write_file(self, filename, contents):
        # TODO write contents variable to filename
        return

    def encrypt_string(self, plaintext_list, key_list):
        # TODO encrypt plaintext using key
        # Iterate character by character over plaintext_list,
        # add corresponding entry in key_list to current character in plaintext_list
        # if resulting number is greater than 255, mod by 256
        # To get the numerical ASCII value for a character using the ord() function
        # To get the ASCII character for a number using the chr() function
        return ""

    def decrypt_string(self, ciphertext_list, key_list):
        # TODO decrypt ciphertext using keyword
        # Iterate character by character over ciphertext_list,
        # *subtract* corresponding entry in key_list to current character in ciphertext_list
        # if resulting number is less than 0, add 256
        # get the numerical ASCII value for a character using the ord() function
        # get the ASCII character for a number using the char() function
        return ""


if __name__ == '__main__':
    Vigenere(sys.argv[1:]).perform_operation()
