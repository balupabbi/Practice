
#Computing the Parity of a word
#How would you compute the parity of a very large number of 64-bit words?
#1011 is 1, 10001000 is 0



PRECOMPUTED_PARITY = {}


#O(n)
# Imagine bits shifting and XOR is used to detect even and odd number of bits
def parity(x:int) -> int:
    result = 0
    while x:
        print("x is: {}".format(x))
        result ^= x & 1
        print("result is: {}".format(result))

        x >>= 1

    return result


#x&(x-1) is x with lowest set bit erased
#O(k)
def parity2(x:int) -> int:
    result = 0
    while x:
        print("x is: {}".format(x))
        result ^= 1    #XOR everytime odd you get 1
        print("result is: {}".format(result))
        x &= x -1

    return result


#Computing parity for very large number of words
#using bit masking

def parity3(x:int) -> int:
    mask_size = 16
    bit_mask = 0xFFFF
    return (PRECOMPUTED_PARITY[x >> (3 * mask_size)])


if __name__ == "__main__":
    res = parity(12)
    print (res)