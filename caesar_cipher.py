""" This is a cipher algorithm
    :function find_index: It's can use instead of `.index` method in Python strings.
    :function caesar_cipher_encrypt: Encrypting by this function.
    :function caesar_cipher_decrypt: Dycrypting by this function.
"""

from string import ascii_letters


def find_index(string: str, char: str) -> int:
    """I don't want to use `.index` method in Python strings, 
    then I wrote this to underestand how `.index.` works.
    """

    for ch in range(0, len(string)):
        if string[ch] == char:
            return ch
    return "Your index not found in this string."

def caesar_cipher_encrypt(input_string: str, key: int) -> int:
    """The encrypting function
        :param input_string: The string that you want to be encrypted.
        :param key: The amount by wich you want to shift to the next letter.
        :variable alpha: This variable has all alpha letters.
        :variable result: The result of encrypting this string.
    """

    alpha = ascii_letters
    result = ''

    for char in input_string:
        if char not in alpha:
            result += char
        else:
            alpha_key = (find_index(alpha, char) + key) % len(alpha)
            # you can use `alpha.index(char)` instead of `find_index(alpha, char)` to use Python abilities.
            result += alpha[alpha_key]
    return result


def caesar_cipher_decrypt(input_string: str, key: int) -> str:
    """The decrypting function
        :param input_string: The string that you want to be encrypted.
        :param key: The amount by wich you want to shift to the next letter.
    """

    key *= -1   # negate the key for reversing the encrypted word
    return caesar_cipher_encrypt(input_string=input_string, key=key)    # return encrypting function with negative key
