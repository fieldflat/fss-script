import hashlib
import sys
import random


class Utils:
    def __init__(self):
        """ init section """

    def prg(input_length: int, output_length: int, seed: bytes):
        BITS_LENGTH = 256

        def internal_prg(input: str):
            if len(input) != input_length:
                print("invalid input length (expected: {}, actual: {})".format(
                    input_length, len(input)), file=sys.stderr)
                sys.exit(1)
            if BITS_LENGTH < output_length:
                print("output_length must be less than {}".format(
                    BITS_LENGTH), file=sys.stderr)
                sys.exit(1)
            x = (int(input, 2) ^ seed).to_bytes(BITS_LENGTH, 'little')
            bin_x = bin(int.from_bytes(hashlib.sha256(x).digest(), 'little'))
            ret = bin_x[-output_length:]
            return ret

        return internal_prg

    def bytes_to_string_with_padding(n: bytes, length):
        bin_n = bin(n)[2:]
        if len(bin_n) < length:
            bin_n = "0"*(length-len(bin_n)) + bin_n
        return bin_n

    def get_random_bits(length: int) -> str:
        r = random.getrandbits(length)
        str_r = bin(r)[2:]
        if len(str_r) < length:
            str_r = "0"*(length-len(str_r)) + str_r
        return str_r

    def xor(a: str, b: str, length: int):
        a, b = int(a, 2), int(b, 2)
        bin_a_b = bin(a ^ b)[2:]
        if len(bin_a_b) < length:
            bin_a_b = "0"*(length-len(bin_a_b)) + bin_a_b
        # print("    ====> {} ^ {} = {}".format(bin(a)[2:], bin(b)[2:], bin_a_b))
        return bin_a_b

    def int2bitstr(a: int, n: int) -> str:
        x = bin(a)[2:]
        if len(x) < n:
            x = "0"*(n-len(x)) + x
        return x
